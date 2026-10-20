# Microfluidics: The key to next-generation medical technology  (Festo, 2026-04-17, 2:22, 16:9, YouTube @festo)
URL: https://www.youtube.com/watch?v=TflksmZ7Hh8
Purpose: application demo / product film (life-science automation demonstrator with diffusion-bonded manifolds), real footage, music only
One-sentence point: Festo's microfluidic manifolds, valves and sensors move and dose tiny amounts of liquid precisely - the base for next-generation lab and medical devices.

## Structure
- 0-7.8 title over a soft-focus wide of the demonstrator (five white modules on a white base): Festo blue line from the left edge into "Next-Gen Life Science Automation" + subline "with Diffusion Bonded Manifolds"; the image racks into focus.
- 7.8-27 module 1, "Capillary Forces in Small Channels": the three-panel wall with the centre lit (the other modules darkened), macro of liquid running through branched channels, a flower-shaped channel filling.
- 27-56 module 2, "High-Precision Dosing": cyan liquid filling a maze-like chip, a pattern of droplets, tubes and a valve stack.
- 56-85 module 3, "Microfluidic Droplets": pipetting heads over a blue well plate, a gold multi-channel dosing head, a touch display with the process view.
- 85-114 module 4, "Manifolds with Integrated Sensors": sensor graphics on the device screen (pressure difference, colour-sensor bar chart, "Bubble Sensor: No bubble detected"), yellow/cyan fluid in long serpentine channels.
- 114-137 module 5, "Manifolds with Integrated Valves": the FESTO logo appears as channels in a chip and fills with cyan liquid; macro of valves and channels.
- 137-142.4 end: blue line + "Automation for a world in motion." then FESTO logo, on white.

## Cut rhythm
- 40 shots in 142.4 s (the other detector finds 57: several soft rack-focus and light changes), ASL 3.56 s, median 2.88 s, 5 % < 1 s, 50 % > 3 s, 16.9 shots/min. ASL per quarter 5.1 / 2.1 / 2.7 / 5.9 s.
- Longest 14.7 s (127.7 s, valve macro to the end), 11.2 s (93.2 s, sensor screen), 7.9 s. Shortest 0.88 s.
- Each module starts with the same lit-panel wide (≈2-3 s), then 3-5 macros of 2-4 s; 3-5 cuts per 10 s in the middle, 0-1 at the start and end.

## Typography
- Festo face (closest free: Fira Sans, which shares its FF Meta roots), semibold, title case, white.
- Title: ≈6 % H, centred, with a Festo-blue (#0091DC) 2 px line from the left frame edge to the first letter; subline semibold ≈3 %, right-aligned under it.
- Module label: blue line ≈7 % W + two-line label ≈4.5 % H, top-right next to the lit module (x ≈64-90 %, y ≈15-25 %); in with the line drawing from left (≈0.4 s), hold ≈3 s.
- Device UI: real screen graphics (bar chart, sensor status), filmed in macro.
- End line: same blue line + "Automation for a world in motion." ≈2 % H, then FESTO logo blue ≈3 % H centred on white.

## Colour/grade
- Cool, desaturated grey-white with crushed contrast; the only strong colour is the cyan/blue liquid (and one gold dosing head, one yellow fluid). Clean white product.

## Camera/shots
- Real product in a studio: locked wide of the whole demonstrator with one module spot-lit, extreme macros on channels with shallow depth of field and rack focus, slow slider moves along tubes and valves, top shots of the well plate.

## Transitions
- Hard cuts and in-shot rack focus; light changes (modules lighting up) act as transitions; fade to white at the end.

## Sound
- Music only (no speech detected), calm electronic with a steady pulse. Integrated -14.0 LUFS, LRA 5.5 LU, true peak -3.0 dBTP. No drop-outs. Rises +17-20 dB every ≈1.5-3 s at 57-69 s (cuts on the beat: 54 % of cuts on onsets vs 36 % chance).

## What makes it premium / credible
- Real fluid in real channels - the macro shows the function, not a render.
- One spot-lit module per chapter gives a clear map of the demonstrator.
- Brand line motif links title, labels and end card.
- Weak: no numbers (volume, precision) although "high-precision dosing" is the claim.

## Recipe (real footage + HTML/GSAP)
- Line + title: `<i class="ln"></i><h1>Next-Gen Life Science Automation</h1>`, `.ln{position:absolute;left:0;top:44vh;height:2px;width:15vw;background:#0091DC;transform-origin:left}`; `gsap.from('.ln',{scaleX:0,duration:.5})` then title fade 0.4 s; `h1{font:600 6vh 'Fira Sans'}`.
- Module label: line 7vw + `font:600 4.5vh/1.1 'Fira Sans'`, top-right; same line-draw in.
- Shoot: one lit wide per module (dim the others), then 3-5 macros at 2-4 s with rack focus; coloured liquid as the only accent.
- Add one number per module (e.g. "0.5 µl ±2 %") if you have it.
