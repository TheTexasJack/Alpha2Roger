# Alpha2-Roger Zones and Travel

**Zones v0.35, 2026-11-11**

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
- Peak height (Claudia, approved by Nathan 2026-11-11): the R5 peaks stand about 3,500 m, about 40 F colder than the lowlands by the lapse rate: cool summers and freezing winters up top, deep below zero in a cold year, a snowcap visible from far off in the warm band.
- Height and difficulty (Nathan, 2026-11-11): the higher up, traditionally, the more chance of caves and such.  As in traditional RPGs, the more complicated and harder a place is to reach, the better the chance of finding something rare.  A peak in the negatives is a good early challenge for dealing with extreme cold, so put something there the player needs.  Reward effort, even when it is impossible at the time.
- The R5 peak holds a derelict relay station, since real relay towers sit on the highest ground for line of sight (Claudia, approved by Nathan 2026-11-11).  It is unreachable without cold gear.  Restoring it could give long-range comms (an early thread for the legal battle), weather warnings, or a region map reveal.  The massif's flanks carry caves and mineral veins.
- Correction (Claudia): from a 3,500 m peak the horizon is about 220 km on Verlassen, and S1 is over 1,100 km away, so the tower cannot be seen from the crash site.
- The 2D map needs a way to show what is in the distance: maybe a spot with a telescope, or pictures from a M.U.L.E. scan that show the relay tower (Nathan, 2026-11-11).
- **Draft (Claudia), seeing far:** (1) descent footage: the M.U.L.E. recorded on the way down, and a few frames show the snowcapped massif and a glint on the summit, shown as comic panels; (2) a faint beacon: the relay still pings on shortwave, which can bounce off the upper atmosphere over thousands of km, so the M.U.L.E. marks it on the region map; (3) vistas: high spots on local maps with a telescope or binoculars show a horizon panel and reveal landmarks within real line-of-sight range on the region map.  Know it from day one, see it within about 200 km, reach it with cold gear.

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
| Region map | about 4 km | Montage travel, roads, rivers, biomes, points of interest, events |
| Local map | 250 by 250 tiles, about 250 m | Turn-based play, camp, combat, walking from map edge to map edge |

