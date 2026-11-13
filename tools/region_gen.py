"""Alpha2-Roger region generator v0.2: builds one region's 480 x 480 region cells from the canon globe.

Rules: docs/design/zones.md, Region biome rules (approved by Nathan 2026-11-12).
For now it runs for R5 only; ice, water biomes, infection levels, and features come before other regions.

Run:  python3 tools/region_gen.py R5
Writes: tools/data/regions/R5.json and assets/maps/regions/R5_biomes_v0.2.png
"""
__version__ = "0.2"
import sys, numpy as np
from scipy import ndimage
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
REPO = str(Path(__file__).resolve().parent.parent)
REGION = (sys.argv[1] if len(sys.argv) > 1 else 'R5').upper()
assert REGION == 'R5', 'v0.2 only supports R5; ice, water biomes, infection, and features come first'
src = open(f"{REPO}/tools/globe_candidates.py").read().split("seeds = [")[0]
G = {}; exec(src, G)
W0, H0 = G["W"], G["H"]
elev, LAT = G["sphere_field"](np.random.default_rng(2718))
sea = np.quantile(elev, 1 - G["LAND_FRAC"])
landg = elev > sea
Lmax = elev[landg].max()
X0, Y0, N, M = 506, 116, 38, 4          # window with a 4 px margin around R5 (x 510..539, y 120..149)
CELLS = 16; KM = 44082 / W0 / CELLS        # about 3.83 km per region cell
win = np.take(elev, range(X0, X0 + N), axis=1, mode="wrap")[Y0:Y0 + N]
# v0.2: everything below is keyed to world coordinates, so neighboring regions agree along shared borders.
# Interpolation is local (cubic B-spline without the global prefilter), and noise is hashed from absolute cell coordinates.
n = N * CELLS
GX = (X0 * CELLS + np.arange(n))[None, :].repeat(n, 0)          # absolute cell column (wraps at W0 * CELLS)
GY = (Y0 * CELLS + np.arange(n))[:, None].repeat(n, 1)          # absolute cell row
coords = np.stack([(GY - Y0 * CELLS + 0.5) / CELLS - 0.5, (GX - X0 * CELLS + 0.5) / CELLS - 0.5])
up = ndimage.map_coordinates(win, coords, order=3, prefilter=False, mode="nearest")
WRAP = W0 * CELLS
def _hash(ix, iy, salt):
    h = (ix.astype(np.uint64) * np.uint64(0x9E3779B1) ^ iy.astype(np.uint64) * np.uint64(0x85EBCA77) ^ np.uint64(salt) * np.uint64(0xC2B2AE3D) ^ np.uint64(2718))
    h ^= h >> np.uint64(15); h *= np.uint64(0x2C1B3C6D); h ^= h >> np.uint64(12); h *= np.uint64(0x297A2D39); h ^= h >> np.uint64(15)
    return (h & np.uint64(0xFFFFFF)).astype(np.float64) / 0xFFFFFF * 2 - 1
def value_noise(scale, salt):
    """Smooth value noise on a lattice of `scale` cells, from absolute cell coordinates (wraps east-west)."""
    fx, fy = GX / scale, GY / scale
    x0, y0 = np.floor(fx).astype(np.int64), np.floor(fy).astype(np.int64)
    tx, ty = fx - x0, fy - y0
    sx, sy = tx * tx * (3 - 2 * tx), ty * ty * (3 - 2 * ty)
    per = int(round(WRAP / scale))
    def h(ix, iy): return _hash(np.mod(ix, per), iy, salt)
    a, b, c, d = h(x0, y0), h(x0 + 1, y0), h(x0, y0 + 1), h(x0 + 1, y0 + 1)
    return (a + (b - a) * sx) + ((c + (d - c) * sx) - (a + (b - a) * sx)) * sy
def fbm(shape, sig):
    salt = int(sig * 101)
    f = value_noise(sig * 2, salt) + 0.5 * value_noise(sig, salt + 7)
    return f / 0.6
std = elev.std()
up = up + std * (0.05 * fbm(up.shape, 6) + 0.025 * fbm(up.shape, 2))
lat = 90 - (Y0 + (np.arange(n) + 0.5) / CELLS) * 180 / (H0 - 1)
LATc = np.repeat(lat[:, None], n, 1)
land = up > sea
meters = np.where(land, 6500 * np.clip((up - sea) / (Lmax - sea), 0, 1) ** 1.63, 0)   # planet top about 6,500 m; R5 top about 3,500 m
# latitude lines (world.md draft table), annual mean F = (summer high + winter low) / 2
lines = np.array([[0, 90, 72], [10, 93, 66], [20, 97, 55], [30, 97, 38], [40, 88, 20], [50, 76, 3], [60, 66, -15]])
mean_lat = np.interp(np.abs(LATc), lines[:, 0], (lines[:, 1] + lines[:, 2]) / 2)
temp = mean_lat - 0.01148 * meters                       # 3.5 F per 1,000 ft
# rivers at region-cell resolution
G["H"], G["W"] = n, n
filled = G["priority_flood"](up, land); acc, down, sink = G["flow"](filled, land)
river = land & (acc > 1800)
creek = land & (acc > 450) & ~river
# moisture: coast and rivers
dcoast = ndimage.distance_transform_edt(land) * KM
driver = ndimage.distance_transform_edt(~river) * KM
moist = np.exp(-dcoast / 700) + 0.35 * np.exp(-driver / 25) + 0.08 * fbm(up.shape, 20)
coast = land & (dcoast <= KM * 1.01)
B = np.full((n, n), "", dtype=object)
warm, temperate = temp >= 60, (temp >= 45) & (temp < 60)
def band(mask, wet, mid, dry):
    B[mask & (moist >= 0.55)] = wet; B[mask & (moist >= 0.30) & (moist < 0.55)] = mid; B[mask & (moist < 0.30)] = dry
