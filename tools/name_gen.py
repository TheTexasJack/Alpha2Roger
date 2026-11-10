"""Alpha2-Roger person name generator v0.1.

regional_first:  regional given name + Japanese family name   (e.g. Shirin Kuroda)
japanese_first:  Japanese given name + regional family name   (e.g. Ren Gallagher)
Seeded, so the same seed always gives the same names.
"""
__version__ = "0.1"

import json, random, sys
from pathlib import Path

DATA = json.loads((Path(__file__).parent / "data" / "names_v0.1.json").read_text())

def person(region, rng):
    r = DATA["regions"][region]; c = DATA["cultures"][r["culture"]]; j = DATA["japanese"]
    while True:
        if r["order"] == "regional_first":
            name = f"{rng.choice(c['given'])} {rng.choice(j['family'])}"
        else:
            name = f"{rng.choice(j['given'])} {rng.choice(c['family'])}"
        if not any(b.lower() in name.lower().split() for b in DATA["blacklist"]):
            return name

PLACES = [(1, "Setareh Minato", "spaceport_coast"), (2, "Ikh Gawa", "southern_steppe"), (3, "Warmes Tani", "west_north"),
          (4, "Svetla Hama", "central_north"), (5, "Khaluun Onsen", "southern_steppe"), (6, "Davs Mizuumi", "southern_steppe"),
          (7, "Shio Loch", "empty_east"), (8, "Darya Kako", "spaceport_coast"), (9, "Zimna Toride", "central_north"),
          (10, "Kawa Fada", "empty_east")]

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 2718
    rng = random.Random(seed); used = set()
    for i, place, region in PLACES:
        n = person(region, rng)
        while n in used:
            n = person(region, rng)
        used.add(n)
        print(f"{i:>2}  {place:<15} {n}")
