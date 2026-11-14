# Alpha2-Roger Zones and Travel

**Zones v0.72, 2026-11-13**

The spec for A2R-102: how the world is layered, generated, traveled, and saved.  It reads the planet data file (`tools/data/planet_verlassen.json`) and a seed.

Decisions are Nathan's unless marked **Draft (Claudia)**.  Drafts are suggestions until Nathan approves them.

## Direction (Nathan, 2026-11-10)

- We do it a little differently from the games it draws on.  It borrows from RimWorld (a world map with travel, zooming into a local map) and from Caves of Qud (each area is a map the player crosses), and it is nothing like Kenshi (just running across the land).
- The crash site and a few key points nearby are fixed; the zones in between are randomly generated.  Once generated, they are fixed.
- Map size decides how many creatures are on the screen and how much is left for the back-end math.  It needs to be big.  RimWorld map sizes are fine, roughly a quarter mile across.
- Traveling map to map to reach a city would take years, even years of game time, and there is merit to that.
- The vast distances lean into a remote start being years before the player reaches a main settlement (also in `world.md`).
- We will have ways to shorten gameplay later (montages, a plane ride).  Specifics get worked out later, if pacing is a problem.

## Build order (Nathan, 2026-11-11)

- The montage is basically an overmap travel mechanic: math estimates that move the engines forward.  The real magic is the region and the local map.
- Start small: build one region and one local map, and start there.
- The first build uses one specific crash spot far out in the wilds, with random starts and a player-picked start planned for later (Nathan, 2026-11-11).
- First crash spot: S1, grid R5, about 26 N, 79.5 E (globe pixel x 519, y 128), a river valley about 5,600 km from the nearest place (Zimna Toride) (Nathan picked from Claudia's three candidates, 2026-11-11).
- Each square on the overall map is a region (Nathan, 2026-11-11): the lettered grid squares A1 to X12, so the first region is R5.  A region is 30 by 30 globe pixels, about 1,840 km north to south; at 16 region cells per pixel, a region map is 480 by 480 cells.  There are 288 regions.  This replaces the 8 by 8 pixel chunk draft.
- The planet file's political regions are renamed territories, so "region" means a map square (Claudia, approved by Nathan 2026-11-11).
- No polar shrinking (Nathan, 2026-11-11).  Squares narrowing toward the poles is globe logic; since this is a 2D game, we drop it.  Every square is the same size for play and travel.  The planet file's `straight_line_km` is globe reference only.

## Region R5, the first region

- R5 from the canon globe (Claudia, approved by Nathan 2026-11-11): latitude 15 to 30 N, all warm band; all land, with the sea just off the west (Q5) and north (R4) edges; the far southeast is about 1,600 km from any coast, the driest interior; about 20% highlands, a massif across the south-center whose highest peaks (the top 5% of land) continue into R6; S1's river runs north to the R4 coast; creeks run east toward S5; no lakes.
- Expected biomes (Claudia, approved by Nathan 2026-11-11): warm forest along the wetter north and west, warm grassland across the middle, scrub desert toward the dry interior, highlands on the massif, a river corridor along S1's river.
- Peak height (Claudia, approved by Nathan 2026-11-11): the R5 peaks stand about 3,500 m (revised 2026-11-12 to about 3,700 m; see Nathan's calls below), about 40 F colder than the lowlands by the lapse rate: cool summers and freezing winters up top, deep below zero in a cold year, a snowcap visible from far off in the warm band.
- Height and difficulty (Nathan, 2026-11-11): the higher up, traditionally, the more chance of caves and such.  As in traditional RPGs, the more complicated and harder a place is to reach, the better the chance of finding something rare.  A peak in the negatives is a good early challenge for dealing with extreme cold, so put something there the player needs.  Reward effort, even when it is impossible at the time.
- The R5 peak holds a derelict relay station, since real relay towers sit on the highest ground for line of sight (Claudia, approved by Nathan 2026-11-11).  It is unreachable without cold gear.  Restoring it could give long-range comms (an early thread for the legal battle), weather warnings, or a region map reveal.  The massif's flanks carry caves and mineral veins.
- Correction (Claudia): from a 3,500 m peak the horizon is about 220 km on Verlassen, and S1 is over 1,100 km away, so the tower cannot be seen from the crash site.
- The 2D map needs a way to show what is in the distance: maybe a spot with a telescope, or pictures from a M.U.L.E. scan that show the relay tower (Nathan, 2026-11-11).
- **Draft (Claudia), seeing far:** (1) descent footage: the M.U.L.E. recorded on the way down, and a few frames show the snowcapped massif and a glint on the summit, shown as comic panels; (2) a faint beacon: the relay still pings on shortwave, which can bounce off the upper atmosphere over thousands of km, so the M.U.L.E. marks it on the region map; (3) vistas: high spots on local maps with a telescope or binoculars show a horizon panel and reveal landmarks within real line-of-sight range on the region map.  Know it from day one, see it within about 200 km, reach it with cold gear.
- Descent footage and the beacon: do both (Nathan, 2026-11-11).  Descent footage means the M.U.L.E. scans nearby points of interest on any random drop, which tags early points of interest on every drop as quests and things to do.
- The M.U.L.E. has a short-range radio, which can introduce local music (Nathan, 2026-11-11).
- **Draft (Claudia), radio:** short range (VHF and FM, line of sight, roughly 50 to 100 km) carries local stations, camp and caravan chatter, and bandits on open channels.  Long range (shortwave) bounces off the upper atmosphere over thousands of km and carries farther at night: the relay beacon and distant city broadcasts heard after dark.  Local music is original, in each cultural region's style.  Chatter is information (caravans, settlement news, bandit plans).  Night shortwave brings news from the wider world.  Music lifts the camp's mood; silence in a cold-year winter weighs on it.

- R5 biome placement draft v0.2 (Claudia, 2026-11-12): heights from the globe in meters, temperature from the latitude lines minus the lapse rate, moisture from coast distance plus rivers, biome from temperature band and moisture, highlands above 2,000 m, river corridors.  Image: now in the repo as `assets/maps/regions/R5_biomes_v0.2.png`, built by `tools/region_gen.py` v0.2.
- Nathan's calls on the draft (2026-11-12): the planet height scale is fine (planet top about 6,500 m, R5 summit about 3,700 m); uplands reading as temperate is fine; S1 landing in warm grassland is fine; lots of rivers is fine, since the cold year's ice and snow melts every third year and makes rivers.
- When a player picks an area on the world map, they pick the region, and that tells the game which 9 maps to load (Nathan, 2026-11-12).
- Scale note (Claudia): one region cell (about 3.8 km) holds 16 by 16 local maps; the 9-map section is about 720 m.  At region detail, the nearest creek is about 80 km south of S1 and the nearest river about 126 km.
- (Claudia, approved by Nathan 2026-11-13) pick flow: world map region, then a region cell on the region map, then the game drops the player into a local map in that cell and loads the 9-map section around it.  Small creeks and ponds are local-map features anywhere.
- Start choice built in from the start (Nathan, 2026-11-13): the random and player-picked start is worked in now, but during development we always click and enter S1 to start.
- Two starts (Nathan, 2026-11-13): a fixed "Tutorial Start" and a "Random Start".  S1 is the Tutorial Start, so the player gets both worlds: a one-click start, and the option to go random.
- (Claudia, approved by Nathan 2026-11-13) tutorial: the Tutorial Start also uses a fixed run seed, so S1's local maps come out the same every time and tutorial beats can be placed at known spots.  The translator calibration (#32) and the mech computer's voice already work as the tutorial; building and testing S1 during development builds the tutorial at the same time.
- Note (Claudia): picking your own region (`concept.md`, Crash site; mechanic #71) is still canon and sits beside Random Start until Nathan says otherwise.
- **Draft (Claudia), how:**
  - The region baker adds a start layer to each region: the cells allowed as a crash spot.  Rule draft: land, below the ice line, at least 2,000 km from any of the ten places, and at least 600 km from an impact site.  That leaves about 63% of usable land across about 125 regions; S1 passes easily (about 5,600 km from Zimna Toride, about 5,000 km from an impact site).  The river preference was for testing only.
  - Start screen: the globe, then a region (or Random), then the region map with allowed cells shaded, then a cell (or Random), then the 9-map section loads and the crash plays.  Random draws a region, then a cell, from the allowed set with the run's seed.
  - Only baked regions can be clicked.  At first that is R5 alone, so the click is always S1; regions light up as they get baked.  The GM tool can add a quick start at S1 to skip the clicks.
- The only reason to be on a river is testing on a river; the randomness of the seed generation guides the specifics, so S1 stays where the seed put it (Nathan, 2026-11-12).
- We need a measurement like the overmap's (R5 and so on) to pinpoint places better (Nathan, 2026-11-12).
- Addresses (Claudia, approved by Nathan 2026-11-12): one block per zoom level: region (A to X, 1 to 12), region cell (column.row, 0 to 479), local map inside the cell (column.row, 0 to 15), tile inside the map (column.row, 0 to 255).  Example: S1's camp spot is R5-152.136-08.08-128.128; dropping blocks zooms out.  Numbers after the first block, since letters run out at 480 columns.  Used by the GM tool (jump to an address, such as a river cell for river testing), seed sharing, bug reports, the camp log, and a cursor readout on the region map.
- The number system is fine as long as players can pin, track, or find addresses, since they may be hard to follow.  Old-school tracking is fine too, but an in-game notes log is good: a "pin to notepad" that adds to a notes section in the M.U.L.E., called the MULEpad so it is not confusing (Nathan, 2026-11-12).
- MULEpad features (Claudia, approved by Nathan 2026-11-12): pin from the region map, a local map, or the cursor readout, saving the address, an automatic label (such as "creek, warm grassland"), and the player's own note; track a pin as a marker on the map and wrist panel, or set it as a montage destination; find pins by name, note, or address, sorted by distance; camp log lines, descent-scan points, quests, and vista sightings arrive with their address attached; players who keep paper notes can ignore it.
- **Draft (Claudia):** after every cold year comes a thaw flood: rivers swell, fords close for weeks, and dry washes run with water.

### Region biome rules (Claudia, approved by Nathan 2026-11-12)

Built by `tools/region_gen.py`; R5 output in `tools/data/regions/R5.json` and `assets/maps/regions/R5_biomes_v0.3.1.png`.  Since generator v0.3 (2026-11-13) the rule numbers, latitude lines, and biome names below are read from the planet file (`region_rules`, `climate`, `biomes`); R5 came out cell for cell identical.

1. Detail: each globe pixel is smoothly upscaled into 16 by 16 region cells, plus fine seeded noise.  Since generator v0.2 (bug fix approved by Nathan 2026-11-12), both the upscaling and the noise are keyed to world coordinates, so neighboring regions agree exactly along shared borders.
2. Height: meters = 6,500 x (relative elevation) ^ 1.63 (planet top about 6,500 m, R5 top about 3,700 m).
3. Temperature: the latitude-line yearly average (midpoint of summer high and winter low), minus about 3.5 F per 1,000 ft.
4. Band: warm at 60 F or more, temperate 45 to 60 F, cold below 45 F.
5. Moisture: coast influence fading over about 700 km inland, a boost within about 25 km of a river, a little seeded noise.
6. Base biome by band and moisture (wet 0.55 and up, middle 0.30 to 0.55, dry below 0.30): warm forest, warm grassland, scrub desert; mixed forest, prairie, steppe; taiga, tundra, cold barrens.
7. Overrides, in order (later wins): highlands above 2,000 m; marsh below 150 m, moisture above 0.75, within 15 km of a river; river corridor within 5 km of a river below 2,000 m; coast on land touching the sea below 300 m; ocean on water.
8. Rivers from flow at cell detail: a river drains about 26,000 km2, a creek about 6,600 km2.
- Not yet in the generator (R5 does not need them): the Ice rule, water biomes, infection levels, and features.  These come before the generator runs anywhere else.

## Grid (Nathan, 2026-11-11)

- Square grid, one grid across the board.  It also makes the math of regions easy: we just pick a grid number.  64 is old-school Minecraft logic, but we fit what meets our needs.
- Local maps are 256 by 256 tiles, RimWorld's tested default.  Bigger maps are possible, but the activity is pretty focused (Nathan, 2026-11-11, after comparing 256 and 512 samples).
- (Claudia, approved by Nathan 2026-11-11) powers of two anchored on the canon globe: one globe pixel (about 61.2 km) is 16 by 16 region cells (about 3.8 km each); one region cell is 16 by 16 local maps; one local map is 256 by 256 tiles (about 240 m); one tile is about 0.93 m.  (Chunk size superseded: a region is one map grid square, see Build order.)  This refines the approved 4 km cells, 250-tile maps, and 10-pixel chunks below.
- (Claudia, approved by Nathan 2026-11-11) diagonal steps cost 1 for movement; range counts diagonals 1, then 2, alternating, so ranges come out nearly round.
- Approved by Nathan 2026-11-11 (Claudia's suggestion): the engine keeps coordinates local to the current map, since the planet is about 47 million tiles around and engines lose precision at huge positions.
- Blockiness is normal (Nathan, 2026-11-11).  Mapped out by region or by local map, the whole world looks blocky and weird.  The more you zoom in, the more a region is a square.  That is where the math and the beauty of the world map cross.
- Edge matching uses the RimWorld logic: a river has a top and a bottom where it enters and leaves, and the inside does not matter as long as the top and bottom match (Nathan, 2026-11-11).  The same goes for roads and other features that cross map edges.
- (Claudia, approved by Nathan 2026-11-11) a crossing point belongs to the edge, not to either map.  It is calculated from the seed and that edge's ID, so both neighbors agree no matter which one is generated first.  The region map decides which edges a river or road crosses; the local generator draws any path between its crossing points.
- Because the inside of a map is free, the engine can slip in a settlement and move the river accordingly (Nathan, 2026-11-11).
- Local generation order (Claudia, approved by Nathan 2026-11-11): edges (crossing points), then placements (settlement, ruin, crash site, downed flier), then routes (rivers and roads between crossings, shaped by the placements), then fill (terrain, plants, rocks, critters).  Settlements want water, so a river is routed past or through a settlement (docks, mill, bridge) rather than away from it.  Handcrafted maps keep fixed edges, and their generated neighbors read crossing points from them.
- Major cities are fixed when we make them.  They are the handcrafted exception; a city of a million people cannot be randomly generated (Nathan, 2026-11-11).
- (Claudia, approved by Nathan 2026-11-11) biome changes blend over a band near region cell edges instead of switching exactly at the line, so a desert cell fades into grass rather than stopping at a straight edge.
- (Claudia, approved by Nathan 2026-11-11) the player's map view shows visited local maps stitched together as squares, with unvisited ones blank, like the reference samples.  The blocky patchwork becomes the record of where the player has been.

## Layers

- Three maps: a globe map, a region map, and local maps.  The region map is the equivalent of the RimWorld world map (Nathan, 2026-11-10).
- (Claudia, approved by Nathan 2026-11-11) scale:

| Layer | One cell is | Used for |
|---|---|---|
| Globe | about 61 km (the canon 720 by 360 map) | Strategic view: where the player is, where the cities are.  Canon, never changes |
| Region map | about 3.8 km | Montage travel, roads, rivers, biomes, points of interest, events |
| Local map | 256 by 256 tiles, about 240 m | Turn-based play, camp, combat, walking from map edge to map edge |

- (Claudia, approved by Nathan 2026-11-11) about 16 by 16 local maps per region cell and about 16 by 16 region cells per globe pixel, an even step at each layer (numbers corrected in the 2026-11-13 review to match the Grid section).
- (Claudia, approved by Nathan 2026-11-11; chunk size superseded 2026-11-11 by one map grid square per region) region maps are fixed square chunks of the globe, not the territories, since about 65% of habitable land belongs to no territory.  Chunks tile seamlessly; territory borders are drawn on top as data.
- (Claudia, approved by Nathan 2026-11-11) each layer is built from the one above it.  The globe feeds the region chunk; the region cell feeds the local map.  A river on the globe stays a river on the region map and in the local map.

## Heat

- Heat bands apply the same way they do on Earth.  That establishes a base heat value for each region and each square (Nathan, 2026-11-11).  The latitude lines are in `world.md`; the chain is mechanic #14.
- (Claudia, approved by Nathan 2026-11-11) base heat for a square: latitude (blended from the latitude-line table), minus about 3.5 F per 1,000 ft of elevation (standard lapse rate), milder on coasts and more extreme inland, plus local geothermal heat.  Then the locked chain applies: calendar day and hemisphere, the cold-year shift, time of day, weather.
- (Claudia, approved by Nathan 2026-11-11) base heat is calculated from the square's exact latitude, not the region cell's, so temperature changes smoothly across cell edges.  Nothing needs storing; it is computed when needed.

## Travel

- Overland travel works Oregon Trail style, with a montage.  The player preps everything and moves it along.  Movement across open land is a montage: time moves at an accelerated rate, random events may go off, there are things to stop and visit, and eventually the player has to stop and set up camp (Nathan, 2026-11-10).
- The region map moves like RimWorld: set a destination and move there, not WASD movement.  World travel is the montage, and it may cost many supplies.  What that means is still to figure out, but it should have considerable impact.  That may be our Oregon Trail logic: Pam died of dysentery, so don't drink the poop water, Pam (Nathan, 2026-11-11).
- What travel costs (Claudia, approved by Nathan 2026-11-11): each travel day draws food, water, and fuel by party size, and wears clothing and gear.  Untreated water risks sickness, so boiling, filters, or tech purification matter.  Weather and the cold year raise the cost per day.  Carrying limits (the M.U.L.E., pack animals, sleds in the cold) cap how far a party can go between resupplies.  River crossings on the route become decisions (ford, build a raft, find a bridge), which ties to the edge logic for rivers.
- An Intelligence-based character could make overworld travel much easier (Nathan, 2026-11-11).
- (Claudia, approved by Nathan 2026-11-11) Intelligence on the road means better route planning (shorter, safer paths), reading the weather a day ahead, purifying water, repairing gear in the field, and stretching fuel.
- Players can walk the whole distance, because some will try, or they may have crashed nearby (Nathan, 2026-11-10).
- (Claudia, approved by Nathan 2026-11-11) walking and the montage are the same world.  The montage is a fast-forward over the same seeded maps; if an event stops the player partway, the local map they land in is the one they would have reached on foot.
- (Claudia, approved by Nathan 2026-11-11) near camp, the player walks off a map edge into the neighboring local map, Qud style.
- Unlike RimWorld, the player can move one map over left, right, up, and down without going to the region map (Nathan, 2026-11-11).
- Four directions only, within a 9-map section: one map in the middle and the maps around it.  Go left and up, then right and down, and the player is back at camp.  That is wide enough for much more diversity and feels more Qud than RimWorld.  Qud gets boring in some areas with fields of marsh, some monkeys, and plants (Nathan, 2026-11-11).
- (Claudia, approved by Nathan 2026-11-11) the 9-map section is centered on where the player is stopped (camp, or where the montage stops); moving camp moves the section.  Walking off the section's outer edge opens the region map.  Every map in the section gets its own feature (a ruin, a hill with a view, a creek ford, a cave mouth, a clan trail, a salt flat), so there are no filler maps.
- (Claudia, approved by Nathan 2026-11-11) a diagonal neighbor takes two moves.  The player enters the new map at the matching edge position.  Maps the player leaves freeze, and the catch-up run works out what changed on return, so only one map is active at a time.  Anything chasing the player near the edge crosses too.

## Stored and unstored maps (Nathan, 2026-11-12)

- Local maps stay unstored: seed, address, and generator version rebuild the same map every time, and only changes are saved, keyed by address.
- Hybrid (Claudia's suggestion, approved): untouched or lightly changed maps stay unstored; any map the player builds on (camp, an outpost, a heavily changed map) is saved in full ("baked") the first time they build there, which makes it immune to generator changes.
- By default nothing is tracked.  Quests and story events are automatic: when one is created, it flags its spot, the same way changes are tracked.
- The M.U.L.E. has a single tracker that acts as a zone loader.  The tracked zone works just like the player's camp.  Players may have several reasons to use it, especially with complex machines later.  A settings flag can raise the number of trackers as players build larger systems, but by default the player chooses one zone to permanently track and load.  Removing the tracker returns the zone to unloading like any other cell.
- Note (Claudia): like the camp, a tracked zone resolves through the catch-up run rather than running live, so it costs no extra engine time while the player is away.  Example: prisoners left in a tracked cellar starve, escape, or are rescued according to their stats, the food left, and the time away.
- A zone for the tracker is the local map it is placed on.  The tracker is a physical beacon tag the M.U.L.E. plants, so it exists in the world (Claudia, approved by Nathan 2026-11-12).
- To place it, the player must be on that map in person, with the M.U.L.E. (Nathan, 2026-11-12).
- A beacon can watch an enemy base: walk into the map, place the beacon, leave, and check back on what they are doing (Nathan, 2026-11-12).
- The beacon does not remove fog of war.  Like the M.U.L.E., it tracks NPCs and others nearby, outlining and highlighting them (Nathan, 2026-11-12).  This also defines the M.U.L.E.'s sensing, which was not defined before.
- Live versus catch-up for a tracked map (Nathan, 2026-11-12): Nathan sides with live.  The tracker is a strategic tool, and the point is to flip over and see what is happening; a live tracked area gives the feeling of living places while everything else is catch-up math.  He also accepts Claudia's points (live cannot run through montages or time skips, so catch-up is needed anyway; two systems must agree), so live gets tested once the engine exists.  Until then, catch-up is the base and the safety net.
- (Claudia, approved by Nathan 2026-11-12) machines are rate-based (given inputs, produce X per hour), so catch-up stays exact whatever the tracker ends up doing.
- **Draft (Claudia):** opening a beacon's view runs the catch-up for that map up to the present and shows the result as a snapshot, which feels like surveillance but costs no live engine time.
- **Draft (Claudia), sensing (M.U.L.E. and beacon):** silhouettes through the fog, with terrain, items, and buildings still hidden; thermal, so sharper in the cold and blurrier in hot places, near geothermal vents, and around fires; infected creatures run cold and barely show; the M.U.L.E.'s range is larger than a beacon's, with numbers set in testing; enemies can spot, destroy, or steal a planted beacon.

## Region file contents (Claudia, approved by Nathan 2026-11-12)

- Header: file version, generator version, seed, region, size (480 by 480), km per cell, origin on the globe.
- Layers, one value per cell: biome; water (none, creek, river); salinity on water (parts per thousand, labeled fresh, brackish, saline); flow direction on water (one of 8, or still); flow speed band (still, slow, moderate, fast); height at full detail (480 by 480); moisture (0 to 9); territory (owner or none).
- Calculated, not stored: temperature, music area, infection level, edge crossings, neighbors, traffic.
- Routes: roads and paths as lists of cells, each with the places it links.  Animal trails stay out of the region file; the local generator scatters them.
- Landmarks: ID, type, address, tier (canon or seeded), short note.  Spawners are landmarks with a spawner type.
- Linked-map entrances: address, kind (cave, cellar, bunker, dungeon), what is behind it (template ID or generated), size, number of floors.
- R5 has no roads or paths today; its route list starts empty.

## Save file

- Free saving (Nathan, 2026-11-13).  Ironman modes always felt weird: just don't load it.  An optional counter can show how many times a save was loaded, for players who want to show it.  Saves are also an easy way to recover from crashes and bugs.
- Automatic and manual saves (Nathan, 2026-11-13): an autosave at the start of each day, with a number of autosaves kept as backups, set in the system menu (maximum 20).  Manual saves at any time.
- (Claudia, approved by Nathan 2026-11-13) during a montage, autosave once when the trip starts and once when it stops, since daily autosaves would burn through every slot on a long trek; on foot, every dawn.  Default kept: 5 (1 to 20), oldest rolled off first.  Manual saves are kept separately and never rolled off.  The load counter lives in the save's info.
- Save contents (Claudia, approved by Nathan 2026-11-13): a folder with (1) a manifest: save format version, game version, generator version (pinned), seed, real created and played times, playtime, game date and place in the cold cycle, start settings (Intelligence 1 challenge, tracker count, difficulty); (2) people: the player (stats, skills, talents, conditions, gear, address), the lineage (original pilot or successor, past characters), the camp roster (companions and androids, relationships, moods, traits), the M.U.L.E. (battery, scan mode, money, MULEpad pins, tracker location); (3) the world, only what changed: changes by address, baked maps as separate files, the watch list with last-visited days, off-map sites, factions (reputation, charters, stance changes), story (quest flags, legal battle, inbox, comics seen), discovery (visited maps and cells), the camp log; (4) a checksum to catch corrupted saves.
- The daily autosaves happen on the player (local) map; on a montage, saving happens only as it starts and when it stops (Nathan, 2026-11-13).
- Manual saves: a maximum of 50 per playthrough, with a system menu option to change the number or remove the cap (Nathan, 2026-11-13).
- Each playthrough has a name, picked by the player when they build the world.  The name organizes the saves and other things (Nathan, 2026-11-13).
- (Claudia, approved by Nathan 2026-11-13) at the manual cap, the game asks which save to overwrite rather than refusing; the playthrough name is the save folder's name and shows on the load screen and the camp log's title; if the player leaves it blank, a default is offered from the seed and start (for example "2718 S1").
- Seeds and names (Nathan, 2026-11-13): the tutorial is just the preset seed 2718 S1.  The playthrough name includes the run seed by default along with the character's name, as "NAME 48213 R7"; the player can rename it, and the seed is baked into the save either way.
- Grouping (Nathan, 2026-11-13): saves are grouped by character, so Brad has all of his saves under him, Janet has hers under her, and Rocky's stay separate, each under the run seed they generated.
- **Draft (Claudia), save layout:**
  - The load screen lists run seeds, then the characters under each seed, then that character's saves.  Two characters on the same seed (Brad and Janet both on 2718, say) sit side by side under it.
  - A successor who finds the M.U.L.E. lands under the same seed as a new character, so the load screen shows the line of pilots in one world.
  - Folders use a fixed ID (the seed plus a short character ID), and the display name lives in the manifest, so renaming never moves files.
  - The autosave and manual caps count per character.

## Edge IDs (Claudia, approved by Nathan 2026-11-12)

- Every edge between two neighboring local maps is named from one side only: the map to the west (for an east-west crossing) or to the north (for a north-south crossing), plus E or S.  Example: the edge between R5-152.136-08.08 and its east neighbor is R5-152.136-08.08:E.  Only E and S appear; a map's west edge is its west neighbor's E edge.
- The rule holds across cell borders, region borders, and the east-west wrap, since the name always uses the full address of the west or north map.
- Crossing points come from the seed, the edge ID, and the generator version (which tile a river or road crosses at, and its width); whether anything crosses comes from the region file (water, flow, routes).
- Handcrafted maps (city gates) write their crossings under the same IDs, and neighboring generated maps read them instead of rolling their own.
- Known follow-up (Claudia): river flow is still traced inside each region's window, so a river whose catchment starts outside the window can be undercounted at a border.  Fix before a second region: feed upstream flow in from the globe at the window edges.

## Underground (Nathan, 2026-11-11)

- Surface caves are like RimWorld caves: possible, but usually small.  Bear homes, alien bug homes, and holes.
- Anything deeper uses linked maps: basements, deep caves, cellars, bunkers, and interiors that do not translate to the overworld map.  Example: an RV.  Spatially it may not make sense, but a small interior map is better than trying to make an RV work on the overworld.
- Dungeons: how deep they go is defined later.  No underdark equivalent spanning the globe, but a player might end up in a 20-floor dungeon somewhere.  A few prebuilt chance spawns can lead to major bosses for loot.
- (Claudia, approved by Nathan 2026-11-11) a linked map is an ordinary local map with an entrance instead of edges, often smaller (64 or 128 tiles).  Each dungeon floor is its own linked map.  Only one map runs at a time, as on the surface.
- (Claudia, approved by Nathan 2026-11-11) prebuilt dungeons are handcrafted templates placed by the seed (the seeded landmarks tier), so the same seed puts the same dungeon in the same place.
- (Claudia, approved by Nathan 2026-11-11) physics: deep caves hold near the area's average yearly temperature, and rock changes slowly, so a cave keeps its warmth for months into a cold year.  Caves are natural cold-year refuges, for people and animals alike.  Dangers: total darkness, carbon dioxide pooling in low spots, flooding at the thaw, cave-ins.
- Cave rules for fires apply: a campfire kills in a cave (Nathan, 2026-11-11).
- Air in enclosed spaces (Claudia, approved by Nathan 2026-11-11): each enclosed space tracks air.  A fire burns oxygen and makes carbon monoxide, which builds up without airflow: headache, then confusion, then sleep, then death.  Openings and natural drafts vent it, so a cave with a chimney or a strong draft allows a small fire, and a sealed one does not.  The same rule covers tents, RVs, bunkers, and sealed shelters.  The wrist unit or a sensor can warn of bad air.  This forces a cold-year choice: a warm sealed cave without fire, or a fire and a vent that lets the heat out.
- Sword of Fargoal rule (Nathan, 2026-11-11): things can come up the stairs.  Which monsters can climb is decided later.  Not every entrance is a ladder; some are just caves.
- A bug cave entrance can be a spawner; the player has to clear it to stop the bugs (Nathan, 2026-11-11).
- (Claudia, approved by Nathan 2026-11-11) clearing a spawner means going in and killing the nest's heart (a queen or brood chamber) in its linked map; sealing the entrance only buys time.
- **Key rule, no major digging (Nathan, 2026-11-11):** hunting for minerals and rocks in caves is valid, but no giant grid digging through mountains.  Caves are caves for a reason; there is no mining crew carving a giant mine.  Old mines can be found with supplies in them; some might be infested, and some might still be in use.  If players need stone, a stone generation system supplies it without destroying the map.
- (Claudia, approved by Nathan 2026-11-11) stone comes from quarry outcrops that yield slowly and never vanish, boulders and scree in the highlands, and rubble from ruins.  Old mines follow mineral veins, which the infection can take, so "infested" can mean bugs or crystal.  A working mine belongs to someone: a faction, a clan, or a lord.

## Travel speeds (Nathan, 2026-11-11)

- On the player (local) map, speed goes by feel and gets tested.
- The overworld uses modern assumptions on travel speed.
- A group is as slow as its slowest unit.
- (Claudia, approved by Nathan 2026-11-11 as starters; marker fixed in the 2026-11-13 review) overworld baselines: about 8 travel hours a day, in km per day: on foot on a road with a light load 30 to 35; on foot in wilderness 15 to 25; hauling a heavy load or sled 10 to 15; deep snow without snowshoes 5 to 10; snowshoes or skis 15 to 30; wagon or cart 25 to 30 (the Oregon Trail's 15 to 20 miles); horse or pack animal 30 to 40; dog sled 40 to 80; vehicle off road 100 to 250; boat downstream 50 to 100, upstream 15 to 25.  Climbing follows Naismith's rule, about one extra hour per 600 m of ascent.
- (Claudia, approved by Nathan 2026-11-11 as starters) what slows a group: terrain (biome, snow depth, climbing; roads speed it up); weather (rain, wind, fog, blizzard); daylight (no moon, so little night travel, and short winter days); load against carrying capacity; condition (wounds, sickness, hunger, fatigue, cold, anyone being carried); animals' grazing time and vehicles' fuel; river crossings; caution through dangerous or infected ground; and the cold year, which multiplies most of these.

## Routes (Nathan, 2026-11-11)

- Route distances are calculated: the region-cell grid, pathfinding across cells, a cost per cell (biome, climbing, rivers, roads, infected ground), and the speed table.  The montage planner shows the result as a range of days (Claudia's basis, agreed).
- No zigzag concern on the region or world maps: there is no WASD travel.  The player sets a path and is taken along it, so diagonals stay as they are.
- Roads run between most major settlements on a continent: 3, 8, 1 (Warmes Tani, Darya Kako, Setareh Minato) and 2, 6, 10, 7 (Ikh Gawa, Davs Mizuumi, Kawa Fada, Shio Loch).
- Paths, smaller than roads but still useful, connect the others, such as 5 to 1 (Khaluun Onsen to Setareh Minato) and 2 to 10 (Ikh Gawa to Kawa Fada).
- Road order and paths (approved by Nathan 2026-11-13): roads are chains in the order listed (3 to 8 to 1; 2 to 6 to 10 to 7).  A path joins 4 and 9 (Svetla Hama and Zimna Toride, on the same island).  The path list is complete; seeded paths to wild settlements and camps come on top.
- Ferries run between the coastal towns 1, 8, 2, 4, 9, 10 (Setareh Minato, Darya Kako, Ikh Gawa, Svetla Hama, Zimna Toride, Kawa Fada).
- Ferry rule (Claudia, approved by Nathan 2026-11-13): any ferry town reaches any other by sea, routed by sea pathfinding, so the route to Kawa Fada runs through the strait by itself.
- Rail (Nathan, 2026-11-13): a spaceport-run train is fast travel from city to city, boarded only in a city.  Its undersea tunnels are deadly to walk: a warning, then the train.  Eight stations on one loop: Setareh Minato, tunnel H8, Ikh Gawa, Davs Mizuumi, Kawa Fada, Shio Loch, tunnel V5 to V6, Khaluun Onsen, Warmes Tani, Darya Kako.  Svetla Hama and Zimna Toride are reached by plane or ferry.  Details in `world.md`, The rail line (mechanic #72f).
- Air (Nathan, 2026-11-13): airports at Setareh Minato and Svetla Hama; a ticket between them is fast travel to the island.  Every city also has a military air base, closed to the player.  Details in `world.md`, Airports (mechanic #72g).
- Checked on the canon globe (Claudia): every road and path stays on one landmass.  S1 shares a continent with 2, 6, 10, and 7.  Setareh Minato and Zimna Toride each sit about 190 to 195 km from the nearest coast (corrected 2026-11-13; first measured as about 180 and 300 km).  Svetla Hama sits about 670 km from the open sea; the shore it is named for is a small lake about 60 km away (open item).
- Ferries to Kawa Fada (10) are long: they go out to the left, through the strait near Shio Loch, and then on down to Kawa Fada (Nathan, 2026-11-11).
- Checked on the canon globe (Claudia): Kawa Fada sits on an enclosed inner sea whose only opening below the ice line is the strait at X3 and W4, beside Shio Loch (V4).  The traced route from Ikh Gawa runs north past Darya Kako, west along row 3, across the map's wrap edge to X3, through the strait, and south to Kawa Fada: about 42,000 km, roughly 2 to 3 months at ferry speeds, with about 8,000 km along 58 N at the edge of the ice.
- Correction (Claudia, 2026-11-13, found while drawing the start candidates map): the opening is a passage, not a narrow strait.  Kawa Fada's inner sea opens only to the north, through a passage east of Shio Loch (W4 and W5) that is about 900 km wide at its narrowest (W5).  Ships from the central sea (Setareh Minato, Darya Kako, Ikh Gawa) reach it only by going around the north near the ice.  The route length depends on how far north the ice lets ships go: about 27,000 km with open water up to 66 N, about 35,000 km held below 62 N, and about 42,000 km hugging 58 N.
- **Draft (Claudia):** the Kawa Fada ferry is seasonal, closed by ice in winter.  In a cold year the northern route freezes and sea ice roads open instead.  Shio Loch sits on the only sea gate to Kawa Fada, which feeds the brothers' feud (2026-11-13: the gate is a passage about 900 km wide and Shio Loch is about 1,200 km from the open sea, so this part needs a rethink).
- Road types (Nathan, 2026-11-12): separate what is visual from what affects movement.  A road gives no speed boost; it simply means travel at your maximum with no limitation.  A path is worn but may be a little muddy, about 80% (an estimate).  Animal trails through a forest and the like are visual only, with no effect on movement: they count as the cells around them, so difficult terrain stays difficult.  A small animal trail might later give some access (like a hole in a wall) once tools and drones exist.
- Roads, paths, and trails are defined on the overmap, then on the region as it is generated, then on the player's local map as it is generated (Nathan, 2026-11-12).
- Building on a road has consequences (Nathan, 2026-11-12).  People use the road, unlike RimWorld, where a road is just a generated tile that does not affect who comes or goes.  Road edges spawn traffic like the other spawners, so travelers run right into a base built on a road, and players learn that lesson.
- Wheels (Claudia, approved by Nathan 2026-11-12): on foot, paths are about 80%; carts, wagons, and vehicles run paths at about 50% and cannot use animal trails.  Weather still applies to roads: snow and thaw floods can bury or wash them out.
- Traffic (Claudia, approved by Nathan 2026-11-12): caravans, patrols, refugees, couriers, and bandits; volume by road importance (main city roads busy, paths quiet), changing with seasons, wars, and the cold year.  A roadside base can run an inn, toll, or waystation, but raiders find it easily, and blocking a road is a political act that angers travelers and the road's lord.  Catch-up includes traffic.
- Tolls (Nathan, 2026-11-12): a gate can charge travelers walking through, as a side source of money.  It must be manned, by one of the player's NPCs (a real sacrifice, since they are valuable) or by a robot.  Travelers complain or agree in a log or chatter, but either way they pay.  It could be abused, so there may be side effects and criteria for creating a toll.  Travelers may turn around and leave, or try to walk around.
- Toll payments (Nathan, 2026-11-12): a toll robot cannot be robbed of money, since money is tracked electronically; money paid in is recorded by the robot and stored, directly.  Bartering is core to almost every RPG, so travelers and traders may pay in goods instead (a sack of potatoes, an animal, things of equal value), and anything paid that way can be stolen.  The whole robot can also be stolen.
- Tolls are placed on the player's local map; everything else about them rolls up into the catch-up math (Nathan, 2026-11-12).
- A toll's map ticks because it is manned: the NPC counts as the player's people, and so does a toll android, so an android-manned toll gets the catch-up run without the M.U.L.E.'s tracker (Claudia's suggestion, agreed by Nathan 2026-11-12).
- In this context the robot is a person.  For separation, it is called an android, as opposed to a machine like a farm robot (Nathan, 2026-11-12).
- Superseded (Claudia, 2026-11-13 review): an earlier draft here had every android talking in simple scripted lines.  Nathan's android tiers in `concept.md` (Androids) replace it: tier 2 androids can have real personalities and still sit below a person, and none is as smart or useful as the M.U.L.E.
- **Draft (Claudia), tolls:** an android collects less and cannot talk anyone down.  The rate is a setting: low rates mostly get paid with grumbling, high rates send more travelers back or around the gate off-road (walls stop that, at a cost).  The camp log carries the chatter.  Charisma collects more and calms complaints, Strength discourages arguing, and bandits attack instead of paying.  Traffic remembers: gouging reroutes caravans over a season.  Criteria come from ownership: a lord's road needs a charter (permission and a cut), and tolling without one is banditry that brings a patrol; unclaimed land can be tolled freely, but traffic there is thin.
- (Claudia, approved by Nathan 2026-11-13) each inland ferry town gets a landing, a small port on the nearest coast tied to the town by road, where the ferry docks (like Athens and Piraeus).  This covers Setareh Minato (about 190 km from the nearest coast) and Zimna Toride (about 195 km) (distances corrected 2026-11-13).

## Montage events (Nathan, 2026-11-11)

- Full event tables wait until more of the game is established, but a number of generic events can be accounted for now: breakdowns, sickness, a trader passing by, attacks (wildlife and bandit), and the ever-popular Oregon Trail events, just more modern.  Dysentery would seem like no problem, until there is no clean water and nobody smart enough to know better.
- (Claudia, approved by Nathan 2026-11-11 as starters) generic events and what helps: breakdown of a vehicle, sled, or gear (Intelligence, spare parts); waterborne sickness and food poisoning (Intelligence, camp rules, water treatment); injuries from native spines, falls, frostbite (Perception, medicine); a pack animal lame or dead (rest, feed); river crossings (boats, Strength, Intelligence); lost days off the trail (Intelligence, Perception, maps); storms and white-outs (weather sensor, shelter); supplies stolen at night (watch rules, Perception); a passing caravan (Charisma); wildlife attack (Perception to spot it early, weapons); bandit attack (Charisma, Strength, cover); good events such as a game herd, a hidden cache, a hot spring, friendly travelers (Perception); infected ground (detours, plant analyzer); a downed flier (#94).
- (Claudia, approved by Nathan 2026-11-11 as starters) each event checks a stat, gear, or camp rule, and offers a choice when there is a real decision.  Events come from what the party lacks, not from bad luck alone.

## Montage stops (Nathan, 2026-11-11)

- Stop rules are simple: food, unable to progress, too many people sick, and the like.
- (Claudia, approved by Nathan 2026-11-11) forced stops: food or water below a set number of days left; the party cannot progress (impassable river, cliff, blizzard, vehicle out of fuel or broken); too many sick or hurt (for example half the party, or anyone critical); someone dying; an event that needs a choice; hostile contact; arrival at the destination or a marked point.
- (Claudia, approved by Nathan 2026-11-11; marker fixed in the 2026-11-13 review) player-set stops, like Oregon Trail's pace and rations: stop at any settlement, stop if food drops below X days, stop at anything interesting.
- (Claudia, approved by Nathan 2026-11-11) nightly camp happens inside the montage and is not a stop, unless something goes wrong in the night.
- Before starting a montage, the player can set how hard they push it (Nathan, 2026-11-11).
- (Claudia, approved by Nathan 2026-11-11) montage settings: Pace (Easy, Steady, Hard, Grueling: more km per day against fatigue, injury, sickness, and gear wear); Rations (Full, Reduced, Bare: food lasts longer against health, mood, and cold resistance, since fewer calories means less body heat); Rest days (none, or every N days); Caution (Bold, Normal, Careful: risky shortcuts and fewer events, or detours around danger and slower travel).  Settings stack with the slowest-unit rule and can be changed at any stop.

## Returning to a site

- When the player returns to the crash site, a quick math and adjustment run determines the state of the site: whether anybody survived or stayed, and what their averages are.  The map is adjusted, then the player enters (Nathan, 2026-11-10).
- (Claudia, approved by Nathan 2026-11-11) the catch-up run is seeded by the run seed, the site, and the time away, so the same absence always gives the same result.

### Catch-up run rules (Nathan, 2026-11-11)

- Broad.  Some things are estimated.  The whole idea is to simplify the main elements so time can move quickly.
- The player is warned on leaving, for example: "You are about to leave the map.  While you are away, your base will manage itself."  The engine then runs the math with nothing animated.
- People can die while the player is away.
- The camp log (Claudia's suggestion, agreed): a quick summary of what was calculated, so the player can review and plan accordingly.
- Only maps where the player's people are tick.  Maps need the player or one of their NPCs.
- Things left on a map with nobody watching can be stolen.  They stay for a time, depending on what is close.  Bandits nearby: it will not last; within days the map is reset and empty.  No bandits, but alien bears nearby: food may be gone while other supplies are fine.  It should be logical.
- Settlements, bandit camps, dungeons, caves, and spawners get basic math (whether anything leaves, raids, and so on), never day-to-day calculation.
- **Draft (Claudia), unattended goods:** each nearby threat takes what it wants: bandits take anything of value, animals take food, weather and time spoil food and wear gear, and infected ground can take mineral goods.  Hidden or locked caches last longer.
- **Draft (Claudia), off-map sites:** each settlement, camp, or spawner carries a few numbers (strength, supplies, mood toward the player) updated in coarse steps; raid chance on the player's camp grows with strength and nearness.

## Cities

- Major cities are handcrafted, so they are uniform and their map tiles are built as we go.  They can hold anything: dungeons, banks, vendors, crime syndicates, points of contention, and the major story points (Nathan, 2026-11-10).
- Staging: start with one major city and one limited area, with play mostly within its range.  Then slowly work out to the outskirts.  Next, add another city, built by hand.  For each one, we roughly build the map design, then add the stories that map brings (Nathan, 2026-11-10).
- Stepping into a town should be a big event.  Depending on where the player steps in, they may get Al-Qadim or Aladdin, New York or Berlin.  This is what sets it apart from RimWorld's random generation: we build story for our hero instead of making just another survival game (Nathan, 2026-11-10).
- We do not map every square of a city, only the areas that are important and that the player needs to go to.  Nobody wants to travel miles of homes with no value in going into them (Nathan, 2026-11-10).
- Each city has a wall, and the player crosses through a gate.  There is an entrance on the side of a map, or just the entrance; the player enters, then gets the city map.  City maps are different from world maps (Nathan, 2026-11-10).
- Entering towns when hated (Nathan, 2026-11-13, a small note for the future): there may be future ways to sneak in, such as with cargo (mechanic #60b).
- The city as a linked space (Nathan, 2026-11-12): a player approaches the gate and deals with the gate guard (or whatever that gate's obstacle is).  The gate acts as an entrance to another space, the same way dungeons, buildings, and RVs work.  Inside, the rules are the same, but the player is no longer on the overmap: the city is like a region of its own whose size we choose.  It can be any shape, any number of maps, and it does not have to match the planet's landscape.  Only maps that tell the story are made (quests, special vendors, story beats); no filler, unlike Skyrim's and Oblivion's houses.  From these maps, the player can drill further into businesses, dungeons, castles, and wherever the main people are.
- City space rules (Claudia, approved by Nathan 2026-11-12): the area is called the city space, made of districts (maps); districts connect by edge walking between neighbors and by the city map for jumps with travel time; each gate opens into a different district; ticking, catch-up, the M.U.L.E., and sensing work the same inside.
- What can be seen from outside must exist inside (Claudia's point, agreed): this is a city design issue for us, not an engine concern.  Players usually see little from outside, but corridors and canals that cross the walls must be mapped inside (Nathan, 2026-11-12).
- On the overworld, the land a city covers is blocked off: roughly 8 to 10 region cells, more or less depending on the city, that we do not have to do anything with, since they are technically inside the city.  Walls on the outskirts stop players from crossing.  If someone ever does cross, that is a bug, and it gets marked.  The generator may still generate things in the blocked cells, so the engine needs no special rule; the walls alone keep people out, and they are impenetrable to anything a player has.  Alternative if wall crossing is ever allowed: a player who crosses simply appears at the nearest gate, as if they had entered (Nathan, 2026-11-12).
- (Claudia, approved by Nathan 2026-11-12) the city file lists its blocked region cells and wall line; the montage's pathfinding treats blocked cells as impassable except through a gate; the GM tool logs any position inside a blocked cell as a bug report.
- First city: Kawa Fada (Nathan, 2026-11-11).  It was going to be Shio Loch or Kawa Fada, since the build extends outward from S1.  Shio Loch is the natural second city, along the road from 10 to 7.  On foot from S1: Kawa Fada about 6,300 km (about 400 days), Shio Loch about 9,600 km (about 620 days); the GM tool removes the wait during testing.
- An easy build mode is needed to create the cities.  This is the main reason cities wait until the game is established: much of what a city needs is built in the early stages (Nathan, 2026-11-11).  See mechanic #87c.
- (Claudia, approved by Nathan 2026-11-11) the city as a hub:
  - The gate map is handcrafted: wall, gate, guards, the queue, the arrival event.  The first ID check happens here.
  - The city map shows the districts.  The player picks a destination; time advances for the trip, with a chance of a short event on the way (pickpocket, a patrol checking papers, a syndicate runner).
  - Only the districts that matter get handcrafted local maps: gate, market, bank, port, slums, syndicate turf, the lord's hall, dungeon entrances.
  - The population lives in the background as crowds, noise, prices, rumors, and faction pressure.
  - Each city has its own data file (districts, vendors, banks, factions, dungeons, story beats, arrival event); the planet file points to it.
- (Claudia, approved by Nathan 2026-11-11) outside the wall are ordinary local maps, with fields, roads, shanties, and traffic thickening toward the gate.
- Superseded (2026-11-13): (Claudia, approved by Nathan 2026-11-11) in early builds with one city, the seed places the crash within reach of that city.  Planet-wide random crashes return as more of the world is built.  The Tutorial Start at S1 and baked regions unlocking replace this.

## Seeds

- Two seeds (Nathan, 2026-11-13, from Claudia's draft): the world seed, 2718, builds the canon planet and never changes; the run seed is one per playthrough and controls everything in the "same for the same seed" tiers below.  Where this file says "the seed" in those tiers, it means the run seed.  The Random Start rolls a run seed, shown on the new-game screen with an edit box, so a player can type in a friend's seed.
- Most landmarks are random by the seed, which makes setting the seed at generation key.  A player with seed X gets the same world as another player with seed X; seed Y may get something different.  Key areas stay the same, but on Y there may be an oasis nearby in a desert area (Nathan, 2026-11-10).
- Landmarks follow the land: a seed picks among places the world allows (an oasis only where water can exist) and never breaks the physics (agreed by Nathan, 2026-11-10).
- Seeds are tied to a generator version.  A save records the generator version that built it, and a shared seed is good for that release (agreed by Nathan, 2026-11-10).
- (Claudia, approved by Nathan 2026-11-11) what the seed controls:

| Tier | Same on every seed? | Examples |
|---|---|---|
| Canon | Always | Globe, the ten places, impact sites, rivers, roads between cities, city gates and districts |
| Seeded landmarks | Same for the same seed | Oases, ruins, caves, hot springs, clan camps, downed fliers (#94), the crash site |
| Local detail | Same for the same seed | Trees, rocks, critters, loot |

## Saving

- (Claudia, approved by Nathan 2026-11-11) "once generated, fixed" needs no stored maps.  Seed plus coordinates plus generator version rebuilds any region chunk or local map exactly; the save stores only what the player changed (delta saves, mechanic #4).  Unvisited maps cost nothing, and montage travel never builds the maps it passes over.

## Performance notes (Claudia, approved by Nathan 2026-11-11)

- Turn-based play costs work per move, not per frame.  A 256 by 256 map is 65,536 tiles, small for the target PC.  The real cost is creature AI and pathfinding each turn; dozens of creatures on a map is fine.

## Zone graph format (approved by Nathan 2026-11-12 to 2026-11-13)

1. Store only what math cannot derive: neighbors, edge crossings, and local maps are calculated (see Stored and unstored maps).
2. Region files: see Region file contents.
3. City files: a city is a linked space (see Cities): its districts, how they connect, which gate opens where, the linked maps hanging off each district, and its blocked region cells and wall line on the overworld.  **Draft (Claudia), the rest of a city file:** header (ID, version, culture, music area, territory, place in the planet file), gate maps with fixed edge crossings, districts (contents, travel time on the city map), named NPCs (district, role, faction, special or not), story beats (arrival comic, quests, local news spin), rules (curfew, weapons, papers, what is illegal); handcrafted maps saved as Godot scenes, referenced by the city file.
4. Edge IDs: see Edge IDs.
5. Save file: see Save file.
6. Format: JSON to start, with the escape hatch built in (Claudia, approved by Nathan 2026-11-13): one save module, the only code that touches save files; every saved thing has to_dict and from_dict with explicit types (Godot's JSON reader returns every number as a decimal and does not know Godot's coordinate types); the manifest records the format and save format version; migrations chain version to version so old saves never break; big grids stay packed; compression on early (Godot writes compressed files directly, including zstd).  Switching formats later means swapping the writer and adding one converter.

## Open

- Full montage event tables, once more of the game exists.
- Draw the rail loop with the routes layer (stations and tunnels are set).
- Svetla Hama is a ferry town but sits about 670 km from the open sea, about 60 km from a small lake: a landing on the sea, a lake ferry only, or no ferry (Nathan's call).
- River inflow across region borders: feed upstream flow from the globe into each region's window (before a second region is built).
- `tools/region_gen.py` to write the newer region layers (salinity, flow direction and speed, full-detail height, moisture, territory, routes, landmarks, entrances).
- Drafts still open in this file (full list from the 2026-11-13 review): seeing far part 3, vistas (the descent footage and beacon are decided); radio ranges; thaw floods; beacon snapshot view; M.U.L.E. and beacon sensing details; Kawa Fada ferry seasons; tolls (rates, chatter, charters, rerouting); unattended goods; off-map site numbers; the rest of the city file contents (Zone graph format, item 3).
