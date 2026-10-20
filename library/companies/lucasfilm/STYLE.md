# Lucasfilm — trailer style

Three official uploads from the Star Wars channel, measured at 480p (analyze_video.py adaptive detector; EBU R128 loudness; speech share from faster-whisper). One film in two formats plus one streaming-series teaser.

| Example | Length | Shots | ASL / median | ASL by quarter | < 1 s / > 3 s | LUFS (I) / LRA | Aspect |
|---|---|---|---|---|---|---|---|
| [The Mandalorian and Grogu, official trailer (Feb 2026)](mandalorian-and-grogu-official-trailer/notes.md) | 131.7 s | 97 | 1.36 / 1.08 | 1.37 · 1.18 · 1.10 · 1.83 | 43 % / 5 % | −14.1 / 8.6 | 2.39:1, cards full frame |
| [The Mandalorian and Grogu, "Monster" TV spot (Apr 2026)](mandalorian-and-grogu-monster-spot/notes.md) | 30.1 s | 30 | 1.00 / 0.80 | 0.94 · 0.94 · 0.68 · 1.25 | 70 % / 3 % | −14.1 / 3.8 | 2.39:1, cards full frame |
| [Ahsoka Season 2, teaser trailer (Aug 2026)](ahsoka-s2-teaser-trailer/notes.md) | 95.1 s | 80 | 1.19 / 0.85 | 1.49 · 0.95 · 1.13 · 1.13 | 66 % / 5 % | −14.1 / 5.9 | 2.39:1 incl. cards |

## Core idea
Lucasfilm cuts fast and evenly (ASL 1.0–1.4 s, flat across the quarters) and uses its colour and type to set the tone of each title: a pulp, retro-serial look for the Mandalorian film (pale green bevelled caps, a slanted 3D logo), a thin glowing look for Ahsoka. The sound is the most consistent in the whole trailer set: all three are mastered to −14.1 LUFS. Text is very rare in the trailers (3 moments) and frequent in the spot (9 moments).

## Shared rules (with numbers)
| Beat | Mando trailer | Mando spot | Ahsoka teaser | Rule |
|---|---|---|---|---|
| Open | graphic sun image 4 s, then 11 s at ASL 0.9 s | 5 s threat, ASL 0.9 s | 20 s dark open with 0.2–0.3 s black dips | no logo first; a strong image or a threat line |
| Studio logo | 15.4 s (12 %) on black | none | 19.7 s (21 %), rebuilt in red light | logo at 12–21 % after a cold open |
| Text before the title | 1 date card (54 %) | 3 taglines + date words over action | 2 cards (26 %, 31 %) | trailers: 1–2 cards; spots: 5–7 |
| Densest 10 s | 68–76 % | 0–10 s | 74–84 % | late density in trailers |
| Title | 91 % | 84 % | 94 % | 84–94 % |
| After the title | 5.4 s comic button + date | end block + call to action | platform logo 3.3 s | film trailers end on the characters, series on the platform |

- **Pace**: 43–70 % of shots under 1 s, only 3–5 % over 3 s. Held shots are the exception (a 3.8 s face, a 3.3 s fog silhouette, a 3.7 s chase).
- **Sound**: −14.1 LUFS in all three, LRA 3.8–8.6 LU. Hits of +15…+32 dB at each new scene. The trailers have no pre-title silence; Ahsoka has one 0.5 s drop-out (−42.5 dBFS) before the last act with the biggest rise (+31.9 dB) right after it.
- **Dialogue and humour**: speech in 57–88 % of the runtime; the film trailer puts a 2–3 s comic beat after each action run and ends on a post-title button.
- **Cards on a plate, never flat black**: starfield (Mando), red-blue nebula with a flare (Ahsoka).

## Sub-styles
**A. Adventure film trailer (Mando).** Graphic first image, fast cold open, logo at 12 %, one date card at 54 %, three acts at ASL 1.1–1.4 s, quiet comic beat, chase with longer shots, 3D pulp title at 91 %, button, date.

**B. TV spot (Mando "Monster").** ASL 1.0 s, 70 % under 1 s, cut on the beat (41 % on onsets vs 31 %), three tagline cards (two-size stack ≈8 % + 12 % H), release facts written over action shots two words at a time, one card dissolving into the picture, compressed mix (LRA 3.8 LU).

**C. Streaming-series teaser (Ahsoka).** Platform bug in the corner for the whole piece, cards inside the letterbox in the show's thin glowing caps (≈7.5 % H, tracking ≈0.12 em), dark open, fog section as a rest, drop-out and hit before the last act, title at 94 %, platform logo at the end.

## Recipe
1. Open on one graphic or dark image; no logo first.
2. Studio logo at 12–21 %, then ASL 1.1–1.4 s, flat.
3. Trailers: 1–2 cards; spots: taglines plus date words over action.
4. Put a short comic or quiet beat after each action run.
5. Title at 84–94 %; film trailers end on a character button, series on the platform logo.
6. Master −14 LUFS, true peak −1 dBTP.
