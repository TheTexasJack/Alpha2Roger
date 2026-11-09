# Alpha2-Roger Concept

**Concept v0.2, 2026-11-09**

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
- Future planets are planned from the start: each planet is built as a data module, so new planets do not require engine rewrites.
- **Draft (Claudia):** randomize the crash site per seed; make route lengths a range (for example 4 to 6 zones) chosen by the seed; tie wilderness biomes to a fixed climate layer.

## Goals and endings

- Alpha2-Roger is Nathan's passion project: the game he wants to play.
- Playthroughs establish the endings.  We find them by playing.
- Endings are marked as milestones.  The game keeps going after an ending is reached.
- The game pushes toward future planets.
- Fade points are design signals: when play starts to fade, that is the point where we add something.
- Replayability: make a new character each run.  The core duplicate and bureaucratic loop remains, but the approach can change.  For example, one run you fight for your identity; another you tell them to fuck off and just be yourself.
- **Draft (Claudia):** keep a boredom log during playtests, recording when and where play fades.  At each fade point, choose between adding a system and pushing the player into the next act.
- **Draft (Claudia):** candidate ending milestones to test in play: Union recognition under a new name; refusing Union and living as yourself; building your own way off planet; staying, with the planet as home.
- **Draft (Claudia):** vary the duplicate setup per run (a sympathetic backup, a backup whose life yours would wreck, a failed restore where nobody claimed your name).

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
