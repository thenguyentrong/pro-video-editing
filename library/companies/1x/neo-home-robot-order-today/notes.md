# NEO The Home Robot | Order Today  (1X, 2025-10-28, 9:53, 16:9, YouTube @1X)
URL: https://www.youtube.com/watch?v=LTYMWadOW7c
Purpose: launch film (keynote-style product launch with pre-order price)
One-sentence point: NEO is a soft, quiet home humanoid you can order now; it does chores (partly with a remote human expert), keeps you company, and is learning to work on its own.

## Structure (measured cut list + 2 s review sheets)
- 0.0-6.8 cold open: founder and NEO side by side in a warm wood studio, one 6.8 s shot.
- 6.8-76 mood montage (26 shots, ASL 2.9 s): teal, film-grain "home movie" look of a coastal drive, then NEO in real-looking homes: carrying laundry, sitting with a family, a person in a VR headset whose arm moves NEO mirror (≈0:48-0:53, teleoperation shown openly as play), sunset.
- 76-116 founder interview (4 shots, ASL ≈10 s), name super left.
- 116-175 design macro block (19 shots, ASL 3.1 s): tendon-drive hand and motor parts on white (render-like, not stated), knitted suit fabric, 3D-lattice padding, speaker grille, camera eye, three colourways.
- 175-300 product presenter (Apple-keynote format): presenter in the wood studio, NEO behind him; spec panels (≈3:10-3:18), a three-panel split "Chores / Companion / Autonomy" (≈3:36-3:50), phone app, the charging dock, a couple meeting NEO.
- 270-300 chapter card "1 Chores" (small number + word, top-left, NEO in studio).
- 300-390 chores block (39 shots, ASL 2.3 s, the densest part): the head ring turns blue and a pill reads "Expert Mode Enabled" (≈5:04); then fish-eye robot-POV clips with a top-centre task pill ("Tidy Living Room", "Laundry", "Empty Dishwasher"...); a remote person on a phone in a car sees the robot view (≈5:28); "Self-Charge Enabled" pill at the wall dock (≈6:10).
- 386-475 chapter "2 Companion": older man asks NEO about a spice jar, dialogue shown as chat bubbles beside the faces; VP of AI interview; NEO at a door, in a kitchen; ASL 7.2 s.
- 475-540 chapter "3 Autonomy": one locked-off wide of a bright living room, 9 shots (ASL 5.4 s, longest 17.6 s): top pill = task ("Get the Door", "Feed Dogs", "Laundry"), bottom = tiny "Autonomous" over the current sub-step ("Grab Handle", "Walk to Door").
- 540-582 close: product beauty shots, founder to camera.
- 582-593 end card on off-white: NEO head, colour dots, two price pills ($20,000 Early Access or $499/mo), then "1X.TECH / NEO".

## Cut rhythm
- 141 shots (scene detector), ASL 4.21 s, median 2.79 s, 5 % < 1 s, 45 % > 3 s, 14.3 shots/min. ASL per quarter 3.45 / 5.49 / 2.97 / 6.18 s.
- The adaptive detector finds 162 shots (25 extra cuts, mostly in the macro and POV blocks): treat ASL as 3.7-4.2 s.
- Longest 21.5 s (392 s, rack-focus dialogue take), 17.6 s (autonomy wide), 17.0 s (215.7 s presenter). Shortest 0.13 s (white flash frames in the cold open).
- Rhythm alternates by chapter: montage 2-3 s, interview 7-10 s, POV chores 2.3 s, autonomy wide 5.4 s. Cuts on audio onsets 28 % vs 35 % chance: cut to speech, not to music.

## Typography
- One grotesk throughout (closest free: Inter; 1X's face has slightly rounder forms, Manrope is a second option). Sentence case, white.
- Task / mode pill: frosted translucent capsule (≈8 % H tall, ≈20-25 % W), text ≈3.3 % H, 500 weight; task pills top centre (y ≈12 %), mode pills ("Expert Mode Enabled", "Self-Charge Enabled") bottom centre (y ≈88 %).
- Autonomy line: "Autonomous" ≈1.7 % H in 60 % white, sub-step ≈2.7 % H white below it, bottom centre, no box.
- Name super: name ≈3 % white 600 + role ≈3 % grey 400, left x ≈3 %, vertically centred (y ≈48-52 %), no box.
- Spec panels: two tall frosted cards left and right of the robot, value ≈4.2 % H + tiny caption ≈1.7 % H, imperial units ("5'6\"", "66 lbs", "22 dB"), title pill "NEO Home Robot" top centre.
- Chapter cards: small number + word, top-left, ≈2 %.
- End card: dark text on off-white, prices ≈3.5 % H in pills.

## Colour/grade
- Warm beige/oat palette that matches the robot's knit suit: wood, linen, plants, soft daylight. Cold open in a teal-green, grainy film look (gate weave, light leaks) for "memory" mood. No hard blacks except the end tail.

## Camera/shots
- Real interiors, soft daylight, slow dolly and handheld; locked-off wide for autonomy; fish-eye robot head camera for teleoperated chores; macro slider shots for design; presenter medium shots on a 2-camera setup.

## Transitions
- Hard cuts; white flash frames in the cold open; a 0.6 s dip to black at 116 s into the design block; 2.5 s black hold at 544 s before the outro.

## Sound
- Voice almost all the way (speech detected in ≈90 % of the runtime, ≈1.8 words/s): founder, presenter, VP of AI, users talking to NEO. Soft piano/ambient bed. Integrated -16.4 LUFS, LRA 13.9 LU (wide: quiet dialogue vs louder music peaks), true peak -0.5 dBTP.
- One drop-out: 394.7-395.7 s (1.0 s, -41 dB floor) right after the "Companion" chapter card. Loudest hits in the closing music (≈524-537 s, +17 to +22 dB).

## What makes it credible (and where it is weak)
- It names the teleoperation: the "Expert Mode Enabled" pill plus a blue head ring mark the human-guided chores, and an operator is shown on a phone. The autonomy chapter carries its own "Autonomous" label per sub-step.
- One locked wide room for the autonomy block, with sub-step labels, so viewers can follow each task.
- Named people with titles; real homes; price and order info on screen.
- Weak: no speed label anywhere (real time not stated); autonomy shots are cut into 2-17 s pieces, not one take; design macro shots may be renders (not stated); 10 minutes is long for a launch film.

## Recipe (real footage + HTML/GSAP)
- Pills: `.pill{padding:1.6vh 2.4vw;border-radius:99px;background:rgba(255,255,255,.18);backdrop-filter:blur(12px);font:500 3.3vh Inter;color:#fff}`; in `autoAlpha 0→1, y 8→0, .35 s power2.out`; task pill top centre, mode pill bottom centre.
- Autonomy stack bottom centre: `<small>Autonomous</small>` (1.7vh, rgba(255,255,255,.6)) above the sub-step (2.7vh 600); swap the sub-step text with a 0.2 s crossfade at each action change.
- Mark teleoperated clips with a mode pill AND a colour change on the robot's status light (one cool accent, e.g. #4DA3FF).
- Chapter cards: number + word, 2vh, top-left, over the product standing in the studio, 3-4 s.
- Grade warm and low-contrast; keep one "memory" grade (teal, grain) only for the cold open.
