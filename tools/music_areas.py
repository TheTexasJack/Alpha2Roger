"""Alpha2-Roger music areas v0.1 (A2R music areas): the music area of every globe pixel, seed 2718.

Rules (Nathan, 2026-11-12, recorded in docs/design/world.md, Music areas):
  land        culture of the nearest of the ten places reachable overland (Japanese + that culture)
  no town     land that reaches no place uses the Overall theme
  near shore  sea within 2 globe pixels (about 120 km) of land takes that land's music
  deep ocean  Japanese + sea shanties
  polar       above 58 degrees, land or sea: ice dread

Run:  python3 tools/music_areas.py       writes tools/data/music_areas.json and assets/maps/verlassen_music_areas_v0.1.png
"""
__version__ = "0.1"
import sys, json, heapq, numpy as np
from collections import Counter, defaultdict
from scipy import ndimage
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
REPO = str(Path(__file__).resolve().parent.parent)
src = open(f"{REPO}/tools/globe_candidates.py").read().split("seeds = [")[0]
G = {}; exec(src, G)
W, H = G["W"], G["H"]
elev, LAT = G["sphere_field"](np.random.default_rng(2718))
latd = np.degrees(LAT)
land = elev > np.quantile(elev, 1 - G["LAND_FRAC"])
P = json.load(open(f"{REPO}/tools/data/planet_verlassen.json"))["places"]
CULT = {1: "Persian", 8: "Persian", 2: "Mongolian", 5: "Mongolian", 6: "Mongolian", 3: "German", 4: "Slavic", 9: "Slavic", 7: "Gaelic", 10: "Gaelic"}
COL = {"Ice": (225, 235, 245), "Shanty": (24, 44, 96), "Overall": (150, 150, 150), "Persian": (214, 160, 60), "Mongolian": (180, 90, 60), "German": (90, 120, 190), "Slavic": (150, 100, 190), "Gaelic": (70, 160, 100), "none": (120, 120, 120)}
owner = np.full((H, W), -1); dist = np.full((H, W), np.inf); pq = []
for p in P:
    y, x = p["px"]["y"], p["px"]["x"]; dist[y, x] = 0; owner[y, x] = p["id"]; heapq.heappush(pq, (0.0, y, x, p["id"]))
while pq:
    d, y, x, o = heapq.heappop(pq)
    if d > dist[y, x]: continue
    for dy, dx, c in [(-1,0,1),(1,0,1),(0,-1,1),(0,1,1),(-1,-1,1.5),(-1,1,1.5),(1,-1,1.5),(1,1,1.5)]:
        ny, nx = y + dy, (x + dx) % W
        if 0 <= ny < H and land[ny, nx] and d + c < dist[ny, nx]:
            dist[ny, nx] = d + c; owner[ny, nx] = o; heapq.heappush(pq, (d + c, ny, nx, o))
cult = np.full((H, W), "Shanty", dtype=object)
for (y, x), o in np.ndenumerate(owner):
    if land[y, x]: cult[y, x] = CULT.get(o, "Overall") if o > 0 else "Overall"
# near-shore water takes the culture of the nearest land within 2 px (about 120 km)
dt, (iy, ix) = ndimage.distance_transform_edt(~land, return_indices=True)
shore = (~land) & (dt <= 2)
cult[shore] = cult[iy[shore], ix[shore]]
# polar ice caps and polar seas: dread
cult[np.abs(latd) > 58] = "Ice"
def grid(y, x): return f"{'ABCDEFGHIJKLMNOPQRSTUVWX'[x*24//W]}{y*12//H+1}"
sq = defaultdict(list); mixed = []
for gy in range(12):
    for gx in range(24):
        block = cult[gy*30:(gy+1)*30, gx*30:(gx+1)*30]
        c = Counter(v for v in block.ravel() if v)
        if not c: continue
        name = f"{'ABCDEFGHIJKLMNOPQRSTUVWX'[gx]}{gy+1}"
        top, n = c.most_common(1)[0]
        sq[top].append(name)
        if len(c) > 1 and c.most_common(2)[1][1] > 0.2 * sum(c.values()): mixed.append(f"{name} ({', '.join(k for k,_ in c.most_common(2))})")
