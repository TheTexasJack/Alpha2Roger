# Alpha2-Roger Concept

**Concept v0.29, 2026-11-09**

Decisions are Nathan's unless marked **Draft (Claudia)**.  Drafts are suggestions until Nathan approves them.

## The name

- Alpha2: you are the second print of the lance's Alpha.
- Roger: as in confirmation.

## Scope: what this game is

- A survival game set in the Lancer world.  Survival comes first.
- A traditional RPG in its rules and structure.  It does not use Lancer's narrative rules.
- A separate game from Lancer, the tabletop RPG, and from the video game Lancer Tactics.
- Mechs are secondary.  They may appear later in a run (for example the scrap-built mech in the story arc), and they never replace the survival core.

## Content rating

- Adult.  Language, violence, and mature themes are fine.
- Not ridiculously sexual.  Intimacy, if it ever comes up, stays abstract (sheets and hearts), since animating anything complex, even with pegs, becomes more art than mechanics.  Details figured out along the way.
- Brawl mechanics: to be dealt with later.
- A difference from RimWorld: no slave cat people and no coats made from human skin.  Cruelty exists in the world to be opposed; the player never profits from it.
- **Draft (Claudia):** concretely, no player-owned slaves, no crafting from human remains, and no organ harvesting.

## Design approach

