# Alpha2-Roger Music

**Music v0.4, 2026-11-12**

The music bible: sound, tools, the riff, and the radio's music.  Decisions are Nathan's unless marked **Draft (Claudia)**.  Drafts are suggestions until Nathan approves them.  News, ads, and talk on the radio live in `docs/design/world.md`; this file covers only the music.

## Tools and pipeline (Nathan, 2026-11-11)

- The DAW is Waveform (Tracktion).  It runs on Beast (Linux Mint).
- No Suno and no other music generator on this project.  Nathan's Suno account belongs to SteamMetal Studio and stays off Alpha2-Roger.
- Claudia composes.  Nathan reviews, modifies, and adds beats that are pleasant on the ear.  If a composition is weak, Nathan may keep only the beat and tone and rebuild the rest.
- **Draft (Claudia), handoff:** Claudia delivers a MIDI file (one track per part, tempo and key set) plus a preview render and a short note (key, tempo, mood, where it plays, loop point).  Nathan mixes in Waveform and exports the final as OGG Vorbis for Godot.  Waveform project files stay on Beast; the repo holds only MIDI and exports.
- **Draft (Claudia), files:** drafts go in `assets/audio/music/drafts/`, finals in `assets/audio/music/`.  Every file carries `_vN` in its name, like the art.

## Sound (Nathan, 2026-11-11)

- Background music stays calm and relaxing.  Touchstones: Skyrim's background music, RimWorld's plucky western tones, and Caves of Qud's weird, almost tribal tones.
- Punchy, heavy beats and riffs belong to the radio, based on the region the player is in.
- **Draft (Claudia):** exploration music stays mostly beatless (soft pulses and texture at most), because the game is turn-based and the player stops to think.  Real beats go to the radio, cities, and tense moments.

## The riff (Nathan, 2026-11-11)

- We pick one riff that becomes ours and weave it into everything, the way the Elder Scrolls theme has run through every game since Morrowind and "Down by the River" is stretched and shifted through Baldur's Gate 3.
- The riff is based on famous Japanese tones, since Japanese is the world's base culture, with a more modern shift and cold, chilling undertones.
- **Draft (Claudia), rules for the riff:** 4 to 8 notes, short enough to survive being cut down.  It must work as a pluck, over a drone with hand drums, and as a slow pad.  In the wilderness only a fragment plays (the first three notes, slowed).  The full theme waits for big moments: reaching the spaceport and the endings.
- **Draft (Claudia), the clone:** the clone twist gets the theme played slightly wrong, one note off, like a copy.

### The pick (Nathan, 2026-11-12)

- Kaze (`riff_b_kaze_v1`) is the riff.  It is a few elements shy of really going somewhere, but the sample left Nathan wanting more of it: he could just about feel the pull of it into the world.

### Nathan's sung guide (Nathan, 2026-11-12)

- Nathan recorded himself singing a guide line to steer Kaze v2: the melody of "Darkness," a song he wrote long ago.  The recording and lyrics stay off the repo.

**Draft (Claudia), what the guide shows:** a low chant that recites on one home note (C) and circles it with half-step neighbors (B below, C sharp above), lifts a fifth to G with A flat on top, falls back home, then a coda that drops a fourth below home and sinks.  The notes around C are C, D flat, F, G, and A flat: the In scale, the same family as Kaze.  The pace is about one note per eighth at 72 BPM, Kaze's own tempo.

### Kaze v2

- Nathan, 2026-11-12: v2 is better than v1.

`riff_b_kaze_v2`: the full theme in A, 72 BPM, 12 bars, shaped by the guide with his reciting note moved to E so it lands inside Kaze.

| Bars | Part | What happens | Colour |
|---|---|---|---|
| 1 to 4 | A, A | Kaze v1 twice: the fall home to A | Koto pluck over bass (RimWorld) |
| 5 to 8 | B | Nathan's line: recite on E with the E-F flick and a dip to B and C, lift to B with C on top, fall and hang on E | Shakuhachi over a drone, soft hand-drum pulse, koto a fourth below (Qud) |
| 9 to 10 | A' | Kaze returns | Bell over a cold pad with wind (Skyrim) |
| 11 to 12 | Coda | Drops below home, like the guide's ending, and settles on low A | Bell and pad |

Chords move A, F, C, E: the C is the one warm moment, and the E at the end of B leans back toward A.

### Candidates v1

All three run at 72 BPM in 4/4.  Each preview plays the riff three ways: pluck (RimWorld), drone with hand drums and shakuhachi-style flute (Qud), then a bell over a cold pad at half speed with wind (Skyrim).

| File | Scale | Idea |
|---|---|---|
| `riff_a_shimo_v1` | In scale (miyako-bushi) on E: E F A B C | Shimo, frost.  The classic koto sound of old Japan, the scale behind "Sakura Sakura."  Rises, then falls home through the half step F to E, the coldest step in the scale. |
| `riff_b_kaze_v1` | Hirajoshi on A: A B C E F | Kaze, wind.  The best-known Japanese scale in Western ears.  Falls from the top in a long, open line, and the bass under it leans on F, so it never fully settles. |
| `riff_c_utsushi_v1` | Yo scale on D, turning to In | Utsushi, the copy.  The first bar is warm min'yo folk.  The second bar repeats it with two notes flattened (B to B flat, E to E flat), so the same tune comes back cold.  The clone idea is built into the riff itself. |

Each MIDI holds seven tracks: koto pluck, bass pluck, hand drums, drone, shakuhachi, bell (half speed), cold pad.  Markers name the three sections.

## Radio music (Nathan, 2026-11-11)

- The radio is built into the M.U.L.E. and the player's wrist unit, from the start of the game.
- Regional stations carry punchy, heavy beats and riffs in the region's style.
- **Draft (Claudia):** each station hides the riff in its own style, the way Skyrim's bards sang the main theme in every tavern.  Ad jingles can carry it too.
- Regional fusion drafts are in `docs/design/concept.md` (Music).

## Open

- What Kaze v3 needs, if anything, after Nathan sits with v2.
- Tempo, key, and length for the first wilderness bed once the riff is locked.
