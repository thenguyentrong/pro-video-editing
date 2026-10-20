# Figure 03 Trailer  (Figure, 2025-10-07, 0:48, 16:9, YouTube @figureai)
URL: https://www.youtube.com/watch?v=IlG3X8zRI2I
Purpose: product reveal teaser (industrial-design trailer)
One-sentence point: Figure 03 is a soft, textile-covered humanoid designed like a consumer product - shown only through materials and details.

Honesty note: everything is studio macro on a seamless warm-grey backdrop. Whether it is real product photography or CGI can't be decided at 480p; the textile, hair-like fibres and reflections look like high-end CGI or a mix (guess).

## Structure (cut list; no voice, music only)
- 0.0-3.3 hook: the black head-face screen; white pixels light up and assemble into the Figure "S" pixel mark (0-2 s). First hit at 1.25 s (+26 dB).
- 3.3-19.7 materials: knitted textile sleeve in extreme macro (3 s), fabric peeling over joints (4-6 s), arm, wrist, hand (10-11 s), black joint caps rotating (13-17 s), neck/shoulder shell (18 s).
- 19.7-23.5 logo on fabric: the pixel "S" mark printed on textile, fibres moving (19-22 s) - the loudest part (20.15 s, -6 dBFS).
- 23.5-34 details: back of the knit "jacket" with ventilation holes and zipper (24-25 s), head profile with "003" (26 s), neck/torso joints, an exploded joint cap (29-30 s), "FIGURE" embossed on the hip (31 s), fingertips with blue tactile sensors (32-33 s), a camera in the palm (34 s).
- 34-44.75 full body (finally): feet in knitted "sneakers" stepping on a glossy floor (36-38 s, 5.5 s longest shot), torso front on dark background with blue edge light (39.5 s), fast 0.21-0.67 s cuts (39.5-41.5 s), back/head 3/4 view (41-44 s).
- 44.75-48 end: black; a white pixel square grows into the "S" logo mark (44-46 s), black.

## Cut rhythm
- 23 shots in 48 s. ASL 2.09 s, median 2.00 s. ASL per quarter 3.00 / 1.71 / 1.71 / 1.50 s.
- Longest 5.50 s (34.0, feet), 4.58 s, 3.79 s, 3.29 s (opening). Shortest 0.21 s, 0.25 s, 0.25 s (the 39.5-41.5 s burst).
- 26 % under 1 s, 30 % over 3 s. Steady ~2 s per shot, then one burst before the logo.

## Typography
- No supers at all. Only the product's own markings ("FIGURE" on the hip, "003" on the head) and the pixel logo animation (head screen at the start, black card at the end, logo ~8 % frame height, centre).

## Colour/grade
- Near-monochrome: warm light grey (#d8d6d2-ish) background, off-white textile, glossy black shells; one accent - small blue light on fingertips/shoulders. Soft, large-source studio light; deep but clean shadows.

## Camera/shots
- Macro-first reveal: the whole robot is never shown until 34 s, and even then never head-to-toe in one frame.
- Slow sliding/orbiting moves at 1-2 % of frame per second, shallow depth of field, rack focus over textures. Floating/exploding parts (29-30 s).
- No action, no task - pure industrial design.

## Transitions
- Hard cuts. A bright light flash at 35 s. Logo pixel build at start and end (bookend).

## Sound
- Loud electronic/percussive track: integrated -7.7 LUFS (very loud, music-video level), median -11.5 dBFS. Spectrogram: dense rhythmic transients, breaks around 12.5 s and 33 s; no voice.
- Biggest rise at 1.25 s (+25.8 dB) on the first pixels.

## What makes it premium
- Apple-style "materials first" reveal: texture -> detail -> part -> full product.
- Strict palette: grey, off-white, black + one blue accent.
- Logo built from the product's own pixel display - brand and product are one.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Shoot macro of real parts (textile/rubber/metal of your machine) on a seamless warm-grey sweep, slider moves, f/2.8-4, 2 s per shot; hold the full product until 70 % of runtime.
- Grade: `filter: saturate(.15) contrast(1.05) brightness(1.05) sepia(.08)`, keep one accent colour un-desaturated (do it in the grade, not in CSS, if possible).
- Pixel logo: a CSS grid of 8x8 `<i>` squares on black; `gsap.from('.px', {autoAlpha:0, scale:0, duration:.12, stagger:{each:.02, from:'random'}})` until the mark is formed; hit SFX on the first pixel.
- Burst: 3 shots of 0.21-0.25 s right before the end card.
