# Versions

**VERSIONS v1.35, 2026-11-11**

Current version of every deliverable.  Update the row whenever a file changes.  Run `python3 tools/version_check.py` to confirm every row matches its file.

## Documents

| File | Version | Date | Notes |
|---|---|---|---|
| VERSIONS.md | v1.35 | 2026-11-11 | This table |
| README.md | v0.5 | 2026-11-10 | Pitch, pillars, repo map, license credits |
| AGENTS.md | v0.4 | 2026-11-10 | Rules for AI collaborators: lanes, conventions, versions, diagnostics |
| CLAUDE.md | v0.1 | 2026-11-10 | Pointer to AGENTS.md for Claude Code |
| STATUS.md | v0.21 | 2026-11-11 | Where things stand and next steps |
| LICENSE.md | v0.2 | 2026-11-09 | All rights reserved, plus Lancer Third Party License terms |
| .gitignore | v0.2 | 2026-11-10 | Ignores caches, Godot imports, diagnostics/ |
| docs/design/concept.md | v0.81 | 2026-11-10 | Game design |
| docs/design/world.md | v0.66 | 2026-11-11 | The planet Verlassen |
| docs/design/mechanics.md | v0.39 | 2026-11-11 | Master mechanics checklist by build tier |
| docs/design/zones.md | v0.2 | 2026-11-11 | Zones and travel spec (A2R-102) |
| docs/plan/Alpha2Roger_Project_Plan.md | v0.26 | 2026-11-11 | Stages, task IDs, gates, changelog |

## Tools and data

| File | Version | Date | Notes |
|---|---|---|---|
| tools/globe_candidates.py | v0.3.1 | 2026-11-09 | Seeded globe generator: land, climate, rivers, salt lakes, geothermal, impacts |
| tools/place_pins.py | v1.0.1 | 2026-11-09 | Ten places by world rules, grid overlay, names; writes places JSON |
| tools/regions.py | v0.1 | 2026-11-09 | Political regions by overland reach |
| tools/name_gen.py | v0.1 | 2026-11-09 | Seeded person name generator |
| tools/planet_pack.py | v0.2 | 2026-11-11 | Packs locked world facts into the planet data file (A2R-101) |
| tools/version_check.py | v0.1 | 2026-11-10 | Checks every file has a version and VERSIONS.md matches |
| tools/system_report.py | v0.1 | 2026-11-10 | One-command diagnostic report for Claudia |
| tools/data/places_v1.0.json | v1.0 | 2026-11-09 | Ten places with coordinates |
| tools/data/planet_verlassen.json | v0.2 | 2026-11-11 | Planet data file the engine reads: seed, places, landmarks, regions, currencies (A2R-101, locked) |
| tools/data/names_v0.1.json | v0.1 | 2026-11-09 | Name lists per culture, region rules, blacklist |

## Maps and art

| File | Version | Date | Notes |
|---|---|---|---|
| assets/maps/verlassen_globe_candidates_v0.3.1.png | v0.3.1 | 2026-11-09 | Four candidate globes |
| assets/maps/verlassen_globe_v1.0.png | v1.0 | 2026-11-09 | Canonical globe, seed 2718 |
| assets/maps/verlassen_pins_draft_v0.1.png | v0.1 | 2026-11-09 | Draft pins (superseded by places v1.0) |
| assets/maps/verlassen_places_v1.0.png | v1.0 | 2026-11-09 | Ten named places |
| assets/maps/verlassen_regions_draft_v0.1.png | v0.1 | 2026-11-09 | Political regions (accepted) |
| assets/art/mule/ | v1 | 2026-11-09 | M.U.L.E. references: Nathan's miniature and Mara variants |
| assets/art/reference/rimworld_reference_pegs_clothing_v1.png | v1 | 2026-11-10 | RimWorld reference screenshot |
