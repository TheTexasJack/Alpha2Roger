# Alpha2-Roger Zones and Travel

**Zones v0.7, 2026-11-11**

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

## Grid (Nathan, 2026-11-11)

- Square grid, one grid across the board.  It also makes the math of regions easy: we just pick a grid number.  64 is old-school Minecraft logic, but we fit what meets our needs.
- **Draft (Claudia), powers of two anchored on the canon globe:** one globe pixel (about 61.2 km) is 16 by 16 region cells (about 3.8 km each); one region cell is 16 by 16 local maps; one local map is 256 by 256 tiles (about 240 m); one tile is about 0.93 m.  Region chunks are 8 by 8 globe pixels, 128 by 128 region cells (about 490 km).  This refines the approved 4 km cells, 250-tile maps, and 10-pixel chunks below.
- **Draft (Claudia):** diagonal steps cost 1 for movement; range counts diagonals 1, then 2, alternating, so ranges come out nearly round.
- Approved by Nathan 2026-11-11 (Claudia's suggestion): the engine keeps coordinates local to the current map, since the planet is about 47 million tiles around and engines lose precision at huge positions.
- Blockiness is normal (Nathan, 2026-11-11).  Mapped out by region or by local map, the whole world looks blocky and weird.  The more you zoom in, the more a region is a square.  That is where the math and the beauty of the world map cross.
- Edge matching uses the RimWorld logic: a river has a top and a bottom where it enters and leaves, and the inside does not matter as long as the top and bottom match (Nathan, 2026-11-11).  The same goes for roads and other features that cross map edges.
- **Draft (Claudia):** a crossing point belongs to the edge, not to either map.  It is calculated from the seed and that edge's ID, so both neighbors agree no matter which one is generated first.  The region map decides which edges a river or road crosses; the local generator draws any path between its crossing points.
- Because the inside of a map is free, the engine can slip in a settlement and move the river accordingly (Nathan, 2026-11-11).
- **Draft (Claudia), local generation order:** edges (crossing points), then placements (settlement, ruin, crash site, downed flier), then routes (rivers and roads between crossings, shaped by the placements), then fill (terrain, plants, rocks, critters).  Settlements want water, so a river is routed past or through a settlement (docks, mill, bridge) rather than away from it.  Handcrafted maps keep fixed edges, and their generated neighbors read crossing points from them.
- **Draft (Claudia):** biome changes blend over a band near region cell edges instead of switching exactly at the line, so a desert cell fades into grass rather than stopping at a straight edge.
- **Draft (Claudia):** the player's map view shows visited local maps stitched together as squares, with unvisited ones blank, like the reference samples.  The blocky patchwork becomes the record of where the player has been.

## Layers

- Three maps: a globe map, a region map, and local maps.  The region map is the equivalent of the RimWorld world map (Nathan, 2026-11-10).
- (Claudia, approved by Nathan 2026-11-11) scale:

| Layer | One cell is | Used for |
|---|---|---|
| Globe | about 61 km (the canon 720 by 360 map) | Strategic view: where the player is, where the cities are.  Canon, never changes |
| Region map | about 4 km | Montage travel, roads, rivers, biomes, points of interest, events |
| Local map | 250 by 250 tiles, about 250 m | Turn-based play, camp, combat, walking from map edge to map edge |

- (Claudia, approved by Nathan 2026-11-11) about 16 by 16 local maps per region cell and about 15 by 15 region cells per globe pixel, an even step at each layer.
- (Claudia, approved by Nathan 2026-11-11) region maps are fixed square chunks of the globe (for example 10 by 10 globe pixels, about 610 km on a side, about 150 by 150 region cells), not the political regions, since about 65% of habitable land belongs to no region.  Chunks tile seamlessly; political borders are drawn on top as data.
- (Claudia, approved by Nathan 2026-11-11) each layer is built from the one above it.  The globe feeds the region chunk; the region cell feeds the local map.  A river on the globe stays a river on the region map and in the local map.

## Travel

- Overland travel works Oregon Trail style, with a montage.  The player preps everything and moves it along.  Movement across open land is a montage: time moves at an accelerated rate, random events may go off, there are things to stop and visit, and eventually the player has to stop and set up camp (Nathan, 2026-11-10).
- Players can walk the whole distance, because some will try, or they may have crashed nearby (Nathan, 2026-11-10).
- (Claudia, approved by Nathan 2026-11-11) walking and the montage are the same world.  The montage is a fast-forward over the same seeded maps; if an event stops the player partway, the local map they land in is the one they would have reached on foot.
- (Claudia, approved by Nathan 2026-11-11) near camp, the player walks off a map edge into the neighboring local map, Qud style.

## Returning to a site

- When the player returns to the crash site, a quick math and adjustment run determines the state of the site: whether anybody survived or stayed, and what their averages are.  The map is adjusted, then the player enters (Nathan, 2026-11-10).
- (Claudia, approved by Nathan 2026-11-11) the catch-up run is seeded by the run seed, the site, and the time away, so the same absence always gives the same result.

## Cities

- Major cities are handcrafted, so they are uniform and their map tiles are built as we go.  They can hold anything: dungeons, banks, vendors, crime syndicates, points of contention, and the major story points (Nathan, 2026-11-10).
- Staging: start with one major city and one limited area, with play mostly within its range.  Then slowly work out to the outskirts.  Next, add another city, built by hand.  For each one, we roughly build the map design, then add the stories that map brings (Nathan, 2026-11-10).
- Stepping into a town should be a big event.  Depending on where the player steps in, they may get Al-Qadim or Aladdin, New York or Berlin.  This is what sets it apart from RimWorld's random generation: we build story for our hero instead of making just another survival game (Nathan, 2026-11-10).
- We do not map every square of a city, only the areas that are important and that the player needs to go to.  Nobody wants to travel miles of homes with no value in going into them (Nathan, 2026-11-10).
- Each city has a wall, and the player crosses through a gate.  There is an entrance on the side of a map, or just the entrance; the player enters, then gets the city map.  City maps are different from world maps (Nathan, 2026-11-10).
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
- Travel speeds on foot, by vehicle, on roads, in snow.
- Montage event tables and stop rules.
- Catch-up run rules.
- Biome regions (moved from A2R-101).
- Route distance ranges (moved from A2R-101).
- Which city is built first.
- The zone graph output format for A2R-103.
