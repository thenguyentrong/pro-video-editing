# Bang & Olufsen - film style

Three official films measured at 480p with `analyze_video.py` (scene detector, adaptive for the dark centenary film; cut lists checked on the sheet, cuts added/removed where noted), EBU loudness, grade numbers at 2 fps, text measured in % of frame height (H), faster-whisper only to check for voice (none found).

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice |
|---|---|---|---|---|---|---|---|
| [Beolab 90 Titan Edition (2026)](beolab90-titan/notes.md) | 60.0 s | 42 | 1.43 / 1.32 | 1.50 · 1.25 · 1.25 · 1.36 | 19 % / 2 % | -16.8 | none |
| [Beo Grace (2025)](beo-grace/notes.md) | 60.0 s | 40 | 1.50 / 1.10 | 1.50 · 1.07 · 1.25 · 2.14 | 48 % / 8 % | -20.4 | none |
| [Sound. Elevated. 90 s (2025)](sound-elevated-90s/notes.md) | 90.0 s | 60 | 1.50 / 1.18 | 1.50 · 1.18 · 1.61 · 1.50 | 40 % / 12 % | -14.0 | none |

## The core idea
B&O sells objects that are also furniture and heritage. The films never explain features. They show the object as craft (raw aluminium to finished speaker), as a quiet companion in big landscapes, or as a period piece in a 100-year story. Text is reduced to the wordmark, a product name and at most one short line. Music carries everything; there is no narrator in any of the three films.

## Sub-styles
**1. Craft film** (Beolab 90 Titan). Real factory footage: grinding, polishing, gloved hands, jigs, then the finished object in an empty white hall and a run of 0.5-1 s driver macros. Cool, low-saturation grade (median saturation 13 %). Wordmark at the start, product name + italic edition line at the end, wordmark on black.

**2. Mood launch** (Beo Grace). Live action in landscapes; one accent colour (red) carried by wardrobe and a vintage train. Long calm shots (2-5 s) broken by 1-3 "flurries" of 3-6-frame texture shots. Tiny lowercase captions (≈ 2.2 % H) low in frame, one brand line in empty space. The logo appears in-world (printed on the train).

**3. Heritage anthem** (Sound. Elevated.). A device (a lift) opens on decades of sound; each world has its own grade and a period object; very dark overall (81 % dark frames); letter-built brand line at the end.

## Measured ranges (3 films)
- ASL 1.43-1.50 s, median 1.10-1.32 s - strikingly constant across very different films. Quarters stay within 1.07-1.61 s, except Beo Grace slowing to 2.14 s at the end.
- 19-48 % of shots under 1 s (macro runs and texture flurries), 2-12 % over 3 s. Longest shots 4-6 s.
- Cuts on onsets: 15-23 % vs 10-15 % chance: loosely on the music, mostly on action.
- Loudness −14.0 to −20.4 LUFS; LRA 6.6-10.8 LU (more dynamic than most product films). Two of three masters have true peaks above 0 dBTP.
- No drop-outs; the films end on the wordmark with ≤ 0.5 s of silence or on the last chord.
- Grade: Titan cool (R-B −10), Grace and Elevated neutral to warm (0 to +9). Median luma 13-107: B&O is not afraid of dark films.

## Typography
- Wordmark "BANG & OLUFSEN" in wide-tracked caps with "Est. 1925" small under it: cap ≈ 9 % H on the craft film, ≈ 4 % H on the anthem; centred.
- Product names in a geometric sans, sentence case, cap ≈ 7 % H (Titan), ≈ 2.5 % H (Grace); edition names in an italic serif. Closest free: Jost (sans) + Libre Caslon Italic or Instrument Serif Italic.
- Lines: "100 years. One journey." cap ≈ 4.6 % H, full stops, centred; "The sound of things to come"-type brand line ≈ 3.3 % H beside a face; captions ≈ 2.2 % H at y ≈ 86 %.
- Animation: fades of ≈ 0.5 s; the anthem builds letters with tracking that settles.

## Colour
- One accent per film (blue crane in the factory, red jumper/train, red bag) inside a restrained palette (aluminium/white, blue-green landscape, dark wood and black).
- Products are never colour-graded: aluminium stays aluminium.

## Camera
- Symmetric hero wides of the object in an empty space; macros with a moving light; tiny figures in huge landscapes; real craft footage with white gloves.

## Transitions
- Hard cuts. Section markers are a short white flash (Titan), 0.6 s of black before a flurry (Grace) or lift doors (Elevated). No decorative wipes.

## Sound
- Music only in all three; mechanical textures in the craft film; airy score with swells in Grace; era-shifting score with +18-23 dB rises in the anthem.

## What makes it premium (across examples)
- Text at the edges only (open and close), small and centred or placed in empty space.
- The object is treated like sculpture: empty halls, white gloves, light sweeps.
- A constant, calm cut rhythm (≈ 1.5 s) whatever the subject, with a few very short bursts for energy.
- One accent colour per film.

## How to recreate with real footage + HTML/GSAP (Hyperframes)
1. Choose the sub-style: craft (process → object), mood (person in landscapes + accent colour) or heritage (device that opens on eras).
2. Cut at 1.3-1.6 s average, flat by quarter; add 1-3 bursts of 3-6-frame shots on music hits.
3. Wordmark: `font: 400 12vh 'Jost'; letter-spacing:.12em; text-transform:uppercase` (cap ≈ 9 % H) + `Est.` line at 4vh; centred, fade 0.5 s.
4. Product name: `font: 500 9.6vh 'Jost'` + edition `font: italic 5.5vh 'Instrument Serif'`, centred over the hero wide; dim the shot before the wordmark on black.
5. Keep one accent colour: grade the world `saturate(.8)` and mask the accent object at full saturation.
6. Music only; master −14 to −16 LUFS, true peak ≤ −1 dBTP.
