# Alpha2-Roger Project Plan

**Plan v0.1, 2026-11-09**

Nathan owns this plan.  Claudia (or Mara) updates it in place and notes each change in the changelog.  Suggestions are marked **Draft (Claudia)** until Nathan approves them.

## How we work

- One stage at a time.  Each stage ends at a gate: Nathan reviews and approves before the next stage starts.
- Small, compartmentalized tasks with clear inputs and outputs.
- Every deliverable carries a visible version number, bumped on every change.
- Commits go straight to `main`.
- Agents only for bounded tasks with a short written brief.  No copying full context into multiple agents.
- PERMA's November first set (due 2026-11-27) takes priority.  Alpha2-Roger runs as a side track until then.

## Stage 0: Concept lock

Goal: settle the decisions that everything else is built on.

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-001 | Movement model | Open | Qud turn sync, or free movement with combat math.  **Draft (Claudia):** Qud-style turns on expeditions, compressed time in camp |
| A2R-002 | Engine | Open | **Draft (Claudia):** prototype in Python, build in Godot 4 |
| A2R-003 | Art style | Open | Two-shade sprites, EGA retro, or other.  Decide before any art |
| A2R-004 | Time scale | Open | How long a day, a season, and a year take in play.  How many years a typical run lasts |
| A2R-005 | Survival pressures | Open | **Draft (Claudia):** 3 or 4, biome-specific (cold, air, water, heat) |
| A2R-006 | Planet basics | Open | Name, size, climate bands, number of fixed cities, where the spaceport is |
| A2R-007 | Local currency | Open | Name and how it trades against Manna |

**Gate:** every Stage 0 item decided and recorded in `docs/concept.md`.

## Stage 1: Zone graph generator (text only)

Goal: prove the seeded map works before any graphics exist.

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-101 | Planet data file | Not started | Fixed cities, landmarks, biome regions, route distance ranges.  Data only, no engine code |
| A2R-102 | Generator spec | Not started | Inputs (planet file, seed) and outputs (zone graph).  Written and approved before code |
| A2R-103 | Generator prototype | Not started | Outputs a readable text map, for example "Crash Site > Spore Thicket > Collapsed Arcology" |
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

## Changelog

- Plan v0.1, 2026-11-09 (Claudia): first plan.  Stages 0 to 4 detailed, later stages outlined.
