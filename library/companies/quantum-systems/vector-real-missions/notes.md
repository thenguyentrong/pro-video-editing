# Vector: Real Missions. Real Results.  (Quantum Systems, 2025-07-25, 3:50, 16:9, YouTube @QuantumSystems)
URL: https://www.youtube.com/watch?v=ysPNZAD6Cho
Purpose: field-proof compilation (operational footage + product spec + field tests)
One-sentence point: the drone's upgrades are presented as lessons from real front-line use, proven with operational sensor footage, then with field tests.

Content note: most of the middle is real military ISR and strike footage from an active war (thermal and daylight sensor views, target markers, damage assessment overlays). Described here only for its editing craft.

## Structure (no voice, captions only)
- 0.0-27.6 timeline on black: three dated entries along a thin vertical line (two past dates, then "today" with a deployment count), then two short text cards (built in battle; lessons shaped every upgrade). Counted as one shot.
- 27.6-72.5 product: the CGI feature sequence from the Vector AI film (title, nine labelled components).
- 72.5-77.5 section card on black (closing the kill chain).
- 77.5-93.5 operator UI: a ground-station view with a target marker, caption "target hand-off" type label + one line of explanation; the result on the same screen.
- 93.5-121.5 thermal sensor-to-shooter footage, captioned.
- 121.5-136.6 ISR footage of a logistics site, captioned.
- 136.6-153.8 daylight strike footage with target box, then a damage-assessment overlay (red polygon + in-source stamp in the local language).
- 153.8-168.2 two section cards on black (system integration; additional capabilities) joined by fades, a rugged tablet UI.
- 168.2-217 field tests (real): GPS-denied vertical landing, flights in grey sky, soldiers assembling the modular airframe, a quarry site, a recovery at sunset - each with a caption.
- 217-226 closing text on black (two lines, one bold phrase each); 226-230 logo.

## Cut rhythm
- 36 shots in 230.2 s (scene detector + 10 cuts added and 1 removed by eye; zooms and smoke inside sensor footage are not cuts). ASL 6.39 s, median 3.60 s. ASL per quarter 5.75 / 7.19 / 4.11 / 8.22 s.
- Inflated by text sections counted as single shots: 27.6 s (opening timeline), 36.6 s (153.8-190.3: cards + field test joined by fades), 26.3 s (end text + logo). Without them the sensor footage runs in 3-15 s takes.
- Cuts per 10 s mostly 0-3; peak 6 at 120-130 s.

## Typography
- Timeline and cards: geometric sans, date bold ≈3.5 % + one regular line ≈2 %, left-aligned at x ≈2 % beside a 1 px vertical line with dots; cards centred-left, one or two words bold inside a regular sentence. Closest free: Montserrat 700/400.
- Captions on footage: bold title-case label ≈3.5 % + regular explanation ≈2 % (1-2 lines), bottom-left, white, no box.
- Product bug: a small drone-silhouette icon top-right (≈3 %) on every operational shot.
- In-source overlays (target boxes, coordinates, stamps) are left untouched.

## Colour/grade
- Operational footage keeps its native look (thermal grey, washed daylight, UI blue). Field tests: natural colour, grey sky, warm sunset. Cards on pure black.

## Camera/shots
- Mostly not filmed by the brand: drone sensor feeds and ground-station screens. Field tests: tripod and drone shots, handheld close-ups of assembly.

## Transitions
- Hard cuts in footage; fades to and from black cards (soft transitions at 158.5, 163.4, 168.2, 176.6, 189.4 s).

## Sound
- No voice. Music bed only; hits recur every ≈22 s (11, 33, 55 ... 150 s), i.e. a looped track. Integrated -15.6 LUFS, LRA 4.5 LU, true peak -1.4 dBTP. No drop-outs. Ending: fade.

## What makes it premium (and credible)
- Proof by native sensor footage with dates and outcomes captioned, not re-shot.
- A timeline with real dates and a deployment count opens the film: claims are anchored in time.
- Every caption names the capability and explains it in one line.
- Weak spots: very long black text sections, a looped music bed, and CGI re-used from another film.

## Recipe (real footage + HTML/GSAP)
- Timeline: `border-left:1px solid #fff` + 8 px dots; each entry Montserrat 700 3.5vh date + 400 2vh line; reveal one entry every 2.5 s.
- Caption on proof footage: label 700 3.5vh + line 400 2vh at `left:4vw; bottom:7vh`; hold the whole take (5-15 s).
- Corner product bug 3vh at `top:4vh; right:3vw`, opacity .8.
- Keep the source overlays; never redraw UI.
- Use fades only for card changes; hard cuts inside footage.
