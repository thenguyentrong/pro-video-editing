# Tesla Bot Update | Sort & Stretch  (Tesla, 2023-09-25, 1:18, 16:9, YouTube @tesla)
URL: https://www.youtube.com/watch?v=D2vj0WcvH5c
Purpose: robot demo / progress update (one task explained step by step)
One-sentence point: Optimus calibrates itself with vision, then sorts blocks by colour autonomously - even when a person messes with them - and ends with a yoga stretch.

## Structure (cut list + on-screen captions; no voice, music only)
- 0.0-7.25 "Optimus is now capable of self-calibrating its arms and legs" - wide, robot in a small studio set (plants, Cybertruck poster) moving its arms.
- 7.25-15.0 "Using only vision and joint position encoders, it can precisely locate its limbs in space" - the robot's own camera view in a rounded inset on black; a cyan 3D model of its arm is overlaid and snaps onto the real arm (11-14 s).
- 15.0-20.5 "Accurately calibrated, Optimus learns various tasks more efficiently" - robot at a table with blue and yellow trays; label "1.5x Speed" top-right (15-17 s).
- 20.5-28.1 "Its neural net runs entirely on-board, using only vision" - robot head-camera view (rounded inset on black) of its hands sorting blocks.
- 28.1-33.7 "For example, it can sort these blocks by color fully autonomously".
- 33.7-44.9 "And it does so while dealing with the dynamic reality of our world" - an engineer keeps moving blocks and trays; robot adapts (11.25 s shot).
- 44.9-52.4 "Optimus also demonstrates autonomous corrective action capabilities" - a picture-in-picture (top-right) zooms in on a block that fell over and is set upright (48-51 s).
- 52.4-60.0 "It can be trained to conduct new tasks, such as un-sorting".
- 60.0-73.4 "And after a long day of work, time to stretch!" - yoga poses on one leg (60-65 s), "Namaste" (69-72 s).
- 73.4-77.8 Tesla "T" logo on black.

## Cut rhythm
- 11 shots in 77.8 s. ASL 7.07 s, median 7.50 s. ASL per quarter 6.48 / 4.86 / 6.48 / 4.86 s.
- Longest 11.25 s (33.67, human interference), 7.79 s, 7.62 s, 7.54 s. Shortest 4.38 s (logo), 5.50 s. 100 % of shots over 3 s.
- One caption = one shot. Music bars are 3.75 s long (~128 BPM; hits at 32.1, 35.85, 39.6, 43.35 ... s); most cuts are 2 bars (7.5 s) apart - shots are phrase-length.

## Typography (data on screen)
- Subtitle-style captions: Tesla's geometric sans (Gotham-like; closest free: Montserrat), white, sentence case, one line, ~1.8 % frame height, centred at the bottom (y ~93 %) on a soft dark gradient band. Hard on with the shot, off with the cut.
- Speed label "1.5x Speed": small (~1.5 %), top-right, white.
- Data/perception: robot camera views in rounded-corner insets on black (~75 % width, centred); cyan 3D arm model overlay aligned to the real arm; PiP close-up (top-right, ~25 % width) to show a detail.

## Colour/grade
- Bright, clean, neutral; set is a living-room-like studio with plants; strong colour only from the blue/yellow trays and green blocks; cyan for the virtual overlay.

## Camera/shots
- Locked-off medium-wide shots, robot full body + the whole table; robot's own POV; one PiP zoom. Real footage (a real person interferes in shot). One shot is labelled 1.5x speed; the others carry no label (assumed real-time - not verified).

## Transitions
- Hard cuts. PiP grows in (48 s, a quick scale/fade).

## Sound
- Upbeat electronic track at ~128 BPM, no VO, no robot sound. Integrated -11.2 LUFS; loudest 53.55 s.

## What makes it credible
- Long locked-off shots (median 7.5 s) of a complete task, with a human disturbing it - shows robustness, not one lucky take.
- The robot's own camera view + the aligned virtual arm explains HOW it knows where its limbs are.
- Speed-up is labelled ("1.5x Speed").
- Plain, factual captions; one claim per shot.
- The yoga ending adds personality and shows balance (a capability) at the same time.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Shots: 6-9 locked-off medium-wides of 5-11 s, each showing one complete sub-task; one shot where a person disturbs the task.
- Caption bar: `.cap{position:absolute;left:0;right:0;bottom:0;height:14vh;background:linear-gradient(transparent,rgba(0,0,0,.45));display:flex;align-items:flex-end;justify-content:center;padding-bottom:3vh;font:400 1.9vh Montserrat;color:#fff}`; swap text with `tl.set(cap,{textContent:'...'}, shotStart)`.
- POV inset: robot/machine camera footage in `border-radius:2.5vh; width:75vw` centred on black; virtual model overlay as a transparent PNG/WebM in cyan `#2de2e6` with `mix-blend-mode:screen`, `gsap.from(model,{x:-30,rotation:-4,duration:.8,ease:'power2.out'})` to "snap" onto the real part.
- PiP detail: `gsap.fromTo(pip,{scale:.6,autoAlpha:0},{scale:1,autoAlpha:1,duration:.35,ease:'back.out(1.4)',transformOrigin:'top right'})`.
- Cut every 2 musical bars (choose a 120-128 BPM track: 2 bars = 7.5-8 s).
