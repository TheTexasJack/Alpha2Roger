# Alpha2-Roger Project Plan

**Plan v0.8, 2026-11-09**

## What this project is

Alpha2-Roger is Nathan's passion project.  It is the game Nathan wants to play, built for Nathan.  Anyone else just gets to go along for the ride.  Design calls are judged by one test: would Nathan want to play it.

Nathan owns this plan.  Claudia (or Mara) updates it in place and notes each change in the changelog.  Suggestions are marked **Draft (Claudia)** until Nathan approves them.

## How we work

- One stage at a time.  Each stage ends at a gate: Nathan reviews and approves before the next stage starts.
- Small, compartmentalized tasks with clear inputs and outputs.
- Every deliverable carries a visible version number, bumped on every change.
- Commits go straight to `main`.
- Agents only for bounded tasks with a short written brief.  No copying full context into multiple agents.

## Stage 0: Concept lock

Goal: settle the decisions that everything else is built on.

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-001 | Movement model | Decided | Turn based: enemies move when you do.  Camp time (compressed or not) deferred until we see gameplay |
| A2R-002 | Engine | Decided | Godot 4, 2D.  Nathan is new to Godot; a learning experience |
| A2R-003 | Art style | Decided | Layered peg people, RimWorld style.  **Draft (Claudia):** defer the palette to the art stage |
| A2R-004 | Time scale | Deferred | Day, season, and run length decided after we see gameplay |
| A2R-005 | Survival pressures | Decided | Biome specific: heat and cold, food and sleep, light sanity (mood debuffs, no insanity), light relationships |
| A2R-006 | Planet basics | In progress | Recorded in `docs/world.md`.  Decided: era 5016u, about 50 years from the current tables, temperate but cold, 14-month year, every third year a cold year, weather sensor warning.  Open: name and physical details, climate bands, fixed places, peoples |
| A2R-007 | Local currency | Deferred | Planned after the lore and era are established |

**Gate:** every Stage 0 item decided or explicitly deferred, and recorded in `docs/concept.md`.

## Stage 1: Zone graph generator (text only)

Goal: prove the seeded map works before any graphics exist.

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-101 | Planet data file | Not started | Fixed cities, landmarks, biome regions, route distance ranges.  Data only, no engine code |
| A2R-102 | Generator spec | Not started | Inputs (planet file, seed) and outputs (zone graph).  Written and approved before code |
| A2R-103 | Generator prototype | Not started | Built in Godot, outputs a readable text map, for example "Crash Site > Spore Thicket > Collapsed Arcology".  Doubles as a first Godot lesson (**Draft (Claudia)**) |
| A2R-104 | Determinism test | Not started | Same seed gives the same map every time; different seeds give different maps |

**Gate:** Nathan runs several seeds and approves the results.

## Stage 2: One zone, on screen

Goal: turn one generated zone into a grid map you can see.

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-201 | Zone tile spec | Not started | Grid size, tile types, how biome and seed shape a zone |
| A2R-202 | Zone renderer | Not started | Placeholder tiles are fine |
| A2R-203 | Delta save | Not started | Saves only what the player changed in a zone |

**Gate:** walk-through of three different zones from three seeds.

## Stage 3: Survive one zone

Goal: the first moment that feels like the game.

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-301 | Player movement on the grid | Not started | Uses the A2R-001 decision |
| A2R-302 | One survival pressure | Not started | The simplest one from A2R-005 |
| A2R-303 | Zone transitions | Not started | Leave one zone, enter the next on the graph |

**Gate:** Nathan plays it and it feels tense.

## Stage 4: Salvage and the first repair

Goal: the core loop.

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-401 | Salvage | Not started | Finding parts in zones |
| A2R-402 | Crash site camp | Not started | The wrecked mech as base |
| A2R-403 | First repair | Not started | One restored system unlocks one capability |

**Gate:** one full loop: leave camp, salvage, return, repair, unlock.

## Later stages (outline only, planned when we reach them)

- Camp NPCs and compressed time
- Biomes and seasons
- The journey to the city
- The city, the spaceport, and the identity questline (inbox UI)
- The franken-mech and recognition
- NPC content lists, kept as data files: backstories, traits, orientations, speech styles.  These feed NPC creation and the dialogue model.
  - Dependency: backstories need the world first (planet, lore, era, places, peoples).  Traits, orientations, and speech styles are mostly world-agnostic and can come earlier.
- NPC voices, ElevenLabs style: much later.  **Draft (Claudia):** local text-to-speech is also an option, in line with the zero-token-cost local model.
- Local AI dialogue for NPCs: planned after the base game works, during NPC and interaction work.  Rules: the engine owns all game state and the model only voices it (fed a character card of traits, mood, relationship, recent events); a local model on Nathan's PC, zero token cost; authored fallback lines when the model is off; the story spine stays hand-written; a lore sheet in the prompt to limit drift.
- Headless sim mode for automated testing (seed sweeps, balance runs such as surviving year one on paste), possible because game logic is separate from rendering.  **Draft (Claudia)**

## Changelog

- Plan v0.8, 2026-11-09 (Nathan): A2R-006 in progress; first world facts in new `docs/world.md` v0.1.
- Plan v0.7, 2026-11-09 (Nathan): backstories depend on the world being established first.
- Plan v0.6, 2026-11-09 (Nathan): NPC content lists (backstory, traits, orientation, speech style) and much-later NPC voices added to later stages.
- Plan v0.5, 2026-11-09 (Nathan): local AI NPC dialogue noted for after the base game, during NPC and interaction work.  Headless sim testing added as a draft.
- Plan v0.4, 2026-11-09 (Nathan): Stage 0 review.  Decided A2R-001, 002, 003, 005.  Deferred A2R-004 and 007.  A2R-006 open.  Concept v0.8 records all answers.
- Plan v0.3, 2026-11-09 (Nathan): A2R-001 decided (turn based); A2R-003 in progress (simple 2D top-down sprites).  Inspirations and core concepts recorded in concept v0.6.
- Plan v0.2, 2026-11-09 (Nathan): Alpha2-Roger is the passion project, built for Nathan.  Removed the PERMA priority line; this plan is measured on its own terms.
- Plan v0.1, 2026-11-09 (Claudia): first plan.  Stages 0 to 4 detailed, later stages outlined.
