# Leica - film style

Three official films measured at 480p with `analyze_video.py` (adaptive detector for all three, checked on the sheets; fades through black added in the M11 film, one scene cut added in The Art of Leica), EBU loudness, grade numbers at 2 fps, text in % of frame height (H), faster-whisper only to find where the VO is.

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice |
|---|---|---|---|---|---|---|---|
| [LEICA Q3 43 - Moments (2024)](q3-43-moments/notes.md) | 54.7 s | 6 (CG takes) | 9.12 / 6.74 | 4.56 · 4.56 · 13.68 · 6.84 | 0 % / 100 % | -9.0 | none |
| [M11 Monochrom - A Symphony of Light and Shadow (2023)](m11-monochrom-symphony/notes.md) | 92.8 s | 37 | 2.51 / 1.84 | 5.80 · 1.93 · 1.66 · 2.32 | 3 % / 27 % | -16.1 | male VO 4-90 s |
| [The Art of Leica (2026)](art-of-leica/notes.md) | 129.1 s | 81 | 1.59 / 1.40 | 1.70 · 1.34 · 1.47 · 1.70 | 16 % / 4 % | -17.7 | male VO 2-127 s |

## The core idea
Leica sells seeing. The camera is shown as a precise, almost sacred object (built from its lenses, revealed by light in darkness, placed on a white plinth), and then the films hand over to photographers and their pictures. The proof is the photograph. Text is close to zero: one word, a model name, and the red dot. The red dot is the only colour the brand insists on, even in a black-and-white film.

## Sub-styles
**1. CG assembly film** (Q3 43). A sunlit beige room with leaf-shadow light; lens elements float in and the camera assembles itself; one long orbit with hidden swaps (hood, edition plate, charger, screen); name card in small wide caps on black; red dot logo. Music only.

**2. Product overture + photographers** (M11 Monochrom). 26 s of the black body in darkness lit by a moving light band, joined by fades through black; then B&W photographers in desert and city; then the camera on a white plinth in grey; the whole film in monochrome with only the red dot in colour; poetic VO.

**3. Brand anthem** (The Art of Leica). "Maker → result" pairs: a photographer at work, then their photograph as a white-bordered print on black; an anaphora VO ("It's the art of ..."); one word on screen at the start; logo grows on black at the end.

## Measured ranges
- People-led films: ASL 1.59-2.51 s, median 1.40-1.84 s, few shots under 1 s (3-16 %). Product overtures and CG takes: 4-21 s shots.
- First quarter is the slowest in two of three films (5.80 s overture in M11; 4.56 s in Q3 43).
- Cuts on onsets 0-19 % vs 2-24 % chance: cuts follow the VO phrases or the CG events, not the beat.
- Loudness −16.1 / −17.7 LUFS for VO films; −9.0 LUFS for the music-only CG film (very loud).
- Endings: logo on black with 1.7-3.2 s of silence in all three.
- Grade: M11 saturation 0 %; Q3 warm daylight (R-B +26, luma 119); Art of Leica keeps each photographer's look (luma 53).

## Typography
- Geometric sans, light or regular weight (closest free: Outfit Light / Jost Light). Model names in wide-tracked caps (≈ +0.08 em), cap ≈ 4 % H, centred on black. One word "Photography" at ≈ 6.3 % H, centred, sentence case.
- No supers, labels or feature names in any of the three films.
- Red dot logo ≈ 9 % H, centred on black; may scale up from ≈ 2 %.

## Colour
- Neutral or monochrome worlds; the red dot is the accent. Warm beige/oak and dappled daylight for the CG product world; deep blacks and bright skies for B&W.

## Camera
- Product: extreme macro, slow slides with a moving light band, assembly from floating parts, white plinth in a grey void, slow orbits.
- People: documentary, handheld, wide lenses, back-light, real photographers on location.

## Transitions
- Fades through black between product macros; hard cuts for people; the still photo on black as a "shutter" after footage.

## Sound
- Poetic male VO with pauses over piano/strings (VO films); minimal electronic with click SFX on each part landing (CG film). Logo always in silence.

## What makes it premium (across examples)
- The product is revealed by light or by its own construction, never by graphics.
- Results (photos) are the proof; the camera appears as craft details.
- Almost no text; the logo is the only graphic.
- Patience: a slow first quarter is allowed.

## How to recreate with real footage + HTML/GSAP (Hyperframes)
1. Product overture: 3-5 macros of 4-10 s in darkness, a light band (`linear-gradient`, `mix-blend-mode:screen`) travelling across, fades through black 0.5 s.
2. People section: 1.4-2 s cuts on VO phrases; after every 4-6 shots a still photo on black (`max-height:62vh`, 6 px off-white border) for 0.8-1.5 s.
3. Product return: white plinth (`#f2f2f2` box) in a grey void (`#8d8d8d → #5d5d5d` radial), slow orbit 3-5 s per shot.
4. Name card: `font: 300 5.5vh 'Jost'; letter-spacing:.08em; text-transform:uppercase` on black, 3 s. Logo on black 2-3 s in silence.
5. Monochrome option: `grayscale(1) contrast(1.15)` on everything except one red element.
6. Master −16 LUFS (VO) / −14 LUFS (music only).
