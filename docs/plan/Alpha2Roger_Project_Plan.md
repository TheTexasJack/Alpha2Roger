# Alpha2-Roger Project Plan

**Plan v0.35, 2026-11-13**

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
| A2R-003 | Art style | Decided | Layered peg people, RimWorld style.  Older style with modern color selection |
| A2R-004 | Time scale | Deferred | Day, season, and run length decided after we see gameplay |
| A2R-005 | Survival pressures | Decided | Biome specific: heat and cold, food and sleep, light sanity (mood debuffs, no insanity), light relationships |
| A2R-006 | Planet basics | Decided | All recorded in `docs/design/world.md`: Verlassen (Kepler-64432p), 5071u (was 5016u), between Cinder Crown and the KTB; Sun-like star, a year of about 14 Earth months (calendar: 12 months of 35 days, 420 days), cold year every third year from a gas giant's 3:1 resonance; globe seed 2718; ten named places and regions; peoples, cultures, government; three infection impact sites |
| A2R-007 | Local currency | In progress | Five regional currencies grouped by place (see `docs/design/world.md`); Manna off-world.  Open: currency names, exchange rates |

**Gate:** every Stage 0 item decided or explicitly deferred, and recorded in `docs/design/concept.md`.  **Passed 2026-11-10: Stage 0 closed.**

## Stage S: Workstation setup (guided)

