"""Alpha2-Roger planet pack v0.1: packs every locked Verlassen fact into one data file the engine reads (A2R-101).

Sources (the pack never invents data; it only gathers and converts):
  tools/data/places_v1.0.json      the ten places and their pixel coordinates
  tools/data/names_v0.1.json       cultural regions, second cultures, word order
  tools/globe_candidates.py        the canon globe, seed 2718, for the three impact sites
  docs/design/world.md v0.58       planet facts, regions, currencies, notable people (copied in below)

Only decisions go in the file.  Drafts stay in world.md until Nathan approves them.  Anything still undecided
is null and listed under "open".

Run:  python3 tools/planet_pack.py      writes tools/data/planet_verlassen.json
"""
__version__ = "0.1"

import json, math
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT = DATA / "planet_verlassen.json"
FILE_VERSION = "0.1"          # bump on every change to the output

SEED = 2718
W, H = 720, 360               # globe raster, equirectangular, wraps east-west
GRID_COLS, GRID_ROWS = 24, 12  # map grid: column letter A to X, row 1 to 12
EARTH_CIRCUMFERENCE_KM = 40075
RADIUS_EARTHS = 1.1
CIRCUMFERENCE_KM = EARTH_CIRCUMFERENCE_KM * RADIUS_EARTHS
KM_PER_PX = CIRCUMFERENCE_KM / W   # east-west at the equator


def latlon(y, x):
    """Pixel to degrees.  Rows run from +90 (top) to -90 (bottom); columns from -180 eastward."""
    return round(90 - y * 180 / (H - 1), 2), round(-180 + x * 360 / W, 2)


def grid_ref(y, x):
    return f"{'ABCDEFGHIJKLMNOPQRSTUVWX'[x * GRID_COLS // W]}{y * GRID_ROWS // H + 1}"


def great_circle_km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return round(CIRCUMFERENCE_KM / math.pi * math.asin(math.sqrt(h)))


def impact_sites():
    """Re-run the canon globe and capture the three impact points it places (third pick_points call)."""
    src = (HERE / "globe_candidates.py").read_text().split("seeds = [")[0]
    G = {}
    exec(src, G)
    calls = []
    real = G["pick_points"]

    def spy(*a, **k):
        pts = real(*a, **k)
        calls.append(pts)
        return pts

    G["pick_points"] = spy
    G["render"](SEED)
    geo, imp = calls[0], calls[1]
    return [(int(y), int(x)) for y, x in imp]


# ---- Locked facts, copied from docs/design/world.md v0.58 (Nathan's decisions) ----

PLACE_FACTS = {
    1: ("Star Harbor", "Spaceport city", "spaceport_coast", "B"),
    2: ("Great River", "Major city, near geothermal heat", "southern_steppe", "C"),
    3: ("Warm Valley", "Major city, near geothermal heat", "west_north", "B"),
    4: ("Bright Shore", "Major city", "central_north", "E"),
    5: ("Hot Hot Springs", "Onsen town", "southern_steppe", "A"),
    6: ("Salt Lake", "Salt-lake trade town", "southern_steppe", "C"),
    7: ("Salt Lake", "Salt-lake trade town", "empty_east", "D"),
    8: ("Sea Mouth", "River-mouth port", "spaceport_coast", "B"),
    9: ("Cold Fort", "Remote holdfast with its own heat source", "central_north", "E"),
    10: ("Long River", "River town", "empty_east", "D"),
}
NOTABLE = {1: "Parisa Kuroda", 2: "Erdene Yamaguchi", 3: "Leopold Matsuda", 4: "Bogdan Ogawa",
           5: "Bolormaa Kobayashi", 6: "Altan Arai", 7: "Akane Keane", 8: "Farrokh Okada",
           9: "Radoslav Nishimura", 10: "Hina Rafferty"}
REGION_NAMES = {"spaceport_coast": "Spaceport coast", "west_north": "West continent north",
                "southern_steppe": "Southern steppe belt", "central_north": "Central-north island",
                "empty_east": "The empty east"}
CURRENCIES = [  # id, issued by, also used in
    ("A", [5], []),
    ("B", [3, 8, 1], []),
    ("C", [2, 6], []),
    ("D", [7], [10]),
    ("E", [4, 9], []),
]
IMPACT_GRIDS = ["M3", "T3", "J10"]   # accepted by Nathan


