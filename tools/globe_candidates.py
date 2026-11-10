"""Verlassen globe candidates v0.3.1: cold-world physics pass, rivers, infection impacts.

About 45% land, drier interiors, big ice caps, geothermal hotspots, salt basins.
Equirectangular, wraps east-west.
"""
__version__ = "0.3.1"

import heapq
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

W, H = 720, 360
LAND_FRAC = 0.45

def sphere_field(rng, octaves=6, base=1.5, waves=8):
    lon = np.linspace(-np.pi, np.pi, W, endpoint=False)
    lat = np.linspace(np.pi / 2, -np.pi / 2, H)
    LON, LAT = np.meshgrid(lon, lat)
    x, y, z = np.cos(LAT) * np.cos(LON), np.cos(LAT) * np.sin(LON), np.sin(LAT)
    total = np.zeros((H, W)); amp, freq = 1.0, base
    for _ in range(octaves):
        for _ in range(waves):
            d = rng.normal(size=3); d /= np.linalg.norm(d)
            total += amp * np.sin(freq * (x * d[0] + y * d[1] + z * d[2]) * np.pi + rng.uniform(0, 2 * np.pi))
        amp *= 0.5; freq *= 2.0
    return total, LAT

def coast_distance(land):
    # distance (in pixels) from ocean, wrapping east-west
    tiled = np.concatenate([land, land, land], axis=1)
    dist = ndimage.distance_transform_edt(tiled)
    return dist[:, W:2 * W]

def pick_points(score, mask, n, min_sep, rng):
    pts = []
    cand = np.argwhere(mask)
    if len(cand) == 0:
        return pts
    order = np.argsort(-score[mask])
    for idx in order:
        y, x = cand[idx]
        if all(min(abs(x - px), W - abs(x - px)) ** 2 + (y - py) ** 2 > min_sep ** 2 for py, px in pts):
            pts.append((y, x))
        if len(pts) >= n:
            break
    return pts

def priority_flood(elev, land):
    """Fill depressions so every land cell drains to the ocean (wraps east-west)."""
    filled = elev.copy()
    done = ~land.copy()
    heap = []
    ocean_edge = land & (ndimage.binary_dilation(~land, structure=np.ones((3, 3))) )
    for y, x in np.argwhere(ocean_edge):
        heapq.heappush(heap, (filled[y, x], y, x)); done[y, x] = True
    eps = 1e-5
    while heap:
        h, y, x = heapq.heappop(heap)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                ny, nx = y + dy, (x + dx) % W
                if 0 <= ny < H and not done[ny, nx]:
                    done[ny, nx] = True
                    if filled[ny, nx] <= h:
                        filled[ny, nx] = h + eps
                    heapq.heappush(heap, (filled[ny, nx], ny, nx))
    return filled

def flow(elev, land):
    """D8 steepest-descent flow accumulation, wrapping east-west.  Returns accumulation and sink mask."""
    acc = np.where(land, 1.0, 0.0)
    down = -np.ones((H, W), dtype=np.int64)
    best = elev.copy()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            nb = np.roll(elev, (-dy, -dx), axis=(0, 1))
            if dy == -1: nb[0, :] = np.inf
            if dy == 1: nb[-1, :] = np.inf
            better = nb < best
            best = np.where(better, nb, best)
            ys, xs = np.indices((H, W))
            tgt = ((ys + dy) % H) * W + (xs + dx) % W
            down = np.where(better, tgt, down)
    flat = elev.ravel(); dflat = down.ravel(); accf = acc.ravel(); landf = land.ravel()
    for i in np.argsort(-flat):
        if landf[i] and dflat[i] >= 0:
            accf[dflat[i]] += accf[i]
    sink = land & (down < 0)
    return accf.reshape(H, W), down, sink

