# Alpha2-Roger World

**World v0.55, 2026-11-10**

Decisions are Nathan's unless marked **Draft (Claudia)**.  Drafts are suggestions until Nathan approves them.

This file holds the world facts that become the planet data file (A2R-101).

## Era and location

- Current Lancer time: 5016u.
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
- The star: Sun-like and yellow (G type), about one solar mass.  Chosen by the physics: with a 14-month year, Verlassen orbits at about 1.1 times Earth's distance and receives roughly 80% of Earth's sunlight, which matches temperate but colder than some.  A massive star would put the temperate zone so far out that a year would take decades; an orange star would leave a 14-month orbit too cold.
- Science and physics win over hip shots: when a stated detail conflicts with real physics, the physics decides.
- **Draft (Claudia):** with the 3:1 resonance, the gas giant orbits about every 3.5 years.
- **Draft (Claudia):** optional lore: the star is aging, for flavor only.
- Temperate, but colder than some.
- Size: slightly larger than Earth (about 10% wider), with about Earth's gravity, so nothing new needs inventing.  Physics note: same gravity at a larger size means a slightly less dense planet (a smaller iron core).
- Moons: none.  No moonlight.  Physics note: tides are small (from the sun only); a moon's long-term tilt stabilizing works over millions of years and does not matter in play.
- Rings: none.
- **Draft (Claudia):** with no moon, nights are pitch black under starlight only.  Darkness becomes a survival pressure that pairs with fog of war and 2D lighting.  The gas giant may be the brightest object in the night sky.
- Year: 14 Earth months.
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

## Life

- The cold is the big bad.  Nothing thrives in the cold year except small critters, fat bears, and various things that adapt.
- Native life is alien.
- A meteoric impact infection: something crystalline (the silicon idea) arrived by meteor.  This leans into the fantasy.
- The infection is weaker in the third (cold) year, so the cold stays the main threat.
- The infection has its own damage type, Crystalline.  Its nature and what it can infect are open; the leading draft is the seed crystal (`concept.md`, Lancer vocabulary).
- The infection is relevant to the player, but exists in only a few places on the globe.
- Each run, a small random infection spawns somewhere on the map, a distance away from the player.  If the player crashes in a remote area far from the major sites, they still have to deal with the infection, just a small bit.
- **Draft (Claudia):** the small spawn is placed by the run's seed, a few zones from the crash site (never adjacent), and stays small compared to the impact sites.
- Native life is carbon based with real-science alien traits: silica armor (glassy spines, shell plates, frosty needles, as diatoms and glass sponges do on Earth); copper-based teal blood; mirror chemistry that humans cannot digest, so native food must be processed (possibly by the paste printer) and Terran crops need rare seeds.
- Big, shaggy, cold-adapted fauna (Bergmann's rule), with migrations as the temperatures change.  Nothing kaiju sized, no giant insects, no Ohmu-style creatures.  Mammoths and giant water creatures are about the largest (water's buoyancy allows whale-scale animals).  Flora is hardy (conifer-like forests, tundra scrub, lichens).
- **Draft (Claudia):** animals evolved around the three-year cycle: fattening before the cold year, then migrating or hibernating, so herd movement is another warning sign.
- **Draft (Claudia):** the infection is the one deliberate exception to "physics stays real," a paracausal mystery that is never fully explained, like the crash.  Each infected place centers on an impact crater landmark; the infection wakes with the thaw after a cold year, and can infect native fauna.

## Roads and bridges

