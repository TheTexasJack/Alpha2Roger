# Alpha2-Roger Mechanics List

**Mechanics v0.83, 2026-11-13**

Every mechanic the design calls for, pulled from `docs/design/concept.md`, `docs/design/world.md`, and the plan.  Use it as a checklist.

Status: **Decided** (Nathan's call), **Draft** (Claudia's suggestion, not yet approved), **Open** (needs a decision), **Later** (parked on purpose).
Tier: the suggested build order.  Tier 1 is the foundation; each tier builds on the ones before it.

## Tier 1: Foundation (Stages 1 to 3)

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 1 | Planet data module | Decided | Fixed map, places, biomes, rules as data; new planets need no engine rewrite.  The planet's environmental enemy (temperature, exposure, infection) is data too, never cold written into the code (approved 2026-11-13) |
| 2 | Seeded zone generator | Decided | Fixed places, random wilderness per seed, zone distances between fixed areas |
| 3 | Zone tile maps | Decided | Grid based, generated from seed plus biome |
| 4 | Delta saves | Decided | Save only what the player changed; maps the player builds on get baked.  Free saving, dawn autosaves, manual saves, playthrough names, JSON with an escape hatch (`zones.md`, Save file) |
| 5 | Turn-based grid movement | Decided | Enemies move when you do |
| 6 | Fog of war | Decided | Sword of Fargoal style: explored map remembered |
| 6b | Line of sight | Decided | Brutal, Caves of Qud style; camp stays visible, wilderness on line of sight (Draft); night and blizzards shrink it (Draft) |
| 6c | M.U.L.E. vision | Decided | Area around the M.U.L.E. always visible, maybe outlines; it is a liability |
| 6d | Sensor arrays | Decided | Buildable; reveals an area |
| 7 | Renderer separate from logic | Decided | Glyph-image placeholders first, swapped later |
| 8 | Layered peg sprites | Decided | Body, head, hat, gun, maybe circle hands; no limb animation |
| 9 | One survival pressure | Decided | First test of the survival loop |
| 10 | Zone transitions | Decided | Move between zones on the graph |
| 10b | Edge walking | Decided | Walk off a local map's edge into the next; the 9-map section around camp loads together (`zones.md`) |
| 10c | Montage travel | Decided | Long trips set a destination on the region map; route by pathfinding, days shown as a range; supplies, events, stops, pace and rations (`zones.md`) |
| 10d | Catch-up on return | Decided | Maps with the player's people (NPCs, androids) tick; others run seeded catch-up math when the player returns; camp log reports it (`zones.md`) |
| 10e | Linked maps | Decided | Underground, interiors, the RV, and city districts hang off local maps as linked maps (`zones.md`) |

## Tier 2: Survival core (Stage 4 and next)

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 11 | Needs: heat and cold, food and sleep | Decided | Biome specific |
| 12 | Light sanity | Decided | Mood debuffs, depression at most; no insanity, no mental breaks |
| 13 | Calendar and seasons | Decided | 12 months of 35 days (420 days), standard seasons, every third year a cold year (about 50 F colder) |
| 14 | Temperature model | Decided | Earth-like bands, warmest at the equator; cold-year shift of -50 F.  Temperature drives the map, and that drives plants, player temperature, and so on (Nathan).  Chain: calendar, latitude, cold year; then altitude, coast, geothermal, time of day, weather; then one value per map and per room, which every system reads (Draft) |
| 15 | Day and night | Draft | No moon, so nights are pitch black; light matters |
| 16 | Weather and forecast | Decided | Weather sensor on the wreck warns of the cold year; repairs extend the forecast (Draft) |
| 17 | Paste food printer | Decided | Bare survival for the player and companions; limited feedstock, morale cost |
| 18 | Native food processing | Decided | Mirror chemistry: native food must be processed.  The paste printer takes almost anything organic, native or human, even wood, no metals; each has a convert rate.  No cannibalism, but pasting a corpse is a desperate, Donner Party option, with real kuru risk.  Rendering fat and a fermentation vat (Draft) |
| 19 | Hunting | Decided | Big shaggy cold-adapted fauna with migrations; Terran game seeded by the settlers' terraforming is edible, native meat needs processing; Terran game near settled land (Draft) |
| 19b | Fishing | Decided | Needed: fish tables by water type and salinity; brackish lakes hold fish found few other places.  Ice fishing in winter and the cold year, nets, traps (Draft) |
| 20 | Farming | Decided | No free seeds; seeds are found, planted, and grown; Terran crops from rare seeds; growing takes full seasons; hunting carries the early game |
| 20b | Gathering plants | Decided | Terran-edible plants for people and Terran animals, native plants for native animals; matters for animal farming and pets |
| 20c | Plant analyzer | Decided | Identifies plants and who can eat them; M.U.L.E. or CompCon function, also checks salt for infection (Draft) |
| 21 | Food preservation and stockpiling | Draft | Salt preserves food; stock a year of food before the cold year |
| 22 | Shelter and walls | Decided | Walls for warmth and shelter, never a trivial defense |
| 23 | Clothing layers | Draft | Visible on the peg sprite |
| 24 | Salvage | Decided | Finding parts in zones |
| 25 | Crash site camp | Decided | The wreck as base |
| 26 | Repairs and restoration | Decided | Repairs unlock capabilities |
| 27 | Licensed gear scrapping | Decided | Licensed gear can be scrapped and remade unlicensed |

