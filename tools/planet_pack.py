"""Alpha2-Roger planet pack v0.11: packs every locked Verlassen fact into one data file the engine reads (A2R-101).

Sources (the pack never invents data; it only gathers and converts):
  tools/data/places_v1.0.json      the ten places and their pixel coordinates
  tools/data/names_v0.1.json       cultural regions, second cultures, word order
  tools/globe_candidates.py        the canon globe, seed 2718, for the three impact sites
  docs/design/world.md v0.99       planet facts, climate lines, biomes, the highest point, cultural regions, currencies, notable people, road network (copied in below)
  docs/design/zones.md v0.64       routes (road, path, ferry) and the region biome rules (copied in below)

Only decisions go in the file.  Drafts stay in world.md until Nathan approves them.  Anything still undecided
is null and listed under "open".

Run:  python3 tools/planet_pack.py      writes tools/data/planet_verlassen.json
"""
__version__ = "0.11"

import json, math
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT = DATA / "planet_verlassen.json"
FILE_VERSION = "0.11"          # bump on every change to the output

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


def globe_land():
    """The canon globe's elevation field and land mask, read the way tools/music_areas.py reads them."""
    import numpy as np
    src = (HERE / "globe_candidates.py").read_text().split("seeds = [")[0]
    G = {}
    exec(src, G)
    elev, _ = G["sphere_field"](np.random.default_rng(SEED))
    return elev, elev > np.quantile(elev, 1 - G["LAND_FRAC"])


def highest_point():
    """The globe pixel with the highest elevation: the planet's top, about 6,500 m by the height scale."""
    import numpy as np
    elev, _ = globe_land()
    y, x = np.unravel_index(int(np.argmax(elev)), elev.shape)
    return int(y), int(x)


def landmasses():
    """Label each landmass on the canon globe (8-connected, wrapping east-west)."""
    import numpy as np
    from scipy import ndimage
    _, land = globe_land()
    lab, _ = ndimage.label(land, structure=np.ones((3, 3)))
    for y in range(H):                       # join masses that touch across the wrap edge
        for dy in (-1, 0, 1):
            yy = y + dy
            if 0 <= yy < H and land[y, 0] and land[yy, W - 1] and lab[y, 0] != lab[yy, W - 1]:
                lab[lab == lab[yy, W - 1]] = lab[y, 0]
    return lab


# ---- Locked facts, copied from docs/design/world.md v0.99 (Nathan's decisions) ----

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

# Routes (Nathan, 2026-11-11 and 2026-11-12; world.md Roads and bridges, zones.md Routes)
ROADS = [[3, 8, 1], [2, 6, 10, 7]]   # chains, in the order Nathan listed them (approved 2026-11-13)
PATHS = [[5, 1], [2, 10], [4, 9]]    # complete (Nathan, 2026-11-13); seeded offshoots come from the seed
FERRY_TOWNS = [1, 8, 2, 4, 9, 10]
INLAND_FERRY_TOWNS = [1, 9]          # about 190 km and 195 km from the nearest coast: each gets a landing there

# Climate (world.md, Climate bands; latitude lines approved by Nathan 2026-11-13)
LATITUDE_LINES = [  # latitude, normal summer high, normal winter low, cold-year high, cold-year low (F)
    (0, 90, 72, 40, 22), (10, 93, 66, 43, 16), (20, 97, 55, 47, 5), (30, 97, 38, 47, -12),
    (40, 88, 20, 38, -30), (50, 76, 3, 26, -47), (60, 66, -15, 16, -65)]

# Biomes (world.md, Biomes; approved by Nathan 2026-11-11): id, name, where, feel or notes
LAND_BIOMES = [
    (1, "Warm forest", "warm band, wet", "evergreen oak and pine, richest forage"),
    (2, "Warm grassland", "warm band, medium", "open plains, herds"),
    (3, "Scrub desert", "warm band, dry", "thorn brush, scarce water"),
    (4, "Mixed forest", "temperate, wet", "deciduous and conifer woods"),
    (5, "Prairie", "temperate, medium", "tall grass, good farming soil"),
    (6, "Steppe", "temperate, dry", "short grass, wind"),
    (7, "Marsh", "wet lowlands, any band", "reeds, bogs, slow travel, bad water"),
    (8, "Taiga", "cold band", "dense conifers, deep snow"),
    (9, "Tundra", "cold band, open", "moss, lichen, migrating herds"),
    (10, "Cold barrens", "cold band, dry", "rock and gravel"),
    (11, "Highlands", "elevation, any band", "ridges, scree, passes, caves"),
    (12, "Ice", "poles, highest peaks", "permanent ice"),
    (13, "Coast", "edge of land", "beaches, cliffs, tidal flats"),
]
WATER_BIOMES = [
    (14, "Deep ocean", "open water; boats, or sea ice in a cold year"),
    (15, "Warm ocean", "warm-band shallows, good fishing; chills hard in the cold year"),
    (16, "Coral reef", "cold-water reefs, since tropical reef corals would die every cold year; rich fishing, navigation hazard"),
    (17, "Inland sea", "huge enclosed water, can be brackish, like the Caspian"),
    (18, "Inland lake", "fresh water, fish, freezes in winter"),
    (19, "River", "river corridor: channel plus floodplain; big rivers only"),
    (20, "Salt river", "saline, flowing from the salt basins; undrinkable, a trade route"),
]

