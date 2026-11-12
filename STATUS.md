# Status

**STATUS v0.107, 2026-11-12**

## Where things stand

- **Stage 0 (concept lock): closed 2026-11-10.**  The concept, the world of Verlassen, and the mechanics list are written down.
- No game code exists yet.  The Godot project has not been created.
- Every file carries a version.  `tools/version_check.py` verifies them against `VERSIONS.md`.  `tools/system_report.py` writes a full diagnostic report to `diagnostics/`.
- World tools exist in `tools/` (globe, places, regions, person names), with canon maps in `assets/maps/`.

## Next steps (Nathan picks the order)

0. **Music:** get the Akai recording in Waveform (now required).  Then Nathan cleans up the Rory Dall feel test and adds an undertone or beat.  Target: the Irish wilds with samurai.
1. **Stage 1, A2R-102 (in progress):** `docs/design/zones.md`.  R5 biome rules approved and `tools/region_gen.py` v0.1 built R5.  Left: the zone graph format, then the spec goes to Nathan for approval.
2. **Draft for Nathan:** cold-rated fliers cost more, so money decides who flies in the cold year (world.md).
3. **Stage S:** guided, secured setup of Nathan's PC (Timeshift, Claude Code, Godot 4).  Best done at the machine.
4. **Design gaps:** stats and skills (#35, the biggest), trade (#70), currency names and rates, what the infection does.

## Open decisions

- Listed at the bottom of `docs/design/concept.md` (Open items) and `docs/design/world.md` (Open).

## Last session

- 2026-11-12 (Claudia): zones.md v0.46, mechanics v0.57.  Nathan approved rate-based machines and the performance readout details.

- 2026-11-12 (Claudia): zones.md v0.45, mechanics v0.56.  Nathan sides with a live tracked map (strategic tool, the feeling of live areas) and agrees to test it once the engine exists; catch-up stays the base.  Performance readout needed in the GM tool and system report (#87e).

- 2026-11-12 (Claudia): zones.md v0.44.  Nathan: beacons can watch enemy bases; beacons and the M.U.L.E. outline NPCs without removing fog of war.  Drafts: snapshot view via catch-up, thermal sensing, cold infected, beacon range and risk.

- 2026-11-12 (Claudia): zones.md v0.43.  Nathan approved the tracker as a physical beacon on one local map; placing it needs the player on that map with the M.U.L.E.

- 2026-11-12 (Claudia): zones.md v0.42, mechanics v0.55.  Nathan: hybrid map storage (baked maps where the player builds); nothing tracked by default; quests and story events flag automatically; the M.U.L.E. has one tracker (zone loader, #87d), settings flag for more.

- 2026-11-12 (Claudia): zones.md v0.41.  Nathan approved the region biome rules.  New `tools/region_gen.py` v0.1 builds R5: `tools/data/regions/R5.json` v0.1 (biomes, rivers and creeks, heights) and `assets/maps/regions/R5_biomes_v0.1.png`.

- 2026-11-12 (Claudia): zones.md v0.40, mechanics v0.54.  Nathan approved the MULEpad features.

- 2026-11-12 (Claudia): zones.md v0.39, mechanics v0.53.  Nathan approved the address system, with a MULEpad (in-game notes in the M.U.L.E.) to pin, track, and find addresses (#87a).

- 2026-11-12 (Claudia): zones.md v0.38.  Nathan: a river is only needed for river testing, seed randomness guides specifics (S1 stays); we need an address system like the overmap's.  Draft: R5-cell-map-tile addresses.

- 2026-11-12 (Claudia): zones.md v0.37, world.md v0.80.  R5 biome placement draft v0.2 reviewed: height scale, temperate uplands, S1 in warm grassland, and many rivers all fine.  Pick flow: region then 9 maps.  Planet top located (M10).  Drafts: cell pick flow, S1 onto the creek, thaw floods.

- 2026-11-12 (Claudia): world.md v0.79, Music areas locked: nearest town overland on land, Overall for town-less land, nearby land's music on near-shore water, sea shanties on the deep ocean, ice dread at the poles.  New tool `tools/music_areas.py` v0.1, data `tools/data/music_areas.json` v0.1, map `assets/maps/verlassen_music_areas_v0.1.png`.

- 2026-11-12 (Claudia): world.md v0.78.  Nathan: the ten places table gains a Culture column (the influence on top of Japanese).

- 2026-11-12 (Claudia): music.md v0.7.  Nathan: after two runs, reverse halfway and finish in the original notes.  Kaze v5a and v5b drafted.

- 2026-11-12 (Claudia): music.md v0.6.  Nathan: v3 was the wrong direction; the full 8-note riff is the core.  Kaze v4 drafted on the whole riff.

- 2026-11-12 (Claudia): music.md v0.5.  Nathan: no off notes yet, build the song first.  Kaze v3 drafted: the full song, 32 bars, loops through the wind.

- 2026-11-12 (Claudia): music.md v0.3.  Kaze v2 drafted from Nathan's sung guide: A A B A' plus coda, chords A F C E.

- 2026-11-12 (Claudia): music.md v0.2.  Nathan picked Kaze as the riff.

- 2026-11-12 (Claudia): music lane.  New `docs/design/music.md` v0.1 (Waveform, no Suno, calm background, radio beats, the riff).  AGENTS v0.5 adds the music lane and `assets/audio/`.  Concept v1.04 points the music pipeline to Waveform.  version_check v0.2 versions audio and MIDI by file name.  Three riff candidates v1 drafted.

- 2026-11-12 (Claudia): world.md v0.77.  Nathan approved the news spin and the dish rebroadcast with two speeds of news.

- 2026-11-12 (Claudia): world.md v0.76.  Nathan: local stations rebroadcast the news with a local spin; the same story changes zone to zone.  Draft: regional spins, the brothers' stations contradict each other.

- 2026-11-12 (Claudia): world.md v0.75.  Nathan: Verlassen is about 50 light years away and only now getting signals and feeds, so current Lancer table material is lore-appropriate news.  Draft: spaceport dish rebroadcast; two speeds of news.

- 2026-11-12 (Claudia): world.md v0.74, plan v0.28, planet pack and data v0.4.  Nathan: the year is 5071u, roughly 50 years after the events on Halas (canon's present is 5016u).

- 2026-11-11 (Claudia): concept v1.03.  Nathan: drop Suno entirely; music is our own MIDI and chiptune.

- 2026-11-11 (Claudia): concept v1.02, new Music section.  Nathan: Suno for feel, then our own MIDI and chiptune music; no current Steam release plan.  Drafts: regional fusions, pipeline.

- 2026-11-11 (Claudia): zones.md v0.36.  Nathan: descent footage and beacon both; the M.U.L.E. scans nearby points of interest on every drop and tags them as early quests; the M.U.L.E. has a short-range radio for local music.  Draft: radio bands, chatter, night shortwave, mood.

- 2026-11-11 (Claudia): zones.md v0.35.  Nathan approved the relay station; the 2D map needs a way to show distance (telescope spot or M.U.L.E. scan pictures).  Corrected: the tower is beyond the horizon from S1.  Drafts: descent footage, beacon, vistas.

- 2026-11-11 (Claudia): zones.md v0.34, new R5 section.  Nathan approved the R5 read, expected biomes, and 3,500 m peaks; higher and harder places hold more caves and rarer finds; the cold peak is an early challenge that holds something the player needs.  Draft: derelict relay station on the peak.

- 2026-11-11 (Claudia): zones.md v0.33.  Nathan: Kawa Fada is the first city.

- 2026-11-11 (Claudia): mechanics v0.52, zones v0.32.  Nathan approved the GM tool commands; an easy city build mode (#87c), the main reason cities wait until the game is established.

- 2026-11-11 (Claudia): mechanics v0.51, zones v0.31.  Nathan: first city likely Shio Loch, Shio Loch or Kawa Fada; GM tool early to skip around in testing, hidden later (#87b).

- 2026-11-11 (Claudia): zones.md v0.30.  Nathan: ferries to Kawa Fada go out to the left, through the strait near Shio Loch, and down.  Verified on the globe (about 42,000 km, 2 to 3 months).  Drafts: seasonal ferry, Shio Loch holds the sea gate.

- 2026-11-11 (Claudia): zones.md v0.29, Routes.  Nathan: route distances are calculated; no zigzag concern without WASD; roads 3-8-1 and 2-6-10-7; paths such as 5-1 and 2-10; ferries 1, 8, 2, 4, 9, 10.  Draft: landings for inland ferry towns (1 and 9).

- 2026-11-11 (Claudia): zones.md v0.28, catch-up run rules.  Nathan: broad estimates; leave warning; people can die; camp log; only maps with the player's people tick; unattended goods vanish logically by nearby threat; other sites get basic math only.

- 2026-11-11 (Claudia): zones.md v0.27.  Nathan approved the montage stop and settings drafts.

- 2026-11-11 (Claudia): zones.md v0.26.  Nathan: settings before a montage for how hard the player pushes.  Draft: pace, rations, rest days, caution.

- 2026-11-11 (Claudia): zones.md v0.25, Montage stops.  Nathan: simple stop rules (food, unable to progress, too many sick).  Drafts: forced stops, player-set stops, nightly camp inside the montage.

- 2026-11-11 (Claudia): zones.md v0.24.  Nathan approved the travel speed and montage event drafts as starters.

- 2026-11-11 (Claudia): zones.md v0.23, Montage events.  Nathan: generic events now (breakdowns, sickness, traders, wildlife and bandit attacks, modern Oregon Trail events); full tables later.  Drafts: event list and how events check the party.

- 2026-11-11 (Claudia): zones.md v0.22, Travel speeds.  Nathan: local map speed by feel and testing; overworld on modern assumptions; a group is as slow as its slowest unit.  Drafts: baseline speeds and slowing factors.

- 2026-11-11 (Claudia): zones.md v0.21.  Nathan approved all remaining zones drafts: power-of-two sizes, diagonal rule, edge crossing points, biome blending, stitched map view, heat formula and exact latitude, Intelligence on the road, 9-map section details, edge-walking details.

- 2026-11-11 (Claudia): zones.md v0.20.  Nathan approved the spawner-clearing and stone and mines drafts.

- 2026-11-11 (Claudia): zones.md v0.19.  Nathan: things can come up the stairs (Sword of Fargoal); bug cave entrances can be spawners to clear; no major digging, only mineral and rock hunting in caves; old mines (infested or still in use); stone from a system that does not destroy the map.

- 2026-11-11 (Claudia): zones.md v0.18.  Nathan approved air tracking and carbon monoxide in enclosed spaces.

- 2026-11-11 (Claudia): zones.md v0.17.  Nathan approved the underground drafts; cave rules for fires apply, a campfire kills in a cave.  Draft: air tracking and carbon monoxide in enclosed spaces.

- 2026-11-11 (Claudia): world.md v0.72, zones.md v0.16.  Nathan approved the biome list and water notes.  Underground: small RimWorld-style surface caves; deeper spaces and interiors (like an RV) are linked maps; dungeon depth later, no global underdark, prebuilt chance-spawn dungeons with major bosses.

- 2026-11-11 (Claudia): concept v1.01, mechanics v0.50.  Nathan approved the crystal graft costs.

- 2026-11-11 (Claudia): concept v1.00, mechanics v0.49.  Nathan's idea: purposeful crystal infections with trade-offs after synthesis (#95, Later).  Drafted seasonal, social, and spread costs.

- 2026-11-11 (Claudia): concept v0.99.  Nathan: kuru should be curable in the far future, maybe through infectious crystal synthesis.  Draft: prions and the infection both spread by templating.

- 2026-11-11 (Claudia): concept v0.98, mechanics v0.48.  Nathan: kuru is a thing for corpse paste.  Draft: prions survive the printer, long incubation, no cure.

- 2026-11-11 (Claudia): concept v0.97.  Nathan: real science; no RimWorld human skin hats and suits.

- 2026-11-11 (Claudia): concept v0.96, mechanics v0.47.  Nathan: no cannibalism, but pasting a corpse is a desperate option with Donner Party similarities.  Draft: lasting consequences.

- 2026-11-11 (Claudia): concept v0.95, mechanics v0.46.  Nathan: the paste printer turns almost anything organic (native or human, even wood, no metals) into paste at a convert rate.  Drafts: convert rates, fat rendering, fermentation vat.

- 2026-11-11 (Claudia): mechanics v0.45.  Nathan: we need a fishing mechanic (#19b) and boats (#72b).

- 2026-11-11 (Claudia): world.md v0.71.  Nathan approved salinity as a water property; brackish lakes are among the few places certain fish can be caught.

- 2026-11-11 (Claudia): world.md v0.70.  Nathan approved the salt notes; Lake Texoma is the model for salt-fed brackish water.  Draft: salinity as a water property.

- 2026-11-11 (Claudia): world.md v0.69.  Nathan added water biomes: warm ocean, deep ocean, coral reef, inland sea, inland lake, river, salt river.  Drafts: cold-water reefs, saline rivers from salt basins, dissolved salt immune to infection.

- 2026-11-11 (Claudia): world.md v0.68, new Biomes section.  Draft list of 13 biomes and features; Nathan: any biome can be infected and spawns differently.  Draft: infection as a level on a cell.

- 2026-11-11 (Claudia): zones v0.15, world v0.67, planet pack and data v0.3.  Nathan approved territories (formerly political regions) and dropped polar shrinking: squares are uniform for play and travel.

- 2026-11-11 (Claudia): zones.md v0.14.  Nathan: first build starts at a fixed crash spot far in the wilds (S1, R5, about 26 N), random and player-picked starts later; each map grid square is a region (R5 is the first).  Drafts: rename political regions to territories; true distance for travel.

- 2026-11-11 (Claudia): concept v0.94.  Nathan approved the panel toggle and critical-vital edge warning.

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