- A road and bridge system, basic and RimWorld style.  Instead of random, it is mostly fixed.
- Small offshoots are random: random settlements in the wild, bandit camps, and similar may have paths.
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
- **Draft (Claudia):** the spaceport sits near the equator on flat ground (real physics: launches near the equator get a boost from the planet's spin, and it is the warmest band).  Trade cities sit at river mouths and coasts.  Salt-lake towns are trade hubs.  Impact sites are placed for story and never on top of a city.

## The ten fixed places

Accepted by Nathan 2026-11-09.  Map: `assets/maps/verlassen_places_v1.0.png` (grid: column letter A to X, row number 1 to 12; the equator sits between rows 6 and 7).

| # | Name | Meaning | Type | Grid |
|---|---|---|---|---|
| 1 | Setareh Minato | Star Harbor | Spaceport city | H7 |
| 2 | Ikh Gawa | Great River | Major city, near geothermal heat | L9 |
| 3 | Warmes Tani | Warm Valley | Major city, near geothermal heat | E4 |
| 4 | Svetla Hama | Bright Shore | Major city | L5 |
| 5 | Khaluun Onsen | Hot Hot Springs (a real-world style redundant name) | Onsen town | A10 |
| 6 | Davs Mizuumi | Salt Lake | Salt-lake trade town | K10 |
| 7 | Shio Loch | Salt Lake | Salt-lake trade town | V4 |
| 8 | Darya Kako | Sea Mouth | River-mouth port | H5 |
| 9 | Zimna Toride | Cold Fort | Remote holdfast with its own heat source | N3 |
| 10 | Kawa Fada | Long River | River town | R8 |

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

- Person names follow the region's word order: regional given name plus Japanese family name, flipped to Japanese given name plus regional family name in the Gaelic east.

## Regions and second cultures

Japanese is the base everywhere.  Each region's second culture flavors its names, art, clothing, and culture.  Each region keeps its own word order in hybrid names.

| Region | Second culture | Word order | Places |
|---|---|---|---|
| Spaceport coast | Persian (KTB) | Persian first | Setareh Minato, Darya Kako |
| West continent north | German | German first | Warmes Tani |
| Southern steppe belt | Mongolian | Mongolian first | Ikh Gawa, Khaluun Onsen, Davs Mizuumi |
| Central-north island | Slavic | Slavic first | Svetla Hama, Zimna Toride |
| The empty east | Gaelic (Irish) | Japanese first | Shio Loch, Kawa Fada |

- The point is easy generation: the region tells the generator which culture and word order to use.

## Government

- There is no central global government.  Each of the ten places is the capital of its region.
- A mix of Lords and Mayors leads the places.
- Each town has a council, not defined yet.
- We follow the 3 tier government method: executive, legislative, and judicial.
- **Draft (Claudia):** in each town, the lord or mayor is the executive, the council is the legislative, and a magistrate or court is the judicial.
- Towns are adjusted to different standards as we play.  Some lords have no power and are purely for show; some hold all the power.  Some places practice slavery; some ban it.  There may be culture wars, or actual wars.
- Regions are political territories around each capital, as in `assets/maps/verlassen_regions_draft_v0.1.png` (generator `tools/regions.py`): each capital claims the land it reaches overland first, up to about 2,400 km; seas block claims; about 65% of habitable land stays unclaimed wilderness.  These ten political regions sit inside the five cultural regions below.  Accepted as is; borders get established more clearly as we zoom in to zones.
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

## Local life around the player

- When local maps are created, a few small settlements and a few enemy locations are placed near the player, RimWorld style, so the area has some life.
- The more remote the player is, the less they are interacted with.  A crash at R5 or X7 means running into no one.
- **Draft (Claudia):** local settlement and enemy density scales with distance from the nearest fixed place, placed by the run's seed.  The small random infection spawn still appears even in the most remote starts.

## Open

- Detailed biomes per region.
- Currency names and exchange rates.
- The two brothers' names, and where the fleeing brother came from.
- Who runs the region's single space station.
- Final road network on the globe.

## Lancer canon notes (alignment reference)

Paraphrased by Claudia from the Lancer core book's history section, 2026-11-09.  Concepts only, no Massif text, per the Lancer Third Party License.

- The "initial outward push" in canon is the Ten: ten huge sublight generation ships launched from Cradle during Old Humanity's collapse, roughly 6000 to 4900 years before Union's year zero (about 10,000 to 11,000 years before 5016u).  The Ten cut contact with Cradle by choice.
- Karrakis, homeworld of the Karrakin Trade Baronies, was settled by the Apollo, the first of the Ten.  Settlers "from the same places as the KTB" therefore points to Apollo lineage: Verlassen could be an early Karrakin daughter colony or a related landfall.
- Karrakin culture developed apart from Union for thousands of years.  Union first contacted it around 2800u; the Baronies became a Union member state after the Interest War around 4630u.  By 5016u the KTB is technically part of Union, so Union reaches Verlassen only indirectly, through Baronic trade.
- Canon cold world to stay distinct from: Sparr, settled by the Yggdrasil (one of the Ten).  It shares tundra, thermal-vent life, megafauna, clans, a habitable equator, a years-long overland trek, and Norse-flavored culture.  Verlassen stays distinct through its Japanese-hybrid culture, the three-year cold cycle (Sparr is frozen year-round), alien mirror-chemistry life, the crystal infection, and the clone premise.