order = sorted(sq, key=lambda k: -len(sq[k]))
for k in order: print(k, len(sq[k]), ' '.join(sorted(sq[k], key=lambda s: (int(s[1:]), s[0]))))
print("mixed:", '; '.join(mixed))
print("S1 R5 culture:", cult[128, 519], " landless-of-place land px:", int(((owner < 0) & land).sum()))
img = np.zeros((H, W, 3), np.uint8)
for k, col in COL.items():
    m = (cult == k)
    img[m] = col if k in ("Ice", "Shanty", "Overall") else tuple(int(v*(1 if True else 1)) for v in col)
water_tint = (~land) & ~np.isin(cult, ["Shanty", "Ice"])
img[water_tint] = (img[water_tint] * 0.55 + np.array([24, 44, 96]) * 0.45).astype(np.uint8)
img[(~land) & (cult == "Ice")] = (170, 190, 215)
S = 2; im = Image.fromarray(img).resize((W*S, H*S), Image.NEAREST); d = ImageDraw.Draw(im)
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
for i in range(25): d.line([(i*60, 0), (i*60, H*S)], fill=(0,0,0), width=1)
for j in range(13): d.line([(0, j*60), (W*S, j*60)], fill=(0,0,0), width=1)
for i in range(24): d.text((i*60+22, 2), "ABCDEFGHIJKLMNOPQRSTUVWX"[i], fill=(255,255,255), font=f, stroke_width=2, stroke_fill=(0,0,0))
for j in range(12): d.text((3, j*60+22), str(j+1), fill=(255,255,255), font=f, stroke_width=2, stroke_fill=(0,0,0))
for p in P:
    cx, cy = p["px"]["x"]*S, p["px"]["y"]*S
    d.ellipse([cx-5, cy-5, cx+5, cy+5], fill=(255,255,255), outline=(0,0,0)); d.text((cx+7, cy-8), str(p["id"]), fill=(255,255,255), font=f, stroke_width=2, stroke_fill=(0,0,0))
cx, cy = 519*S, 128*S; d.ellipse([cx-6, cy-6, cx+6, cy+6], fill=(220,40,40), outline=(255,255,255), width=2); d.text((cx+8, cy-8), "S1", fill=(255,255,255), font=f, stroke_width=2, stroke_fill=(0,0,0))
lg = Image.new("RGB", (W*S, 40), (20,20,20)); ld = ImageDraw.Draw(lg); x0 = 10
ld.text((x0, 12), "Music areas v0.1:", fill=(255,255,255), font=f); x0 += 220
for k, lab_ in [("Gaelic","Gaelic"),("Mongolian","Mongolian"),("Persian","Persian"),("German","German"),("Slavic","Slavic"),("Shanty","Sea shanty"),("Ice","Ice dread"),("Overall","Overall")]:
    ld.rectangle([x0, 12, x0+18, 28], fill=COL[k], outline=(255,255,255)); ld.text((x0+22, 12), lab_, fill=(255,255,255), font=f); x0 += 135
out = Image.new("RGB", (W*S, H*S+40)); out.paste(lg, (0,0)); out.paste(im, (0,40)); out.save(f"{REPO}/assets/maps/verlassen_music_areas_v0.1.png")
NAMES = {"Gaelic": "japanese_gaelic", "Mongolian": "japanese_mongolian", "Persian": "japanese_persian", "German": "japanese_german", "Slavic": "japanese_slavic", "Shanty": "japanese_sea_shanty", "Ice": "ice_dread", "Overall": "overall"}
codes = list(NAMES.values())
grid_rows = ["".join("0123456789"[codes.index(NAMES[c])] for c in row) for row in cult]
data = {"version": "0.1", "generated_by": f"tools/music_areas.py v{__version__}", "seed": 2718,
        "width_px": W, "height_px": H, "areas": codes,
        "note": "one character per globe pixel, row by row from the top; the digit indexes areas",
        "rows": grid_rows}
open(f"{REPO}/tools/data/music_areas.json", "w").write(json.dumps(data, indent=0) + "\n")
print("wrote assets/maps/verlassen_music_areas_v0.1.png and tools/data/music_areas.json")
