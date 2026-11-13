"""Alpha2-Roger culture map v0.1: the second culture of every globe pixel, seed 2718.

Rules (Nathan, 2026-11-12 and 2026-11-13, recorded in docs/design/world.md):
  base        Japanese is the base everywhere, so the map ignores it and records only the second culture
  land        the second culture of the nearest of the ten places reachable overland
  grouped     places that share a culture share one area (Kawa Fada and Shio Loch are one Gaelic area)
  none        water, and land with no place on its landmass: Japanese base only
  not ideals  culture is not ideals; cities and their rulers set those (territories, factions)

Readers: music areas, radio, news, and settlement names read this map.  It reads nothing from them.

Run:  python3 tools/culture_map.py       writes tools/data/culture_map.json and assets/maps/verlassen_culture_v0.1.png
"""
__version__ = "0.1"
import json, heapq, numpy as np
from collections import Counter, defaultdict
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SEED = 2718
src = (REPO / "tools/globe_candidates.py").read_text().split("seeds = [")[0]
G = {}
exec(src, G)
W, H = G["W"], G["H"]
elev, _ = G["sphere_field"](np.random.default_rng(SEED))
land = elev > np.quantile(elev, 1 - G["LAND_FRAC"])

planet = json.loads((REPO / "tools/data/planet_verlassen.json").read_text())
P = planet["places"]
REGION_OF = {r["id"]: r for r in planet["cultural_regions"]}
CULTURE_OF_PLACE = {p["id"]: REGION_OF[p["cultural_region"]]["second_culture"] for p in P}
CULTURES = ["none"] + [r["second_culture"] for r in planet["cultural_regions"]]
CODE = {c: i for i, c in enumerate(CULTURES)}

# nearest place reachable overland: multi-source Dijkstra, 8 neighbors, wraps east-west
owner = np.full((H, W), -1)
dist = np.full((H, W), np.inf)
pq = []
for p in P:
    y, x = p["px"]["y"], p["px"]["x"]
    dist[y, x] = 0
    owner[y, x] = p["id"]
    heapq.heappush(pq, (0.0, y, x, p["id"]))
while pq:
    d, y, x, o = heapq.heappop(pq)
    if d > dist[y, x]:
        continue
    for dy, dx, c in [(-1, 0, 1), (1, 0, 1), (0, -1, 1), (0, 1, 1), (-1, -1, 1.5), (-1, 1, 1.5), (1, -1, 1.5), (1, 1, 1.5)]:
        ny, nx = y + dy, (x + dx) % W
        if 0 <= ny < H and land[ny, nx] and d + c < dist[ny, nx]:
            dist[ny, nx] = d + c
            owner[ny, nx] = o
            heapq.heappush(pq, (d + c, ny, nx, o))

culture = np.zeros((H, W), np.uint8)               # 0 = none (Japanese base only)
for pid, c in CULTURE_OF_PLACE.items():
    culture[land & (owner == pid)] = CODE[c]

# summary: share of land and the grid squares where each culture holds most of the land
GRID = "ABCDEFGHIJKLMNOPQRSTUVWX"
squares = defaultdict(list)
for gy in range(12):
    for gx in range(24):
        block = culture[gy * 30:(gy + 1) * 30, gx * 30:(gx + 1) * 30][land[gy * 30:(gy + 1) * 30, gx * 30:(gx + 1) * 30]]
        if block.size:
            squares[CULTURES[Counter(block.tolist()).most_common(1)[0][0]]].append(f"{GRID[gx]}{gy + 1}")
n_land = int(land.sum())
summary = []
for c in CULTURES:
    share = round(float((culture[land] == CODE[c]).sum()) / n_land, 3)
    summary.append({"culture": c, "places": [p for p, pc in CULTURE_OF_PLACE.items() if pc == c],
                    "land_share": share, "grid_squares": squares.get(c, [])})
    print(f"{c:<10} land {share:>6.1%}  places {summary[-1]['places']}  squares {len(squares.get(c, []))}")

data = {
    "version": "0.1",
    "generated_by": f"tools/culture_map.py v{__version__}",
    "seed": SEED,
    "width_px": W, "height_px": H,
    "base_culture": "japanese",
    "cultures": CULTURES,
    "cultural_regions": {r["second_culture"]: r["id"] for r in planet["cultural_regions"]},
    "rule": "land takes the second culture of the nearest place reachable overland; water and land with no place on its landmass are none (Japanese base only)",
    "note": "one character per globe pixel, row by row from the top; the digit indexes cultures",
    "summary": summary,
    "rows": ["".join(str(v) for v in row) for row in culture],
}
(REPO / "tools/data/culture_map.json").write_text(json.dumps(data, indent=0) + "\n")

# image
COL = {"none": (150, 150, 150), "persian": (214, 160, 60), "german": (90, 120, 190), "mongolian": (180, 90, 60),
       "slavic": (150, 100, 190), "gaelic": (60, 160, 90)}
img = np.zeros((H, W, 3), np.uint8)
img[:] = (24, 44, 96)
for c, col in COL.items():
    img[land & (culture == CODE[c])] = col
S = 2
im = Image.fromarray(img).resize((W * S, H * S), Image.NEAREST)
d = ImageDraw.Draw(im)
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
for i in range(25):
    d.line([(i * 60, 0), (i * 60, H * S)], fill=(0, 0, 0), width=1)
for j in range(13):
    d.line([(0, j * 60), (W * S, j * 60)], fill=(0, 0, 0), width=1)
for i in range(24):
    d.text((i * 60 + 22, 2), GRID[i], fill=(255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
for j in range(12):
    d.text((3, j * 60 + 22), str(j + 1), fill=(255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
for p in P:
    cx, cy = p["px"]["x"] * S, p["px"]["y"] * S
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(255, 255, 255), outline=(0, 0, 0))
    d.text((cx + 7, cy - 8), str(p["id"]), fill=(255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
cx, cy = 519 * S, 128 * S
d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(220, 40, 40), outline=(255, 255, 255), width=2)
d.text((cx + 8, cy - 8), "S1", fill=(255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
lg = Image.new("RGB", (W * S, 40), (20, 20, 20))
ld = ImageDraw.Draw(lg)
x0 = 10
ld.text((x0, 12), "Culture map v0.1 (on a Japanese base):", fill=(255, 255, 255), font=f)
x0 += 330
for c, label in [("gaelic", "Gaelic"), ("mongolian", "Mongolian"), ("slavic", "Slavic"), ("persian", "Persian"),
                 ("german", "German"), ("none", "Base only")]:
    ld.rectangle([x0, 12, x0 + 18, 28], fill=COL[c], outline=(255, 255, 255))
    ld.text((x0 + 22, 12), label, fill=(255, 255, 255), font=f)
    x0 += 140
out = Image.new("RGB", (W * S, H * S + 40))
out.paste(lg, (0, 0))
out.paste(im, (0, 40))
out.save(REPO / "assets/maps/verlassen_culture_v0.1.png")
print("wrote tools/data/culture_map.json and assets/maps/verlassen_culture_v0.1.png")
