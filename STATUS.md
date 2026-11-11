# Status

**STATUS v0.44, 2026-11-11**

## Where things stand

- **Stage 0 (concept lock): closed 2026-11-10.**  The concept, the world of Verlassen, and the mechanics list are written down.
- No game code exists yet.  The Godot project has not been created.
- Every file carries a version.  `tools/version_check.py` verifies them against `VERSIONS.md`.  `tools/system_report.py` writes a full diagnostic report to `diagnostics/`.
- World tools exist in `tools/` (globe, places, regions, person names), with canon maps in `assets/maps/`.

## Next steps (Nathan picks the order)

1. **Stage 1, A2R-102 (in progress):** `docs/design/zones.md` v0.2: Nathan's direction, with Claudia's drafts approved 2026-11-11.  Next: the open items (sizes, travel speeds, montage events, catch-up rules, biomes, route distances, first city, zone graph format).
2. **Draft for Nathan:** cold-rated fliers cost more, so money decides who flies in the cold year (world.md).
3. **Stage S:** guided, secured setup of Nathan's PC (Timeshift, Claude Code, Godot 4).  Best done at the machine.
4. **Design gaps:** stats and skills (#35, the biggest), trade (#70), currency names and rates, what the infection does.

## Open decisions

- Listed at the bottom of `docs/design/concept.md` (Open items) and `docs/design/world.md` (Open).

## Last session

- 2026-11-11 (Claudia): concept v0.93.  Nathan: the stats panel can be hidden for full screen (best screenshots).

- 2026-11-11 (Claudia): concept v0.92.  Nathan approved the stats display: slim always-on wrist-unit panel (vitals, temperatures, date, message log), full sheet on a key.

- 2026-11-11 (Claudia): concept v0.91.  Nathan: RPG-style dialogue, on-screen comics for the major story beats.  Stats window (Qud panel or RimWorld hidden) under discussion.

- 2026-11-11 (Claudia): concept v0.90.  Nathan approved anger outlets and NPC judgment (a story, not weird pawn rules).  Narrative presentation (RPG or visual novel) under discussion.

- 2026-11-11 (Claudia): concept v0.89.  Nathan: no rage breaks for NPCs either (no setting the stockpile on fire).  Drafts: social outlets for anger; camp rules, traits, and stats drive NPC judgment.

- 2026-11-11 (Claudia): zones.md v0.13.  Nathan approved the travel cost list; Intelligence builds make overworld travel much easier.

- 2026-11-11 (Claudia): zones.md v0.12.  Nathan: region map travel is set-a-destination like RimWorld, no WASD; world travel is the montage and costs supplies with considerable impact (Oregon Trail logic).

- 2026-11-11 (Claudia): zones.md v0.11.  Nathan: edge walking happens inside a 9-map section around the middle map, four directions only; more diversity, more Qud than RimWorld.

- 2026-11-11 (Claudia): zones.md v0.10.  Nathan: local maps are 256 by 256 (RimWorld default) after comparing 256 and 512 samples; move one map left, right, up, or down without the region map.

- 2026-11-11 (Claudia): zones.md v0.9.  Nathan: Earth-style heat bands give each region and square a base heat value.  Drafts: latitude, lapse rate, coast, geothermal; computed from exact latitude.

- 2026-11-11 (Claudia): zones.md v0.8.  Nathan approved the generation order; major cities are fixed and handcrafted, the exception to generation.

- 2026-11-11 (Claudia): zones.md v0.7.  Nathan: the engine can slip a settlement into a map and move the river accordingly.  Draft generation order added.

- 2026-11-11 (Claudia): zones.md v0.6.  Nathan: RimWorld edge logic, a river only has to match where it enters and leaves a map.  Replaces the shared-noise draft.

- 2026-11-11 (Claudia): zones.md v0.5.  Nathan: blockiness at the region and local scale is normal; approved local coordinates.  Drafts: shared noise across edges, biome blending, stitched visited-map view.

- 2026-11-11 (Claudia): zones.md v0.3.  Nathan: the montage is overmap travel math; the magic is the region and local maps; start by building one region and one local map.  Grid shape under discussion.
- 2026-11-11 (Claudia): zones.md v0.4.  Nathan: square grid across the board.  Power-of-two sizes anchored on the globe pixel drafted for approval.

- 2026-11-11 (Claudia): concept v0.88, mechanics v0.44.  Nathan: Charisma makes companions available earlier, not more; the camp cap reserves the back-end engine and may expand later.

- 2026-11-11 (Claudia): concept v0.87.  Nathan approved backgrounds setting stats; Intelligence builds get drones and faster tech, Charisma builds get more NPCs and easier friendships; not every problem is solved with guns (factions survive too; raiders stay hostile).

- 2026-11-11 (Claudia): concept v0.86.  Nathan: a genetically modified super soldier is one background option, background fluff only; all Lancers are heroes who got there by various means.

- 2026-11-11 (Claudia): concept v0.85, mechanics v0.43.  Nathan: adapt Lancer pilot gear to a traditional form; heavy weapons need STR; top-down TTRPG-style map.  Drafts: weapon classes, archaic ammo, item traits.

- 2026-11-11 (Claudia): concept v0.84, mechanics v0.42.  Nathan: create pilot talents (buffs); use Lancer gear names but define effects ourselves; weapons are a start to flavor.  Drafts: tag rewrite, visor stops snow blindness, three-rank talents.

- 2026-11-11 (Claudia): concept v0.82, mechanics v0.40.  Nathan set the character system direction (#35): traditional stats, Lancer background labels as stat configurations, no triggers, uncapped builds, tune after prototype, Starforged-style tables.
- 2026-11-11 (Claudia): concept v0.83, mechanics v0.41.  Nathan: Starforged was only an example of data tables; we do not use it.  SPECIAL noted as grown out of GURPS.

- 2026-11-11 (Claudia): zones.md v0.2.  Nathan approved all of Claudia's zones drafts (scale numbers, chunks, layers built top-down, walking equals montage, edge walking, seeded catch-up, city as hub, outskirts, early crash fencing, seed tiers, delta saves).  Next talks: Godot, stats, gear.

- 2026-11-11 (Claudia): mechanics v0.39.  Nathan: temperature drives the map temperature, which drives plants, player temperature, and so forth (#14).

- 2026-11-11 (Claudia): world.md v0.66.  Nathan: the -50 cold-year shift stays; freezing at night is fine since the wild would not thaw before refreezing.  Latitude lines and city cold-year temperatures added as drafts.

- 2026-11-11 (Claudia): calendar locked by Nathan: 12 months of 35 days, 420 days, aligned to the orbit; meme ignored.  world.md v0.65, mechanics v0.38, planet pack and planet data file v0.2 (calendar block; day length open).

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
