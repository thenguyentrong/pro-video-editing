# Panel Bending Machine TruBend Center 7020 | Intelligent Automation for the Smart Factory  (TRUMPF, 2026-01-26, 3:14, 9:16 vertical, YouTube @TRUMPFtube)
URL: https://www.youtube.com/watch?v=KR6EyC14Zgc
Purpose: application demo (a vertical, phone-style one-take of an automated panel-bending cell; Spanish captions, likely from a national TRUMPF team)
One-sentence point: The TruBend Center 7020 with its loading robot bends complex parts on its own - watch one full cycle.

## Structure
- 0-11.3 HMI screens: camera image of the bending tools and the control software (two screens stacked in the vertical frame).
- 11.3-24.8 wide of the robot track with a large sheet being moved.
- 24.8-≈187.5 one uncut locked take (≈163 s): the panel bender with its loading table and a pallet in front; the yellow robot arm enters from the left at ≈125 s, picks the bent part and stacks it on the pallet; two small Spanish captions appear at ≈96 s ("total flexibility for complex geometries") and ≈184 s ("automation makes the future").
- ≈187.5-194.5 TRUMPF logo on white (≈7 s).

## Cut rhythm
- 3 detected shots + the logo card: ASL by detector 64.8 s; real structure ≈11 s + ≈13.5 s + ≈163 s + ≈7 s. Shots per minute ≈1.2.
- Nothing is cut out of the cycle: loading, bending (≈100 s with little visible motion) and stacking all stay in.

## Typography
- Only two captions: white regular humanist sans (closest free: Noto Sans), ≈2.5 % of the frame height, centred, lower third (y ≈70 %), two short lines, no box; ≈3-4 s each. TRUMPF logo blue on white at the end.

## Colour/grade
- Ungraded factory light, slightly cool; yellow robot, light-grey machine, green/brown pallet.

## Camera/shots
- Vertical phone or vertical gimbal, locked on a tripod at ≈1.5 m height, three-quarter view of the cell that shows machine + table + pallet in one frame. Real time.

## Transitions
- Hard cuts; fade to the white logo card.

## Sound
- Music only (no speech detected), one loud steady track. Integrated -11.3 LUFS, LRA 3.6 LU, true peak +0.1 dBTP (clips). No drop-outs, no silence. Machine sound is not audible.

## What makes it credible
- One uncut real-time take of the full cycle: nothing hidden.
- Vertical framing fits a tall machine and phone viewing.
- Weak: ≈100 s of slow bending with music only - no cycle time, no part count, no labels; the machine sound that would prove real time is replaced by music.

## Recipe (real footage + HTML/GSAP)
- Shoot 9:16 on a tripod, frame machine + loading table + output pallet together; record one full cycle plus 10 s before and after.
- Open with 10 s of the HMI (screen recording is cleaner than filming the screen).
- Add what it lacks: a running cycle timer top-right (`font:600 3vh Inter; color:#fff`, `tl.to(timer,{textContent:163, duration:163, snap:{textContent:1}, ease:'none'})`), a "Real time" label, and the machine's own sound under the music at -12 dB relative.
