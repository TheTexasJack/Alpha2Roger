"""Verlassen places v1.0 (from pin draft v0.1): 10 fixed places on the canonical globe (seed 2718), with a grid overlay.

Placement follows the world rules: major cities near water and heat, spaceport near the equator on flat
ground, salt-lake towns as trade hubs, onsen towns on geothermal sites, one remote holdfast with its own heat.
"""
__version__ = "1.0"

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

src = open(__file__.replace("place_pins.py", "globe_candidates.py")).read().split("seeds = [")[0]
G = {}
exec(src, G)
W, H = G["W"], G["H"]
SEED = 2718


def fields(seed):
    rng = np.random.default_rng(seed)
    elev, LAT = G["sphere_field"](rng)
    heat, _ = G["sphere_field"](np.random.default_rng(seed + 7), octaves=3, base=3.0)
    latdeg = np.degrees(np.abs(LAT))
    sea = np.quantile(elev, 1 - G["LAND_FRAC"])
    land = elev > sea
    dist = G["coast_distance"](land)
    hi = land & (elev > np.quantile(elev[land], 0.85))
    filled = G["priority_flood"](elev, land)
    depth = np.where(land, filled - elev, 0)
    acc, _, _ = G["flow"](filled, land)
    habitable = land & (latdeg < 55)
    geo = G["pick_points"](heat + 0.6 * (elev - sea), habitable & (dist > 3), 5, 70, rng)
    lbl, n = ndimage.label(depth > 0.02)
    salt = []
    if n:
        sizes = ndimage.sum(np.ones_like(depth), lbl, index=range(1, n + 1))
        for k in np.argsort(-sizes):
            comp = lbl == (k + 1)
            cy, cx = np.argwhere(comp).mean(axis=0)
            if dist[comp].mean() > 8 and np.degrees(abs(LAT[int(cy), 0])) < 55:
                salt.append((int(cy), int(cx)))
            if len(salt) >= 4:
                break
    return dict(elev=elev, latdeg=latdeg, land=land, dist=dist, hi=hi, acc=acc, geo=geo, salt=salt)


def wrapdist(a, b):
    dy = a[0] - b[0]; dx = abs(a[1] - b[1]); dx = min(dx, W - dx)
    return (dy * dy + dx * dx) ** 0.5


def near(mask, pt, r):
    y, x = pt
    ys, xs = np.ogrid[:H, :W]
    dx = np.minimum(abs(xs - x), W - abs(xs - x))
    return mask & ((ys - y) ** 2 + dx ** 2 <= r * r)


def best(score, mask, taken, min_sep):
    s = np.where(mask, score, -np.inf)
    for idx in np.argsort(-s, axis=None):
        y, x = divmod(idx, W)
        if not np.isfinite(s[y, x]):
            return None
        if all(wrapdist((y, x), t) > min_sep for t in taken):
            return (y, x)


F = fields(SEED)
land, latdeg, acc, dist, elev, hi = F["land"], F["latdeg"], F["acc"], F["dist"], F["elev"], F["hi"]
river = land & (acc > 120)
bigriver = land & (acc > 900)
riv_near = ndimage.binary_dilation(river, iterations=3)
bigriv_near = ndimage.binary_dilation(bigriver, iterations=4)
rough = ndimage.generic_filter(elev, np.std, size=5, mode="wrap")
warm = np.clip(1 - latdeg / 60, 0, 1)
geo_near = np.zeros_like(land)
for g in F["geo"]:
    geo_near |= near(land, g, 14)

pins, taken = [], []

def add(kind, pt):
    if pt is not None:
        pins.append((kind, pt)); taken.append(pt)

# 1. Spaceport: near equator, flat, by a big river
score = 3 * (1 - latdeg / 90) - 4 * rough + 0.5 * np.log1p(acc)
add("Spaceport city", best(score, land & bigriv_near & ~hi & (latdeg < 20), taken, 40))
# 2-4. Major cities: water + heat, warmer bands
score = 2 * warm + 0.6 * np.log1p(acc) + 1.5 * geo_near
for _ in range(3):
    add("Major city", best(score, land & riv_near & (latdeg < 45) & ~hi, taken, 70))
# 5-6. Onsen towns at geothermal sites not already used
for g in F["geo"]:
    if len([p for p in pins if p[0] == "Onsen town"]) >= 2:
        break
    if all(wrapdist(g, t) > 45 for t in taken) and latdeg[g] < 50:
        add("Onsen town", g)
# 7-8. Salt-lake trade towns at lake edges
for s_ in F["salt"]:
    if len([p for p in pins if p[0] == "Salt-lake trade town"]) >= 2:
        break
    if all(wrapdist(s_, t) > 40 for t in taken):
        add("Salt-lake trade town", s_)
