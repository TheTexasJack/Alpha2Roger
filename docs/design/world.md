# Alpha2-Roger World

**World v0.86, 2026-11-13**

Decisions are Nathan's unless marked **Draft (Claudia)**.  Drafts are suggestions until Nathan approves them.

This file holds the world facts that become the planet data file (A2R-101).  The packed file is `tools/data/planet_verlassen.json`, built by `tools/planet_pack.py`.  Only decisions go into it; drafts stay here until approved.  Change a fact here first, then update the pack and rerun it.

## Era and location

- Current time: 5071u (Nathan, 2026-11-12), roughly 50 years after the events on Halas at Nathan's Lancer table.  Note (Claudia): the Lancer core book's present is 5016u, so the game is set about 55 years after canon's present day.  Earlier drafts said 5016u.
- Verlassen is about 50 light years away, and the planet is only now getting signals, feeds, and other things from the spaceport and elsewhere.  So current material from Nathan's Lancer tables can be used as news and other in-world information, and it is lore appropriate (Nathan, 2026-11-12).
- Local stations rebroadcast the old news (Nathan, 2026-11-12).  Each puts its local spin on it: moving to another zone, the player hears the same story told with that zone's spin.
- Spin (Claudia, approved by Nathan 2026-11-12): one source story, retold through each region's concerns (the steppe asks about the horses, the salt traders about salt prices, the spaceport sounds dry and official).  Shio Loch and Kawa Fada tell the same story in opposite ways, each making the other brother look bad, so the feud plays out on the air.  Built as one story file plus one spin per cultural region.
- (Claudia, approved by Nathan 2026-11-12) a handheld radio cannot catch a broadcast from 50 light years away, so the spaceport's big dish catches the old light-speed broadcasts and local stations rebroadcast them (an "old news hour" on the M.U.L.E.'s radio).  That makes two speeds of news: old light-lagged news free on the radio, and live omninet contact through the spaceport, instant and expensive, the same channel the legal battle's messages use, costing Manna per transmission.
- Radio and news feed off the culture map, not the other way, and not off the music areas (Nathan, 2026-11-13).  There will be some overlap with the music, but radio and news are mostly flavor elements we need to record: simple musical elements, voice recordings, and things we can create regardless of anything else.
- Weather is different and is not part of the radio and news flavor (Nathan, 2026-11-13).
- Stations (Claudia, approved by Nathan 2026-11-13): each station belongs to a place (one of the ten, or a seeded settlement) and takes that place's cultural region from the planet file; the player hears whichever stations are in range (radio ranges in `zones.md`).
- Culture map (Claudia, approved by Nathan 2026-11-13; built, see Culture map): until now the only every-spot culture map lived inside `tools/music_areas.py` (land takes the culture of the nearest place reachable overland).  Split it out as its own culture map (`tools/culture_map.py` writing `tools/data/culture_map.json`); music areas then read the culture map and add their own music-only layers (sea shanty, ice dread, Overall, shore water), and radio, news, and settlement names read the culture map too.  Culture feeds music, radio, and news; music feeds nothing.
- On the galaxy map, about 50 years from the worlds of Nathan's current game tables.  Reachable, but out of the way and untouched by any current table or players.
- Location on the Errans Inter Astra Atlas of the Known Diaspora: far to the left, between Cinder Crown (deep-field relay) and the Karrakin Trade Baronies.  Nothing else is charted there; well out of the way, near the horizontal line through the galactic core.
- **Draft (Claudia):** Cinder Crown is the relay every blink message from the planet passes through, which is why replies take weeks or months.
- The Karrakin Trade Baronies are the nearest real power and the closest trading location.
- The region also has a few small colonies on some other planets, and a single space station.
- Who runs the space station is deferred to later.
- **Draft (Claudia):** some of those colonies may sit in Verlassen's own crowded star system.  They are natural candidates for future expansion planets.
- **Draft (Claudia):** Baronic traders may keep the spaceport alive while the locals keep them at arm's length.

## The planet

