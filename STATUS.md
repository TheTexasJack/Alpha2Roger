# Status

**STATUS v0.6, 2026-11-10**

## Where things stand

- **Stage 0 (concept lock): closed 2026-11-10.**  The concept, the world of Verlassen, and the mechanics list are written down.
- No game code exists yet.  The Godot project has not been created.
- Every file carries a version.  `tools/version_check.py` verifies them against `VERSIONS.md`.  `tools/system_report.py` writes a full diagnostic report to `diagnostics/`.
- World tools exist in `tools/` (globe, places, regions, person names), with canon maps in `assets/maps/`.

## Next steps (Nathan picks the order)

1. **Stage 1, A2R-101 (in review):** Nathan reviews `tools/data/planet_verlassen.json` v0.1 and locks it, or sends changes.
2. **Stage 1, A2R-102:** write the zone generator spec for Nathan's review before any code.
3. **Stage S:** guided, secured setup of Nathan's PC (Timeshift, Claude Code, Godot 4).  Best done at the machine.
4. **Design gaps:** stats and skills (#35, the biggest), trade (#70), currency names and rates, what the infection does.

## Open decisions

- Listed at the bottom of `docs/design/concept.md` (Open items) and `docs/design/world.md` (Open).

## Last session

- 2026-11-10 (Claudia): world.md v0.60, War at continent scale.  Nathan: long distances between rivals are good (Nausicaa-style wars with fliers and missiles); far future tech with fliers, droids, and mutants; air fleets sit out the cold year; downed fliers in the remote wild are resources, rescues, and faction hooks.  The planet data file is unchanged.

- 2026-11-10 (Claudia): A2R-101 planet data file v0.1.  `tools/planet_pack.py` packs the locked facts from `world.md`, `places_v1.0.json`, `names_v0.1.json`, and the seed 2718 globe into `tools/data/planet_verlassen.json`.  Decisions only; open items are null and listed under `open`.  Impact sites recomputed from the globe and checked against M3, T3, J10.  Straight-line distances use a planet 1.1 times Earth's width (about 61 km per map pixel).

- 2026-11-10 (Claudia): design decisions.  Money is weightless and held by the M.U.L.E., bank accounts included; no spending while it is out, no theft, transfers to the successor.  Damage types lean on Lancer (Crystalline for the infection; heat is environmental).  Range and Line attack patterns.  The infection is the seed crystal: an alien mineral that converts salt, minerals, bone, and teeth, refracts beams, is brittle to Kinetic and Explosive, slows in the cold, and moves the infected by piezoelectric control.  The infected are complicators; people are the villains.  Crystal hive mind parked as a possible expansion.
- Next thread (Nathan): the planet data file, A2R-101.

- 2026-11-10 (Claudia): moved maps and art from `docs/` to `assets/` so `docs/` stays text only and fits the claude.ai project sync.

- 2026-11-10 (Claudia): versioning and diagnostics.  Versions added to every tool and data file, art renamed with `_v1`, `version_check.py` and `system_report.py` added, rules written into `AGENTS.md`, mechanic #92 drafted.

- 2026-11-10 (Claudia): repo cleanup.  Design docs moved to `docs/design/`, the plan to `docs/plan/`, concept and world sections put in logical order, stale open-items lists refreshed, and `AGENTS.md`, `CLAUDE.md`, `STATUS.md`, and `.gitignore` added.