- (Claudia, approved by Nathan 2026-11-11) about 16 by 16 local maps per region cell and about 15 by 15 region cells per globe pixel, an even step at each layer.
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
- **Draft (Claudia), overworld baselines,** about 8 travel hours a day, in km per day: on foot on a road with a light load 30 to 35; on foot in wilderness 15 to 25; hauling a heavy load or sled 10 to 15; deep snow without snowshoes 5 to 10; snowshoes or skis 15 to 30; wagon or cart 25 to 30 (the Oregon Trail's 15 to 20 miles); horse or pack animal 30 to 40; dog sled 40 to 80; vehicle off road 100 to 250; boat downstream 50 to 100, upstream 15 to 25.  Climbing follows Naismith's rule, about one extra hour per 600 m of ascent.
- (Claudia, approved by Nathan 2026-11-11 as starters) what slows a group: terrain (biome, snow depth, climbing; roads speed it up); weather (rain, wind, fog, blizzard); daylight (no moon, so little night travel, and short winter days); load against carrying capacity; condition (wounds, sickness, hunger, fatigue, cold, anyone being carried); animals' grazing time and vehicles' fuel; river crossings; caution through dangerous or infected ground; and the cold year, which multiplies most of these.

## Routes (Nathan, 2026-11-11)

- Route distances are calculated: the region-cell grid, pathfinding across cells, a cost per cell (biome, climbing, rivers, roads, infected ground), and the speed table.  The montage planner shows the result as a range of days (Claudia's basis, agreed).
- No zigzag concern on the region or world maps: there is no WASD travel.  The player sets a path and is taken along it, so diagonals stay as they are.
- Roads run between most major settlements on a continent: 3, 8, 1 (Warmes Tani, Darya Kako, Setareh Minato) and 2, 6, 10, 7 (Ikh Gawa, Davs Mizuumi, Kawa Fada, Shio Loch).
- Paths, smaller than roads but still useful, connect the others, such as 5 to 1 (Khaluun Onsen to Setareh Minato) and 2 to 10 (Ikh Gawa to Kawa Fada).
- Ferries run between the coastal towns 1, 8, 2, 4, 9, 10 (Setareh Minato, Darya Kako, Ikh Gawa, Svetla Hama, Zimna Toride, Kawa Fada).
- Checked on the canon globe (Claudia): every road and path stays on one landmass.  S1 shares a continent with 2, 6, 10, and 7.  Setareh Minato is about 180 km and Zimna Toride about 300 km from the sea.
- Ferries to Kawa Fada (10) are long: they go out to the left, through the strait near Shio Loch, and then on down to Kawa Fada (Nathan, 2026-11-11).
- Checked on the canon globe (Claudia): Kawa Fada sits on an enclosed inner sea whose only opening below the ice line is the strait at X3 and W4, beside Shio Loch (V4).  The traced route from Ikh Gawa runs north past Darya Kako, west along row 3, across the map's wrap edge to X3, through the strait, and south to Kawa Fada: about 42,000 km, roughly 2 to 3 months at ferry speeds, with about 8,000 km along 58 N at the edge of the ice.
- **Draft (Claudia):** the Kawa Fada ferry is seasonal, closed by ice in winter.  In a cold year the northern route freezes and sea ice roads open instead.  Shio Loch sits on the only sea gate to Kawa Fada, which feeds the brothers' feud.
- **Draft (Claudia):** each inland ferry town gets a landing, a small port on the nearest coast tied to the town by road, where the ferry docks (like Athens and Piraeus).

## Montage events (Nathan, 2026-11-11)

- Full event tables wait until more of the game is established, but a number of generic events can be accounted for now: breakdowns, sickness, a trader passing by, attacks (wildlife and bandit), and the ever-popular Oregon Trail events, just more modern.  Dysentery would seem like no problem, until there is no clean water and nobody smart enough to know better.
- (Claudia, approved by Nathan 2026-11-11 as starters) generic events and what helps: breakdown of a vehicle, sled, or gear (Intelligence, spare parts); waterborne sickness and food poisoning (Intelligence, camp rules, water treatment); injuries from native spines, falls, frostbite (Perception, medicine); a pack animal lame or dead (rest, feed); river crossings (boats, Strength, Intelligence); lost days off the trail (Intelligence, Perception, maps); storms and white-outs (weather sensor, shelter); supplies stolen at night (watch rules, Perception); a passing caravan (Charisma); wildlife attack (Perception to spot it early, weapons); bandit attack (Charisma, Strength, cover); good events such as a game herd, a hidden cache, a hot spring, friendly travelers (Perception); infected ground (detours, plant analyzer); a downed flier (#94).
- (Claudia, approved by Nathan 2026-11-11 as starters) each event checks a stat, gear, or camp rule, and offers a choice when there is a real decision.  Events come from what the party lacks, not from bad luck alone.

## Montage stops (Nathan, 2026-11-11)

- Stop rules are simple: food, unable to progress, too many people sick, and the like.
- (Claudia, approved by Nathan 2026-11-11) forced stops: food or water below a set number of days left; the party cannot progress (impassable river, cliff, blizzard, vehicle out of fuel or broken); too many sick or hurt (for example half the party, or anyone critical); someone dying; an event that needs a choice; hostile contact; arrival at the destination or a marked point.
- **Draft (Claudia), player-set stops,** like Oregon Trail's pace and rations: stop at any settlement, stop if food drops below X days, stop at anything interesting.
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
- An easy build mode is needed to create the cities.  This is the main reason cities wait until the game is established: much of what a city needs is built in the early stages (Nathan, 2026-11-11).  See mechanic #87c.
- (Claudia, approved by Nathan 2026-11-11) the city as a hub:
  - The gate map is handcrafted: wall, gate, guards, the queue, the arrival event.  The first ID check happens here.
  - The city map shows the districts.  The player picks a destination; time advances for the trip, with a chance of a short event on the way (pickpocket, a patrol checking papers, a syndicate runner).
  - Only the districts that matter get handcrafted local maps: gate, market, bank, port, slums, syndicate turf, the lord's hall, dungeon entrances.
  - The population lives in the background as crowds, noise, prices, rumors, and faction pressure.
  - Each city has its own data file (districts, vendors, banks, factions, dungeons, story beats, arrival event); the planet file points to it.
- (Claudia, approved by Nathan 2026-11-11) outside the wall are ordinary local maps, with fields, roads, shanties, and traffic thickening toward the gate.
- (Claudia, approved by Nathan 2026-11-11) in early builds with one city, the seed places the crash within reach of that city.  Planet-wide random crashes return as more of the world is built.

## Seeds

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

- Turn-based play costs work per move, not per frame.  A 250 by 250 map is 62,500 tiles, small for the target PC.  The real cost is creature AI and pathfinding each turn; dozens of creatures on a map is fine.

## Open

- Exact local map size in tiles, and meters per tile.
- Region cell size and chunk size.
- Full montage event tables, once more of the game exists.
- Biome placement per region cell in R5 (the expected biomes are set).
- First city: Kawa Fada (Nathan, 2026-11-11).  It was going to be Shio Loch or Kawa Fada, since the build extends outward from S1.  Shio Loch is the natural second city, along the road from 10 to 7.  On foot from S1: Kawa Fada about 6,300 km (about 400 days), Shio Loch about 9,600 km (about 620 days); the GM tool removes the wait during testing.
- The zone graph output format for A2R-103.
