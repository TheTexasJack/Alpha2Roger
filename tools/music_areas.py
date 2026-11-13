"""Alpha2-Roger music areas v0.2: the music area of every globe pixel, seed 2718.

Since v0.2 (2026-11-13) this tool reads the culture map and pairs each culture with its music.  It no longer
works out who lives where itself: that moved to tools/culture_map.py, which radio, news, and settlement names
also read.  The output is unchanged from v0.1, pixel for pixel.

Pairing (Nathan, 2026-11-12 and 2026-11-13; music areas in docs/design/world.md, music in docs/design/music.md):
  gaelic, mongolian, persian, german, slavic   Japanese plus that culture
  ice                                           ice dread (cold, long notes with small hints of other songs)
  open_water                                    Japanese plus sea shanties
  base_only                                     the Overall theme

Music stays in music: change the pairing here, never the culture map.  The culture map feeds this tool; this
tool feeds nothing else.

Run:  python3 tools/culture_map.py   (first, if the culture map changed)
      python3 tools/music_areas.py   writes tools/data/music_areas.json and assets/maps/verlassen_music_areas_v0.1.png
"""
__version__ = "0.2"
import json, numpy as np
from collections import Counter, defaultdict
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
culture_map = json.loads((REPO / "tools/data/culture_map.json").read_text())
P = json.loads((REPO / "tools/data/planet_verlassen.json").read_text())["places"]
W, H = culture_map["width_px"], culture_map["height_px"]

# culture (from the culture map) -> music area key used below
PAIRING = {"gaelic": "Gaelic", "mongolian": "Mongolian", "persian": "Persian", "german": "German", "slavic": "Slavic",
           "ice": "Ice", "open_water": "Shanty", "base_only": "Overall"}
cultures = culture_map["cultures"]
assert set(cultures) == set(PAIRING), f"culture map has cultures with no music pairing: {set(cultures) ^ set(PAIRING)}"
codes = np.array([[int(ch) for ch in row] for row in culture_map["rows"]])
cult = np.array([PAIRING[c] for c in cultures], dtype=object)[codes]

# land mask, for drawing only (the music itself comes from the culture map)
src = (REPO / "tools/globe_candidates.py").read_text().split("seeds = [")[0]
G = {}
exec(src, G)
elev, _ = G["sphere_field"](np.random.default_rng(culture_map["seed"]))
land = elev > np.quantile(elev, 1 - G["LAND_FRAC"])

COL = {"Ice": (225, 235, 245), "Shanty": (24, 44, 96), "Overall": (150, 150, 150), "Persian": (214, 160, 60),
       "Mongolian": (180, 90, 60), "German": (90, 120, 190), "Slavic": (150, 100, 190), "Gaelic": (70, 160, 100)}
GRID = "ABCDEFGHIJKLMNOPQRSTUVWX"

sq = defaultdict(list)
mixed = []
for gy in range(12):
    for gx in range(24):
        block = cult[gy * 30:(gy + 1) * 30, gx * 30:(gx + 1) * 30]
        c = Counter(v for v in block.ravel() if v)
        if not c:
            continue
        name = f"{GRID[gx]}{gy + 1}"
        top, n = c.most_common(1)[0]
        sq[top].append(name)
        if len(c) > 1 and c.most_common(2)[1][1] > 0.2 * sum(c.values()):
            mixed.append(f"{name} ({', '.join(k for k, _ in c.most_common(2))})")
for k in sorted(sq, key=lambda k: -len(sq[k])):
    print(k, len(sq[k]), " ".join(sorted(sq[k], key=lambda s: (int(s[1:]), s[0]))))
print("mixed:", "; ".join(mixed))
print("S1 R5 music area:", cult[128, 519])

img = np.zeros((H, W, 3), np.uint8)
for k, col in COL.items():
    img[cult == k] = col
water_tint = (~land) & ~np.isin(cult, ["Shanty", "Ice"])
img[water_tint] = (img[water_tint] * 0.55 + np.array([24, 44, 96]) * 0.45).astype(np.uint8)
img[(~land) & (cult == "Ice")] = (170, 190, 215)
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
ld.text((x0, 12), "Music areas v0.1:", fill=(255, 255, 255), font=f)       # image unchanged since v0.1
x0 += 220
for k, label in [("Gaelic", "Gaelic"), ("Mongolian", "Mongolian"), ("Persian", "Persian"), ("German", "German"),
                 ("Slavic", "Slavic"), ("Shanty", "Sea shanty"), ("Ice", "Ice dread"), ("Overall", "Overall")]:
    ld.rectangle([x0, 12, x0 + 18, 28], fill=COL[k], outline=(255, 255, 255))
    ld.text((x0 + 22, 12), label, fill=(255, 255, 255), font=f)
    x0 += 135
out = Image.new("RGB", (W * S, H * S + 40))
out.paste(lg, (0, 0))
out.paste(im, (0, 40))
out.save(REPO / "assets/maps/verlassen_music_areas_v0.1.png")

NAMES = {"Gaelic": "japanese_gaelic", "Mongolian": "japanese_mongolian", "Persian": "japanese_persian",
         "German": "japanese_german", "Slavic": "japanese_slavic", "Shanty": "japanese_sea_shanty", "Ice": "ice_dread",
         "Overall": "overall"}
area_codes = list(NAMES.values())
grid_rows = ["".join("0123456789"[area_codes.index(NAMES[c])] for c in row) for row in cult]
data = {"version": "0.2", "generated_by": f"tools/music_areas.py v{__version__}", "seed": culture_map["seed"],
        "culture_map": f"tools/data/culture_map.json v{culture_map['version']}",
        "width_px": W, "height_px": H, "areas": area_codes,
        "note": "one character per globe pixel, row by row from the top; the digit indexes areas",
        "rows": grid_rows}
(REPO / "tools/data/music_areas.json").write_text(json.dumps(data, indent=0) + "\n")
print("wrote assets/maps/verlassen_music_areas_v0.1.png and tools/data/music_areas.json")
