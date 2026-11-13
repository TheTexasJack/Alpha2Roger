# Alpha2-Roger Music

**Music v0.27, 2026-11-13**

The music bible: sound, tools, the riff, and the radio's music.  Decisions are Nathan's unless marked **Draft (Claudia)**.  Drafts are suggestions until Nathan approves them.  News, ads, and talk on the radio live in `docs/design/world.md`; this file covers only the music.

## Tools and pipeline (Nathan, 2026-11-11)

- The DAW is Waveform (Tracktion).  It runs on Beast (Linux Mint).
- No Suno and no other music generator on this project.  Nathan's Suno account belongs to SteamMetal Studio and stays off Alpha2-Roger.
- Claudia composes.  Nathan reviews, modifies, and adds beats that are pleasant on the ear.  If a composition is weak, Nathan may keep only the beat and tone and rebuild the rest.
- **Draft (Claudia), handoff:** Claudia delivers a MIDI file (one track per part, tempo and key set) plus a preview render and a short note (key, tempo, mood, where it plays, loop point).  Nathan mixes in Waveform and exports the final as OGG Vorbis for Godot.  Waveform project files stay on Beast; the repo holds only MIDI and exports.
- **Draft (Claudia), files:** drafts go in `assets/audio/music/drafts/`, finals in `assets/audio/music/`.  Every file carries `_vN` in its name, like the art.

## Traditional Gaelic tunes on Japanese instruments (Nathan, 2026-11-12)

- Building every track from scratch would take years longer than the coding, so Nathan is changing direction.
- Nathan tested Suno on the starting area (Japanese and Gaelic).  It ignored the instrument instructions and put a violin in everything, which gave a mashup that sounds off.  Suno is all the way out.
- New direction: traditional Gaelic songs or tunes that are free to use and include, as MIDI, played on traditional Japanese instruments.
- **Draft (Claudia), sourcing rules:**
  - Each tune must be traditional and published long enough ago to be public domain, such as O'Neill's Music of Ireland (1903).
  - Watch for modern songs that only sound old.  Ashokan Farewell is one known example.
  - Transcribe from scans of the original books ourselves.  Online transcriptions carry their own licenses: the O'Neill's Project ABC files are GPL, and Nigel Gatherer's are his own copyright.
  - Log each tune with its source book, page, and year.
- This has to work for every area of influence (Gaelic, Mongolian, Slavic, Persian, German; see `world.md`).  The tunes are old, and there is molding we can do with them.  Without common ground that works across all of them, we would be learning new styles one by one and forcing Japanese into each, which takes a music master.
- **Draft (Claudia), one recipe for every region:**
  1. The Japanese side stays the same everywhere: koto, shakuhachi, shamisen, taiko.  Kaze threads through all of it.
  2. Common ground is the five-note scale.  Keep tunes that fit a pentatonic scale, or bend into one with small changes.  A script can score whole public domain collections for fit.
  3. Each culture brings one signature beyond the melody, played on the Japanese instruments: Gaelic jig lilt; Mongolian drone and long free-time phrases; Slavic minor modes; German march and waltz; Persian ornaments and bent notes (shakuhachi and koto both bend pitch).
  4. Fit by region, easiest first: Gaelic and Mongolian (both lean pentatonic), Slavic, German, Persian (its scales use notes between our notes).
