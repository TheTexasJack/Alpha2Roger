# Status

**STATUS v0.160, 2026-11-13**

## Where things stand

- **Stage 0 (concept lock): closed 2026-11-10.**  The concept, the world of Verlassen, and the mechanics list are written down.
- No game code exists yet.  The Godot project has not been created.
- Every file carries a version.  `tools/version_check.py` verifies them against `VERSIONS.md`.  `tools/system_report.py` writes a full diagnostic report to `diagnostics/`.
- World tools exist in `tools/` (globe, places, territories, person names, planet pack, music areas, region generator), with canon maps in `assets/maps/` and the first region (R5) in `tools/data/regions/`.

## Next steps (Nathan picks the order)

0. **Music:** first read "Notes from the zones thread" at the top of `docs/design/music.md` (culture map split out, music areas tool now reads it, output unchanged).  Then get the Akai recording in Waveform (now required).  Then Nathan cleans up the Rory Dall feel test and adds an undertone or beat.  Target: the Irish wilds with samurai.
1. **Stage 1, A2R-102 (in review):** `docs/design/zones.md` is complete through the zone graph format.  Nathan's final sign-off is next; open items are listed at the bottom of zones.md.
2. **Draft for Nathan:** cold-rated fliers cost more, so money decides who flies in the cold year (world.md).
3. **Stage S:** guided, secured setup of Nathan's PC (Timeshift, Claude Code, Godot 4).  Best done at the machine.
4. **Design gaps:** stats and skills (#35, the biggest), conditions (#52d), factions and beliefs (#50b), trade (#70), currency names and rates, what the infection does.

## Open decisions

- Listed at the bottom of `docs/design/concept.md` (Open items) and `docs/design/world.md` (Open).

## Last session

- 2026-11-13 (Claudia): world.md v0.98, concept v1.22, mechanics v0.78, planet file v0.10, music.md v0.33 (note 10).  Nathan narrowed the rail line to two coded things: fast travel between cities, and the track-side event (the train crosses and hits everything).  Tunnels are a point, an explanation, and a map; no distances or science to model.  Tech level restated: Nausicaa (wood, almost medieval, some guns, flamers; big airplanes and a train); Model T cars were aura only.  Drafts: tunnel A (H8 to H8, spaceport continent to Ikh Gawa's) and tunnel B (J4 to H5, island to the spaceport continent).

- 2026-11-13 (Claudia): the rail line.  world.md v0.97 (new section, The rail line), zones.md v0.65, mechanics v0.77 (#72f), planet file v0.9 (`routes.rail`), music.md v0.32 (note 9 for the music thread: train sounds, note only).  Nathan: spaceport-run bullet train with a front piercer, boarded only in a city, fast travel city to city; undersea tunnels at a couple of crossings, deadly to walk; bait raiders onto the track.  Drafts: all ten places are stations, track in the road corridors, heated rails.  Open: map the pathway.

- 2026-11-13 (Claudia): concept v1.21, mechanics v0.76.  Nathan approved: the planet's environmental enemy is data in the planet module, never cold written into the code (#1).  Applies from A2R-103 on.

- 2026-11-13 (Claudia): concept v1.20, mechanics v0.75.  Nathan approved the shown-not-flown off-planet ending: an orbital launch would remove the cold as the enemy.  Expansions go to new planets with their own environmental enemy (heat, infection).  Draft: the planet's enemy lives in the planet module as data, not cold written into code.

- 2026-11-13 (Claudia): concept v1.19, mechanics v0.74.  Nathan: no orbital play in this design; spaceships and orbit belong to the expansions (#87).  Draft: the off-planet ending is shown, not flown, and hands off to an expansion.  Also pointed the old "route lengths decided later" line in concept to the pathfinding rule.

- 2026-11-13 (Claudia): world.md v0.96, mechanics v0.73.  Nathan: a thermal icebreaker beats trying to tech a flier, since airflow works against keeping things warm.  Physics note added: seawater stays near -2 C while flight air is -60 to -100 C; jet fuel freezes about -47 C.

- 2026-11-13 (Claudia): world.md v0.95, mechanics v0.72.  Nathan: thermal icebreakers as potential future tech, rarest of the rare because money limits it; a late-game player upgrade for world sea travel (#72e).

- 2026-11-13 (Claudia): world.md v0.94.  Nathan: the southern seas are ice, so no travel around the globe along rows 11 and 12; confirmed on the globe (land blocks row 11 anyway; the only southern sea ring is past 75 S).  Draft: permanent sea ice past 66 degrees, seasonal from 58 to 66 (where the Kawa Fada ferry runs).

- 2026-11-13 (Claudia): Start_Candidates_v3.0.png drawn (outside the repo, `/home/claude/samples/`) with every decision so far.  Drawing it surfaced corrections, now in zones.md v0.64 and the planet file v0.8: the way into Kawa Fada's sea is a passage about 900 km wide at W5, not a narrow strait; Setareh Minato and Zimna Toride sit about 190 to 195 km from the coast (were 180 and 300); Svetla Hama, a ferry town, sits about 670 km from the open sea by a small lake (Nathan's call).  `tools/region_gen.py` v0.3.1 points to the planet file by path only, so planet changes no longer touch R5 (image now `R5_biomes_v0.3.1.png`).

- 2026-11-13 (Claudia): world.md v0.93, mechanics v0.71.  Nathan approved the Yamajira eruption draft as a possible future special event or challenge (#96).

- 2026-11-13 (Claudia): world.md v0.92.  Nathan: Yamajira (M10) is left free, no aggregator; if it erupts it is left alone, and it is far enough away.  Draft: its ash would still reach everyone (world event), and an eruption at the ice edge brings a glacial outburst flood.

- 2026-11-13 (Claudia): world.md v0.91.  Nathan: distance is no limit for volcanic heat (insulate it, or lava to energy to heater); Claudia's 100 to 200 km limit assumed modern tech and is removed.  Draft: heat and power lines as cold-year targets.

- 2026-11-13 (Claudia): world.md v0.90.  Nathan's terraforming idea: eruptions are celebrated, and geothermic aggregators on the peaks pump lava around the cities.  Drafts: lava tubes and gravity for the run down (Undara about 160 km), why eruptions are celebrated (greenhouse; explosive ones are the disaster), aggregator lords and lava-ring moats.  Open: which peaks are volcanic.

- 2026-11-13 (Claudia): planet file v0.7, `tools/region_gen.py` v0.3, R5.json v0.3, world.md v0.89, zones.md v0.63, mechanics v0.70, plan v0.32.  Nathan approved: latitude lines, with the terraformers rule (the terraformers can compensate for science errors in planet, flora, and fauna lore; first use, a thicker greenhouse under 80% sunlight); biomes and region rules stored in the planet file (region_gen reads them; R5 cell for cell identical, image now `R5_biomes_v0.3.png`); roads as chains; path 4 to 9, path list complete; ferries any to any by sea, landings for inland ferry towns; future note on entering towns when hated (#60b).  Cold-year cause: dust or pull, decided with the map and art designs.

- 2026-11-13 (Claudia, zones thread): `tools/music_areas.py` v0.2 reads the culture map and only pairs culture to music; `music_areas.json` rows and the music areas image are unchanged.  Nathan asked for detailed notes for the music thread: music.md v0.28, "Notes from the zones thread".  world.md v0.88.

- 2026-11-13 (Claudia): culture map v0.2 (`tools/culture_map.py` v0.2), world.md v0.87, music.md v0.27.  Nathan: the ice caps and open water are cultures of their own (ice: cold, long notes with small hints of other songs; open water pairs with sea shanties).  v0.1 had missed them.  The map now pairs one to one with the music areas, pixel for pixel.  Polar base-only draft withdrawn.

- 2026-11-13 (Claudia): world.md v0.86, AGENTS v0.7, new `tools/culture_map.py` v0.1.  Nathan approved the stations and culture map drafts: similar styles grouped, Japanese base left off the map, Kawa Fada to Shio Loch one culture, culture is not ideals (cities and rulers set those).  Culture map built (`tools/data/culture_map.json`, `assets/maps/verlassen_culture_v0.1.png`); matches the music areas below the ice line.  Draft: polar land as base only.  Next: music areas read the culture map.

- 2026-11-13 (Claudia): world.md v0.85.  Nathan: radio and news feed off the culture map, not the music areas (overlap is fine; they are flavor: simple musical elements, voice recordings); weather is separate.  Drafts: stations take their place's cultural region; split a culture map out of `tools/music_areas.py` so culture feeds music, radio, and news.

- 2026-11-13 (Claudia): planet file v0.6 (`tools/planet_pack.py` v0.6), world.md v0.84, concept v1.18.  Nathan named the highest point Yamajira (M10, 53.4 S, 8.5 E, about 6,500 m); the packer finds it on the globe and checks it stays in M10.  Music stays in music: it evolves on its own and should not impact anything else, so the planet file only points to the music files.  Next: Nathan's calls on the remaining planet file items (latitude lines, biomes as data, road order, paths, ferries, cold-year cause).

- 2026-11-13 (Claudia): planet file v0.5 (`tools/planet_pack.py` v0.5).  Nathan asked for the road decisions in the planet file: roads 3-8-1 and 2-6-10-7, paths 5-1 and 2-10, ferry towns 1, 8, 2, 4, 9, 10, the Kawa Fada ferry through the strait by Shio Loch, cold-year sea ice, canon vs seeded routes, distances calculated never stored.  The packer now checks every road and path stays on one landmass.  Stale open items replaced; sources now world.md v0.83 and zones.md v0.62.

- 2026-11-13 (Claudia): full review.  Data rebuilds byte-identical; version check clean.  Fixed: zones.md v0.62 (layer table and tile counts now 3.8 km / 256 tiles / 16 cells per globe pixel, R5 peak pointer, R5 image path, two approved drafts that kept their Draft markers, superseded android draft, full list of open zones drafts); mechanics v0.69 (duplicate #87b, hive mind now #87g; #4 saves Decided; new #10b to #10e for edge walking, montage, catch-up, linked maps; GM tool and performance readout moved to Always on, M.U.L.E. items to Tier 3); world.md v0.83 (cultural region wording, Open list); concept v1.17 (Open items, music draft pointer); plan v0.30 (A2R-006 year wording, A2R-S07 Done); README v0.6 and AGENTS v0.6 repo maps.  Decisions for Nathan listed in chat.

- 2026-11-13 (Claudia): zones.md v0.61.  Restored the first-city decision (Kawa Fada) to the Cities section after the Open list refresh dropped it.

- 2026-11-13 (Claudia): zones.md v0.60, plan v0.29.  Nathan approved JSON with the format escape hatch.  Zone graph format complete; A2R-102 in review.  Open list in zones.md refreshed.

- 2026-11-13 (Claudia): zones.md v0.59.  Nathan approved the save cap behavior and playthrough name defaults.  Zone graph format: only JSON left.

- 2026-11-13 (Claudia): zones.md v0.58.  Nathan approved the save drafts; daily autosaves on the local map; manual saves capped at 50 per playthrough (adjustable or removable); each playthrough has a name picked at world build that organizes its saves.

- 2026-11-13 (Claudia): zones.md v0.57, new Save file section.  Nathan: free saving with an optional load counter; autosave at the start of each day, number kept set in the system menu (max 20); manual saves anytime.  Drafts: montage autosave rule, defaults, save contents.

- 2026-11-12 (Claudia): zones.md v0.56.  Nathan approved the edge ID convention and the seam fix.  `tools/region_gen.py` v0.2 keys interpolation and noise to world coordinates (seam test: 0.0 difference); R5 regenerated as `R5.json` v0.2 and `R5_biomes_v0.2.png`.  Follow-up noted: river inflow across region borders.

- 2026-11-12 (Claudia): mechanics v0.68.  Nathan approved the illness drafts: rabies as a rare travel event, sources of alien illness, medicine access, native illnesses.

- 2026-11-12 (Claudia): mechanics v0.67.  Nathan: alien illnesses work on alien creatures, so native illnesses get invented too.  Draft: die-offs, erratic sick creatures, warning signs, no jump to people.

- 2026-11-12 (Claudia): mechanics v0.66.  Nathan: rabies is no longer a big threat in the far future; common illnesses are easily cured with access to modern medicine; humans brought illnesses and new alien ones get invented.  Draft: sources of alien illness under mirror chemistry.

- 2026-11-12 (Claudia): zones.md v0.55, mechanics v0.65.  Nathan approved the city blocked-cells draft and the structures for conditions (#52d) and factions and beliefs (#50b).

- 2026-11-12 (Claudia): concept v1.16, mechanics v0.64.  Nathan: Intelligence can reach 0 in rare cases (a gunshot, extreme infection), and 0 equals death.

- 2026-11-12 (Claudia): mechanics v0.63.  Nathan added two topics to outline formally: Conditions (#52d: mental conditions, debuffs, illnesses, other conditions) and Factions and beliefs (#50b: faction beliefs such as slavery, and individuals who agree or disagree).

- 2026-11-12 (Claudia): zones.md v0.54.  Nathan: a city is a linked space entered through its gates, any shape, story maps only, with drill-down; city space rules approved; overworld land under a city is blocked off behind impenetrable walls (crossing is a bug, or sends the player to the nearest gate).

- 2026-11-12 (Claudia): concept v1.15.  Pam's full name is Pam Cramples; her other details wait for player stats and settings.

- 2026-11-12 (Claudia): concept v1.14.  Nathan approved an optional Intelligence 1 challenge start, noting major conversations need Intelligence 1 variants.  Drafts: limit variants to major scenes, creation floor 2, drops to 1 in play, 0 locked.

- 2026-11-12 (Claudia): concept v1.13, mechanics v0.62.  The Intelligence floor is noted in the stats design (Character system and #35).

- 2026-11-12 (Claudia): concept v1.12.  Pam has Intelligence 2; Intelligence 1 cannot speak (Fallout style), 0 is a rock.

- 2026-11-12 (Claudia): concept v1.11.  New list: Potential special NPCs.  First entry: Pam (Intelligence 0, drinks the stagnant water she complains about).

- 2026-11-12 (Claudia): world.md v0.82, zones.md v0.53.  Nathan: salt zone values (key areas set, per-region baseline) and river flow direction set at generation, some stagnant.  Claudia's salinity (ppt, downstream flow) and flow rules approved; region file gains flow direction and speed.

- 2026-11-12 (Claudia): zones.md v0.52.  Nathan approved the region file contents (with salinity).  Zone graph format: point 1 of 5 done; next city files, edge IDs, save file, JSON.

- 2026-11-12 (Claudia): concept v1.10.  Nathan: the M.U.L.E. stays unique and special; no other droid or android is as useful or smart.

- 2026-11-12 (Claudia): concept v1.09, world v0.81.  Nathan corrected the android draft: 3PO and HK-47 are reprogrammable droids, lesser than a person; NHPs are caskets holding alien minds that want to be human, and "no NHPs" means nothing that can cascade into eldritch concepts; tier 3 is a big robot with lots of guns.

- 2026-11-12 (Claudia): concept v1.08, mechanics v0.60.  Nathan: androids are built in three tiers (clunker, human-like, super soldier) (#72d).  Drafts: scripted minds to respect the NHP rule, sourcing by tier, camp-cap slot, upkeep.

- 2026-11-12 (Claudia): zones.md v0.51.  Nathan: a toll android counts as the player's people for ticking; androids are distinct from machines like farm robots.

- 2026-11-12 (Claudia): zones.md v0.50.  Nathan: tolls are placed on the local map; everything else rolls into catch-up.  Draft: robot-manned tolls count as the player's people for ticking.

- 2026-11-12 (Claudia): zones.md v0.49.  Nathan: toll money is electronic and cannot be stolen; barter goods paid at the toll can be; the whole robot can be stolen.

- 2026-11-12 (Claudia): zones.md v0.48, mechanics v0.59.  Nathan approved the wheels and traffic drafts; road tolls (#72c): manned by an NPC or robot, travelers complain and pay or turn back or go around, with anti-abuse criteria.  Draft: rates, chatter, charters, rerouting.

- 2026-11-12 (Claudia): zones.md v0.47.  Nathan: road types (road at full speed, path about 80%, animal trails visual only); defined overmap, region, then local; road edges spawn traffic, so building on a road has consequences.  Drafts: wheels on paths, traffic types and roadside bases.

- 2026-11-12 (Claudia): concept v1.07.  Nathan approved the solar and cold battery physics.

- 2026-11-12 (Claudia): concept v1.06.  Nathan: the M.U.L.E.'s battery was implied by the cold; he charges through rest and time with deployable or rooftop solar.  Draft: solar and cold physics.

- 2026-11-12 (Claudia): concept v1.05, mechanics v0.58.  Nathan: M.U.L.E. scan modes (thermal, outline, motion, lidar, EM/crystal as a ghost box), cycled in his menu, persisting until off or out of battery; extra scans drain faster (#87f).

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
