# Microsoft - video style (2022-2026)

Built from 3 official examples, analysed 20 Oct 2026 (480p / 360p, cuts checked by eye, EBU loudness, text measured in % of frame height H):

| Example | Type | Length | Shots | ASL / median | % < 1 s | % > 3 s | Loudness | Voice |
|---|---|---|---|---|---|---|---|---|
| [copilot-everyday-ai-companion](copilot-everyday-ai-companion/notes.md) | AI launch ad | 45.1 s | 60 | 0.75 / 0.52 s | 80 | 3 | -21.5 LUFS | none |
| [surface-laptop-ultra-film](surface-laptop-ultra-film/notes.md) | hardware launch film | 82.2 s | 35 | 2.35 / 1.67 s | 17 | 23 | -13.3 LUFS | none |
| [anthem-for-all](anthem-for-all/notes.md) | accessibility documentary | 184.7 s | 58 | 3.18 / 2.20 s | 10 | 33 | -19.2 LUFS | interviews |

## In one sentence
Microsoft builds each film around ONE graphic or human idea - a prefix ("Co-") stuck to forty verbs, a decoding pixel terminal font, or real veterans telling their own story - and lets that one idea carry the film instead of a narrator.

## Sub-styles

### 1. One-word montage (Copilot launch ad)
- "Co-" in white + a gradient verb, cap ≈13 % H, centred, over real people at real crafts; frosted prompt pills (≈59 % W) type over the person; real product UI between.
- ASL 0.75 s, then a 1.7 s flash run of 3-4-frame word cards before the logo.
- Music only, mastered very quietly (−21.5 LUFS).

### 2. Engineering launch (Surface Laptop Ultra)
- One 15.8 s opening move from screen content out to the laptop; then a lab and machine-shop story (white gloves, anechoic chamber, CNC, knolled parts).
- Every claim typed in a glitchy pixel monospace (cap ≈3.8 % H) with a white "selection" block and a cursor; the same font on the end card.
- Music + mechanical SFX, −13.3 LUFS, cut on the beat (29 % vs 11 % chance).

### 3. Human documentary (Anthem for All)
- 2.39:1 letterbox, interviews on long lenses, archive photos as small insets on black, a 29 s quiet black text section as the turn, then the real event as payoff.
- Lower thirds and text cards in small Segoe (2-2.3 % H); end line in Segoe Light ≈3.75 % H.
- Dialogue-led, −19.2 LUFS, a 2.9 s near-silence before the music returns (+36 dB).

## Measured ranges
- ASL 0.75 s (montage ad) / 2.35 s (engineering film) / 3.18 s (documentary). Quarter curves: flat-fast then a flash run; long-open + dense middle; slow first half then speed-up.
- Loudness −13.3 to −21.5 LUFS - no house loudness; the two ads differ by 8 LU.
- No narrator in any of the three.

## Typography
- Segoe UI / Segoe UI Variable (proprietary): free stand-in **Selawik** (Microsoft's open Segoe fallback) or **Inter**.
- Each film has one type idea: gradient verb (Copilot), pixel monospace decode (Surface; free **Departure Mono** / **VT323**), tiny documentary captions (Anthem).
- Copilot gradient: blue → teal on cool shots, pink → orange → purple on warm shots.

## Colour
- Copilot: each shot keeps its own colour world; the pill and the gradient word are the glue; end on pale blue-white.
- Surface: warm creator desk vs cold steel-grey lab, low key.
- Anthem: warm natural documentary low key, then saturated arena colour.

## Camera
- Real people at real tasks; hands macros; real screen recordings; product only in use (Copilot, Anthem) or as an engineered object (Surface).

## Transitions
- Hard cuts. Specials: overlays that run across cuts (prompt pill, word card), type that decodes and scrambles, a long in-camera pull-back from screen to device, fades through black.

## Sound
- Music-only ads; documentary with interview voices and the anthem as the payoff. Use silence before the emotional turn (2.9 s).

## Recipe (pick the sub-style)
- One-word montage: 15-20 craft clips at 0.4-0.9 s, word card `font:700 13vh Inter` with a gradient verb typed per letter, frosted prompt pill, 2 s flash run, 5 s logo card.
- Engineering launch: 12-16 s opener move, macros of making, decode type `3.8vh Departure Mono` with a selection block, 12-15 s slow build, lockup 5 s.
- Documentary: letterbox 2.39:1, interviews first, archive as insets, 25-30 s text section at ≈25 % of runtime, real event payoff.
