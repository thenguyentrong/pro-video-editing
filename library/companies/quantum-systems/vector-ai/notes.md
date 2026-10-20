# Vector AI: The next-generation, AI-powered tactical sUAS  (Quantum Systems, 2025-03-27, 0:50, 16:9, YouTube @QuantumSystems, best available 360p)
URL: https://www.youtube.com/watch?v=mnlKJicrADY
Purpose: product reveal (CGI feature film)
One-sentence point: the upgraded drone is taken apart feature by feature, one labelled component per shot.

Honesty note: this is a full CGI film (transparent fuselage, floating parts, light-streak void); it is not labelled as render, but nothing pretends to be real footage. The same animation is re-used inside the company's field-proof film (vector-real-missions).

## Structure (no voice)
- 0.0-4.8 title: product name, bold + light weight, on black; dark light-streaks pass behind. Silent until 3.95 s.
- 4.8-34.4 nine features, one per shot (2.5-5 s each): AI computer modules seen through a transparent skin, downward camera, antennas, GNSS receiver, swappable nose, battery, connector, 2-in-1 rotor kit, tether kit.
- 34.4-46.0 outro: the drone on its tether, then flying through light streaks (10.5 s, the longest).
- 46.0-50.0 company logo on black.

## Cut rhythm
- 12 shots in 50.0 s (adaptive; 2 extra cuts checked by eye). ASL 4.17 s, median 3.60 s. ASL per quarter 3.13 / 2.50 / 3.13 / 6.26 s.
- 0 % under 1 s, 75 % over 3 s. Cuts per 10 s: 2, 3, 3, 3. A steady one-feature-per-3.6 s grid. 64 % of cuts land on an audio onset (chance 28 %): cut to the beat.

## Typography
- Title: geometric sans, first word 800, second word 300, caps, ≈16 % H, centred-left. Closest free: Montserrat 800/300.
- Feature label: bold ≈4 % (sentence/title case) + one-line benefit ≈2.3 % regular under it, right-aligned at bottom-right (x ≈95 %, y ≈88 %), white, no box; held for the whole shot.

## Colour/grade
- White drone, black void, grey light streaks; blue/teal only on circuit boards. High contrast.

## Camera/shots
- Slow virtual orbits and push-ins; X-ray transparency to show inner parts; exploded views of the 2-in-1 kit.

## Transitions
- Hard cuts on the beat.

## Sound
- No voice. Silent title (0-3.95 s), music hit at 4.75 s on the first feature cut. Integrated -19.0 LUFS, LRA 9.0 LU, true peak -0.7 dBTP. Drop-out 43.6-45.2 before the logo hit (45.55 s). Ending: fade.

## What makes it premium
- One component, one label, one benefit per shot: easy to read as a datasheet.
- Transparency shows real internal parts (named by supplier where relevant) instead of abstract glows.
- Silence under the title makes the first hit land.

## Recipe (HTML/GSAP over renders or product macro)
- Title on black: Montserrat 800 + 300 caps 16vh, 4 s, no music.
- Per feature (3.5 s): one clip + `<div class=feat>`: `right:5vw; bottom:8vh; text-align:right`, name `700 4vh`, benefit `400 2.3vh`; `gsap.from(feat,{autoAlpha:0,y:10,duration:.3})` 0.2 s after the cut.
- Cut every 2 bars of a ≈120-130 BPM track; 1.5 s drop-out before the logo.
