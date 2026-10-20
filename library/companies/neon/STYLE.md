# NEON — trailer style

Three official uploads from the NEON channel, measured at 480p (analyze_video.py adaptive detector; EBU R128 loudness; speech share from faster-whisper, not usable for the Japanese-language film). An auteur drama teaser, a horror main trailer and a festival horror final trailer.

| Example | Length | Shots | ASL / median | ASL by quarter | < 1 s / > 3 s | LUFS (I) / LRA | Aspect |
|---|---|---|---|---|---|---|---|
| [Paper Tiger, official teaser (Aug 2026)](paper-tiger-official-teaser/notes.md) | 61.3 s | 34 | 1.80 / 1.19 | 3.83 · 1.53 · 1.02 · 1.92 | 32 % / 12 % | −16.2 / 8.7 | 2.39:1 |
| [Hokum, official trailer (Mar 2026)](hokum-official-trailer/notes.md) | 119.9 s | 90 | 1.33 / 1.12 | 1.58 · 1.50 · 1.50 · 0.88 | 41 % / 3 % | −16.2 / 9.7 | 2.39:1 |
| [Exit 8, final trailer (Apr 2026)](exit-8-final-trailer/notes.md) | 84.1 s | 77 | 1.09 / 0.58 | 1.11 · 0.91 · 0.66 · 3.50 | 70 % / 6.5 % | −12.3 / 13.6 | 1.85:1 |

## Core idea
NEON sells **prestige**: festival laurels, critics' quotes, Academy Award nominees and "from the director of" credits. Its craft is to put that prestige **inside the film's world** instead of on slides: laurels composited into a shot, quotes over blurred footage or typed like a terminal, the NEON logo rebuilt as a neon sign in a hotel set, the date written as a room number. The NEON logo itself comes first (0–3 s) or as an object in the film at ≈20 %. Mixes are mostly quiet (−16.2 LUFS) and silence is a main tool.

## Shared rules (with numbers)
| Beat | Paper Tiger | Hokum | Exit 8 | Rule |
|---|---|---|---|---|
| NEON logo | 0–2 s, silver | 24.2 s (21 %), a red neon sign in the set | 2.0 s, yellow counter | first, or rebuilt inside the film |
| Prestige | 2 festival laurels + 3 quotes + 3 nominee cards | 2 "director/producer of" cards | Cannes notice + 3 quotes | 2–8 prestige moments per piece |
| Prestige placement | laurels in shots, quotes over blurred footage | serif cards dissolving into shots | quotes typed letter by letter, the last one over the picture | never a plain slide |
| Silence | none | 3 drop-outs of 2.0–3.65 s + 0.6 s digital silence | 0.55 s before the title, 3.3 s digital silence in a 10.8 s take | 2–4 s silences before scares (horror) |
| Title | 88 % over a landscape | 96 % on black | 73 %, then a scare and one more quote | 73–96 % |
| Date | "NOVEMBER" over the same landscape | "CHECK IN 5.1" (room number) | yellow card "APRIL 10" | month or a date as an in-world object |

- **Pace**: drama teaser ASL 1.8 s with an 8.7 s open; horror trailers ASL 1.1–1.3 s, last quarter fastest (0.66–0.88 s) or replaced by one long take.
- **Type** comes from the film: condensed cream caps (period drama), classic serif (gothic hotel horror), monospace yellow on black (subway signage).
- **Loudness**: −16.2 LUFS for both English-language titles; Exit 8 −12.3 LUFS with true peak +1.4 dBTP (the loud exception; do not copy).

## Sub-styles
**A. Prestige drama teaser (Paper Tiger).** Logo, an 8.7 s held night image under voice-over, laurels in the picture, three quotes over blurred light (≈3 % H, hold 1.75–3.5 s), a cast run of nominee cards, then one 8.4 s landscape that carries title, credit and date.

**B. Horror main trailer (Hokum).** A 4.6 s pre-hook of the scariest flashes, "TRAILER STARTS NOW", a slow open (5.2 s corridor), logo as a prop at 21 %, quiet serif credit cards dissolving into shots, three drop-outs of 2–3.65 s each followed by +29…+43 dB, montage at 0.5 s per shot in the last quarter, title at 96 %.

**C. Critics' horror, sign-system (Exit 8).** Yellow-black type from the film's exit signs, typed quotes, a strobe run of 0.12–0.3 s shots, a montage at 0.5 s per shot at −9 dBFS, the title on full yellow at 73 % after a cut to silence, then a 10.8 s take with 3.3 s of digital silence and a final scare.

## Recipe
1. Collect the prestige (festival, quotes, director, stars) and decide where each one lives inside a shot or in the film's own type.
2. Logo first (2 s) or as an object in the film at ≈20 %.
3. Quotes: 2 lines, ≈3–4.5 % H, over blurred footage or typed in; hold 1.5–3.5 s.
4. Horror: mute 2–4 s before each big scare; drama: no drop-outs, soft fades.
5. Title at 73–96 %; write the date as part of the world if possible.
6. Master −16 LUFS, true peak −1 dBTP.