## Tier 3: The M.U.L.E. and the CompCon

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 28 | CompCon voice | Decided | Particularly smart CompCon, not an NHP; Subnautica-style voiced lines |
| 29 | M.U.L.E. follower | Decided | Utility workhorse, not rideable, maybe an early second fighter |
| 30 | M.U.L.E. cargo | Draft | Carries goods; ties into journey weight |
| 31c | M.U.L.E. returns | Decided | If not retrieved, it wanders back on its own, repaired enough to move but probably still damaged; never damaged so badly it cannot move.  Its captors are decimated (10%) when it returns |
| 31b | M.E.W.L. mode | Decided | If captured, the M.U.L.E. escapes as M.E.W.L. (Murder Everything With Lasers): red eye, inner whir, Congo-style cutting beam (best weapon in the game), calms down on return.  Only when kidnapped; exploitable, and that is accepted; comes back damaged (Draft).  The thing inside is never explained |
| 31 | M.U.L.E. limits | Draft | Batteries drain faster in the cold; can be knocked out and repaired |
| 32 | Translator calibration | Decided | Tutorial calibrates through sample languages (563 detected), then English |
| 32b | Wrist display interface | Decided | Menus feel like checking in with the M.U.L.E., even when it is away; Fallout-style but more advanced; never breaks (Draft) |
| 33 | Subtitles and message log | Draft | Always on, rereadable |
| 87a | MULEpad | Decided | In-game notes in the M.U.L.E.: pin addresses to the notepad, track and find them.  Pin, track, find, linked log entries (approved) |
| 87d | M.U.L.E. tracker | Decided | One zone loader: the tracked zone works like the camp (catch-up on return); a settings flag can raise the count; removing it returns the zone to normal.  Quests and story events flag their spots automatically |
| 87f | M.U.L.E. sensing | Decided | Scan modes: thermal, outline, motion, lidar, EM/crystal (ghost box style); the player cycles the mode in his menu, it persists until off or the battery runs out, and extra scans drain the battery faster |

