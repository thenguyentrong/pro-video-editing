# Atlas | Product Features  (Boston Dynamics, 2026-01-05, 1:43 incl. ~10 s black tail, 16:9, YouTube @BostonDynamics)
URL: https://www.youtube.com/watch?v=rrUHZKlrxms
Purpose: product reveal / spec film (product Atlas, CES 2026 launch)
One-sentence point: The product Atlas is an enterprise humanoid with clear numbers - 1.9 m, 90 kg, 56 DoF, 2.3 m reach, 50/30 kg payload, 4 h runtime, swappable battery, human detection.

Honesty note: everything looks like a 3D render (clean CGI factory, CGI worker, perfect lighting). This is a spec animation, not a real-robot demo.

## Structure (cut list; no voice-over)
- 0.0-6 hook: macro parts in the dark - blue joint shells, a finger, the head ring (0-6 s), "Boston Dynamics" debossed on the chest.
- 6.4-8.8: 0.3 s digital silence, then the Atlas logo builds on black: yellow ring icon (6-7 s) -> "Atlas" wordmark (8 s).
- 9-14: logo stays while the scene fades in - Atlas walks in a car-body factory (logo over footage, 9 s), wide top shot of a cell.
- 15-25 specs 1: "[height] 1.9 m | 6.2 ft" + "[weight] 90 kg | 198 lbs" (15-20 s), "[degrees of freedom] 56" (20-22 s), "[reach] 2.3 m | 7.5 ft" with a yellow vertical dimension line from floor to hand (22-25 s).
- 25-39 work + specs 2: Atlas handles car body panels; "[weight capacity - instant] 50 kg | 110 lbs" with a yellow leader line from the part to the label (33-35.5 s); "[weight capacity - sustained] 30 kg | 66 lbs" (36-39 s).
- 39-60 capabilities: "continuous joint rotation" (word-by-word build, 40-42 s), "safe operation with human detection" with yellow concentric floor rings around the robot and a worker walking in (43-47 s), "[runtime] 4 hours" (48-49 s), "self-swappable battery for continuous operation" (50-56 s), tote picking (57-60 s).
- 61-74 design principles on black: arm/hand/head parts floating, "designed for reliability / repairability / upgradability" (61-68 s), head ring lights up (71 s).
- 75-87 finale: loading dock with truck and Stretch, Spot walking, Atlas carrying parts; logo builds again over the scene (82-86 s), then on black (87-88 s).
- 89-92: Boston Dynamics logo on black, small. 93-103: black.

## Cut rhythm
- 27 shots in 103 s. ASL 3.83 s, median 2.59 s. ASL per quarter 3.23 / 2.58 / 2.87 / 8.61 s (the last quarter is logo + black).
- Longest 19.77 s (83.58, logo + black tail), 6.59, 6.51, 6.42 s. Shortest 1.29 s (25.78). 0 % under 1 s, 44 % over 3 s.
- Each spec gets its own shot of 2.5-6.5 s; the cut comes after the number has been read.

## Typography (data/specs on screen)
- Geometric sans (closest free: Montserrat), white, lower case for words, no boxes.
- Spec block = 3 parts: `[label]` in brackets, Regular, ~2.8 % frame height; value Bold, cap height ~6.5 %; then a thin vertical divider and the imperial value in Regular ~3.5 %. Example: "[height] / 1.9 m | 6.2 ft".
- Placement: in the empty side of the frame next to the robot (x 30-80 %), stacked when there are two values. Hold 3-5 s.
- Graphics in brand yellow (~#F2D100): 1-2 px leader line from the object to the label with a small circle at the object end; vertical dimension line with two circle endpoints for reach; flat concentric rings on the floor (perspective-matched) for human detection. All tracked to the 3D scene.
- Word callouts ("safe operation with human detection"): Bold, lower case, ~6 % cap height, 1-2 lines, left-aligned, bottom-left/centre; build word by word (40-41 s).
- "designed for" small Regular (~3 %) above a big Bold word (~6 %), on black next to floating parts.
- Logo: yellow ring icon draws first, then "Atlas" wordmark slides out of it.

## Colour/grade
- Cool grey-blue industrial palette, dark backgrounds, robot in dark blue + black; the only accent colour is brand yellow (head ring, lines, rings). Product macro on pure black.

## Camera/shots
- CGI camera: slow dolly/orbit around the robot, top-down plan views, macro of parts on black. Medium-wide shots so the full body and its task are visible.
- No slow motion; robot motions look physically plausible (no flips) - "enterprise" not "stunt".

## Transitions
- Hard cuts and fades to/from black for the logo sections; logo composited over footage (9 s, 83 s).

## Sound
- No VO. Minimal electronic score with gated, staccato hits: 29 micro-silences (0.15-0.8 s, down to digital silence -120 dBFS) right before each spec or callout appears, then a hit (+29 to +103 dB rise, e.g. 34.6 s, 73.4 s, 75.75 s). The "click on" of each number is audible.
- Integrated -24.4 LUFS (quiet master).

## What makes it premium
- Specs are designed like a datasheet: bracketed label, big metric value, small imperial value.
- One accent colour for all data graphics, matched in 3D to the scene (lines touch the real object).
- Each number gets its own shot and its own sound hit.
- Calm camera; the robot does plausible industrial work, not tricks.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Spec block HTML: `<div class="spec"><span class="lbl">[payload]</span><span class="val">25 kg</span><i></i><span class="alt">55 lbs</span></div>`; `font-family: Montserrat`; `.lbl{font-size:2.8vh;font-weight:400}`, `.val{font-size:8.5vh;font-weight:700}`, `i{display:inline-block;width:1px;height:5vh;background:#fff;margin:0 1.2vh}`, `.alt{font-size:3.5vh}`.
- Reveal: `tl.from(spec.lbl,{autoAlpha:0,y:8,duration:.25}).from(spec.val,{autoAlpha:0,y:12,duration:.3,ease:'power3.out'},'<.08').from(spec.i,{scaleY:0,duration:.2},'<.1').from(spec.alt,{autoAlpha:0,duration:.2},'<.05')`; play a short click SFX after a 0.2-0.4 s music cut.
- Leader line on real footage: track the object point (manual keyframes every 4-6 frames) and draw an SVG `<line>` + `<circle r=4>` in `#F2D100`, `stroke-width:2`; animate `stroke-dashoffset` 0.4 s.
- Dimension line: vertical SVG line with circle endpoints from ground contact to tool tip; grow with `scaleY` from the bottom, 0.5 s.
- Floor rings: 2-3 SVG ellipses with `transform: perspective(800px) rotateX(70deg)` placed under the machine, opacity .6, slow pulse.
- For a construction robot on a real site: shoot locked-off medium-wide shots (full machine + task visible), 4-6 s each, and put one spec per shot.