- Official name: Kepler-64432p.
- Local name: Verlassen (German for abandoned, forsaken, left behind).
- The system is crowded: "p" makes Verlassen at least the 15th planet catalogued around its star.  This leaves room for the gas giant behind the cold year.
- The star: Sun-like and yellow (G type), about one solar mass.  Chosen by the physics: with a year of about 14 Earth months, Verlassen orbits at about 1.1 times Earth's distance and receives roughly 80% of Earth's sunlight, which matches temperate but colder than some.  A massive star would put the temperate zone so far out that a year would take decades; an orange star would leave a 14-month orbit too cold.
- Science and physics win over hip shots: when a stated detail conflicts with real physics, the physics decides.
- **Draft (Claudia):** with the 3:1 resonance, the gas giant orbits about every 3.5 years.
- **Draft (Claudia):** optional lore: the star is aging, for flavor only.
- Temperate, but colder than some.
- Size: slightly larger than Earth (about 10% wider), with about Earth's gravity, so nothing new needs inventing.  Physics note: same gravity at a larger size means a slightly less dense planet (a smaller iron core).
- Moons: none.  No moonlight.  Physics note: tides are small (from the sun only); a moon's long-term tilt stabilizing works over millions of years and does not matter in play.
- Rings: none.
- **Draft (Claudia):** with no moon, nights are pitch black under starlight only.  Darkness becomes a survival pressure that pairs with fog of war and 2D lighting.  The gas giant may be the brightest object in the night sky.
- Year: 14 Earth months, as first set.
- Calendar (Nathan, 2026-11-11): 12 months of 35 days, 420 days a year.  Aligning to the planet's orbit beats making it feel alien for its own sake.  The 420 meme is ignored.
- Physics note (Claudia): Kepler's law for about 1.1 AU around a one-solar-mass star gives about 421 days, so 420 matches the orbit.  A 35-day month is exactly five 7-day weeks, so every month starts on the same weekday, and 12 months split into four seasons of three months.  Day length is not set; the count assumes a 24-hour day.
- Every third year is a cold year.  The whole planet goes through a cold phase lasting about a planet year as it moves away from the sun.
- Normal years have a full standard seasonal year.
- In the cold year, everything shifts down about 50 degrees Fahrenheit.  Summers that would hit 100 only reach about 50, and even summers can sit in the 30s.  Winters that would sit around 0 drop to -50 or colder.
- The cold year is something the player builds up for.
- **Draft (Claudia):** consequences to design around: the cold year has no real growing season, so the camp must stockpile about a full year of food beforehand; -50 and colder makes exposure lethal fast, so shelter, heat, and clothing layers matter; long journeys during a cold year are effectively impossible.
- The mechanism behind the three-year cycle: a gas giant neighbor in a 3:1 orbital resonance pulls the planet onto a wider orbit every third year.  Normal axial-tilt seasons happen in the other years.

## The warning

- A working weather sensor on the mech wreckage gives notice.  As things get colder, it warns that the winter will last months.
- Like Subnautica: scripted computer voice lines, ElevenLabs style, explain the weather patterns of the planet the player just crashed on.
- **Draft (Claudia):** repairing the mech's sensors extends the forecast, so the first repair buys warning time.
- **Draft (Claudia):** the mech computer's voice doubles as the tutorial.  Subtitles are always on, with a log the player can reread.  The voice glitches and cuts out with damage and cleans up as systems are repaired, and late in a cold year it gets quieter as power runs low.  Because it is a fixed, hand-written set of lines generated once, it can come well before live NPC voices.
- **Draft (Claudia):** the seed picks where in the three-year cycle the crash happens.  Crashing just before a cold year makes a brutal run.

## Climate bands

- Similar to Earth: warmest along the equator, colder toward the poles.
- The upper edges take the cold year's -50 shift on top of the cold they already have, so they might reach -150 F once the cold year is established (Nathan, 2026-11-10).
- The -50 shift stays (Nathan, 2026-11-11).  Cold is the enemy, so no city sits in the 50s in a cold year.  Freezing at night is fine: out in the wilderness, a day above freezing would not thaw things before they freeze and ice again.
- **Draft (Claudia), latitude lines,** Earth-like inland temperatures in F (normal summer high / normal winter low, then cold year high / low at -50):

| Latitude | Normal high | Normal low | Cold year high | Cold year low |
|---|---|---|---|---|
| 0 | 90 | 72 | 40 | 22 |
| 10 | 93 | 66 | 43 | 16 |
| 20 | 97 | 55 | 47 | 5 |
| 30 | 97 | 38 | 47 | -12 |
| 40 | 88 | 20 | 38 | -30 |
| 50 | 76 | 3 | 26 | -47 |
| 60 | 66 | -15 | 16 | -65 |
| Ice caps | | -80 | | -130 to -150 |

- **Draft (Claudia), the ten places in a cold year** (high / low, F): Setareh Minato 38 to 42 / 17 to 20; Svetla Hama 47 / 3; Kawa Fada 47 / -2; Darya Kako 44 / 0; Ikh Gawa 46 / -14; Warmes Tani 45 / -17; Shio Loch 35 / -35; Khaluun Onsen 27 / -45; Davs Mizuumi 25 / -49; Zimna Toride 23 / -52.  Hemispheres run opposite seasons.
- **Draft (Claudia):** daytime thaws only melt the surface, which refreezes overnight as crust and black ice, so cold-year travel in the warm bands is treacherous rather than easy.
- Physics note (Claudia): plausible.  Earth's coldest recorded air is about -129 F (Vostok, Antarctica), with satellite readings near -144 F on the high ice, and Verlassen gets about 80% of Earth's sunlight.  At those temperatures ordinary steels turn brittle, rubbers and plastics crack, and batteries fail, so cold is cold and metal is metal even for far-future gear.
- **Draft (Claudia):** the high north is where cold-rated gear stops being a luxury and becomes the price of entry.  Zimna Toride (about 53 N) and the T3 impact site (about 58 N) sit near that edge.

## Geography