- If no public domain tunes can be found for a culture, we shift to getting the feel (Nathan, 2026-11-12).  The real challenge is giving it the feel and making the player think they are in that area, and it needs to be reasonable.
- Oceans and polar caps have their own music too (Nathan, 2026-11-12).
- From `world.md`: the deep ocean is Japanese plus sea shanties.  The polar ice caps are areas of dread, with deep-cold music.
- **Draft (Claudia), oceans and poles:** shanties are old work songs, and plenty of traditional ones are public domain, so the ocean can use the same tune-sourcing route as Gaelic: real shanties, verified per tune, on Japanese instruments, with taiko keeping the work rhythm.  For the poles, the dread comes from low drones, long silences, and the sound of ice, with Kaze heard only far off or not at all.
- Poles (Nathan, 2026-11-12): one lone, constant low tone, with a few notes from various songs interjected here and there.  Just a hint.
- Ice and open water are cultures of their own (Nathan, 2026-11-13; culture map in `world.md`).  Ice music: cold, long notes with bits of other songs, just small hints.  Open water pairs with sea shanties.
- **Draft (Claudia):** the game picks those few notes live from the other regions' tunes and Kaze, seeded per run, spaced far apart, so the ice never plays the same thing twice.
- **Draft (Claudia), feel kit and the test:** each region gets a short kit of three or four markers (scale, rhythm, texture, ornament).  Original tunes written with that kit carry the feel.  The test is blind: someone hears a clip with no label and names the region.  If they can, the feel works.
- **Draft (Claudia), why it fits:** many Gaelic airs are pentatonic, and the Japanese Yo scale is pentatonic too, so a lot of these tunes sit on koto and shakuhachi without changing a note.

### Japanese + Gaelic shortlist v1 (Draft, Claudia, awaiting Nathan's pick)

Slow airs from O'Neill's Music of Ireland (1903).  Numbers are O'Neill's.  Shio Loch and Kawa Fada are Irish Gaelic in `world.md`, so an Irish book fits.  Each pick still gets checked against the 1903 scan before use.

| No. | Tune | Key and meter in O'Neill's | Why |
|---|---|---|---|
| 89 | The Coolin | C, 3/4 | One of the best-known Irish slow airs; long, open phrases made for shakuhachi |
| 70 | The Little Black Rose (Róisín Dubh) | C minor, 3/4 | Iconic and dark; suits the cold |
| 58 | The Parting Glass | A, common time | Widely known farewell tune; use O'Neill's setting only |
| 59 | Shule Aroon | D minor, common time | Famous, simple, singable; a likely radio piece |
| 69 | O'Carolan's Lament | D minor, 3/4 | Carolan (1670 to 1738); harp tune, a natural koto fit |
| 47 | Rory Dall's Sister's Lament | A Dorian, 3/4 | Dorian sits closest to the Japanese minor sound |

**Scale fit v1 (Claudia, 2026-11-12):** share of each tune's note time that lands in the best-fitting Japanese scale.  Yo is the pentatonic with no half steps; In is the Japanese minor, Kaze's family.  Scored from the O'Neill's Project ABC (analysis only, not stored or shipped); the notes were read through a web tool, so small errors are possible.  Final transcriptions come from the 1903 scan.

| Tune | Yo | In | Notes outside the best scale |
|---|---|---|---|
| Rory Dall's Sister's Lament | 95% | 66% | F sharp only |
| The Coolin | 85% | 66% | C, C sharp, F |
| The Little Black Rose | 84% | 82% | Fits both; a bridge between the Gaelic region and Kaze |
| Shule Aroon | 81% | 73% | Several passing notes |
| O'Carolan's Lament | 77% | 80% | Several passing notes |
| The Parting Glass | 73% | 67% | D, G, G sharp |

