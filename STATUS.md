# Status

**STATUS v0.3, 2026-11-10**

## Where things stand

- **Stage 0 (concept lock): closed 2026-11-10.**  The concept, the world of Verlassen, and the mechanics list are written down.
- No game code exists yet.  The Godot project has not been created.
- Every file carries a version.  `tools/version_check.py` verifies them against `VERSIONS.md`.  `tools/system_report.py` writes a full diagnostic report to `diagnostics/`.
- World tools exist in `tools/` (globe, places, regions, person names), with canon maps in `assets/maps/`.

## Next steps (Nathan picks the order)

1. **Stage 1, A2R-101:** pack the planet data (globe seed 2718, ten places, regions, cultures, currencies) into one data file the engine will read.
2. **Stage 1, A2R-102:** write the zone generator spec for Nathan's review before any code.
3. **Stage S:** guided, secured setup of Nathan's PC (Timeshift, Claude Code, Godot 4).  Best done at the machine.
4. **Design gaps:** stats and skills (#35, the biggest), trade (#70), currency names and rates, what the infection does.

## Open decisions

- Listed at the bottom of `docs/design/concept.md` (Open items) and `docs/design/world.md` (Open).

## Last session

- 2026-11-10 (Claudia): moved maps and art from `docs/` to `assets/` so `docs/` stays text only and fits the claude.ai project sync.

- 2026-11-10 (Claudia): versioning and diagnostics.  Versions added to every tool and data file, art renamed with `_v1`, `version_check.py` and `system_report.py` added, rules written into `AGENTS.md`, mechanic #92 drafted.

- 2026-11-10 (Claudia): repo cleanup.  Design docs moved to `docs/design/`, the plan to `docs/plan/`, concept and world sections put in logical order, stale open-items lists refreshed, and `AGENTS.md`, `CLAUDE.md`, `STATUS.md`, and `.gitignore` added.