- The globe: candidate B, seed 2718, is canon.  Map: `assets/maps/verlassen_globe_v1.0.png` (generator `tools/globe_candidates.py`).  Its continents stretch across the globe, so in the cold year, with frozen straits, the whole planet can be traversed on foot.  Climate bands on the map are placeholders; cities, spaceport, and final impact sites are still to be placed.
- Volcanic and geothermal areas that do not freeze: springs and Yellowstone-type geysers.
- Salt lakes that might never freeze, except on the coldest days of the third year.
- Rivers.  All major cities sit near rivers.
- Three infection impact sites on the globe.
- **Draft (Claudia):** salt lakes are terminal basins where interior rivers end, as real salt lakes do.
- **Draft (Claudia):** a cold planet shows more land than Earth (water locked in ice lowers sea level), about 50 to 60% ocean, with drier interiors (cold steppe and tundra, forests near coasts) and large permanent ice caps.
- **Draft (Claudia):** sea ice forms every cold year, freezing straits and opening temporary ice bridges between landmasses.
- **Draft (Claudia):** geothermal valleys are cold-year refuges for animals, clans, and the player, with built-in dangers (boiling pools, gas pockets, thin crust).  The Frostpunk cities sit on geothermal sites, which is why they are where they are.  Salt from the salt lakes preserves food for the cold-year stockpile, making it a precious trade good.

## Music areas (Nathan, 2026-11-12)

Every spot on the planet has a music area.  It sets the feel of the area's influence and is the trigger the system uses to pick the background music set.  It also drives radio stations, news, and other things, beyond a few key exceptions (changed by Nathan 2026-11-13: radio and news feed off the culture map instead; see Era and location).  Map: `assets/maps/verlassen_music_areas_v0.1.png`; data: `tools/data/music_areas.json`, built by `tools/music_areas.py`.

- Land takes the culture of the nearest of the ten places reachable overland; each town's influence shapes the music around it (Mongolian throat singing down south, and so on).
- Land with no town in reach uses the Overall theme, which shows these areas have no direct influence.
- Water just outside the land (coastlines, shore water, coral reefs, within about 120 km) takes the music of that land for now.  A judgment call comes when those areas are visited.  The image in mind: a Japanese take on The Little Mermaid.
- The deep ocean is Japanese plus sea shanties.
- The polar ice caps are areas of dread, with deep-cold music.