- Approach (Nathan, 2026-11-12): this first pass is to start getting the feel.  The Akai and Nathan's ear come next.  Lean on our strengths, and shift when we have to.
- **Feel test v1 (Claudia, 2026-11-12):** Rory Dall's Sister's Lament, played as written at 60 BPM.  Koto plays the air once, then shakuhachi plays it with the koto under it, over a low A and E drone in the style of pipe drones.  It is built from the GPL transcription, so it stays off the repo and was sent to Nathan only.
- Nathan, 2026-11-12: feel test v1 is good; it would be better with a bamboo flute.
- **Feel test v2 (Claudia, 2026-11-12):** the same, with the shakuhachi replaced by a shinobue (side-blown bamboo festival flute), which sits high and airy like an Irish whistle.
- Nathan, 2026-11-12: v2 sits just on the outside of almost.  It is good and the right direction, and still the best direction as we get into different areas.  Two things need to happen: the notes and tune need adjusting and cleaning up, and it needs an undertone or beat, which Nathan will add.  This is where the Akai has to be up.
- Background music is usually long tones and hints at a full song.  Nobody sings Skyrim's background music, but they are listening to it (Nathan, 2026-11-12).
- The target for this region: the song makes you think you are in the Irish wilds with samurai (Nathan, 2026-11-12).
- The koto is a traditional instrument, but it has no long notes (Nathan, 2026-11-12).
- **Draft (Claudia), who holds the long tones:** the koto plays hints and fragments.  Long tones go to instruments that sustain: the shō (mouth organ, sustained chords; the natural partner to a pipe drone), the kokyū (bowed, the Japanese answer to the Irish fiddle), and the shakuhachi and shinobue (breath).
- Nathan is leaning on the breathy flute now (Nathan, 2026-11-12).
- **Shortlist MIDI v1 (Claudia, 2026-11-12):** The Coolin, The Little Black Rose, O'Carolan's Lament, Shule Aroon, and The Parting Glass, each with a breathy flute melody (written notes, lifted whole octaves where needed so the lowest note sits at G4 or higher) and a tonic-and-fifth drone.  Built from the GPL transcription, so they stay off the repo and were sent to Nathan only.

## Sound (Nathan, 2026-11-11)

- Background music stays calm and relaxing.  Touchstones: Skyrim's background music, RimWorld's plucky western tones, and Caves of Qud's weird, almost tribal tones.
- Punchy, heavy beats and riffs belong to the radio, based on the region the player is in.
- No combat music, not directly (Nathan, 2026-11-12).  The background music and the radio have no secret knowledge the player does not have.
- Tense moments stay for scripted story elements: comics and key points, such as when you learn you are not you anymore (Nathan, 2026-11-12).
- **Draft (Claudia), what that rules out:** no music that starts when an enemy is near, swells before an ambush, or changes when a fight begins.  Music can follow only what the player already knows: where they are, the time, the weather, the radio signal.
- **Draft (Claudia):** exploration music stays mostly beatless (soft pulses and texture at most), because the game is turn-based and the player stops to think.  Real beats go to the radio and cities.

## The riff (Nathan, 2026-11-11)

- We pick one riff that becomes ours and weave it into everything, the way the Elder Scrolls theme has run through every game since Morrowind and "Down by the River" is stretched and shifted through Baldur's Gate 3.
- The riff is based on famous Japanese tones, since Japanese is the world's base culture, with a more modern shift and cold, chilling undertones.
- **Draft (Claudia), rules for the riff:** 4 to 8 notes, short enough to survive being cut down.  It must work as a pluck, over a drone with hand drums, and as a slow pad.  In the wilderness only a fragment plays (the first three notes, slowed).  The full theme waits for big moments: reaching the spaceport and the endings.
- No off notes for now (Nathan, 2026-11-12): build the song first and establish the core.  If an off note is used for the story, it comes in the moment.
- **Draft (Claudia), on hold per the line above:** the clone twist gets the theme played slightly wrong, one note off, like a copy.

### The pick (Nathan, 2026-11-12)

- Kaze (`riff_b_kaze_v1`) is the riff.  It is a few elements shy of really going somewhere, but the sample left Nathan wanting more of it: he could just about feel the pull of it into the world.

### Nathan's sung guide (Nathan, 2026-11-12)

- Nathan recorded himself singing a guide line to steer Kaze v2: the melody of "Darkness," a song he wrote long ago.  The recording and lyrics stay off the repo.  The lyrics are not for Alpha2-Roger; the tone only leans in to help Kaze.

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

### Kaze v5: reversing halfway (Draft, Claudia)

- Nathan, 2026-11-12: v4 is better and stronger, but it just repeats the 8 notes.  After the first 2 runs, try reversing halfway, then finish the riff in the original notes.

- Nathan, 2026-11-12: neither landed ("nah").  He is ruminating and will come back with direction.