Goal: Claude hand-holds Nathan through setting up Beast for local Godot development with Claude Code, and secures the machine first so nothing gets accidentally wiped.  One step at a time, each confirmed before the next.

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-S01 | Safety net first | Not started | Timeshift system snapshot (built into Linux Mint) before anything else; confirm a backup of the home folder |
| A2R-S02 | Fence the workspace | Not started | One dedicated project folder; Claude Code runs only inside it, never as root or with sudo |
| A2R-S03 | Install Claude Code | Not started | Native Linux install; log in with the Claude plan (no API key set, so usage stays on the plan) |
| A2R-S04 | Lock down Claude Code permissions | Not started | Ask-before-acting permission mode; deny rules for destructive commands (for example recursive deletes and anything outside the project folder) |
| A2R-S05 | Git as the undo button | Not started | Clone the repo into the project folder; GitHub is the off-machine backup; small commits to main |
| A2R-S06 | Install Godot 4 | Not started | Pin the exact version in the README |
| A2R-S07 | Shared rules file | Done | `AGENTS.md` at the repo root (read by Claude Code and by Codex-style tools on Mara's side): style, versioning, compartmentalized steps, one AI per file at a time |
| A2R-S08 | Headless test check | Not started | A Godot test add-on runs from the command line, so changes can be verified without clicking through the game |
| A2R-S09 | Plan check | Not started | Start on the current plan; move to Max, then Ultra, only if usage limits actually bite |
| A2R-S10 | Python for the baker | Not started | Python 3 with numpy, scipy, and Pillow on Beast, so the world tools and the region baker run there.  Nathan likely has Python and Pillow already; confirm versions when it is time (Nathan, 2026-11-13): `python3 tools/system_report.py` lists all four.  The tools were verified with Python 3.13, numpy 2.5, scipy 1.18, and Pillow 12.3 |

**Gate:** Nathan restores a test file from Timeshift and from git, confirming both safety nets work, and Claude Code runs one harmless test command inside the fenced folder.

## Stage 1: World generator (baked regions, first local maps, text output)

Goal: prove the seeded world works before any graphics exist.  Region maps are baked ahead of time by the Python baker on Beast; Godot builds the local maps from them (option A, decided by Nathan 2026-11-13).

| ID | Task | Status | Notes |
|---|---|---|---|
| A2R-101 | Planet data file | Done | Locked by Nathan 2026-11-10 at v0.1; v0.2 (2026-11-11) adds the calendar; v0.5 to v0.7 (2026-11-13) add the route network, the highest point (Yamajira), the climate lines, the biomes, and the region rules: `tools/data/planet_verlassen.json` (built by `tools/planet_pack.py`), with seed, ten places, impact sites, regions, cultures, currencies, straight-line distances.  Data only, no engine code.  Fixed file name, version inside.  Biome regions and route distance ranges moved to A2R-102 |
| A2R-102 | Generator spec | Done | Signed off by Nathan 2026-11-13, with the remaining drafts parked as later items until a working concept is confirmed.  Spec in `docs/design/zones.md`.  First region R5 built by `tools/region_gen.py`.  Inputs (planet file, world seed, run seed); outputs: baked region files (Python baker) and seeded local maps (Godot).  Also defines biome regions and route distance ranges (moved from A2R-101).  Written and approved before code |
| A2R-103 | First Godot load | Not started | Godot reads the planet file and R5's baked region file, takes the Tutorial Start (world seed 2718, run seed 2718, S1), and builds S1's 9-map section of local maps from the run seed, printing a text summary of each map (biome, water, edges, crossing points).  Doubles as a first Godot lesson.  Rewritten 2026-11-13 for option A; the old text zone chain ("Crash Site > Spore Thicket > Collapsed Arcology") is retired |
| A2R-104 | Determinism test | Not started | The same run seed gives the same local maps every time; different run seeds give different maps; neighboring maps agree on their shared edges.  Runs headless (A2R-S08).  Rewritten 2026-11-13 for option A |
| A2R-105 | Region baker, full layers | Not started | **Draft (Claudia):** `tools/region_gen.py` writes the remaining layers (salinity, flow, full-detail height, moisture, territory, routes, landmarks, entrances, and the start cells) in a packed format; R5 first, then the 147 regions with land below the ice line |

**Gate:** Nathan runs the Tutorial Start and a few run seeds at S1 and approves the results.

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
- Town banks: currency exchange, storage, loans (see Currency in `docs/design/world.md`).
- In-game credits screen carrying the Lancer Third Party License requirements: the acknowledgement, "Lancer is copyright Massif Press", thanks to Massif Press, and a "Powered by Lancer" mark.  Required in the final product.
- Random settlement name list: about 200 names for small local settlements, built with the hybrid naming rule (Japanese base plus the region's second culture), kept as a data file.  Depends on the regional culture assignments.
- NPC content lists, kept as data files: backstories, traits, orientations, speech styles.  These feed NPC creation and the dialogue model.
  - Dependency: backstories need the world first (planet, lore, era, places, peoples).  Traits, orientations, and speech styles are mostly world-agnostic and can come earlier.
- NPC voices, ElevenLabs style: much later.  **Draft (Claudia):** local text-to-speech is also an option, in line with the zero-token-cost local model.
- Local AI dialogue for NPCs: planned after the base game works, during NPC and interaction work.  Rules: the engine owns all game state and the model only voices it (fed a character card of traits, mood, relationship, recent events); a local model on Nathan's PC, zero token cost; authored fallback lines when the model is off; the story spine stays hand-written; a lore sheet in the prompt to limit drift.
- Headless sim mode for automated testing (seed sweeps, balance runs such as surviving year one on paste), possible because game logic is separate from rendering.  **Draft (Claudia)**

## Changelog

- Plan v0.35, 2026-11-13 (Nathan): A2R-102 signed off and done; remaining zones drafts parked as later items.
- Plan v0.28, 2026-11-12 (Nathan): the year is 5071u; planet data file v0.4.
- Plan v0.27, 2026-11-11 (Nathan): planet data file v0.3, political regions renamed territories; cultural regions get their own key.
- Plan v0.26, 2026-11-11 (Nathan): planet data file v0.2 with the 12 by 35 day calendar.
- Plan v0.34, 2026-11-13 (Nathan): A2R-S10 accepted; versions get confirmed when Stage S runs.
- Plan v0.33, 2026-11-13 (Nathan): option A, regions baked ahead of time by the Python baker.  Stage 1 renamed; A2R-103 and A2R-104 rewritten; A2R-105 (region baker) and A2R-S10 (Python on Beast) added as drafts.
- Plan v0.32, 2026-11-13 (Claudia): A2R-101 note: planet file v0.7 holds the climate lines, biomes, and region rules.
- Plan v0.31, 2026-11-13 (Claudia): A2R-101 note: planet file v0.5 carries the route network.
- Plan v0.30, 2026-11-13 (Claudia): review fixes.  A2R-006 year wording matches the 12-month calendar; A2R-S07 marked Done (`AGENTS.md` exists since plan v0.22).
- Plan v0.29, 2026-11-13 (Nathan): A2R-102 in review; zone graph format complete.
- Plan v0.25, 2026-11-10 (Nathan): A2R-102 in progress; zones and travel direction recorded in `docs/design/zones.md`.
- Plan v0.24, 2026-11-10 (Nathan): A2R-101 locked and done; biome regions and route distance ranges moved to A2R-102.
- Plan v0.23, 2026-11-10 (Claudia): A2R-101 in review; planet data file v0.1 packed.
- Plan v0.22, 2026-11-10 (Claudia): repo cleanup; plan moved to `docs/plan/`, design docs to `docs/design/`; `AGENTS.md` and `STATUS.md` added.
- Plan v0.21, 2026-11-10 (Nathan): town banks added to later stages.
- Plan v0.20, 2026-11-10 (Nathan): A2R-007 in progress: five regional currencies grouped.
- Plan v0.19, 2026-11-10 (Nathan): A2R-003 and A2R-006 decided; Stage 0 closed.
- Plan v0.18, 2026-11-09 (Nathan): government recorded: lords and mayors, councils, the 3 tier method.
- Plan v0.17, 2026-11-09 (Nathan): regional second cultures and names for the ten places locked.
- Plan v0.16, 2026-11-09 (Nathan): Stage S added: guided workstation setup with safety first (Claude drafted the steps).
- Plan v0.15, 2026-11-09 (Nathan): note to generate about 200 random settlement names.
- Plan v0.14, 2026-11-09 (Nathan): ten fixed places accepted; local life and remoteness rule recorded.
- Plan v0.13, 2026-11-09 (Claudia): in-game credits task added after checking the full Lancer Third Party License text.
- Plan v0.12, 2026-11-09 (Nathan): globe locked to candidate B, seed 2718.
- Plan v0.11, 2026-11-09 (Nathan): globe approach approved; candidate generator and map saved to the repo.  Naming rule recorded in concept v0.21.
- Plan v0.10, 2026-11-09 (Nathan): planet physical details decided.
- Plan v0.9, 2026-11-09 (Nathan): planet named Kepler-64432p, locally Verlassen; location set.
- Plan v0.8, 2026-11-09 (Nathan): A2R-006 in progress; first world facts in new `docs/design/world.md` v0.1.
- Plan v0.7, 2026-11-09 (Nathan): backstories depend on the world being established first.
- Plan v0.6, 2026-11-09 (Nathan): NPC content lists (backstory, traits, orientation, speech style) and much-later NPC voices added to later stages.
- Plan v0.5, 2026-11-09 (Nathan): local AI NPC dialogue noted for after the base game, during NPC and interaction work.  Headless sim testing added as a draft.
- Plan v0.4, 2026-11-09 (Nathan): Stage 0 review.  Decided A2R-001, 002, 003, 005.  Deferred A2R-004 and 007.  A2R-006 open.  Concept v0.8 records all answers.
- Plan v0.3, 2026-11-09 (Nathan): A2R-001 decided (turn based); A2R-003 in progress (simple 2D top-down sprites).  Inspirations and core concepts recorded in concept v0.6.
- Plan v0.2, 2026-11-09 (Nathan): Alpha2-Roger is the passion project, built for Nathan.  Removed the PERMA priority line; this plan is measured on its own terms.
- Plan v0.1, 2026-11-09 (Claudia): first plan.  Stages 0 to 4 detailed, later stages outlined.