| Music area | Places | Main grid squares | Squares |
|---|---|---|---|
| Japanese + Gaelic | Shio Loch, Kawa Fada | P to W, rows 3 to 10 (the S1 continent's north and east) | 25 |
| Japanese + Mongolian | Ikh Gawa, Davs Mizuumi, Khaluun Onsen | H to O rows 9 to 10; A to D rows 9 to 10; V to X rows 6 to 10 | 34 |
| Japanese + Slavic | Svetla Hama, Zimna Toride | K to N, rows 3 to 6 | 12 |
| Japanese + Persian | Setareh Minato, Darya Kako | E to H, rows 4 to 8 | 12 |
| Japanese + German | Warmes Tani | B to F, rows 3 to 6 | 10 |
| Japanese + sea shanty | (deep ocean) | the open seas | 99 |
| Ice dread | (none) | rows 1, 2, 11, 12 | 96 |
| Overall | (none) | small town-less islands (U5, W5, U6, M8) | partial |

- Music stays in music (Nathan, 2026-11-13): as it evolves and grows, it is a feel all on its own and should not impact anything else.  The planet file only points to the music areas; music data lives in its own files (`tools/data/music_areas.json`, `docs/design/music.md`).
- **Draft (Claudia):** music crossfades over a few region cells at each border, so it shifts as the player walks instead of snapping.
- **Draft (Claudia):** key exceptions override the area, for example the spaceport sounding Union and off-world.

## Heights

- Height scale (Nathan, 2026-11-12, from Claudia's draft): the planet's highest point is about 6,500 m; R5's peaks reach about 3,500 to 3,700 m.
- The highest point sits in grid M10, about 53 S, 8.5 E, in the Mongolian belt near Davs Mizuumi at the edge of the southern ice.  Its name is Yamajira (Nathan, 2026-11-13).

## Biomes

- **Draft (Claudia):** no jungle anywhere.  Every third year even the equator freezes at night, which kills frost-sensitive plants, and the terraformers planted frost-hardy species.  The warmest forests are evergreen oak and pine, like the southern US or southern China.
- 13 land biomes (Claudia, approved by Nathan 2026-11-11):

| # | Biome | Where | Feel |
|---|---|---|---|
| 1 | Warm forest | warm band, wet | evergreen oak and pine, richest forage |
| 2 | Warm grassland | warm band, medium | open plains, herds |
| 3 | Scrub desert | warm band, dry | thorn brush, scarce water |
| 4 | Mixed forest | temperate, wet | deciduous and conifer woods |
| 5 | Prairie | temperate, medium | tall grass, good farming soil |
| 6 | Steppe | temperate, dry | short grass, wind |
| 7 | Marsh | wet lowlands, any band | reeds, bogs, slow travel, bad water |
| 8 | Taiga | cold band | dense conifers, deep snow |
| 9 | Tundra | cold band, open | moss, lichen, migrating herds |
| 10 | Cold barrens | cold band, dry | rock and gravel |
| 11 | Highlands | elevation, any band | ridges, scree, passes, caves |
| 12 | Ice | poles, highest peaks | permanent ice |
| 13 | Coast | edge of land | beaches, cliffs, tidal flats |

- Water biomes to add (Nathan, 2026-11-11): warm ocean, deep ocean, coral reef, inland sea, inland lake, river, salt river.
- Salt notes approved by Nathan 2026-11-11: salt rivers flow from the salt basins, and dissolved salt is immune to the infection.
- Water biome notes (Claudia, approved by Nathan 2026-11-11):

| # | Biome | Notes |
|---|---|---|
| 14 | Deep ocean | open water; boats, or sea ice in a cold year |
| 15 | Warm ocean | warm-band shallows, good fishing; chills hard in the cold year |
| 16 | Coral reef | cold-water reefs (real on Earth, as off Norway, at about 4 to 12 C), since tropical reef corals would die every cold year; rich fishing, navigation hazard |
| 17 | Inland sea | huge enclosed water, can be brackish, like the Caspian |
| 18 | Inland lake | fresh water, fish, freezes in winter |
| 19 | River | river corridor: channel plus floodplain; big rivers only |
| 20 | Salt river | saline, flowing from the salt basins (real, like Arizona's Salt River); undrinkable, a trade route |

- Model for salt-fed water: Lake Texoma (Nathan, 2026-11-11).  The Red River carries salt from ancient deposits through natural seeps upstream, making the lake brackish; it holds both freshwater and saltwater species, and striped bass, a saltwater fish, reproduce there.
- Salinity is a property of water (fresh, brackish, saline), not a separate biome (Claudia, approved by Nathan 2026-11-11).  A lake fed by a salt river is brackish, with a mixed fish table (freshwater and sea species), making it one of the richest fishing spots; its water needs treating before drinking.
- Like Texoma, a brackish lake is one of the few places certain fish can be caught (Nathan, 2026-11-11).
- Salt zone values (Nathan, 2026-11-12): key areas (sea, brackish, others) are set directly; a salt value per region sets the baseline, so an all-inland region with no salt is 0, while ocean access or nearby salt flats make it salty.
- Salinity rules (Claudia, approved by Nathan 2026-11-12): the salt value is in parts per thousand (fresh under 0.5, brackish 0.5 to 30, saline over 30; seawater about 35); salt follows the water, flowing downstream from a source (a salt flat or salt lake) and diluting as tributaries join; near a river mouth the sea pushes brackish water a short way upstream; lakes with no outlet in dry areas become salt lakes; the thaw flood freshens brackish water for a season.  R5 is 0 throughout.
- River flow direction is set during generation.  Some directions are obvious, some are not, and some water is stagnant (Nathan, 2026-11-12).
- Flow rules (Claudia, approved by Nathan 2026-11-12): each water cell drains downhill to one of its 8 neighbors; stagnant water forms in sinks (ponds, lakes, marshes, and salt lakes in dry areas) and on flats below a minimum slope (oxbows, bogs, backwaters); speed comes from slope and volume (fast mountain streams, slow lowland rivers) and sets fording difficulty, fishing, and boat travel (quick downstream, a crawl upstream); stagnant water is the riskiest to drink; the thaw flood speeds everything up, and dry washes run only in thaw years.


- **Draft (Claudia):** features sit on top of a biome rather than being biomes: geothermal valleys, salt flats and salt lakes, small creeks and ponds, impact craters, ruins.  Big rivers and lakes are water biomes.
- **Draft (Claudia):** each biome becomes data: temperature band, moisture range, plants, animals, resources, travel cost per day, and the local map art palette.
- Any biome can be infected, and it spawns differently when it is (Nathan, 2026-11-11).
- **Draft (Claudia):** infection is a level on a cell (for example 0 to 3), not a duplicate biome.  It is highest at the impact craters and fades with distance; it rises with the thaw and drops in the cold year.  Each level changes spawns (infected fauna, crystal growth), resources, and art tint.  Ice can never be infected, since the infection cannot take ice; salt flats infect worst.  Salt dissolved in water is not a crystal, so oceans and salt rivers are immune, but salt crust on a salt river's banks can be infected.

## Life

- The cold is the big bad.  Nothing thrives in the cold year except small critters, fat bears, and various things that adapt.
- Native life is alien.
- A meteoric impact infection: something crystalline (the silicon idea) arrived by meteor.  This leans into the fantasy.
- The infection is weaker in the third (cold) year, so the cold stays the main threat.
- The infection has its own damage type, Crystalline.  It is the seed crystal: an alien mineral that converts salt, mineral deposits, bone, and teeth into its own structure on contact (`concept.md`, Lancer vocabulary).
- The infection is relevant to the player, but exists in only a few places on the globe.
- Each run, a small random infection spawns somewhere on the map, a distance away from the player.  If the player crashes in a remote area far from the major sites, they still have to deal with the infection, just a small bit.
- **Draft (Claudia):** the small spawn is placed by the run's seed, a few zones from the crash site (never adjacent), and stays small compared to the impact sites.
- Native life is carbon based with real-science alien traits: silica armor (glassy spines, shell plates, frosty needles, as diatoms and glass sponges do on Earth); copper-based teal blood; mirror chemistry that humans cannot digest, so native food must be processed (possibly by the paste printer) and Terran crops need rare seeds.
- Big, shaggy, cold-adapted fauna (Bergmann's rule), with migrations as the temperatures change.  Nothing kaiju sized, no giant insects, no Ohmu-style creatures.  Mammoths and giant water creatures are about the largest (water's buoyancy allows whale-scale animals).  Flora is hardy (conifer-like forests, tundra scrub, lichens).
- **Non-native fauna (Nathan, 2026-11-10):** the settlers brought Terran animals, so people have regular animals to hunt and eat: pigs, turkeys, cows, rabbits, deer, elk, and the like.  Native fauna remains.
- **Terraforming (Nathan, 2026-11-10):** the settlement ships carried terraforming tech.  The planet would not have matched, so the settlers seeded Terran plants and animals, whatever was needed to support the population.  That is why the world is a mix of Terran and native life.
  - Gathering matters later: plants that Terran animals and people can eat versus plants that native animals can eat, if the game gets into farming animals or keeping pets.
- **Draft (Claudia), making the mix work:**
  - Terran animals cannot digest native plants, for the same mirror-chemistry reason humans cannot, so they live where the terraforming plants took hold.  Terran crops still need rare seeds; the hardy seeded grasses and forage plants are what spread wild.
  - The terraforming was never finished: the ships stopped coming, which fits the name Verlassen.  So it took around the settled lands and faded with distance.
  - That makes a food gradient: Terran grassland and game cluster around the old terraformed land and roads, and the deep wilderness is native only.  A remote crash means hunting native animals and processing the meat, which fits "the more remote, the harder."
  - Wild Terran animals must survive the cold year, so cold-hardy kinds go wild: elk, deer, reindeer, bison, yak, musk ox, wild goats and sheep, hares, feral pigs.  Warm-climate kinds such as ostriches and turkeys live only on farms with heated barns, or in the warm band.
  - Five thousand years of cold years have changed them: shaggier coats, fattening before the cold year, migrating with the native herds.  Still recognizably elk.
- **Draft (Claudia):** animals evolved around the three-year cycle: fattening before the cold year, then migrating or hibernating, so herd movement is another warning sign.
- **Draft (Claudia):** the infection is the one deliberate exception to "physics stays real," a paracausal mystery that is never fully explained, like the crash.  Each infected place centers on an impact crater landmark; the infection wakes with the thaw after a cold year, and can infect native fauna.

## Roads and bridges

- A road and bridge system, basic and RimWorld style.  Instead of random, it is mostly fixed.
- Small offshoots are random: random settlements in the wild, bandit camps, and similar may have paths.
- Road network (Nathan, 2026-11-11): roads link 3, 8, 1 and 2, 6, 10, 7; paths link others such as 5 to 1 and 2 to 10; ferries run between 1, 8, 2, 4, 9, 10.  Details in `zones.md`, Routes.
- Sea roads: in the cold year the sea ice opens new routes.  Suddenly, getting from Setareh Minato to Ikh Gawa is a land trip.
- **Draft (Claudia):** main roads follow the land (river valleys, mountain passes, coasts) and link the ten places, with fixed bridges at major river crossings.  Random paths fork toward seeded settlements and camps, so a path in the wild means someone is out there.  Vehicles keep to roads and open land.  In the cold year, snow buries roads.  In normal years, crossings like Setareh Minato to Ikh Gawa mean a boat or a long trek around the coast.

## Population

- About 10 million people.  Enough for cities, with plenty of hundreds of miles of nothing.
- **Draft (Claudia):** distribution: one big spaceport city of a couple million (the only real off-world contact); 3 to 5 regional cities of a few hundred thousand each, linked by long roads or rail; towns and outposts (farming, mining, waystations); small, scattered clans and homesteaders in the deep wilderness; most of the planet empty.  The cold-year cycle pushes settlement toward the warmer bands.
- In the third (cold) year, the cities become very Frostpunk.
- **Draft (Claudia):** cold-year cities huddle around central heat plants, with districts ranked by distance to the heat; cold-year laws bring rationing, curfews, and work quotas; refugees pour in from the wilds.  With no ID there is no ration card, heat allocation, or work permit.  Arriving in a normal year means a gritty but open city; arriving in a cold year means being an unwanted refugee, though the chaos means fewer people checking papers.

## Peoples

- History: in Lancer lore, Verlassen was settled by ships sent in the initial outward push from Cradle.  Settlement is old, which fits the archaic languages and the long drift into 563 languages.
- People have been on Verlassen longer than Earth has recorded history (over about 5,000 years).  Names and languages have drifted and blended so far that they no longer fit any original grammar.
- KTB languages are among those spoken on the planet.
- Primary culture: Japanese (names romanized), with influence from all the major cultures.  An easy feudal concept for how power works.
- **Draft (Claudia):** feudal lords hold the heat sources; villages pay tribute for warmth.  This meshes with the KTB's baronial style.
- The settlers came from the same places as the Karrakin Trade Baronies.
- The KTB is the closest trading location, so there is some influence from KTB proper.
- **Draft (Claudia):** the colony drifted out of contact for ages, which is why Union is only a rumor here.  The name Verlassen may come from the first settlers, once the ships stopped coming.
- People are of various races, and they do not need to be human.  We make them as we pick.
- In Lancer lore aliens exist, but SecComm holds a humans-first stance; there is a whole thing about it.  We have the option to expand on that.
- Not a lot of animalistic people.
- Moth people exist in Lancer, but probably not on a cold planet.
- Genetic (bioengineered) people could be cool, like Alex's goat people, who are only slightly goatish.  We can science some hybrids.
- **Draft (Claudia):** goat traits suit a cold, mountainous world, so a goatfolk line fits Verlassen.  Any goatfolk here are a separate engineered line from the Halas family in Errans Inter Astra.

## Technology and NHPs

- Verlassen has almost no NHPs.  That is all outside this colony.
- What an NHP is (Nathan, 2026-11-12): technically an alien mind encased in a casket, told it is human, and so it wants to be human.  NHPs have the potential to be more than humans in logic and concept; they just do not want to be.  "No NHPs" means no entities that can fully cascade into eldritch concepts.  Droids and androids, even ones with personalities, are lesser than a person and can be reprogrammed.
- There may be one or two NHPs at the spaceport, but they would be new and foreign.
- Because of the NHPs at the spaceport, no one is going to successfully attack it: not with missiles, armies, or anything.
- In Lancer, NHPs can network into a gestalt called a fleet legion (canon: the ships' NHPs build a virtual war room, a hybrid one-and-many mind, for space battles).  On Verlassen, the spaceport's NHPs forming one would be an epic, almost magical thing.
- It happened once, recently (the spaceport NHPs are new), when a lord tried to take the port.  Eyewitnesses are still around, the story is already legend, and no one has tried since.  To locals it is like seeing Son Goku or Dr. Manhattan: "Superman is real, and he's in Setareh Minato."
- **Draft (Claudia):** this makes the spaceport neutral, untouchable ground, and is one reason the Warmes Tani feud stays cultural and political.
- Locals know nothing about RA; the main character would.
- In Lancer, NHPs are an everyday thing.  On Verlassen they are mythical, almost wizards.
- The mech's computer is a CompCon (not an NHP): a particularly smart CompCon.
- **Draft (Claudia):** the player's knowledge of NHPs, RA, and paracausal science is outsider knowledge nobody local shares.

## Fixed places: placement criteria

- Fixed places (cities, spaceport, landmarks, impact sites) are placed logically, once, and stay canon.  Random is for the wilderness and the crash site.
- At least one spaceport.
- Major cities sit near water and near heat (rivers, geothermal).
- Remote, tiny places are rare, unless they can secure a heat source for the cold year.
- A spaceport across the globe from the crash site can mean years of travel.  That is fine.
- The vast distances lean into a remote start being years before the player reaches a main settlement (Nathan, 2026-11-10).
- Measured on the seed 2718 globe (Claudia, 2026-11-10), straight-line distance from habitable land to the nearest of the ten places: half of it is over 2,550 km, a quarter over 3,900 km, and the farthest about 6,300 km.  Overland routes run longer than straight lines.
- **Draft (Claudia):** the spaceport sits near the equator on flat ground (real physics: launches near the equator get a boost from the planet's spin, and it is the warmest band).  Trade cities sit at river mouths and coasts.  Salt-lake towns are trade hubs.  Impact sites are placed for story and never on top of a city.

## The ten fixed places

Accepted by Nathan 2026-11-09.  Map: `assets/maps/verlassen_places_v1.0.png` (grid: column letter A to X, row number 1 to 12; the equator sits between rows 6 and 7).

Culture is the influence on top of the Japanese base (Nathan, 2026-11-12).

| # | Name | Meaning | Culture | Type | Grid |
|---|---|---|---|---|---|
| 1 | Setareh Minato | Star Harbor | Persian | Spaceport city | H7 |
| 2 | Ikh Gawa | Great River | Mongolian | Major city, near geothermal heat | L9 |
| 3 | Warmes Tani | Warm Valley | German | Major city, near geothermal heat | E4 |
| 4 | Svetla Hama | Bright Shore | Slavic | Major city | L5 |
| 5 | Khaluun Onsen | Hot Hot Springs (a real-world style redundant name) | Mongolian | Onsen town | A10 |
| 6 | Davs Mizuumi | Salt Lake | Mongolian | Salt-lake trade town | K10 |
| 7 | Shio Loch | Salt Lake | Gaelic (Irish) | Salt-lake trade town | V4 |
| 8 | Darya Kako | Sea Mouth | Persian | River-mouth port | H5 |
| 9 | Zimna Toride | Cold Fort | Slavic | Remote holdfast with its own heat source | N3 |
| 10 | Kawa Fada | Long River | Gaelic (Irish) | River town | R8 |

- The west holds most places; the east (columns P to X) is largely empty wilderness.
- The three infection impact sites on the map are accepted (grid M3, T3, J10).  They sit close to the cold areas, which may benefit the player and the story.  What the infection mechanic does is decided later.

## Notable people of the ten places

Generated with `tools/name_gen.py` (seed 2718) and accepted by Nathan 2026-11-09.  One notable person per place; their roles are set when we decide who is in charge.

| # | Place | Person |
|---|---|---|
| 1 | Setareh Minato | Parisa Kuroda |
| 2 | Ikh Gawa | Erdene Yamaguchi |
| 3 | Warmes Tani | Leopold Matsuda |
| 4 | Svetla Hama | Bogdan Ogawa |
| 5 | Khaluun Onsen | Bolormaa Kobayashi |
| 6 | Davs Mizuumi | Altan Arai |
| 7 | Shio Loch | Akane Keane |
| 8 | Darya Kako | Farrokh Okada |
| 9 | Zimna Toride | Radoslav Nishimura |
| 10 | Kawa Fada | Hina Rafferty |

- Person names follow the cultural region's word order: regional given name plus Japanese family name, flipped to Japanese given name plus regional family name in the Gaelic east.

## Cultural regions and second cultures

Japanese is the base everywhere.  Each cultural region's second culture flavors its names, art, clothing, and culture.  Each cultural region keeps its own word order in hybrid names.  (Renamed in the 2026-11-13 review: "region" alone now means a map square.)

| Cultural region | Second culture | Word order | Places |
|---|---|---|---|
| Spaceport coast | Persian (KTB) | Persian first | Setareh Minato, Darya Kako |
| West continent north | German | German first | Warmes Tani |
| Southern steppe belt | Mongolian | Mongolian first | Ikh Gawa, Khaluun Onsen, Davs Mizuumi |
| Central-north island | Slavic | Slavic first | Svetla Hama, Zimna Toride |
| The empty east | Gaelic (Irish) | Japanese first | Shio Loch, Kawa Fada |

- The point is easy generation: the cultural region tells the generator which culture and word order to use.

## Culture map (Nathan, 2026-11-13)

- Areas with similar styles are grouped.  Japanese is the base and influences everything, so the map ignores it and records only the second culture.
- Kawa Fada to Shio Loch is one culture, since they are the same type; the other groupings work the same way.
- Culture does not mean the same ideals.  Ideals are set by the cities and their rulers, who might still share a culture.
- Built by `tools/culture_map.py` v0.1: `tools/data/culture_map.json` (one digit per globe pixel) and `assets/maps/verlassen_culture_v0.1.png`.  Land takes the second culture of the nearest place reachable overland, the same rule the music areas used; water, and land with no place on its landmass (U5, W5, U6, M8), are base only.  Below the ice line it matches the music areas pixel for pixel.
- Share of land: Gaelic 44.6%, Mongolian 30.7%, Persian 8.4%, Slavic 8.3%, German 7.7%, base only 0.3%.  About 35% of all land lies past the ice line (58 degrees), and most of it reads Gaelic (the north cap) or Mongolian (the south cap).
- **Draft (Claudia), polar land:** land past the ice line is base only, since nobody lives on the caps.  That leaves Gaelic at 16.7% and Mongolian at 23.8% of land.  Music keeps ice dread there either way.
- Next: `tools/music_areas.py` reads the culture map and adds its music-only layers, with its output unchanged.

## Government

- There is no central global government.  Each of the ten places is the capital of its territory.
- A mix of Lords and Mayors leads the places.
- Each town has a council, not defined yet.
- We follow the 3 tier government method: executive, legislative, and judicial.
- **Draft (Claudia):** in each town, the lord or mayor is the executive, the council is the legislative, and a magistrate or court is the judicial.
- Towns are adjusted to different standards as we play.  Some lords have no power and are purely for show; some hold all the power.  Some places practice slavery; some ban it.  There may be culture wars, or actual wars.
- Territories (formerly political regions; renamed 2026-11-11 so "region" means a map square) surround each capital, as in `assets/maps/verlassen_regions_draft_v0.1.png` (generator `tools/regions.py`): each capital claims the land it reaches overland first, up to about 2,400 km; seas block claims; about 65% of habitable land stays unclaimed wilderness.  These ten territories sit inside the five cultural regions below.  Accepted as is; borders get established more clearly as we zoom in to zones.
- Work camps: maybe.  Some are just for profit; some are for labor.  Slaves were always those things.  Some NPCs justify it; some say the enslaved are better off.  We know all these stories because history tells us them, and we do not sugar coat or hide from history as many do.
- In keeping with Lancer's tone, cruelty such as slavery exists in the world to be opposed, never celebrated.  It has to exist so the player can save people from it.
- **Draft (Claudia):** lords rule where someone holds the heat (Warmes Tani, Ikh Gawa, Khaluun Onsen, Zimna Toride); mayors lead the trade towns (Setareh Minato, Darya Kako, Davs Mizuumi, Shio Loch, Svetla Hama, Kawa Fada).

## Currency

Five regional currencies, grouped by place (names and exchange rates still open):

| Currency | Issued by | Also used in |
|---|---|---|
| A | 5 Khaluun Onsen | |
| B | 3 Warmes Tani, 8 Darya Kako, 1 Setareh Minato | |
| C | 2 Ikh Gawa, 6 Davs Mizuumi | |
| D | 7 Shio Loch | 10 Kawa Fada |
| E | 4 Svetla Hama, 9 Zimna Toride | |

- Kawa Fada is weird and uses Shio Loch's currency (see Conflicts: the two brothers).
- Manna is for off-world business at the spaceport.
- Towns have banks.
- **Money (Nathan, 2026-11-10):**
  - Money has no weight.  It is stored with the M.U.L.E.
  - Banks are still a thing; the accounts are held under the M.U.L.E.
  - If the M.U.L.E. is knocked out or away, the player cannot spend.  Rescue it or wait for its return.
  - No theft.  The M.U.L.E.'s tech is beyond anyone on the planet; it would take an NHP to hack it.
  - On death, the money transfers to the successor with the M.U.L.E.
- **Draft (Claudia):** banks exchange currencies for a cut, and make loans; loan sharks offer a darker, no-questions version.  A real bank needs ID, so early on the player relies on cash, barter, wilderness caches, or a shady back-room bank.  Opening a first real account is a quiet milestone in the identity questline.
- **Draft (Claudia):** the engine tracks one hidden value unit; each currency is a display name plus an exchange rate in a data file, so the code stays simple.  Barter and commodities work everywhere, with salt as the closest thing to a universal currency (the word salary traces back to salt).  Money changers in each city convert currencies and take a cut.  Rates shift with the world: in a cold year, currencies backed by heat-holding lords rise and trade-town currencies fall.

## Conflicts

1. Warmes Tani versus the spaceport mayors (Setareh Minato, Darya Kako): a cultural and political war, never a physical one.  The spaceport area is where most people live, and people do not live in a war-torn area.
2. Khaluun Onsen versus Ikh Gawa: two Mongolian heat lords with different currencies, fighting over the steppe and the salt road to Davs Mizuumi.  Whoever controls salt controls the cold-year food supply.
3. Shio Loch and Kawa Fada: the old-fashioned two brothers trope.  The brothers are the leaders of the two towns.  The towns were established long before; one brother fled Shio Loch and became the leader of Kawa Fada.  The names of the notable people do not matter here; the brothers' names are still open.
   - **Draft (Claudia):** the fleeing brother brought his home town's coin, which is why Kawa Fada uses Shio Loch's currency.
4. Zimna Toride is our version of The Wall, or the battles in Lord of the Rings that no one knows about: a fight goes on there that others only hear rumors of.  The other two impact sites (T3, J10) are usually too cold to be an issue, sitting close to the frozen borders.
- **Draft (Claudia):** planet-wide tensions: heat holders (lords) versus traders (mayors), sharpest in cold years; slavers versus abolitionists over work camps; locals versus outsiders (KTB traders, Union rumors, the player).  Cold-year raids target stored food and salt, and refugee waves head for the heat cities.

## War at continent scale (Nathan, 2026-11-10)

- The long distances between rivals are good.  Feuds run at continent scale, like the wars in Nausicaa of the Valley of the Wind: airplanes, missiles, and other long-range attacks make them feasible.
- Some areas are low tech, but this is the far, far future.  Fliers, droids, and mutants all exist.  The planet was terraformed, and these people live thousands of years after that.
- Cold-year flight (Nathan, 2026-11-10): grounding by the extreme cold is a modern standard.  These vehicles are thousands of years in the future, and a people who traveled through space and terraformed a planet may have found a solution.  Still, cold is cold and metal is metal, and there may be physics that limit what can happen.  Lack of money is what prevents most innovation.
- **Draft (Claudia):** cold-rated fliers exist but cost more to build and run, so who flies in the cold year comes down to money: rich powers keep flying, poor ones are grounded.
- Remote crashes: downed fliers and wreckage out in the deep wild are places for the player to find resources, maybe someone to save, and potential faction increases.
- Droids are dumber than a CompCon.  The M.U.L.E. is smarter than a standard CompCon, and very smart compared to most common droids.
- **Draft (Claudia):** mutants trace back to the terraforming, the infection, or old bioengineering, case by case.
- Forced truce: on hold.  It will be an engine mechanic, with criteria established later (mechanic #93).  The idea on the table: wars pause in the cold year and restart with the thaw, the same time the infection wakes.
- Downed flier: a future seed-spawned event that can happen, and it is random (mechanic #94).
- **Draft (Claudia):** the survivor belongs to one of the feuding powers, so saving them is a faction hook, and the war shows up even where no one lives.

## Local life around the player

- When local maps are created, a few small settlements and a few enemy locations are placed near the player, RimWorld style, so the area has some life.
- The more remote the player is, the less they are interacted with.  A crash at R5 or X7 means running into no one.
- **Draft (Claudia):** local settlement and enemy density scales with distance from the nearest fixed place, placed by the run's seed.  The small random infection spawn still appears even in the most remote starts.

## Open

- Currency names and exchange rates.
- The two brothers' names, and where the fleeing brother came from.
- Who runs the region's single space station.
- Road paths drawn on the globe: which places link is decided (Roads and bridges); the generator's routes layer still has to draw the paths.

## Lancer canon notes (alignment reference)

Paraphrased by Claudia from the Lancer core book's history section, 2026-11-09.  Concepts only, no Massif text, per the Lancer Third Party License.

- The "initial outward push" in canon is the Ten: ten huge sublight generation ships launched from Cradle during Old Humanity's collapse, roughly 6000 to 4900 years before Union's year zero (about 10,000 to 11,000 years before canon's present, 5016u).  The Ten cut contact with Cradle by choice.
- Karrakis, homeworld of the Karrakin Trade Baronies, was settled by the Apollo, the first of the Ten.  Settlers "from the same places as the KTB" therefore points to Apollo lineage: Verlassen could be an early Karrakin daughter colony or a related landfall.
- Karrakin culture developed apart from Union for thousands of years.  Union first contacted it around 2800u; the Baronies became a Union member state after the Interest War around 4630u.  By 5016u, canon's present, the KTB is technically part of Union, so Union reaches Verlassen only indirectly, through Baronic trade.
- Canon cold world to stay distinct from: Sparr, settled by the Yggdrasil (one of the Ten).  It shares tundra, thermal-vent life, megafauna, clans, a habitable equator, a years-long overland trek, and Norse-flavored culture.  Verlassen stays distinct through its Japanese-hybrid culture, the three-year cold cycle (Sparr is frozen year-round), alien mirror-chemistry life, the crystal infection, and the clone premise.
