# Introducing Rapid Response: Extending ANYmal's Reach in Emergencies  (ANYbotics, 2024-09-09, 1:29, 16:9, YouTube @anybotics)
URL: https://www.youtube.com/watch?v=wrn1S0RL1_U
Purpose: feature launch film (software feature for the existing robot)
One-sentence point: when an alarm goes off, an operator can send ANYmal into the smoke from a desk and see what it sees, before people go in.

## Structure (studied from the sheet and metrics)
- 0.0-2.9 logo sting: coral red frame, white symbol animates.
- 2.9-12 the incident: robot on a stair landing in smoke; operator at a desk with a control-room wall screen and laptop (3 s); full-screen recording of the real operator app with the robot's camera (4-6 s); smoke in the hall; fire truck arrives outside (9-10 s); robot leaves the building towards camera, firefighters run past it (12-15 s).
- ≈15.1-16.8 title card: coral full frame, "ANYmal / Rapid Response" two lines centred.
- 16.8-56 the mission: workers leave the hall (17-23 s, one 7.1 s take); robot opens/passes a door; operator types (27-33 s, 6.6 s); 3D map view (37-38 s); app with robot camera (40-41 s); robot climbs stairs (42-43 s, 51-54 s); app full screen with lidar map and robot icon (47-50 s).
- 56-82 the find: robot reaches the smoking equipment; app shows the robot camera inset + magenta lidar map + the robot icon walking a path (61-65 s); robot close-up in smoke; operator watches the inset feed (70-72 s, 77 s); app camera view (73-76 s).
- 82-86 handover: firefighters arrive with a hose at the door the robot came out of.
- 86-89 end card: coral, wordmark, then symbol + "Zurich | San Francisco".

## Cut rhythm
- 35 shots in 89.2 s (scene). Adaptive also flags 1.76 s (logo animation), 15.12 s (title-card entry, likely real) and 49.4 s; not added. ASL 2.55 s, median 1.68 s; per quarter 2.48 / 2.48 / 2.48 / 2.03 s.
- 5.7 % under 1 s, 22.9 % over 3 s, 23.5 shots/min. Cuts per 10 s: 2-6, peak 6 at 60-70 s (the find).
- Longest real takes 7.08 s (16.8, evacuation), 6.56 s (26.8, operator), 4.8 s; end card 7.26 s.
- 62 % of cuts on an audio onset (chance 47 %): music-cut.

## Typography
- Title card: humanist/grotesk semibold, white, two centred lines, cap height ≈7 % H (line ≈9 %), on coral. Closest free: Barlow SemiBold.
- End card: "Zurich | San Francisco" ≈2 % H light grey under the symbol.
- No captions, no supers, no speed labels. All other text is the real app UI (tiny, ≈1-1.5 % H): top bar shows the control mode - the 5 s screen reads MANUAL, the 62 s screen reads AUTO - plus P-STOP button and battery.

## Colour/grade
- Clean commercial grade, white smoke (stage fog), red robot, yellow hi-vis; app UI in dark grey with saturated green bar and red stop button; coral brand frames.

## Camera/shots
- Real chemical/pharma pilot plant and a staged office desk; fog for the emergency; real fire brigade truck and two firefighters.
- Robot shots: low gimbal at robot height, robot walking towards or past camera; stairs from below.
- Screen recordings of the real operator app full frame (≈13 of 89 s) - the machine's view, the map and the mode.

## Transitions
- Hard cuts; dissolve into and out of the title card (soft candidates 14.7-15.4 s) and a 0.5 s dissolve to the end card (85.3 s).

## Sound
- Music-led, no speakers on camera, no voice heard in the profile (flat, LRA 2.5 LU). Integrated -16.8 LUFS, true peak -2.4 dBTP. No drop-outs or silences. Biggest hit +24.7 dB at 15.7 s (the title card), others +16-26 dB at 16.75, 27.65, 32.05, 51.15, 86.6 s.

## What makes it credible
- Teleoperation is not hidden: the film's story is an operator at a desk driving the robot, and the UI mode field shows MANUAL and AUTO in different steps.
- The real app is shown full screen, with the robot camera, lidar map and stop button.
- Real responders and a real site; the robot hands over to firefighters (does not claim to replace them).
- Weak spot: mode change is only readable in tiny UI text; no label says which shots are autonomous, and fog is staged (not stated).

## Recipe (real footage + HTML/GSAP)
- Story in 5 beats: alarm → operator → robot goes in → robot sees → humans go in safely. 2-6 cuts per 10 s on the music.
- Record the real control app with OBS at native resolution; cut it full frame for 2-4 s each time the operator acts.
- If you use teleop, say it: add a corner label `MANUAL` / `AUTONOMOUS` (Inter 600 2vh caps, top-right, `rgba(0,0,0,.55)` pill) that switches with `tl.set` at the mode change.
- Title card on the brand colour at ≈17 % of runtime with the biggest music hit.
