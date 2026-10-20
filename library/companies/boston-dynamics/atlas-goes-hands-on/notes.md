# Atlas Goes Hands On  (Boston Dynamics, 2024-10-30, 2:53 incl. ~11 s black tail, 16:9, YouTube @BostonDynamics)
URL: https://www.youtube.com/watch?v=F_7IPm7f1vI
Purpose: robot demo (proof of autonomy, one-take)
One-sentence point: Atlas moves engine covers between shelving carts fully autonomously, in one uncut take, and you can see what it sees.

## Structure (cut list)
- 0.0-158.3: ONE continuous shot (158.3 s). A camera operator on a gimbal walks around the robot in a real lab (wide lens, lab clutter, cables, other people's desks). Atlas picks automotive engine covers from one cart and places them into slots of another cart, again and again, turning on the spot with its continuous-rotation joints.
  - Small white label "Fully Autonomous" bottom-right from 1 s to the end of the shot.
  - 64-73 s and 78-89 s (and later): picture-in-picture of the robot's own camera view (left side, ~33 % of frame width) with a blue/purple segmentation mask on the part it is grasping - perception made visible.
- 158.26-162: Boston Dynamics logo on a dark blue gradient (icon, then wordmark slides in).
- 162-172.6: black.

## Cut rhythm
- 2 shots in 172.6 s (1 cut). ASL 86.3 s. The demo itself is a single 158 s take.
- soft.py reports many "soft" candidates (4.7, 16.6, 18.0 s...) - these are camera moves; a 4 fps strip of 14.5-19 s shows a continuous move, no hidden cut.
- Speed looks real-time (no "1x"/"2x" label is shown; robot motion looks natural) - an assumption, not verified.

## Typography
- One label: "Fully Autonomous", white, semibold sans (closest free: Inter SemiBold), ~2 % frame height, bottom-right (x ~65-80 %, y ~86 %), no box, constant for the whole take.
- Logo end card: white icon + "BostonDynamics" wordmark on navy radial gradient, ~4 % height.

## Colour/grade
- Neutral, natural lab light (mixed daylight and fluorescent), no stylised grade. Robot silver/white against dark carts.

## Camera/shots
- Wide-angle gimbal, eye level to slightly low, operator follows the robot around the work cell; full body always in frame, often including the cart and the target slot so the task is readable.
- PiP inset = robot's head camera + live segmentation overlay. This is the "data on screen" of this film: no numbers, only the perception.

## Transitions
- None inside the demo. Hard cut to the logo.

## Sound
- No music detected (spectrogram 0-60 s: steady broadband room tone, short vertical transients = footsteps and part contacts, faint bands around 10-12 kHz during movement - probably motor/servo whine, a guess).
- Very quiet: integrated -29.9 LUFS, median -35.5 dBFS. Biggest transients at 8.0 s and 15.7 s (+19 dB) - contacts/steps.

## What makes it credible (the point of this film)
- One take, no cuts, for 2.5 minutes - you can't fake that in edit.
- "Fully Autonomous" stated once, small, all the time - not a claim card, a label.
- The robot's own view with the segmentation mask shows HOW it works.
- Raw lab sound, real messy background, people working behind.
- It is boring on purpose: repetitive, real work.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Shoot: one gimbal take, 24 mm-equivalent, follow the machine at 2-4 m, keep the whole machine + workpiece + target in frame. Don't cut. Use the real site sound (lavalier on the machine or a shotgun on the camera); no music or very low pads.
- Label: `<div class="tag">Fully autonomous</div>` `position:absolute; right:6vw; bottom:6vh; font: 600 2vh Inter; color:#fff; text-shadow:0 0 8px rgba(0,0,0,.5)`. Show at 1 s, never animate.
- PiP: `<video class="pip">` of the robot camera/sensor feed (or a screen recording of your perception UI), `left:0; top:15vh; width:33vw; border:none`, mask overlay as a semi-transparent `#5b4dff` layer (`opacity:.6`). Fade in 0.3 s when the interesting step starts, out after the step.
- If speed-up is needed, say so ("2x") in the same label style - BD-style credibility depends on not hiding edits.
- End: 3-4 s logo on a dark brand gradient.
