# Alpha2-Roger Concept

**Concept v0.1, 2026-11-09**

Decisions are Nathan's unless marked **Draft (Claudia)**.  Drafts are suggestions until Nathan approves them.

## Premise

- Lancer universe, Lancer-adjacent.  Uses the lore, does not follow the Lancer rules.
- Your mech crashed and was damaged on a rim world.  You are stuck, possibly for years, until rescue or until you get yourself off planet.
- The planet is so far out that Union holds no sway.  Union is known, but the locals are in control.
- The planet has its own economy and currency.  Manna can be exchanged for it at the spaceport.

## The twist (hold back from marketing)

- The player is a Thomas Riker.  A backup of you was restored and went home.  That version holds your name, identity, and licenses.
- Reaching the spaceport is allowed at any time.  Once there, you cannot print anything and your ID is taken, so you start over.  That becomes a quest line.
- Printers will not fabricate without a valid license, which is why you cannot simply print a way off planet.

## Story arc

1. Survive the crash and the wilderness.  Build a camp.
2. Prepare for, and survive, the journey of hundreds of miles to the city and spaceport.
3. The legal battle for your identity.  It happens on planet, through holo calls, email, and blink messages.  Your path determines the hoops.
4. Once established, you get your ID and can start proving you are a Lancer.
5. Eventually you get a mech: a non-standard one built from bits and pieces, inspired by the unlabeled clan hunting-rig art in the Lancer core book.
6. You prove yourself before any of the big manufacturers recognize you.

## Map

- A fixed overall planet map.  Cities and landmarks are fixed.
- Wilderness is random per seed.
- Zone distances are set between fixed areas.
- Zone based, not open world.
- Future expansions may add planets.
- **Draft (Claudia):** randomize the crash site per seed; make route lengths a range (for example 4 to 6 zones) chosen by the seed; tie wilderness biomes to a fixed climate layer; build each planet as a data module so expansions do not require engine rewrites.

## Play style

- Grid based, like Caves of Qud or old school RPGs.
- Qud-style turn sync (everything moves when you move) is fine; RimWorld-style free movement with combat math is also acceptable.
- Survival logic closer to RimWorld than to most RPGs.
- No constant raiders or mech battles.  A few NPCs: 5 or 6 in camp, not a colony sim.
- Rules: pick what fits the game, borrowing lore elements from Lancer.  No adaptation of Lancer's narrative rules.
- **Draft (Claudia):** expeditions in Qud-style turns and camp in compressed time, so years can pass; 3 or 4 biome-specific survival pressures instead of many always-on meters; borrow Lancer vocabulary (Heat, HASE, licenses, Structure and Stress) as flavor.

## Engine

- **Draft (Claudia):** prototype the seeded zone generator first as plain text output, then build the game in Godot 4.

## Open items

- Feel and timing of the journey and of the years spent stranded.
- Local currency name.
- Movement model: Qud turn sync or free movement.
- Engine choice.