def render(seed):
    rng = np.random.default_rng(seed)
    elev, LAT = sphere_field(rng)
    heat, _ = sphere_field(np.random.default_rng(seed + 7), octaves=3, base=3.0)
    latdeg = np.degrees(np.abs(LAT))
    sea = np.quantile(elev, 1 - LAND_FRAC)
    land = elev > sea
    dist = coast_distance(land)
    hi = land & (elev > np.quantile(elev[land], 0.85))
    filled = priority_flood(elev, land)
    depth = np.where(land, filled - elev, 0)
    acc, down, sink = flow(filled, land)

    img = np.zeros((H, W, 3), dtype=np.uint8)
    img[:] = (22, 48, 78)                                  # deep ocean
    img[(~land) & (elev > sea - 0.35)] = (34, 70, 106)    # shallows / shelf
    img[land] = (74, 104, 70)                              # coastal forest
    img[land & (dist > 12)] = (138, 132, 94)               # dry interior steppe
    img[land & (latdeg > 45)] = (112, 120, 104)            # tundra
    img[hi] = (128, 118, 104)                              # highlands
    img[(~land) & (latdeg > 64)] = (196, 210, 222)         # permanent sea ice
    img[land & (latdeg > 58)] = (228, 234, 240)            # permanent land ice

    habitable = land & (latdeg < 55)
    geo = pick_points(heat + 0.6 * (elev - sea), habitable & (dist > 3), 5, 70, rng)
    lakes_lbl, n = ndimage.label(depth > 0.02)
    salt_mask = np.zeros_like(land)
    if n:
        sizes = ndimage.sum(np.ones_like(depth), lakes_lbl, index=range(1, n + 1))
        order = np.argsort(-sizes)
        picked = 0
        for k in order:
            comp = lakes_lbl == (k + 1)
            cy, cx = np.argwhere(comp).mean(axis=0)
            if dist[comp].mean() > 8 and np.degrees(abs(LAT[int(cy), 0])) < 55:
                core = comp & (depth > np.quantile(depth[comp], 0.6))
                salt_mask |= core
                picked += 1
            if picked >= 4:
                break
    salt = []
    imp = pick_points(heat * -1 + rng.normal(size=heat.shape) * 0.5, land & (latdeg < 58) & (dist > 4), 3, 160, rng)

    cold = latdeg > 58
    river = land & (acc > 120) & ~cold
    big = ndimage.binary_dilation(land & (acc > 900) & ~cold) & land
    img[river] = (70, 140, 200)
    img[big] = (96, 168, 226)
    img[salt_mask] = (236, 230, 214)
    im = Image.fromarray(img)
    d = ImageDraw.Draw(im)
    for y, x in salt:
        d.ellipse([x - 6, y - 4, x + 6, y + 4], fill=(236, 230, 214), outline=(120, 110, 90))
    for y, x in geo:
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(232, 96, 48), outline=(60, 20, 10))
    for y, x in imp:
        d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=(170, 70, 220), outline=(40, 10, 60))
    return im, land.mean()

seeds = [1042, 2718, 5016, 64432]
pad, top, cap = 16, 56, 40
out = Image.new("RGB", (W * 2 + pad * 3, (H + cap) * 2 + top + 70), (12, 14, 20))
d = ImageDraw.Draw(out)
try:
    f = ImageFont.truetype("DejaVuSans-Bold.ttf", 20); fs = ImageFont.truetype("DejaVuSans.ttf", 15)
except OSError:
    f = fs = ImageFont.load_default()
d.text((pad, 16), "Verlassen globe candidates  v0.3.1   rivers, salt lakes, infection impacts   (north up, wraps east-west)", fill=(235, 235, 240), font=f)
for i, s in enumerate(seeds):
    im, lf = render(s)
    cx = pad + (i % 2) * (W + pad); cy = top + (i // 2) * (H + cap)
    out.paste(im, (cx, cy))
    d.text((cx, cy + H + 8), f"{'ABCD'[i]}   seed {s}   land {lf*100:.0f}%", fill=(200, 205, 215), font=fs)

ly = top + (H + cap) * 2 + 8
legend = [((74, 104, 70), "coastal forest"), ((138, 132, 94), "dry steppe"), ((112, 120, 104), "tundra"),
          ((128, 118, 104), "highlands"), ((228, 234, 240), "permanent ice"), ((232, 96, 48), "geothermal"),
          ((236, 230, 214), "salt basin (terminal lake)"), ((96, 168, 226), "rivers"), ((170, 70, 220), "infection impact")]
lx = pad
for col, name in legend:
    d.rectangle([lx, ly + 4, lx + 16, ly + 18], fill=col, outline=(80, 80, 90))
    d.text((lx + 22, ly + 2), name, fill=(200, 205, 215), font=fs)
    lx += 30 + int(d.textlength(name, font=fs)) + 18
out.save("verlassen_globe_candidates_v0.3.1.png")
print("ok")
