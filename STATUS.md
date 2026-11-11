# Status

**STATUS v0.17, 2026-11-10**

## Where things stand

- **Stage 0 (concept lock): closed 2026-11-10.**  The concept, the world of Verlassen, and the mechanics list are written down.
- No game code exists yet.  The Godot project has not been created.
- Every file carries a version.  `tools/version_check.py` verifies them against `VERSIONS.md`.  `tools/system_report.py` writes a full diagnostic report to `diagnostics/`.
- World tools exist in `tools/` (globe, places, regions, person names), with canon maps in `assets/maps/`.

## Next steps (Nathan picks the order)

1. **Stage 1, A2R-102 (in progress):** `docs/design/zones.md` v0.1 holds Nathan's direction and Claudia's drafts.  Next: Nathan reviews the drafts, then the open items (sizes, travel speeds, montage events, catch-up rules, biomes, route distances, first city, zone graph format).
2. **Draft for Nathan:** cold-rated fliers cost more, so money decides who flies in the cold year (world.md).
3. **Stage S:** guided, secured setup of Nathan's PC (Timeshift, Claude Code, Godot 4).  Best done at the machine.
4. **Design gaps:** stats and skills (#35, the biggest), trade (#70), currency names and rates, what the infection does.

## Open decisions

- Listed at the bottom of `docs/design/concept.md` (Open items) and `docs/design/world.md` (Open).

## Last session

- 2026-11-10 (Claudia): concept v0.81.  Nathan: successors are random and not all young; ages and training span later.

- 2026-11-10 (Claudia): concept v0.80.  Nathan: after the successor's walk-up, a montage of a year or so explains the training.

- 2026-11-10 (Claudia): concept v0.79.  Nathan: a successor who reaches a port gets the same story with a few word changes; it is not their clone, but they learn about it; the struggle to be a Lancer is the same.

- 2026-11-10 (Claudia): concept v0.78, mechanics v0.37.  Nathan: companions follow the no-miss rule for now; low skill can add debuffs instead.

- 2026-11-10 (Claudia): concept v0.77, mechanics v0.36.  Nathan: enemies are deadly too, so defenses and hard cover come in; the successor is the same as the main character.

- 2026-11-10 (Claudia): concept v0.76, mechanics v0.35.  Nathan: no ranged skill; the player is a Lancer and knows how to shoot; shots hit, minus effects or armor; mechanic #47d.

- 2026-11-10 (Claudia): started `docs/design/zones.md` v0.1 for A2R-102.  Nathan: three layers (globe, region map as the RimWorld world map equivalent, local maps); RimWorld map sizes; Oregon Trail montage travel; walking the full distance allowed; catch-up run on returning to a site; handcrafted walled cities with gates, built one at a time, only important areas mapped; most landmarks random by seed, key areas fixed; landmarks follow the land; seeds tied to generator version.

- 2026-11-10 (Claudia): world.md v0.64.  Nathan: the upper edges take the -50 shift on top of their cold and might reach -150 F in an established cold year.

- 2026-11-10 (Claudia): world.md v0.63.  Nathan: cold-year grounding is a modern standard; far-future fliers may have solved it, though physics may still limit things, and lack of money prevents most innovation.

- 2026-11-10 (Claudia): A2R-101 locked and done at planet data v0.1.  Nathan: droids are dumber than a CompCon, the M.U.L.E. is smarter than a standard CompCon; forced truce on hold as engine mechanic #93; downed flier is random seed-spawned event #94.  Cold-year grounding back to draft until discussed.

- 2026-11-10 (Claudia): world.md v0.61.  Nathan: a remote start can be years before the player reaches a main settlement.  Distances from habitable land to the nearest place measured on the canon globe and recorded.

- 2026-11-10 (Claudia): world.md v0.60, War at continent scale.  Nathan: long distances between rivals are good (Nausicaa-style wars with fliers and missiles); far future tech with fliers, droids, and mutants; air fleets sit out the cold year; downed fliers in the remote wild are resources, rescues, and faction hooks.  The planet data file is unchanged.

- 2026-11-10 (Claudia): A2R-101 planet data file v0.1.  `tools/planet_pack.py` packs the locked facts from `world.md`, `places_v1.0.json`, `names_v0.1.json`, and the seed 2718 globe into `tools/data/planet_verlassen.json`.  Decisions only; open items are null and listed under `open`.  Impact sites recomputed from the globe and checked against M3, T3, J10.  Straight-line distances use a planet 1.1 times Earth's width (about 61 km per map pixel).

- 2026-11-10 (Claudia): design decisions.  Money is weightless and held by the M.U.L.E., bank accounts included; no spending while it is out, no theft, transfers to the successor.  Damage types lean on Lancer (Crystalline for the infection; heat is environmental).  Range and Line attack patterns.  The infection is the seed crystal: an alien mineral that converts salt, minerals, bone, and teeth, refracts beams, is brittle to Kinetic and Explosive, slows in the cold, and moves the infected by piezoelectric control.  The infected are complicators; people are the villains.  Crystal hive mind parked as a possible expansion.
- Next thread (Nathan): the planet data file, A2R-101.

- 2026-11-10 (Claudia): moved maps and art from `docs/` to `assets/` so `docs/` stays text only and fits the claude.ai project sync.

- 2026-11-10 (Claudia): versioning and diagnostics.  Versions added to every tool and data file, art renamed with `_v1`, `version_check.py` and `system_report.py` added, rules written into `AGENTS.md`, mechanic #92 drafted.

- 2026-11-10 (Claudia): repo cleanup.  Design docs moved to `docs/design/`, the plan to `docs/plan/`, concept and world sections put in logical order, stale open-items lists refreshed, and `AGENTS.md`, `CLAUDE.md`, `STATUS.md`, and `.gitignore` added.