## Tier 4: Character and companions

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 34 | Character creation | Decided | RPG style, built from peg parts |
| 34b | Equipment slots | Decided | No separate armor slots; hand slots for weapons and tools; details with character creation |
| 35 | Stats and skills | Decided | Traditional stat system of our own; backgrounds use Lancer name labels as RimWorld-style stat configurations plus flavor; no triggers; no ranged skill (#47d); uncapped builds; tune after the prototype; our own data tables; Intelligence 1 cannot speak, 0 is a rock.  Stat list, skills layer, soft caps (Draft) |
| 36 | NPC generation | Decided | Rolled once and locked; core plus changing state (Draft) |
| 37b | Pilot talents | Decided | Lancer has no pilot talents; we create our own, buffs at the end of the day.  Three ranks (Draft) |
| 37c | Gear from Lancer | Decided | Lancer names, our system effects; weapons are a start that we flavor; pilot gear adapted to a traditional form, heavy weapons need STR.  Weapon classes, tags, item traits (Draft) |
| 37d | Equipment catalog | Later | Parked (Nathan, 2026-11-13): weapons, tools, armor, clothing, and their respective settings, tackled once a working concept is confirmed |
| 37 | Traits | Decided | Includes negative and dark traits, balanced, never glorified |
| 38 | Relationships | Decided | Organic, RimWorld-like, light; family to protect; romance and intimacy only at 18 and up |
| 39 | Orientation | Decided | Varies per pawn, including ace; romantic and sexual dials (Draft) |
| 40 | Recruitment | Decided | Companions are free people won over by choices |
| 41 | Leaving | Draft | Companions treated badly can leave |
| 42 | Nicknames | Decided | Player can call NPCs anything |
| 43 | Camp jobs | Decided | 5 or 6 companions, not a colony sim.  The cap reserves the back-end engine and may grow later; Charisma brings companions earlier, not more of them |
| 44 | Compressed camp time | Open | Decide after seeing gameplay |
| 45 | Ages | Decided | Pawns 16 and up; babies much later; genetics and long lifespans later |
| 46 | Name generators | Decided | People done (`tools/name_gen.py`); about 200 settlement names to build |

## Tier 5: Combat and capture

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 47 | Turn-based combat | Decided | Combat math on the grid |
| 47b | Damage types | Decided | Lean on Lancer; Crystalline for the infection; Kinetic, Energy, Explosive, Burn, resistance halving (Draft); heat is environmental |
| 47d | No ranged skill | Decided | The player is a Lancer and knows how to shoot; shots hit, then effects or armor reduce them; shooting ability is not tracked.  Enemies are deadly too, so defenses and hard cover matter.  The successor is the same.  Companions follow the same rule for now; low skill adds debuffs instead (debuff list Draft).  Situation shapes damage (Draft) |
| 47c | Range and Line | Decided | Lancer attack patterns; Range needs line of sight, Line stops at walls (Draft) |
| 48 | Weapon feel | Decided | Snappy effects, short shake moments only, speed-up option |
| 49 | Capture | Decided | Non-lethal tools (Draft) |
| 50 | Coercion | Decided | Player can coerce NPCs |
| 50b | Factions and beliefs | Open | To outline formally (Nathan, 2026-11-12): factions plus the beliefs they follow (for example slavery: some practice it, some do not), and a belief structure for individuals, since a faction member may or may not agree with the faction's beliefs.  Structure (Claudia, approved): belief axes (such as slavery, the Union, the infection, NHPs, androids, outsiders, heat and who owns it); each faction takes a stance on each axis, and each person holds their own stance, which can differ from their faction's, the source of defectors, informants, and conflicted guards |
| 51 | Prisoner fates | Decided | Free, kill, or convert; no slave labor |
| 52 | Prisoners turning | Decided | Unrescued prisoners may join their captors |
| 52b | Released prisoners return | Decided | A prisoner let go might show up later |
| 52d | Conditions | Open | To outline formally (Nathan, 2026-11-12): mental conditions, debuffs, illnesses, and other conditions that players and NPCs can get.  Hinted so far: light sanity (#12), dysentery from bad water, kuru, frostbite, snow blindness, carbon monoxide, cold hands, Intelligence drops (0 equals death in rare cases), wounds (#52c), crystal grafts (#95), traits (#37).  Structure (Claudia, approved): sorted into mind, body, environment, illness, and chosen; each with cause, effects, duration, cure or treatment, and whether it spreads.  Illness (Nathan, 2026-11-12): far in the future, rabies is no longer the threat it is today; it is bad untreated, but common present-day illnesses are easily cured with access to modern medicine.  Humans brought illnesses with them, and there are plenty of new alien illnesses to invent.  Rabies is real but rare (Claudia: about one reported rabid animal per 2,000 km2 per year in the US, mostly wildlife).  Approved (Claudia's drafts, 2026-11-12): rabies is a rare travel event, usually one small Terran animal, and natives cannot carry it; mirror chemistry stops native germs from infecting people, so alien illness comes from Terran germs evolved over about 11,000 years, native toxins, allergic reactions to foreign proteins, physical parasites, the infection, and prions; medicine is easy, access is hard (cities and the spaceport).  Alien illnesses still work on alien creatures, so native illnesses get invented too (Nathan, 2026-11-12).  Approved (Claudia's draft): native illnesses cause die-offs in native herds (hunting dries up), occasional erratic sick creatures (rare, can gore but cannot infect), and warning signs (sick herds, carcasses); they never jump to people or Terran animals |
| 52c | Injuries | Decided | No limb mechanic; general wounds and conditions (Draft) |
| 53 | Player capture instead of death | Decided | Kenshi style: wake up in the camp's prison; escape play (Draft) |
| 54 | Death | Decided | The cold and the wild kill for real |
| 55 | Succession | Decided | Years pass; a random person, such as a lost 16-year-old, finds the M.U.L.E.; new playthrough (adult start, Draft).  Anyone who left the camp is first in line |
| 56 | Legacy camp | Draft | Old camp, graves, and repairs remain |

## Tier 6: World, factions, and economy

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 57 | Local life by remoteness | Decided | Small settlements and enemy camps near the player; the more remote, the fewer encounters |
| 57b | Tracked enemy groups | Decided | Persistent headcounts; no endless waves; groups learn (after 12 of them die, they stop going there).  Finite numbers and revenge exceptions (Draft) |
| 57c | Roads and bridges | Decided | Basic, RimWorld style; mostly fixed main roads; random offshoot paths to wild settlements and bandit camps |
| 58 | Infection | Decided | Three impact sites plus a small random spawn per run; weaker in the cold year; Crystalline damage type; beams refract off crystal; complicators that drive story (infected survivors, infected dead); seed crystal: converts salt, minerals, bone, teeth; piezoelectric control of the infected; standalone crystal entities or infected versions of existing enemies, decide with gameplay |
| 59 | Regions and control | Decided | Ten capitals, no global government |
| 60 | Factions and reputation | Decided | Faction-based reputation, no Qud web; bandits are factionless (the factionless faction) but tracked per group (#57b) |
| 60b | Entering towns when hated | Later | Possible future ways to sneak in, such as with cargo (Nathan, 2026-11-13) |
| 61 | Town governments | Decided | Lords or mayors, councils, judiciary |
| 62 | Cold-year city laws | Draft | Frostpunk: rationing, curfews, heat allocation |
| 63 | Work camps | Decided | Maybe: profit or labor; NPCs justify them; no sugar coating |
| 64 | Conflicts | Decided | Spaceport culture war, salt road war, two brothers, Zimna Toride's hidden war |
| 65 | Cold-year raids and refugees | Draft | Raids on food and salt; refugee waves |
| 66 | Currencies | Decided | Five regional currencies plus Manna; one hidden value inside (Draft) |
| 67 | Barter and salt | Draft | Salt as the near-universal trade good |
| 68 | Exchange rates | Draft | Rates shift in cold years |
| 69 | Banks | Decided | Accounts held under the M.U.L.E.; exchange and loans, real banks need ID (Draft) |
| 69b | Money on the M.U.L.E. | Decided | Weightless, stored with the M.U.L.E., no spending while it is out, no theft (NHP-level tech), transfers to the successor |
| 70 | Trade | Open | Shops and traders not designed yet |

## Tier 7: Journey, story, and endings

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 71 | Crash site selection | Decided | Pick a region or random; always away from civilization; distance shown (Draft).  Two starts (Nathan, 2026-11-13): a fixed Tutorial Start at S1, one click, and a Random Start |
| 72 | Journey prep | Decided | Weight limits, supply caches, who stays behind, point of no return |
| 72b | Boats | Decided | Needed for lakes, rivers, and seas.  From rafts to river boats and coastal craft; river crossings on the montage (Draft) |
| 72d | Androids | Later | Creating and building androids in three tiers (Nathan): tier 1 clunkers (basic Star Wars droids, Fallout's first-generation synths); tier 2 human-like (think C-3PO or HK-47); tier 3 super soldier.  Tier 2 has real personalities but is a reprogrammable droid, lesser than a person; tier 3 is a big robot with lots of guns.  Camp-cap slot, built from salvage, battery and cold upkeep (Draft) |
| 72c | Road tolls | Later | A manned gate (NPC or robot) charges road traffic; travelers complain, pay, turn back, or go around; criteria and side effects against abuse (charter on a lord's road, rerouting traffic; Draft) |
| 72e | Thermal icebreaker | Later | Late-game upgrade for world sea travel through the polar pack ice; future tech that only the rarest of the rare have, because money limits it; better than trying to tech a flier (Nathan, 2026-11-13) |
| 72f | Rail line | Decided | Only two things to code: fast travel between cities (boarded only in a city), and an occasional event when the player builds next to the track: the train crosses and hits everything (bait raiders onto it).  One loop of eight stations with tunnels at H8 and V5 to V6; Svetla Hama and Zimna Toride are off the line.  Tunnels are a point, an explanation, and a map; walking one is a warning, then the train.  Flavor disguised as a combat mechanic, mostly fast travel (Nathan, 2026-11-13; `world.md`, The rail line) |
| 72g | Air travel | Decided | Airports at Setareh Minato and Svetla Hama only; a flight ticket between them is fast travel, grounded in a cold year unless paid at cold-rated prices.  Every city has a military and a military air base, closed to the player (Nathan, 2026-11-13; `world.md`, Airports) |
| 72h | Ferries | Decided | For now, ferries are fast travel spots; seasons or time delays may be assigned in the future (Nathan, 2026-11-13) |
| 73 | Sea roads | Decided | Sea ice opens routes in the cold year; Setareh Minato to Ikh Gawa becomes a land trip |
| 74 | Identity questline | Decided | Legal battle by holo, email, and blink messages; new name at License Level 0 |
| 75 | Inbox | Decided | Blink messages bundled and slow; cost per message (Draft); letters from the other self (Draft) |
| 76 | Choices and consequences | Decided | Real options, temptation never coercion, "oh shit" moments, return later |
| 77 | Philosophies | Draft | Open Palm vs Closed Fist mapped to the heat |
| 78 | Ending milestones | Decided | Plan for four, build one at a time; play continues after |
| 79 | Duplicate setup per run | Decided | Varies each run |
| 80 | The crash glimpse | Decided | Flashes and a glimpse; attacker never named |
| 81 | Scrap mech | Decided | Late game, non-standard, built from pieces |
| 82 | Recognition | Decided | Prove yourself before the big manufacturers notice |

## Later systems

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 82b | Vehicles | Later | Speeders, motorbikes, trucks on open land, never through forests; rare planes; maybe spider walkers; rare early, small options in big cities; the M.U.L.E. rides on the back |
| 83 | Local AI dialogue | Later | Engine owns state, model only talks; authored fallback |
| 84 | NPC voices | Later | ElevenLabs style or local text to speech |
| 85 | Babies and genetics | Later | Much later, like RimWorld |
| 86 | Brawl mechanics | Later | |
| 87 | Expansion planets | Later | Return to the old wreck after a few expansions.  Orbital travel and spaceships live here, beyond this design.  Each new planet brings its own environmental enemy (heat, infection, and so on) that changes how the game is played (Nathan, 2026-11-13) |
| 87c | City build mode | Decided | An easy build mode to create handcrafted cities.  Waits until the game is established, since much of what it needs (building pieces, NPCs, items) is built in the early stages.  In-game builder in the GM tool that saves to the city's data file, plus Godot's own tile map editor (Draft) |
| 87g | Crystal hive mind | Later | Sidelined; a possible future expansion, not part of the base game (renumbered from a duplicate 87b in the 2026-11-13 review) |
| 88 | Headless sim testing | Draft | Seed sweeps and balance runs |
| 93 | Forced truce | Later | On hold.  Engine mechanic; criteria established later.  Idea: wars pause in the cold year, restart with the thaw |
| 95 | Crystal grafts | Later | After infection synthesis: purposeful infections, small benefits with trade-offs (lose one stat, gain another), visible crystals on the pawn.  Seasonal, social, and spread costs; no cold immunity; costly removal; successors start clean |
| 94 | Downed flier event | Later | Future seed-spawned random event; resources, someone to save, faction gains |
| 96 | Yamajira eruption | Later | Possible future special event or challenge (Nathan, 2026-11-13): the ash circles the planet and reaches everyone, brutal if it lands on a cold year; the melt at the ice edge sends a glacial outburst flood that reshapes the rivers below (`world.md`, Heights) |
| 97 | Pirate or smuggler airfield | Later | Random event: a pirate or smuggler airfield found out in the wild (Nathan, 2026-11-13) |

## Always on

| # | Mechanic | Status | Notes |
|---|---|---|---|
| 88b | Intro sequence | Decided | Short intro movie or comic showing the basics |
| 88c | Skip cinematics | Decided | Option to skip cinematics |
| 89 | Options menu | Draft | Effect toggles, speed-up, temperature units |
| 90 | Credits screen | Decided | Lancer Third Party License requirements in the game itself |
| 91 | Boredom log | Decided | Nathan reports fade points |
| 92 | Diagnostics export | Draft | One key writes a report: build version, seed, save state, log tail, settings.  Mirrors tools/system_report.py |
| 87b | GM tool | Decided | Built early to skip around while testing (no waiting a year to test something), hidden later.  Jump, time skip, spawn, fire events, edit, run catch-up, load seed; debug builds only (approved) |
| 87e | Performance readout | Decided | The GM tool and the system report need machine CPU, GPU, and memory usage, to test a live tracked map (Nathan).  In game: Godot's Performance monitors plus a custom monitor timing the tracked map's simulation; outside: `tools/system_report.py` adds CPU, memory, and GPU load and VRAM via nvidia-smi (approved) |
