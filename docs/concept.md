# Alpha2-Roger Concept

**Concept v0.7, 2026-11-09**

Decisions are Nathan's unless marked **Draft (Claudia)**.  Drafts are suggestions until Nathan approves them.

## Scope: what this game is

- A survival game set in the Lancer world.  Survival comes first.
- A traditional RPG in its rules and structure.  It does not use Lancer's narrative rules.
- A separate game from Lancer, the tabletop RPG, and from the video game Lancer Tactics.
- Mechs are secondary.  They may appear later in a run (for example the scrap-built mech in the story arc), and they never replace the survival core.

## Model and inspirations

The model: top-down dungeon crawler and open explorer.  Old brain, old gaming style.  Simple 2D, with enough on screen that the imagination does the rest.

- Sword of Fargoal
- Decklin's Domain: Demise: Rise of the Ku'tan and Demise: Ascension
- Caves of Qud
- RimWorld

## Core concepts

- Fog of war.
- Turn based: enemies move when you do.
- RPG-style character creation.
- Survival-lite: challenging, but fun.  Balance should not take a degree to figure out.
- No exploits that trivialize the game.  In RimWorld, building walls trivializes almost everything, and seeds are basically free.
- No tree punching.
- No free plants.  Seeds must be found, and growing takes full seasons.
- Seasons.
- Not a full community: 5 or 6 companions.
- Relationships: an organic system similar to RimWorld.
- Not everything is a faction.  No Qud-style reputation web where plants turn hostile because someone wronged a deer.
- Art: simple 2D top-down sprites.  Peg people like RimWorld (body, head, hat, gun, maybe circle hands) or a single sprite; the feel comes from the weapon effects.

More to come.

- **Draft (Claudia):** layered peg sprites, so gear is visible on the character and character creation comes from mixing parts.
- **Draft (Claudia):** keep weapon effects snappy (under about half a second) with a speed-up option, so turns never drag.
- **Draft (Claudia):** since growing takes full seasons, early food must come from scavenging, hunting, and trading, so a new camp is not doomed before its first harvest.
- Idea (Nathan): an early food printer in the mech.  The food is not good; it is just enough to survive, and that is it.  Details to work out.
- **Draft (Claudia):** the food printer is the one printer that works for the player, since nutrient paste needs no license.  Eating only paste costs mood or morale, and its feedstock (mech power or a finite cartridge) slowly pushes the player toward hunting, trading, and the first harvest.
- **Draft (Claudia):** walls exist for shelter and warmth; threats come mostly from the environment, so walling in is never the answer to everything.

## Premise

- Lancer universe, Lancer-adjacent.  Uses the lore, does not follow the Lancer rules.
- Your mech crashed and was damaged on a rim world.  You are stuck, possibly for years, until rescue or until you get yourself off planet.
- The planet is so far out that Union holds no sway.  Union is known, but the locals are in control.
- The planet has its own economy and currency.  Manna can be exchanged for it at the spaceport.

## The twist (hold back from marketing)

- The player is a Thomas Riker.  A backup of you was restored and went home.  That version holds your name, identity, and licenses.
- Reaching the spaceport is allowed at any time.  Once there, you cannot print anything and your ID is taken, so you start over.  That becomes a quest line.
- Printers will not fabricate without a valid license, which is why you cannot simply print a way off planet.

## The crash

- The cause of the crash is shown only as flashes and a glimpse, then the crash.  Nothing is explained, ever.
- The attacker is never named in game.  It is an open slot: any player can plug in their own mystery ship.
- Nathan's private headcanon may be the Black Fleet or the Ants from Errans Inter Astra.  Since this game is for Nathan, it does not need to match the other games.

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
- Idea: after two or three expansions, the player can return to the first planet and find their old crashed mech, while flying something far better than that old mess.
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
- Turn based, Qud-style: enemies move when you do.
- Survival logic closer to RimWorld than to most RPGs.
- No constant raiders or mech battles.  A few NPCs: 5 or 6 in camp, not a colony sim.
- Rules: pick what fits the game, borrowing lore elements from Lancer.  No adaptation of Lancer's narrative rules.
- **Draft (Claudia):** expeditions in Qud-style turns and camp in compressed time, so years can pass; 3 or 4 biome-specific survival pressures instead of many always-on meters; borrow Lancer vocabulary (Heat, HASE, licenses, Structure and Stress) as flavor.

## Engine

- **Draft (Claudia):** prototype the seeded zone generator first as plain text output, then build the game in Godot 4.

## Open items

- Feel and timing of the journey and of the years spent stranded.
- Local currency name.
- Engine choice.