def build():
    places_src = json.loads((DATA / "places_v1.0.json").read_text())["places"]
    names = json.loads((DATA / "names_v0.1.json").read_text())

    places = []
    coords = {}
    for p in places_src:
        meaning, kind, region, cur = PLACE_FACTS[p["id"]]
        ll = latlon(p["y"], p["x"])
        coords[p["id"]] = ll
        assert grid_ref(p["y"], p["x"]) == p["grid"], f"grid mismatch for {p['name']}"
        places.append({
            "id": p["id"],
            "name": p["name"],
            "meaning": meaning,
            "type": kind,
            "grid": p["grid"],
            "px": {"x": p["x"], "y": p["y"]},
            "lat": ll[0], "lon": ll[1],
            "cultural_region": region,
            "political_region": p["id"],      # each place is the capital of its own region
            "currency": cur,
            "notable_person": {"name": NOTABLE[p["id"]], "role": None},
            "leader_title": None,              # lord or mayor, not yet set per place
        })

    impacts = []
    for y, x in impact_sites():
        g = grid_ref(y, x)
        la, lo = latlon(y, x)
        impacts.append({"grid": g, "px": {"x": x, "y": y}, "lat": la, "lon": lo})
    found = sorted(i["grid"] for i in impacts)
    assert found == sorted(IMPACT_GRIDS), f"impact sites moved: {found}"
    impacts.sort(key=lambda i: IMPACT_GRIDS.index(i["grid"]))
    for n, i in enumerate(impacts, 1):
        i["id"] = n

    ids = sorted(coords)
    distances = {str(a): {str(b): great_circle_km(coords[a], coords[b]) for b in ids if b != a} for a in ids}

    cultural = []
    for key, rule in names["regions"].items():
        cultural.append({
            "id": key,
            "name": REGION_NAMES[key],
            "base_culture": "japanese",
            "second_culture": rule["culture"],
            "word_order": rule["order"],
            "places": [p["id"] for p in places if p["cultural_region"] == key],
        })

    return {
        "version": FILE_VERSION,
        "planet_id": "verlassen",
        "generated_by": f"tools/planet_pack.py v{__version__}",
        "sources": {
            "world": "docs/design/world.md v0.58",
            "places": f"tools/data/places_v1.0.json v1.0",
            "names": f"tools/data/names_v{names['version']}.json v{names['version']}",
            "globe": "tools/globe_candidates.py v0.3.1",
        },
        "planet": {
            "official_name": "Kepler-64432p",
            "local_name": "Verlassen",
            "local_name_meaning": "abandoned, forsaken, left behind (German)",
            "era_u": 5016,
            "star": {"class": "G", "color": "yellow", "mass_solar": 1.0},
            "orbit_au": 1.1,
            "insolation_earth": 0.8,
            "radius_earths": RADIUS_EARTHS,
            "gravity_g": 1.0,
            "moons": 0,
            "rings": 0,
            "year_earth_months": 14,
            "cold_year": {
                "every_n_years": 3,
                "length_planet_years": 1,
                "temperature_shift_f": -50,
                "cause": "gas giant neighbor in a 3:1 orbital resonance",
            },
            "population": 10_000_000,
            "union_presence": "none; Union holds no sway, reached only through Baronic trade",
            "nearest_power": "Karrakin Trade Baronies",
        },
        "globe": {
            "seed": SEED,
            "generator": "tools/globe_candidates.py",
            "map": "assets/maps/verlassen_globe_v1.0.png",
            "width_px": W, "height_px": H,
            "projection": "equirectangular, wraps east-west",
            "grid": {"cols": GRID_COLS, "rows": GRID_ROWS, "col_letters": "A-X", "equator_between_rows": [6, 7]},
            "circumference_km": round(CIRCUMFERENCE_KM),
            "km_per_px_equator": round(KM_PER_PX, 1),
        },
        "places": places,
        "landmarks": {
            "infection_impact_sites": impacts,
        },
        "regions": {
            "cultural": cultural,
            "political": {
                "rule": "each capital claims the land it reaches overland first; seas block claims",
                "reach_km": 2400,
                "unclaimed_habitable_land_share": 0.65,
                "generator": "tools/regions.py",
                "map": "assets/maps/verlassen_regions_draft_v0.1.png",
                "capitals": ids,
            },
        },
        "currencies": {
            "regional": [
                {"id": cid, "name": None, "rate": None, "issued_by": iss, "also_used_in": also}
                for cid, iss, also in CURRENCIES
            ],
            "offworld": {"name": "Manna", "exchange": "spaceport only", "where": [1]},
            "rules": [
                "money has no weight and is held by the M.U.L.E., bank accounts included",
                "no spending while the M.U.L.E. is knocked out or away",
                "no theft",
                "on death, money transfers to the successor with the M.U.L.E.",
                "towns have banks",
            ],
        },
        "straight_line_km": distances,
        "open": [
            "currency names and exchange rates",
            "leader title (lord or mayor) per place",
            "notable people's roles",
            "detailed biomes per region",
            "final road network and route distance ranges",
            "the two brothers' names",
            "who runs the region's space station",
        ],
    }


if __name__ == "__main__":
    data = build()
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {OUT.relative_to(HERE.parent)}  v{data['version']}")
    for p in data["places"]:
        print(f"  {p['id']:>2} {p['name']:<15} {p['grid']:<4} lat {p['lat']:>7} lon {p['lon']:>7}  {p['cultural_region']:<16} {p['currency']}")
    for i in data["landmarks"]["infection_impact_sites"]:
        print(f"  impact {i['id']} {i['grid']:<4} lat {i['lat']:>7} lon {i['lon']:>7}")
