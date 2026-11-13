# Versions

**VERSIONS v1.202, 2026-11-13**

Current version of every deliverable.  Update the row whenever a file changes.  Run `python3 tools/version_check.py` to confirm every row matches its file.

## Documents

| File | Version | Date | Notes |
|---|---|---|---|
| VERSIONS.md | v1.202 | 2026-11-13 | This table |
| README.md | v0.6 | 2026-11-13 | Pitch, pillars, repo map, license credits |
| AGENTS.md | v0.7 | 2026-11-13 | Rules for AI collaborators: lanes, conventions, versions, diagnostics; music lane |
| CLAUDE.md | v0.1 | 2026-11-10 | Pointer to AGENTS.md for Claude Code |
| STATUS.md | v0.168 | 2026-11-13 | Where things stand and next steps |
| LICENSE.md | v0.2 | 2026-11-09 | All rights reserved, plus Lancer Third Party License terms |
| .gitignore | v0.2 | 2026-11-10 | Ignores caches, Godot imports, diagnostics/ |
| docs/design/concept.md | v1.22 | 2026-11-13 | Game design |
| docs/design/music.md | v0.33 | 2026-11-13 | Music bible: tools, sound, the riff (Kaze), radio music |
| docs/design/world.md | v1.05 | 2026-11-13 | The planet Verlassen |
| docs/design/mechanics.md | v0.81 | 2026-11-13 | Master mechanics checklist by build tier |
| docs/design/zones.md | v0.69 | 2026-11-13 | Zones and travel spec (A2R-102) |
| docs/plan/Alpha2Roger_Project_Plan.md | v0.32 | 2026-11-13 | Stages, task IDs, gates, changelog |

## Tools and data

| File | Version | Date | Notes |
|---|---|---|---|
| tools/globe_candidates.py | v0.3.1 | 2026-11-09 | Seeded globe generator: land, climate, rivers, salt lakes, geothermal, impacts |
| tools/place_pins.py | v1.0.1 | 2026-11-09 | Ten places by world rules, grid overlay, names; writes places JSON |
| tools/regions.py | v0.1 | 2026-11-09 | Political regions by overland reach |
| tools/name_gen.py | v0.1 | 2026-11-09 | Seeded person name generator |
| tools/planet_pack.py | v0.14 | 2026-11-13 | Packs locked world facts into the planet data file (A2R-101) |
| tools/region_gen.py | v0.3.1 | 2026-11-13 | Builds a region's 480 x 480 cells (R5 only for now) |
| tools/culture_map.py | v0.2 | 2026-11-13 | Builds the culture map (culture of every globe pixel) |
| tools/music_areas.py | v0.2 | 2026-11-13 | Pairs the culture map with music: builds the music areas map and data |
| tools/version_check.py | v0.2 | 2026-11-12 | Checks every file has a version and VERSIONS.md matches; audio and MIDI by file name |
| tools/system_report.py | v0.1 | 2026-11-10 | One-command diagnostic report for Claudia |
| tools/data/places_v1.0.json | v1.0 | 2026-11-09 | Ten places with coordinates |
| tools/data/planet_verlassen.json | v0.14 | 2026-11-13 | Planet data file the engine reads: seed, places, landmarks, climate lines, biomes, region rules, cultural regions, territories, currencies, routes (A2R-101, locked) |
| tools/data/regions/R5.json | v0.3.1 | 2026-11-13 | R5 region cells: biomes, rivers and creeks, heights |
| tools/data/culture_map.json | v0.2 | 2026-11-13 | Culture of every globe pixel: land cultures, ice, open water, base only (Japanese base implied) |
| tools/data/music_areas.json | v0.2 | 2026-11-13 | Music area of every globe pixel |
| tools/data/names_v0.1.json | v0.1 | 2026-11-09 | Name lists per culture, region rules, blacklist |

## Maps and art

| File | Version | Date | Notes |
|---|---|---|---|
| assets/maps/verlassen_globe_candidates_v0.3.1.png | v0.3.1 | 2026-11-09 | Four candidate globes |
| assets/maps/verlassen_globe_v1.0.png | v1.0 | 2026-11-09 | Canonical globe, seed 2718 |
| assets/maps/regions/R5_biomes_v0.3.1.png | v0.3.1 | 2026-11-13 | R5 biome map |
| assets/maps/verlassen_culture_v0.2.png | v0.2 | 2026-11-13 | Culture map |
| assets/maps/verlassen_music_areas_v0.1.png | v0.1 | 2026-11-12 | Music areas map |
| assets/maps/verlassen_pins_draft_v0.1.png | v0.1 | 2026-11-09 | Draft pins (superseded by places v1.0) |
| assets/maps/verlassen_places_v1.0.png | v1.0 | 2026-11-09 | Ten named places |
| assets/maps/verlassen_regions_draft_v0.1.png | v0.1 | 2026-11-09 | Political regions (accepted) |
| assets/art/mule/ | v1 | 2026-11-09 | M.U.L.E. references: Nathan's miniature and Mara variants |
| assets/audio/music/drafts/ | v5 | 2026-11-12 | Riff candidates v1; Kaze v2 theme; Kaze v3, v4, v5a, v5b songs: MIDI and OGG previews |
| assets/art/reference/rimworld_reference_pegs_clothing_v1.png | v1 | 2026-11-10 | RimWorld reference screenshot |