HIGHEST = {"name": "Yamajira", "grid": "M10", "height_m": 6500}   # Nathan named it 2026-11-13


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
            "territory": p["id"],             # each place is the capital of its own territory
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

    hy, hx = highest_point()
    assert grid_ref(hy, hx) == HIGHEST["grid"], f"highest point moved: {grid_ref(hy, hx)}"
    hla, hlo = latlon(hy, hx)
    top = {"name": HIGHEST["name"], "grid": HIGHEST["grid"], "px": {"x": hx, "y": hy}, "lat": hla, "lon": hlo,
           "height_m": HIGHEST["height_m"]}

    ids = sorted(coords)
    distances = {str(a): {str(b): great_circle_km(coords[a], coords[b]) for b in ids if b != a} for a in ids}

    lab = landmasses()
    mass = {p["id"]: int(lab[p["px"]["y"], p["px"]["x"]]) for p in places}
    for link in ROADS + PATHS:                # every road and path must stay on one landmass
        assert len({mass[i] for i in link}) == 1, f"route crosses water: {link}"
    RAIL = [1, 2, 6, 10, 7, 5, 3, 8]            # rail loop; tunnels between 1 and 2 (H8) and 7 and 5 (V5 to V6)
    for a_, b_ in zip(RAIL, RAIL[1:] + RAIL[:1]):
        tunnel = {a_, b_} in ({1, 2}, {7, 5})
        assert (mass[a_] != mass[b_]) == tunnel, f"rail leg {a_} to {b_}: tunnel={tunnel} but landmasses {mass[a_]} and {mass[b_]}"

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
            "world": "docs/design/world.md v0.99",
            "zones": "docs/design/zones.md v0.64",
            "places": f"tools/data/places_v1.0.json v1.0",
            "names": f"tools/data/names_v{names['version']}.json v{names['version']}",
            "globe": "tools/globe_candidates.py v0.3.1",
        },
        "planet": {
            "official_name": "Kepler-64432p",
            "local_name": "Verlassen",
            "local_name_meaning": "abandoned, forsaken, left behind (German)",
            "era_u": 5071,
            "star": {"class": "G", "color": "yellow", "mass_solar": 1.0},
            "orbit_au": 1.1,
            "insolation_earth": 0.8,
            "radius_earths": RADIUS_EARTHS,
            "gravity_g": 1.0,
            "moons": 0,
            "rings": 0,
            "calendar": {
                "months": 12,
                "days_per_month": 35,
                "days_per_week": 7,
                "days_per_year": 420,
                "day_length_hours": None,
            },
            "cold_year": {
                "every_n_years": 3,
                "length_planet_years": 1,
                "temperature_shift_f": -50,
                "cause": "gas giant neighbor in a 3:1 orbital resonance",
                "cause_detail": None,
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
        "climate": {
            "latitude_lines_f": [
                {"lat": la, "normal_high": nh, "normal_low": nl, "cold_year_high": ch, "cold_year_low": cl}
                for la, nh, nl, ch, cl in LATITUDE_LINES
            ],
            "ice_caps_f": {"normal_low": -80, "cold_year_low": [-150, -130]},
            "lines_note": "inland temperatures, summer high and winter low; hemispheres run opposite seasons",
            "lapse_f_per_m": 0.01148,
            "lapse_note": "about 3.5 F per 1,000 ft",
            "greenhouse": "Earth-like temperatures under about 80% of Earth's sunlight: the terraformers thickened the greenhouse "
                          "to make up for the dimmer sun (Nathan, 2026-11-13)",
        },
        "biomes": [{"id": i, "name": n, "kind": "land", "where": w, "feel": f} for i, n, w, f in LAND_BIOMES]
                  + [{"id": i, "name": n, "kind": "water", "notes": f} for i, n, f in WATER_BIOMES],
        "region_rules": {
            "source": "docs/design/zones.md, Region biome rules (approved by Nathan 2026-11-12); read by tools/region_gen.py",
            "cells_per_globe_px": 16,
            "height": {"top_m": HIGHEST["height_m"], "exponent": 1.63},
            "temperature": "latitude-line yearly mean (summer high plus winter low, halved) minus the lapse rate",
            "bands_f": {"warm_min": 60, "temperate_min": 45},
            "moisture": {"coast_fade_km": 700, "river_boost": 0.35, "river_fade_km": 25, "noise": 0.08,
                         "wet_min": 0.55, "dry_below": 0.30},
            "base_biomes": {"warm": [1, 2, 3], "temperate": [4, 5, 6], "cold": [8, 9, 10],
                            "order": "wet, middle, dry"},
            "overrides": [
                {"biome": 11, "min_m": 2000},
                {"biome": 7, "max_m": 150, "min_moisture": 0.75, "max_river_km": 15},
                {"biome": 19, "max_river_km": 5, "max_m": 2000},
                {"biome": 13, "touches_sea": True, "max_m": 300},
            ],
            "overrides_note": "applied in this order on land; a later rule wins; all water is ocean until the water biomes are built",
            "rivers": {"river_min_flow_cells": 1800, "creek_min_flow_cells": 450,
                       "river_drains_km2": 26000, "creek_drains_km2": 6600},
            "salinity_ppt": {"fresh_below": 0.5, "brackish_to": 30, "seawater": 35},
            "not_yet": ["ice rule", "water biomes", "infection levels", "features"],
        },
        "places": places,
        "landmarks": {
            "infection_impact_sites": impacts,
            "highest_point": top,
        },
        "heights": {
            "planet_top_m": HIGHEST["height_m"],
            "rule": "docs/design/zones.md, Region biome rules, step 2",
        },
        "music": {
            "areas": "tools/data/music_areas.json",
            "bible": "docs/design/music.md",
            "rule": "music lives in its own files and evolves on its own; the planet file only points to it (Nathan, 2026-11-13)",
        },
        "cultural_regions": cultural,
        "territories": {
            "rule": "each capital claims the land it reaches overland first; seas block claims",
            "reach_km": 2400,
            "unclaimed_habitable_land_share": 0.65,
            "generator": "tools/regions.py",
            "map": "assets/maps/verlassen_regions_draft_v0.1.png",
            "capitals": ids,
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
        "routes": {
            "roads": [{"from": a, "to": b} for r in ROADS for a, b in zip(r, r[1:])],
            "roads_note": "chains in the order Nathan listed them; the generator's routes layer draws the paths on the globe, then each region, then each local map",
            "paths": [{"from": a, "to": b} for a, b in PATHS],
            "paths_complete": True,
            "ferry_towns": FERRY_TOWNS,
            "ferry_rule": "any ferry town reaches any other by sea; routes come from sea pathfinding",
            "ferry_landings": {"towns": INLAND_FERRY_TOWNS,
                               "rule": "an inland ferry town gets a landing, a small port on the nearest coast tied to the town by road"},
            "ferry_routes": [
                {"to": 10, "via": "the passage east of Shio Loch (W4 and W5), about 900 km wide at its narrowest (W5)",
                 "why": "Kawa Fada's inner sea opens only to the north; ships from the central sea go around the north near the ice"},
            ],
            "cold_year": "sea ice opens new routes; Setareh Minato (1) to Ikh Gawa (2) becomes a land trip",
            "seed_rules": {
                "canon": "roads between the ten places are the same on every seed",
                "seeded": "small paths to wild settlements, bandit camps, and similar offshoots are random by the seed",
            },
            "distances": "calculated, never stored: pathfinding across region cells with a cost per cell "
                         "(biome, climbing, rivers, roads, infected ground) and the speed table; "
                         "the montage planner shows a range of days",
            "rail": {
                "owner": 1,
                "boarding": "only in a city; no stops in the wild",
                "line": "one loop, in this order, back to the start",
                "stations": [1, 2, 6, 10, 7, 5, 3, 8],
                "off_line": {"places": [4, 9], "reach": "by plane or ferry"},
                "undersea": "underwater rails or waterproof tunnels at a couple of crossings; deadly to walk",
                "train": "bullet train with a front piercer; plows through ice, snow, animals, creatures, avalanches",
                "in_game": ["fast travel from city to city",
                            "track-side event: when the player builds next to the track, the train occasionally crosses and hits everything"],
                "tunnels": [
                    {"id": "H8", "between": [1, 2], "from": {"grid": "H8", "lat": -15.8, "lon": -71.5}, "to": {"grid": "H8", "lat": -19.8, "lon": -66.0},
                     "km": 800, "connects": "the west continent (Setareh Minato) to Ikh Gawa's continent"},
                    {"id": "V5-V6", "between": [7, 5], "from": {"grid": "V5", "lat": 24.8, "lon": 143.0}, "to": {"grid": "V6", "lat": 13.8, "lon": 145.5},
                     "km": 1400, "connects": "Shio Loch's continent to the far side of the west continent, which runs down and across the wrap to Khaluun Onsen"},
                ],
                "window_view": "Yamajira, from the Davs Mizuumi leg, shown during a montage",
                "source": "docs/design/world.md, The rail line (Nathan, 2026-11-13)",
            },
            "types": ["road", "path", "animal_trail"],
            "types_rules": "docs/design/zones.md, Routes (road types, wheels)",
        },
        "straight_line_km": distances,
        "open": [
            "currency names and exchange rates",
            "day length (calendar assumes 24 hours)",
            "leader title (lord or mayor) per place",
            "notable people's roles",
            "road paths drawn on the globe (the generator's routes layer)",
            "cold-year cause detail: a dust band the gas giant herds, or its pull (decide with the map and art designs)",
            "Svetla Hama is a ferry town about 670 km from the open sea, by a small lake: sea landing, lake ferry, or no ferry",
            "rail: schedule and ticket prices; the routes layer draws the line",
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
