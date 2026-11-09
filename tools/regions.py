"""Verlassen regions draft v0.1: each of the ten capitals claims the land it can reach overland first.

Claims spread across land only (seas block them, straits do not freeze in this draft), wrap east-west,
and stop at a reach limit, so land beyond every capital's reach is unclaimed wilderness.
Scale: 720 px around the planet; about 60 km per pixel east-west at the equator.
"""
import heapq, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

HERE = Path(__file__).parent
src = (HERE / "globe_candidates.py").read_text().split("seeds = [")[0]
G = {}; exec(src, G)
W, H = G["W"], G["H"]
REACH = 40          # pixels, about 2,400 km
places = json.loads((HERE / "data" / "places_v1.0.json").read_text())

rng = np.random.default_rng(2718)
elev, LAT = G["sphere_field"](rng)
sea = np.quantile(elev, 1 - G["LAND_FRAC"])
land = elev > sea
latdeg = np.degrees(np.abs(LAT))
walkable = land & (latdeg < 60)

owner = -np.ones((H, W), dtype=int)
cost = np.full((H, W), np.inf)
heap = []
for k, p in enumerate(places):
    cost[p["y"], p["x"]] = 0; heap.append((0.0, p["y"], p["x"], k))
heapq.heapify(heap)
while heap:
    c, y, x, k = heapq.heappop(heap)
    if c > cost[y, x] or owner[y, x] >= 0 and owner[y, x] != k:
        continue
    owner[y, x] = k
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == dx == 0:
                continue
            ny, nx = y + dy, (x + dx) % W
            if not (0 <= ny < H) or not walkable[ny, nx]:
                continue
            step = 1.414 if dy and dx else 1.0
            step *= 1.0 + 0.6 * max(0.0, float(elev[ny, nx] - elev[y, x]))  # uphill is harder
            nc = c + step
            if nc <= REACH and nc < cost[ny, nx]:
                cost[ny, nx] = nc; heapq.heappush(heap, (nc, ny, nx, k))

palette = [(255, 214, 64), (255, 140, 66), (120, 200, 255), (190, 140, 255), (255, 100, 120),
           (140, 230, 140), (255, 180, 220), (90, 220, 200), (230, 230, 120), (200, 160, 110)]
base, _ = G["render"](2718)
arr = np.asarray(base).astype(float)
for k in range(len(places)):
    m = owner == k
    arr[m] = arr[m] * 0.45 + np.array(palette[k]) * 0.55
img = Image.fromarray(arr.astype(np.uint8)).resize((W * 2, H * 2), Image.NEAREST)

left, top = 20, 64
out = Image.new("RGB", (img.width + left * 2, img.height + top + 210), (12, 14, 20))
out.paste(img, (left, top))
d = ImageDraw.Draw(out)
fb = ImageFont.truetype("DejaVuSans-Bold.ttf", 22); f = ImageFont.truetype("DejaVuSans.ttf", 15); fbs = ImageFont.truetype("DejaVuSans-Bold.ttf", 14)
d.text((left, 20), "Verlassen regions draft v0.1   (overland reach about 2,400 km from each capital)", fill=(235, 235, 240), font=fb)
land_total = (walkable).sum()
rows = []
for k, p in enumerate(places):
    px, py = left + p["x"] * 2, top + p["y"] * 2
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=palette[k], outline=(0, 0, 0), width=2)
    d.text((px + 10, py - 10), f"{p['id']} {p['name']}", fill=(255, 255, 255), font=fbs, stroke_width=3, stroke_fill=(0, 0, 0))
    rows.append((p, palette[k], 100 * (owner == k).sum() / land_total))
unclaimed = 100 * (walkable & (owner < 0)).sum() / land_total
ly = top + img.height + 14
for j, (p, col, pct) in enumerate(rows):
    cx = left + (j // 5) * 720; cy = ly + (j % 5) * 26
    d.rectangle([cx, cy + 3, cx + 16, cy + 17], fill=col, outline=(0, 0, 0))
    d.text((cx + 24, cy), f"{p['id']}. {p['name']} region   {pct:.1f}% of habitable land", fill=(220, 225, 235), font=f)
d.text((left, ly + 5 * 26 + 12), f"Unclaimed wilderness: {unclaimed:.0f}% of habitable land (uncolored).  Seas block claims; frozen straits are ignored in this draft.", fill=(160, 165, 175), font=f)
out.save(HERE.parent / "docs" / "maps" / "verlassen_regions_draft_v0.1.png")
print(f"unclaimed {unclaimed:.1f}%")
for p, _, pct in rows:
    print(p["id"], p["name"], f"{pct:.1f}%")
