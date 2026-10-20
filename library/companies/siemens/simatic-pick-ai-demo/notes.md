# SIMATIC Robotic Pick-AI: Object Recognition and Demo  (Siemens, 2026-03-05, 2:04, 16:9, YouTube @Siemens)
URL: https://www.youtube.com/watch?v=wMv-s2ooJJk
Purpose: robot demo / explainer (customer-style dialogue in Siemens' own logistics plant)
One-sentence point: Pick-AI lets a standard cobot pick unknown objects from a box - "can it pick my phone?" - and the software UI shows how.

## Structure (cut list + English captions)
- 0.0-3 hook: animated panel/split-screen intro - three vertical panels slide in (robot tool macro left, a woman with a tablet in the middle, cell right) (1-2 s), resolving into a two-shot.
- 3-18.5 setup: two-shot in the plant (visitor in a white lab coat, Siemens engineer in a blue coat), cell wide with the cobot and HMIs (6.5-10.7 s). Lower third "Julian Brau / Project Manager Logistic Automation, Digital Industries, Motion Control, Siemens AG" (10.7-17 s). "Our main challenge... products we receive from external partners. We have no information about their dimensions and weights..."
- 18.5-41 problem -> solution: intercut singles/two-shots; "That's exactly where Pick AI comes in, enabling us to automatically pick unknown objects."
- 41-49.5 the test: "What about my phone?" "We can put it to a test." She drops her phone into the box with the cardboard parts (46-48 s).
- 49.5-62.4 proof: monitor with the Pick-AI UI - camera image of the box with blue/red bounding frames, the phone highlighted, a green "Pick calculation status" panel with a check mark (49.5-53.5 s); the cobot picks (53.5-58 s, locked-off wide, slow); hand; full-screen UI "Ok. Pick point calculation is successful." (59-62 s). VO explains: 3D camera -> shape, position, orientation -> optimal gripping point -> robot.
- 62.4-110 the rest of the process: engineer explains singles; robot b-roll of picking, turning 360 degrees at the scanner, dropping into the box (75-78 s, 96-109 s).
- 110.4-114.8 end of story: "Lara, your phone's still in one piece?" smiles, a third colleague joins.
- 114.8-124.2: SIEMENS wordmark on dark navy (fade in/out), then YouTube end screen ("Subscribe", "See more").

## Cut rhythm
- 29 shots in 124 s. ASL 4.28 s, median 3.96 s. ASL per quarter 4.44 / 2.82 / 3.88 / 5.18 s.
- Longest 9.44 s (logo/end screen), 7.88 s (10.68, the lower-third single), 7.8 s, 7.24 s (robot b-roll). Shortest 1.0 s (58.12, hand insert), 1.2 s.
- 0 % under 1 s, 72 % over 3 s. ffmpeg (0.2-0.3) and cuts2 agree on all cuts.

## Typography (data on screen)
- Lower third: Siemens Sans (closest free: Inter / Source Sans 3), name Bold ~3 % height + role Regular ~2.5 %, white on a dark navy box (#000028-ish, Siemens "deep blue"), right side over the speaker's chest (x 72-97 %, y 63-85 %). The box wipes in from the left (10.7 s: empty box first, then text), holds ~6 s, fades.
- No other supers; the data is the product UI itself, filmed on a monitor and also shown full-screen as a clean screen recording: camera view with bounding frames, status tiles ("Camera Connected", "PLC Connected"), green success panel with check mark and message.
- End: white SIEMENS wordmark centred on navy, fade in/out.

## Colour/grade
- Clean, bright, slightly cool industrial white; blue workwear, Siemens petrol/green accents in the UI. Natural skin tones; soft contrast.

## Camera/shots
- Two-camera interview coverage (wide two-shot + over-the-shoulder singles) on location in the real plant.
- Robot b-roll: locked-off medium-wide shots of the full cell (robot, box, scanner), real speed, 3-8 s each.
- Screen: monitor at an angle with shallow depth of field (49 s), then the clean UI full frame (59-62 s).

## Transitions
- Opening split-panel slide; then hard cuts; fade to the logo.

## Sound
- Dialogue (English, scripted but natural) over a quiet music bed. Integrated -22.6 LUFS (quiet), loudest at the logo sting (115.95 s, +41.7 dB rise).

## What makes it credible
- The "drop your own phone in" test: an unknown object chosen on camera.
- The UI shows the AI's decision (bounding frames + "Pick point calculation is successful") right before the robot moves.
- Real plant, real people with full titles, real-speed robot shots, and the full process (pick -> scan -> 360 turn -> box / return) shown.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Story: visitor asks, engineer answers, visitor brings a "test object" (for construction: a random brick/offcut/a dirty pallet), machine handles it, UI confirms.
- Lower third: `.lt{position:absolute;right:3vw;bottom:15vh;background:#000028;color:#fff;padding:1.6vh 1.6vw}`; `b{font:700 3vh Inter}`, `span{font:400 2.5vh Inter;display:block}`; `tl.from(lt,{clipPath:'inset(0 100% 0 0)',duration:.4,ease:'power2.out'}).from(lt.children,{autoAlpha:0,duration:.25,stagger:.08})`, hold 6 s.
- UI proof: record your real software (OBS) and cut in full-screen for 3-4 s right before the machine acts; add a green check panel if the UI has one - don't fake it.
- Robot shots: locked-off wide of the whole cell, 4-8 s, real speed.
- Opening: 3 vertical panels `width:33.3vw` sliding in with `stagger:.12`, then expanding to the two-shot.