band(land & warm, "Warm forest", "Warm grassland", "Scrub desert")
band(land & temperate, "Mixed forest", "Prairie", "Steppe")
band(land & (temp < 45), "Taiga", "Tundra", "Cold barrens")
B[land & (meters > 2000)] = "Highlands"
B[land & (meters < 150) & (moist > 0.75) & (driver < 15)] = "Marsh"
corridor = land & (driver <= 5) & (meters < 2000)
B[corridor] = "River"
B[coast & (meters < 300)] = "Coast"
B[~land] = "Ocean"
COL = {"Warm forest": (52, 110, 58), "Warm grassland": (150, 170, 80), "Scrub desert": (196, 170, 110), "Mixed forest": (70, 120, 70),
       "Prairie": (160, 180, 90), "Steppe": (180, 170, 110), "Taiga": (40, 80, 60), "Tundra": (150, 160, 140), "Cold barrens": (150, 140, 130),
       "Highlands": (120, 100, 80), "Marsh": (90, 120, 100), "River": (110, 150, 120), "Coast": (220, 205, 150), "Ocean": (30, 60, 110)}
img = np.zeros((n, n, 3), np.uint8)
for k, c in COL.items(): img[B == k] = c
shade = np.clip(meters / 3500, 0, 1)[..., None]
img = (img * (1 - 0.35 * shade) + np.array([235, 235, 235]) * 0.35 * shade * (meters[..., None] > 2600)).astype(np.uint8)
img[creek] = (90, 140, 200); img[river] = (40, 100, 190)
c0 = M * CELLS; cut = img[c0:c0 + 30 * CELLS, c0:c0 + 30 * CELLS]; Bc = B[c0:c0 + 480, c0:c0 + 480]; Tc = temp[c0:c0 + 480, c0:c0 + 480]; Mc = meters[c0:c0 + 480, c0:c0 + 480]
S = 2; im = Image.fromarray(cut).resize((480 * S, 480 * S), Image.NEAREST); d = ImageDraw.Draw(im)
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
for i in range(0, 481, 16):
    d.line([(i * S, 0), (i * S, 480 * S)], fill=(0, 0, 0, 60), width=1); d.line([(0, i * S), (480 * S, i * S)], fill=(0, 0, 0), width=1)
sx, sy = (519 - 510) * 16 + 8, (128 - 120) * 16 + 8
d.ellipse([sx * S - 7, sy * S - 7, sx * S + 7, sy * S + 7], fill=(220, 40, 40), outline=(255, 255, 255), width=2)
d.text((sx * S + 10, sy * S - 9), "S1", fill=(255, 255, 255), font=f, stroke_width=3, stroke_fill=(0, 0, 0))
pk = np.unravel_index(np.argmax(Mc), Mc.shape)
d.text((pk[1] * S + 8, pk[0] * S - 8), f"peak {Mc[pk]:.0f} m", fill=(255, 255, 255), font=f, stroke_width=3, stroke_fill=(0, 0, 0))
order = [k for k in COL if (Bc == k).any()]
H_leg = 30 + 22 * ((len(order) + 3) // 4)
out = Image.new("RGB", (480 * S, 480 * S + H_leg), (20, 20, 20)); od = ImageDraw.Draw(out)
od.text((8, 6), f"{REGION} biomes, region_gen v{__version__}   grid lines = 1 globe pixel = 16 x 16 region cells (~61 km)", fill=(255, 255, 255), font=f)
for i, k in enumerate(order):
    x, y = 8 + (i % 4) * 238, 30 + (i // 4) * 22
    od.rectangle([x, y, x + 16, y + 16], fill=COL[k]); od.text((x + 22, y), f"{k} {100 * (Bc == k).mean():.0f}%", fill=(255, 255, 255), font=f)
out.paste(im, (0, H_leg))
Path(f"{REPO}/assets/maps/regions").mkdir(parents=True, exist_ok=True)
out.save(f"{REPO}/assets/maps/regions/{REGION}_biomes_v0.2.png")
import json
codes = list(COL.keys())
key = "abcdefghijklmnopqrstuvwxyz"
Rc = river[c0:c0 + 480, c0:c0 + 480]; Kc = creek[c0:c0 + 480, c0:c0 + 480]
data = {"version": "0.2", "generated_by": f"tools/region_gen.py v{__version__}", "seed": 2718, "region": REGION,
        "cells": 480, "km_per_cell": round(KM, 2), "origin_globe_px": [510, 120],
        "biomes": {key[i]: k for i, k in enumerate(codes)},
        "biome_rows": ["".join(key[codes.index(v)] for v in row) for row in Bc],
        "water_key": {"0": "none", "1": "creek", "2": "river"},
        "water_rows": ["".join("2" if r else ("1" if k else "0") for r, k in zip(rr, kk)) for rr, kk in zip(Rc, Kc)],
        "height_m_rows": [[int(round(v)) for v in row] for row in Mc[::4, ::4]],
        "height_note": "every 4th cell in each direction (120 x 120)"}
open(f"{REPO}/tools/data/regions/{REGION}.json", "w").write(json.dumps(data, separators=(",", ":")) + "\n")
print(f"wrote tools/data/regions/{REGION}.json and assets/maps/regions/{REGION}_biomes_v0.2.png")
for k in order: print(f"{k:15s} {100 * (Bc == k).mean():5.1f}%")
print("temp range F", round(float(Tc[Bc != 'Ocean'].min()), 1), round(float(Tc.max()), 1), " peak m", round(float(Mc.max())), " S1 biome:", Bc[sy, sx], " S1 temp", round(float(Tc[sy, sx]), 1), "m", round(float(Mc[sy, sx])))
