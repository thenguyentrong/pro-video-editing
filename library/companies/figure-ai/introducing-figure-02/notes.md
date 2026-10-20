# Introducing Figure 02  (Figure, 2024-08-06, 2:03, 16:9, YouTube @figureai)
URL: https://www.youtube.com/watch?v=0SRVJaOg9Co
Purpose: product reveal (spec film on real footage, ending in a real customer plant)
One-sentence point: Figure 02 is a new-generation humanoid with clear upgrades (hands, vision, compute, battery) and it already works autonomously in BMW's plant.

## Structure (cut list; no voice found, music + SFX)
- 0.0-4.3 hook: black; a silhouette fades up in the dark (2-4 s).
- 4.3-12.8 reveal: hard cut to a wide studio shot - the robot stands in front of a huge light wall in a dark hall (backlit silhouette, 4-9 s), then the light wall dims and the robot is lit from the front; "FIGURE 02" types on letter by letter over the left half (10-11.5 s).
- 12.8-55.5 ONE 42.7 s camera move: a motion-controlled orbit rising from the feet (concrete floor) past knees, hips, hands, head (verified continuous with a 3 fps strip; it looks like real footage of the real robot - motion-control rig, a guess). Spec labels type on during the move: "HAND DESIGN / 4th Generation / 16 Degrees of Freedom" (49-53 s, top-right), "SENSORS / AI Driven Vision / 6 Cameras" (54-58 s, top-right).
- 55.5-59.7 transition shot into the lab.
- 59.7-86.9 ONE 27.2 s tracking shot: Figure 02 walks through Figure's lab (carts, test cells, other robots working in the background). Labels bottom-left "INTELLIGENCE / 3x Compute / Onboard AI Inference" (63-69 s), "AI CAPABILITY / Onboard VLM / Speech-to-Speech Reasoning" (70-76 s), bottom-right "BATTERY / 2.25 KWh / +50% Runtime" (77-83 s).
- 86.9-112.5 customer proof: BMW plant. "TESTING / BMW Production Line / Plant Spartanburg - SC" (87-90 s); robot inserts sheet-metal parts into a fixture, green fixture lights (91-101 s); "MANIPULATION / 100% Autonomous / Neural Network Learned Placement" (93-98 s); "MANIPULATION / Self-correcting / Learned Behavior" (102-108 s) over a close-up where the hand re-adjusts a part.
- 112.5-122.6 end: wide shot of the BMW cell with the robot working; the pixel "S" logo builds over it (117-118 s), then the logo alone on a darkened frame.

## Cut rhythm
- 11 shots in 122.6 s. ASL 11.15 s, median 4.96 s. ASL per quarter 10.22 / 10.22 / 10.22 / 6.13 s.
- Longest 42.71 s (12.8, orbit), 27.23 s (59.7, lab walk), 10.09 s (end), 9.88 s (102.6, self-correcting close-up). Shortest 2.21 s (91.0).
- 0 % under 1 s, 91 % over 3 s. This is a "oner" film: few, long, continuous shots.
- ffmpeg scene detection and cuts2 agree (10 cuts); soft.py candidates are camera moves.

## Typography (data/specs on screen)
- Title: "FIGURE 02", monospaced grotesk caps (closest free: Space Mono / JetBrains Mono), white, ~20 % frame height, left side over the robot; types on one letter at a time (~6 letters per second).
- Spec label = 3 lines: category in tiny tracked caps (~1.5 % height, e.g. "HAND DESIGN"), then 2 lines in a medium grotesk (closest free: Inter Medium), ~3.2 % height each: line 1 = the headline value ("4th Generation", "3x Compute", "2.25 KWh"), line 2 = the meaning ("16 Degrees of Freedom", "+50% Runtime").
- Placement rotates by shot: top-right right-aligned (x ends 97 %), bottom-left left-aligned (x 4 %), bottom-right right-aligned. Colour adapts: black on the white backdrop, white on dark scenes.
- Animation: TYPEWRITER on (left to right, ~25-30 characters/s) and typewriter OFF (characters delete from the end) - visible as half-written labels at 49 s, 53 s, 58 s, 69 s, 83 s, 102 s.
- Hold ~4-6 s per label. No boxes, no lines, no icons.

## Colour/grade
- Desaturated, cool neutral: black robot, grey concrete, white walls; a near-monochrome look. Only colour: green fixture lights and yellow machinery in the BMW plant.

## Camera/shots
- Motion-control orbit and slow dolly/tracking moves; long continuous takes so the robot's movement is visibly real.
- Real locations: Figure's lab (with other robots and people working in the background) and the BMW production line.
- Inserts: macro hand and part placement at the fixture.
- No slow motion detected; no speed ramps.

## Transitions
- Hard cuts only; long takes do the transitions (camera move reveals the next "scene").

## Sound
- Music + SFX, no voice found. Integrated -13.3 LUFS; quiet start (first hit at 1.0 s is still -57 dBFS), loudest at 113.05 s (end, -10.5 dBFS). No drop-outs.

## What makes it credible
- Long continuous takes (42.7 s, 27.2 s): hard to fake in edit.
- Real lab with clutter, carts and other robots; then a named real customer site ("BMW Production Line, Plant Spartanburg - SC").
- Specific, checkable numbers ("16 Degrees of Freedom", "6 Cameras", "2.25 KWh", "3x Compute") + explicit autonomy claim ("100% Autonomous").
- Shows a correction ("Self-correcting / Learned Behavior") - not only perfect moves.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Shoot 2-3 long takes: (1) a slow rising orbit around the machine (gimbal on a crane or a slow walk-around, 30-45 s), (2) a 20-30 s tracking shot of the machine moving on the real site, (3) one close-up of the tool fixing/correcting a placement.
- Label component: `<div class="lbl"><small>PAYLOAD</small><b>25 kg</b><span>per lift</span></div>`; `small{font: 600 1.5vh Inter; letter-spacing:.12em; text-transform:uppercase}`, `b,span{display:block; font: 500 3.2vh Inter; line-height:1.2}`.
- Typewriter (seek-safe): split into `<i>` per character, `tl.from(chars,{autoAlpha:0, duration:.001, stagger:.035})` in; out `tl.to([...chars].reverse(),{autoAlpha:0,duration:.001,stagger:.025}, tOut)`.
- Rotate positions: top-right on light backgrounds (`color:#111`), bottom-left/right on dark (`color:#fff`).
- Title: `font: 400 20vh 'Space Mono'; letter-spacing:.02em`, typewriter at ~6 letters/s over the hero wide.
- End: the logo built from pixels over the real customer site wide.