# 9. River-mouth port
mouth = land & bigriver & (dist <= 2)
add("River-mouth port", best(warm + 0.3 * np.log1p(acc), mouth, taken, 60))
# 10. Remote holdfast: cold band, near any geothermal-ish heat or river
score = latdeg / 60 + 0.3 * np.log1p(acc)
add("Remote holdfast (own heat source)", best(score, land & (latdeg > 42) & (latdeg < 57) & riv_near, taken, 60))
# fill any shortfall with river towns
while len(pins) < 10:
    add("River town", best(warm + 0.5 * np.log1p(acc), land & riv_near & (latdeg < 50), taken, 50))

# render base map at 2x with grid
im, _ = G["render"](SEED)
S = 2
big = im.resize((W * S, H * S), Image.NEAREST)
cols, rows = 24, 12
cw, rh = W * S / cols, H * S / rows
left, top = 44, 70
out = Image.new("RGB", (big.width + left + 20, big.height + top + 210), (12, 14, 20))
out.paste(big, (left, top))
d = ImageDraw.Draw(out, "RGBA")
fb = ImageFont.truetype("DejaVuSans-Bold.ttf", 22); f = ImageFont.truetype("DejaVuSans.ttf", 15); fbs = ImageFont.truetype("DejaVuSans-Bold.ttf", 14)
d.text((left, 20), "Verlassen places v1.0   seed 2718   (grid: column letter + row number)", fill=(235, 235, 240), font=fb)
letters = "ABCDEFGHIJKLMNOPQRSTUVWX"
for c in range(cols + 1):
    x = left + c * cw
    d.line([(x, top), (x, top + big.height)], fill=(255, 255, 255, 60), width=1)
    if c < cols:
        d.text((x + cw / 2 - 5, top - 20), letters[c], fill=(200, 205, 215), font=fbs)
for r in range(rows + 1):
    y = top + r * rh
    d.line([(left, y), (left + big.width, y)], fill=(255, 255, 255, 60), width=1)
    if r < rows:
        d.text((left - 26, y + rh / 2 - 8), str(r + 1), fill=(200, 205, 215), font=fbs)
colors = {"Spaceport city": (255, 220, 60), "Major city": (255, 255, 255), "Onsen town": (232, 96, 48),
          "Salt-lake trade town": (236, 230, 214), "River-mouth port": (96, 200, 255),
          "Remote holdfast (own heat source)": (170, 255, 170), "River town": (200, 200, 200)}
NAMES = {1: 'Setareh Minato', 2: 'Ikh Gawa', 3: 'Warmes Tani', 4: 'Svetla Hama', 5: 'Khaluun Onsen',
         6: 'Davs Mizuumi', 7: 'Shio Loch', 8: 'Darya Kako', 9: 'Zimna Toride', 10: 'Kawa Fada'}
legend_lines = []
for i, (kind, (y, x)) in enumerate(pins, 1):
    px, py = left + x * S, top + y * S
    col = colors.get(kind, (255, 255, 255))
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=col + (255,), outline=(0, 0, 0, 255), width=2)
    d.text((px + 11, py - 11), f"{i} {NAMES[i]}", fill=(255, 255, 255), font=fbs, stroke_width=3, stroke_fill=(0, 0, 0))
    gref = f"{letters[int(x * S // cw)]}{int(y * S // rh) + 1}"
    legend_lines.append((i, kind, gref, col))
ly = top + big.height + 16
for j, (i, kind, gref, col) in enumerate(legend_lines):
    cx = left + (j // 5) * 720; cy = ly + (j % 5) * 26
    d.ellipse([cx, cy + 3, cx + 14, cy + 17], fill=col, outline=(0, 0, 0))
    d.text((cx + 22, cy), f"{i}.  {NAMES[i]}: {kind}   ({gref})", fill=(220, 225, 235), font=f)
d.text((left, ly + 5 * 26 + 14), "Placed by the world rules (water and heat, equator spaceport, salt-lake hubs).  Names: Japanese plus regional second culture.", fill=(150, 155, 165), font=f)
d.text((left, ly + 5 * 26 + 36), "Purple infection impacts are still provisional and not counted among the 10 places.", fill=(150, 155, 165), font=f)
out.save(__file__.replace("tools/place_pins.py", "docs/maps/verlassen_places_v1.0.png"))
import json
json.dump({"version": "1.0", "places": [{"id": i, "name": NAMES[i], "type": kind, "y": int(y), "x": int(x), "grid": g}
           for (i, kind, g, _), (_, (y, x)) in zip(legend_lines, pins)]},
          open(__file__.replace("place_pins.py", "data/places_v1.0.json"), "w"), indent=1)
for i, kind, gref, _ in legend_lines:
    print(i, kind, gref)