Two readings, same layout as v4.  Runs 1 and 2 are the original riff in both.

| File | Runs 3 to 8 | Length |
|---|---|---|
| `kaze_song_v5a` | The first half backward (E F E A), then the second half as written (C B C A).  Still 2 bars. | About 1 minute 7 |
| `kaze_song_v5b` | The first half as written (A E F E), turn at the halfway point and walk back up (F E A), then finish as written (C B C A).  3 bars. | About 1 minute 31 |

### Kaze v4: the riff song (superseded by v5)

- Nathan, 2026-11-12: v3 went the wrong direction.  The full riff was good: those first 8 notes.

`kaze_song_v4`: the song built on the whole 8-note riff (A E F E C B C A).  Every statement plays all 8 notes intact; only the instruments and the chords under it change.  About 1 minute 7, eight statements at 72 BPM, every note inside A B C E F.

| Statement | Riff on | Under it |
|---|---|---|
| 1 | Koto alone | Nothing |
| 2 | Koto | Bass: A, then F to A |
| 3 | Shakuhachi, koto an octave under | Bass and drone |
| 4 | Shakuhachi and koto | Drone and soft pulse: F, then C to A |
| 5 | Bell, half speed | Pad, the warm one: C, then E to A |
| 6 | Bell and koto | Cold pad and drone: F, then C to A |
| 7 | Bell, koto, shakuhachi | Everything: the fullest point |
| 8 | Koto alone | Home, into the wind |

### Kaze v3: the song (superseded by v4)

`kaze_song_v3`: the full song, core only, every note inside Kaze's set (A B C E F).  About 1 minute 50, 32 bars at 72 BPM, and it begins and ends in wind so it can loop.  v2's second voice in fourths (it hit a tritone, B over F) and the flute's flat scoop into each note are gone, and the koto is now tuned exactly.

| Bars | Section | What happens |
|---|---|---|
| 1 to 4 | Intro | Wind and drone; the first three notes of Kaze on koto, twice |
| 5 to 8 | A | Kaze on koto over bass |
| 9 to 12 | B | Nathan's line on shakuhachi over drone, soft pulse; hangs on E |
| 13 to 16 | A | Kaze on shakuhachi; koto answers with the fragment |
| 17 to 20 | Bridge | The warm moment: long bell notes over C and F, leaning on E |
| 21 to 24 | B | Nathan's line again, shakuhachi and koto in octaves |
| 25 to 28 | A | Kaze on bell and koto with pad, drone, and pulse: the fullest point |
| 29 to 32 | Coda | Nathan's ending drops below home, the fragment once more, back to the wind |

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

## Ambience (Nathan, 2026-11-12)

- Keep an ear out for crickets, night sounds, rivers, and water.  Nathan may record a lot of it himself on his phone.
- **Draft (Claudia), recording tips:** set the phone down instead of holding it; shield it from wind (foam, or a sock over the mic); use a recorder app that saves uncompressed audio with noise reduction and auto gain off; record 3 to 5 minutes per take so there is room to cut clean loops; go late at night or early morning, away from roads, air conditioners, and planes; avoid catching people's voices; name each file with what, where, and when.
- Nathan's recording list (2026-11-12): his older phones as dedicated recorders; Lake Texoma; storms; boat motors (the world has boats); Foley at home, as he and Alex did for a Remnant video.  The cold works in our favor: it is a cold world.  Highway 75 carries on some nights.
- **Draft (Claudia), fit with the rules:** ambience follows only what the player knows (biome, time, weather), so it obeys the no-secret-knowledge rule.

## Open

- Now required (Nathan, 2026-11-12): set up the Akai so Waveform records from the keyboard.  Known so far: Linux sees it (client 28, port 0 carries the keys), notes reach Waveform, but the instrument plays one note at a time and nothing records.
- Nathan's next direction for Kaze, after he ruminates.  v4 is the strongest version so far.
- Tempo, key, and length for the first wilderness bed once the riff is locked.
