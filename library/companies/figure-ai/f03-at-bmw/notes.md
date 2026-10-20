# F.03 at BMW  (Figure, 2026-06-30, 1:00, 16:9, YouTube @figureai)
URL: https://www.youtube.com/watch?v=tv90GFM9RAo
Purpose: robot demo / customer deployment update (social-length)
One-sentence point: A fleet of Figure 03 robots is working in BMW's plant - walking the aisles, loading parts into carts, moving carts.

## Structure (cut list; no voice found, music only)
- 0.0-6.5 hook: one 6.5 s handheld wide of the real BMW plant (car bodies overhead, aisles, workers), then a fleet of F.03 robots standing in a row by green bins. Title "F.03 AT BMW" types on letter by letter (2-3 s), holds, deletes letter by letter (4-5 s).
- 6.5-23 the fleet at work: robots lined up (8-9 s), one robot walking away down the aisle (12-13 s), hand macro pushing a cart (15-16 s), a robot pulling a parts cart (17-19 s), a head close-up passing the camera (20 s).
- 23-40 the task: picking black plastic parts from green bins and placing them into cart slots - a mix of medium shots, over-the-shoulder, a high top-down wide-angle view looking down on the robot (31-32 s, likely a pole/crane cam - a guess), hand close-ups at the slots (33-39 s).
- 40-51 cart handling + fleet: pushing a full cart (40-46 s), 3-4 robots side by side (48-50 s).
- 51.5-54.6 hero: slow close-up of an F.03 head in the plant (3.2 s).
- 54.6-59.8 end: pixel "S" logo on black (5.1 s).

## Cut rhythm
- 33 shots in 60 s. ASL 1.81 s, median 1.38 s. ASL per quarter 2.13 / 1.36 / 1.36 / 2.13 s.
- Longest 6.51 s (opening), 5.13 s (logo), 3.17 s (head hero), 2.79 s. Shortest 0.88 s, 1.04 s. Only 3 % under 1 s, 9 % over 3 s - an even, calm pulse.
- Music grid: strong hits every 4.80 s (9.85, 19.45, 24.25, 29.05, 33.85, 38.65, 43.45, 48.25 s = one bar at ~100 BPM). Cuts mostly every ~1.2 s (2 beats), with a cut within ±0.3 s of most bar hits. Onset sync measured 9 % vs 6 % chance because the track has few transients between bar hits.

## Typography
- One title: "F.03 AT BMW", monospaced grotesk caps (same family as "FIGURE 02"; closest free: Space Mono), white, ~9 % frame height, top-left (x 2-40 %, y ~12-25 %), over the plant. Typewriter on (~6 letters/s), hold ~1 s, typewriter off.
- No other supers. Logo: white pixel "S" on black, ~8 % height, centre.

## Colour/grade
- Strongly desaturated, cool, slightly lifted blacks; the black robots read as graphic shapes. The only saturated colours left: green bins, yellow guard rails. Clean, documentary look.

## Camera/shots
- 100 % real plant footage (as far as visible): handheld/gimbal medium shots, a few top-down wide-angle shots, hand inserts at the slots, a fleet shot (several robots in one frame).
- No slow motion, no speed ramps visible; robots move at natural speed.
- Real background: workers, forklifts, car bodies on conveyors.

## Transitions
- Hard cuts on a 2-beat grid; the title is the only graphic.

## Sound
- Music only (no VO, no robot sound audible as a feature). Integrated -10.4 LUFS (loud, social level). Bar hits +17 to +27 dB rise every 4.8 s.

## What makes it credible
- Named real customer site in the title, real plant noise in the picture (workers, cars, forklifts).
- Fleet shots: several robots working at once suggest scale, not a single staged unit.
- Repetitive real task (bins -> cart) shown from many angles.
- Weakness vs. Boston Dynamics: fast cutting hides how long a task takes; no "autonomous" label in this cut.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Shoot: 25-35 real-site clips: 1 wide establishing (6 s), fleet/line-up, task from 4 angles (wide, medium, top-down, hand insert), one slow hero close-up.
- Grade: `filter: saturate(.35) contrast(1.05) brightness(1.02)`; let brand colours of the site stay (or grade them back in).
- Cut on a grid: `beat = 0.6 s` (100 BPM); shots of 2 beats (1.2 s), occasional 3 beats; land the section changes on the bar hit (every 8 beats = 4.8 s).
- Title typewriter: `font: 400 9vh 'Space Mono'; color:#fff; left:2vw; top:12vh`; characters on at 0.16 s each, hold 1 s, delete at 0.08 s each.
- End: 5 s logo on black.
