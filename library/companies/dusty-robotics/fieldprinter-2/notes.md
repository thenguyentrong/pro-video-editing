# Dusty Robotics FieldPrinter 2: Smarter, Faster. More Powerful.  (Dusty Robotics, 2024-01-23, 1:12, 16:9, YouTube @DustyRobotics)
URL: https://www.youtube.com/watch?v=xIb_yiOHjWY
Purpose: product launch film (second-generation layout-printing robot)
One-sentence point: The new FieldPrinter drives itself across a raw concrete deck and prints the full floor layout (lines, text, curves) through dirt, puddles and clutter at 1/16" accuracy.

## Structure (music only, no voice-over)
- 0.0-1.5 (0-2 %) logo on white (orange icon + grey wordmark), centred.
- 1.5-6.5 (2-9 %) stutter intro: five ~1.0 s shots of the robot on the deck, each followed by 2-3 black frames (black dips at 1.5, 2.5, 3.5, 4.5, 5.5, 6.5 s) - a "heartbeat" reveal on the music.
- 6.5-9.4 (9-13 %) robot drives through the frame; behind it the product name "FieldPrinter 2" stands on the floor plane in orange (the robot wipes past and reveals it).
- 9.4-13.5 (13-19 %) top-down close-up of the robot (status LEDs, QR plate) + low wide; tagline caption.
- 13.5-48.2 (19-67 %) capability blocks, one caption per claim, each held over 1-2 shots (4-6 s): print complete layout / rough surfaces / dirt and puddles / (free driving 23.5-30.9) / obstacles and clutter / print text / print curves.
- 48.2-57.6 (67-80 %) no captions: low tracking shots, a red pipe-stand obstacle, a worker in boots and gloves swaps the battery (only human in the film besides a hi-vis vest at 5 s).
- 57.6-61.5 (80-86 %) spec claim "Guarantee 1/16" accuracy".
- 61.5-70.0 (86-98 %) finale: robot under timber shoring, white haze transition (64.3 s), low wide, robot drives past the floating orange name again (occlusion), black.
- 70.0-71.5 logo on white.

## Cut rhythm
- 31 shots in 71.6 s (26 detected + 4 verified by eye: 9.4 hard cut missed under the title, 41.46 and 53.51 found by the adaptive detector, 64.3 white-haze transition). ASL 2.31 s, median 1.96 s, 9.7 % under 1 s.
- ASL per quarter 1.79 / 2.24 / 2.24 / 2.24 s: fastest in the stutter intro, then a steady ~2 s pulse.
- Longest 6.05 s (print complete layout, 13.5 s), 5.77 s (finale wide), 4.80 s (curves). Shortest real shots 0.96 s (intro stutter).
- Cuts per 10 s: 6 / 4 / 3 / 5 / 3 / 5 / 2 / 2 - even.

## Typography
- Captions: bold grotesk (Helvetica Neue Bold / SF look; free: Inter Bold 700), white, sentence case, no box, soft shadow; cap height ≈5.4 % H, centred at ≈86 % from top. 3-5 words per caption ("Print curves with precision"). Hard on/off with the cut; hold 4-6 s across 1-2 shots.
- Product name: same face in brand orange (≈#F07C1E), ≈7 % H, placed in 3D on the floor plane mid-frame, so the robot drives in front of it (occlusion reveal, used at 7-9 s and 67-69 s).
- Logo cards: orange icon + grey wordmark on pure white, ≈10 % H.

## Colour/grade
- Neutral-cool concrete greys, blown window light, slight warm lift on timber; the robot's orange shell is the only saturated colour (plus yellow pipe protectors, red stands). Clean, low-contrast commercial grade. No grain, no letterbox.

## Camera/shots
- Almost all ground-level: lens 5-30 cm above the slab, wide lens, robot at eye level of the camera (makes a 40 cm robot look heroic). Gimbal dolly/tracking alongside, low push-ins, a few top-down overheads on printed lines and text.
- Real site: unfinished concrete deck, shoring posts, pipes, puddles, timber - real dirt. Printed text close-up ("626 ELECTRIC ROOM", door/ceiling notes) proves the output.
- No drone, no UI/BIM screen, no data card besides the accuracy caption, no timelapse. Real footage only; speed looks real-time (no label).

## Transitions
- Hard cuts; intro uses 2-3-frame black dips between 1 s shots; one white-haze (dust/fog) transition at 64.3 s; logo cards cut in hard.

## Sound
- Upbeat electronic/drum track, 2 s phrase grid (hits at 8.1, 10.1, 12.1 ... s; ≈120 BPM, a bar per 2 s). Caption changes land on bar hits. No VO, no robot SFX audible.
- Integrated -19.6 LUFS, LRA 7.7 LU, true peak -6.4 dBTP. Drop-out 65.65-66.1 s (0.45 s) right before the last reveal; silence 69.9-71.6 s under the end logo. Biggest hits +39 dB at 12.1 s and +38 dB at 8.1 s (start of the tagline section). Cut-to-onset sync 54 % vs 51 % chance (cuts follow bars, not every beat).

## What makes it premium
- Camera at robot height: a small floor robot gets a car-commercial hero treatment.
- One claim per caption, 3-5 words, each proved by the shot under it (puddle shot under "puddles", printed text under "text").
- Real dirty site kept dirty; the clean orange robot pops against grey.
- Name placed in 3D space and occluded by the robot: a cheap but strong "it's really there" trick.

## Recipe (real footage + HTML/GSAP)
- Shoot on a gimbal with the lens 10-20 cm above the slab, 24 mm equivalent, 24p; tracking shots 2-6 s; 4 top-down shots of printed lines/text.
- Intro stutter: 5 clips of 1.0 s, each followed by `tl.set(black,{opacity:1})` for 0.1 s.
- Captions: `font:700 5.4vh Inter; color:#fff; text-shadow:0 2px 8px rgba(0,0,0,.4); bottom:11vh; text-align:center`; `tl.set` on at the cut, off at the next claim; 4-6 s each, on the bar hit.
- Floor title: rotoscoped matte of the robot (or simply cut the title layer under a foreground clip) - `transform: perspective(800px) rotateX(55deg)`, colour `#F07C1E`, 7vh, fade-free.
- Music 120 BPM, cut every bar (2 s), 0.45 s silence before the final reveal, logo on white in silence.