- Gameplay first.  The experience is the game play.  Science and physics stay real, so nothing needs awkward explaining (the cold year, orbits, exposure).  The rest of the galaxy and universe can shift to fit our needs (the map, the star system's layout, where things sit).
- Engine first.  Build the systems and let the interactions fall into place, then fine tune later.  This gives the most versatility, instead of writing in every option step by step.
- **Draft (Claudia):** keep traits, needs, moods, and relationship rules in data files, so tuning means editing numbers instead of rewriting code.
- **Draft (Claudia):** systems drive the people (pawns, survival, relationships); the story spine stays authored (the crash, the twist, the cities, the legal path).

## Naming

- Names can be generated randomly.
- Use old reference names from past cultures.  There are already a million names in the world; no reason to reinvent them.  This avoids typical AI names (like Voss).
- Primary naming culture: Japanese, with English spellings (romanized).  Influence from all the major cultures on top.  This gives a central feel and an easy feudal concept.  American-style Japanese (as familiar to Western audiences) is a common thing to lean on.
- **Draft (Claudia):** generate place names from real Japanese name parts matched to terrain (-yama mountain, -kawa river, -mura village, -machi town, -jima island, -zaki cape), and skip famous real cities.  Geothermal cities become onsen towns.
- The German local name Verlassen stays.
- Hybrid place names: split a name half Japanese and half another culture.  Each area pairs Japanese with a second culture.  Example, in a Japanese and German area: Traurige Heigen (German traurige, sad, plus Japanese heigen, plains: the Sad Plains).
- **Draft (Claudia):** the generator builds hybrid names from a Japanese terrain word matched to the land (heigen plains, yama mountain, kawa river, mori forest, mizuumi lake) plus a word from the region's second culture, so each region has its own recognizable pair.
- **Draft (Claudia):** give each region one or two source cultures so its names feel consistent; skip famous historical figures; keep a blacklist of AI-cliche names (Voss, Kael, Elara, Thorne, Lyra, Vex, Nyx, Zephyr, Seraphina, Aria) and never generate them.

## Model and inspirations

The model: top-down dungeon crawler and open explorer.  Old brain, old gaming style.  Simple 2D, with enough on screen that the imagination does the rest.

- Sword of Fargoal
- Decklin's Domain: Demise: Rise of the Ku'tan and Demise: Ascension
- Caves of Qud
- RimWorld

What sets us apart from those games: a voiced mech computer, Subnautica style, that explains the planet and its weather (see `docs/world.md`).  None of the reference games do that.

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
- Not everything is a faction.  No Qud-style reputation web where plants turn hostile because someone wronged a deer.
- Walls are for warmth and shelter.  Threats are mostly environmental.
- Early food: a food printer in the mech.  It makes paste: just enough to survive.  It works for the companions too, and it is still just paste.  Eating only paste costs mood or morale, and its limited feedstock slowly pushes the camp toward hunting, trading, and the first harvest.  It is the one printer that works for you, since paste needs no license.

## Survival pressures

- Biome specific.
- Heat and cold.
- Food and sleep.
- Sanity, light: some depression mood debuffs at most.  No insanity and no RimWorld-style mental breaks (nobody digs up a corpse).  You were once a Lancer; you can handle a little hardship.

## Relationships

- A light relationship mechanic, organic like RimWorld.
- Relationships matter for the journey: companions may not like you enough to come along, or you might have a poly relationship.  The engine and the player decide.
- Every pawn is different, worked through pawn to pawn.  Orientations vary: one might be straight, one might be ace.
- Ace pawns can still be sexual; they just care less about sex than other people might.
- **Draft (Claudia):** track romantic interest and sexual interest as two separate dials per pawn, so an ace companion can still fall hard for someone romantically.

## NPC creation

- Like the engine, we build the base of the NPCs first.  NPCs may be randomized at creation.
- What is rolled at creation is solidified into who they are.  That profile is what gets sent to the dialogue model later.
- Nickname system: the player's character can call NPCs whatever they like.
- **Draft (Claudia):** a nickname is a display layer over the NPC's real name, which stays locked in their core; other NPCs keep using the real name.
- **Draft (Claudia):** split each NPC into a core that is locked at creation (name, backstory, traits, orientation, speech style) and a state that changes in play (mood, needs, relationship scores, recent events).  Both go to the model.  Rolls use the run's seed, so the same seed gives the same crew.

## Art and feel

- Pillar: old-school bones, modern effects.  Caves of Qud does this in places.
- Effects rule: this is Nathan A, not triple A.  No ambient occlusion, no motion blur, and nothing that every player just turns off.  A little frost creeping in is fine.
- A little screen shake is fine in places: short moments only, never constant, since constant shake makes the screen hard to read.
- **Draft (Claudia):** also out by that rule: film grain, chromatic aberration, depth of field, heavy bloom, and lens flare.  Screen shake stays tiny and has a toggle.  Every effect that remains should tell the player something (cold, damage, light).
- **Draft (Claudia):** where modern effects shine: real 2D lighting (a campfire glow pushing back the fog of war), frost creeping in at the screen edges as it gets colder, weather particles that build through the cold year, and light shader polish (heat shimmer near the reactor, screen flicker when the mech computer glitches).
- Simple 2D top-down sprites.
- Peg people, RimWorld style: layered body, head, hat, and gun, maybe circle hands.  Easy to add new weapons and gear, and no animation of hands, arms, legs, or running, which saves the engine for other things.
- The feel comes from the weapon effects.  Good weapon feel makes or breaks immersion.  Effects stay snappy, with a speed-up option.
- Palette: open.
- Placeholders (Nathan delegated this call to Claudia): early stages use simple glyph-image placeholder tiles, swapped for real peg sprites once the core loop works.  The peg layering system is built early with rough placeholder layers.  No permanent ASCII mode.
- Game logic never depends on how anything looks; the renderer is separate, so swapping art is a texture change.

## Lancer vocabulary

- Heat, HASE, Structure, and Stress stay out until mechs come into play, but are referenced when needed to keep the lore intact.

## Premise

- Lancer universe, Lancer-adjacent.  Uses the lore, does not follow the Lancer rules.
- Your mech crashed and was damaged on a rim world.  You are stuck, possibly for years, until rescue or until you get yourself off planet.
- The planet is so far out that Union holds no sway.  Union is known, but the locals are in control.
- The planet has its own economy and currency.  Manna can be exchanged for it at the spaceport.  Currency details wait until the lore and era are established.

## The twist (hold back from marketing)

- The player is a Thomas Riker.  A backup of you was restored and went home.  That version holds your name, identity, and licenses.
- The duplicate setup varies per run (for example a sympathetic backup, a backup whose life yours would wreck, or a failed restore where nobody claimed your name).
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
4. The legal win registers you as a new person: new name, License Level 0.
5. Once established, you can start proving you are a Lancer.
6. Eventually you get a mech: a non-standard one built from bits and pieces.
7. You prove yourself before any of the big manufacturers recognize you.

## The journey

- Prep matters: weight limits, supply caches along the route, who stays behind, and a point of no return.
- Who comes along depends on relationships.

## Communications

- Per Lancer lore, messages across blinkspace are bundled and take time.  A reply may come weeks or months later.
- **Draft (Claudia):** each transmission costs Manna (holo calls most, text least), and at some point letters arrive from your other self.

## Language and translation

- The player has cybernetics: an implanted universal translator.
- Right after the crash, a calibration process in the tutorial runs through a bunch of sample languages spoken on the planet, then calibrates.  After that, everything is in English.
- The calibration reports 563 independent languages detected: some archaic, some Karrakin Trade Baronies (KTB), and a lot of deviations and newly evolved languages.
- No constructed languages and no coded dialects.
- **Draft (Claudia):** real-world check: Papua New Guinea has about 10 million people and 800+ languages, so 563 on Verlassen is believable.  It implies old settlement in many waves.  Like PNG's Tok Pisin, a trade creole likely grew up around the spaceport and salt-lake hubs as the common market tongue.
- **Draft (Claudia):** the calibration samples double as a first taste of the planet's peoples and regions.

## The M.U.L.E.

- M.U.L.E.: Multimodal Utility Language Entity.  Based on Nathan's hand-crafted miniature (later variants adjusted with Mara); references in `docs/art/mule/`.
- The CompCon assumes the M.U.L.E. early on.  It follows the player as a utility workhorse.  Not big enough to ride.
- Maybe an early second fighter, defending while the player prepares.
- No need to go back to the mech every time to talk to the CompCon.
- **Draft (Claudia):** as the Language Entity, the M.U.L.E. carries the translator and the computer voice.  It carries cargo, which ties into journey prep and weight limits.
- **Draft (Claudia):** limits so it never trivializes survival: it runs on batteries that lose capacity in the cold, so it weakens in the cold year; it can be knocked out and repaired, and while it is down the CompCon falls back to the mech.
- **Draft (Claudia):** keep the no-animation rule with a two-frame skitter or a simple bob for its legs.

## Licenses and the scrap mech

- Per Lancer lore, you cannot use licensed gear, but licensed gear can be scrapped and remade into unlicensed gear.  That is how the scrap mech becomes possible.
- The clan hunting-rig art in the Lancer core book is a reference only: an ideal of what we might do, and no commitment.

## Map

- A fixed overall planet map.  Cities and landmarks are fixed.
- Wilderness is random per seed.
- Wilderness biomes are tied to a fixed climate layer.
- Crash site: the player selects a crash region or picks random.  Always away from civilization.  Crashing far from the spaceport can mean years of travel; if that is an issue, do not pick a crash site that far, or live with the random roll.
- **Draft (Claudia):** the crash selection screen shows a rough distance to the spaceport for each region.
- Zone distances are set between fixed areas.  Exact route lengths are decided when we design the maps.
- Zone based, not open world.
- Future planets are planned from the start: each planet is built as a data module, so new planets do not require engine rewrites.
- Idea: after two or three expansions, the player can return to the first planet and find their old crashed mech, while flying something far better than that old mess.

## Goals and endings

- Alpha2-Roger is Nathan's passion project: the game he wants to play.
- Playthroughs establish the endings.  We find them by playing.
- Endings are marked as milestones.  The game keeps going after an ending is reached.
- Plan for four ending milestones, built one at a time, in stages.  Candidates: Union recognition under a new name; refusing Union and living as yourself; building your own way off planet; staying, with the planet as home.
- The game pushes toward future planets.
- Fade points are design signals: when play starts to fade, that is the point where we add something or push the player into the next act.  Nathan (and any playtesters) report fade points.
- Replayability: make a new character each run.  The core duplicate and bureaucratic loop remains, but the approach can change.  For example, one run you fight for your identity; another you tell them to fuck off and just be yourself.

## Play style

- Grid based, like Caves of Qud or old school RPGs.
- Turn based, Qud-style: enemies move when you do.
- Survival logic closer to RimWorld than to most RPGs.
- No constant raiders or mech battles.  A few NPCs: 5 or 6 in camp, not a colony sim.
- Rules: pick what fits the game, borrowing lore elements from Lancer.  No adaptation of Lancer's narrative rules.

## Engine

- Godot 4, 2D.  A learning experience: Nathan is new to Godot.
- **Draft (Claudia):** build the Stage 1 zone generator in Godot as a text-output tool, so it doubles as a first Godot lesson.

## Open items

- Camp time: compressed time or not.  Decide after seeing gameplay.
- Time scale: day, season, and run length.  Decide after seeing gameplay.
- Planet basics: name, size, climate bands, cities, spaceport location.
- Local currency: after the lore and era are set.
- Palette.
