# Optimus - Gen 2 | Tesla  (Tesla, 2023-12-13, 1:43, 16:9, YouTube @tesla)
URL: https://www.youtube.com/watch?v=cpraXaw7dyc
Purpose: product reveal (version update with feature captions on real footage)
One-sentence point: Optimus Gen 2 is faster, lighter and has new hands with tactile sensing - shown with short captions over real test footage.

## Structure (cut list; no voice, electronic music)
- 0.0-9 version timeline on black: dim previous robots, text fades in/out beside them - "Bumblebee / September 2022" (0-4.5 s, left), "Optimus - Gen 1 / March 2023" (5-9 s, right).
- 9-21 macro reveal in the dark: blue rim light on feet (10 s), leg shell, hand (12-13 s), shoulder, a white light line tracing the body edge (16-20 s). Cuts every 1.375 s (11.5, 12.875, 14.25, 15.625 s).
- 21-32.8 hero: locked-off wide of Gen 2 standing in front of a concrete wall with plants; "Introducing" (25-28 s) then "Optimus - Gen 2 / December 2023" (29-32 s) fade in left/right of the robot. The robot waves (31 s).
- 32.8-85 feature list over real footage (one caption per shot, sometimes lines added):
  - "Tesla-designed actuators & sensors" (33-35 s), "2-DoF actuated neck" (36-39 s) - studio, robot turns head and gestures.
  - "Actuators-integrated electronics & harnessing" (40-43 s), "30% walk speed boost" (44-47 s) - walking in a garage with Cybertrucks.
  - "Foot force/torque sensing / Articulated toe sections / Human foot geometry" (48-52 s) - side tracking shot of the feet; the three lines appear one after another.
  - "10kg total weight reduction / without sacrifice" (53-57 s) - second line appended later.
  - "Improved balance & full-body control" (59-62 s) - gym room, squats (63-66 s).
  - "Faster, 11-DoF brand-new hands" (68-71 s).
  - "Tactile sensing on all fingers" (73-76 s) + a live sensor HUD on the right: "Right / Left" rows of thumb and index pads that glow pink when touched (73-84 s); "Delicate objects manipulation" - picking up an egg (77-83 s).
- 85-90.5 "Stay tuned to see what Optimus will do next!" - robot walking in the garage.
- 90.5-95.3: Tesla "T" logo on black (fade out ~94 s), 0.65 s digital silence (94.1 s).
- 95.3-103 post-credit gag: two Optimus robots dancing in purple/cyan club light (loudest hit 95.4 s, +39.5 dB).

## Cut rhythm
- 22 shots in 103 s. ASL 4.69 s, median 4.50 s. ASL per quarter 3.22 / 6.44 / 3.68 / 4.30 s.
- Longest 11.71 s (21.08, hero studio wide), 11.50 s (opening timeline), 8.21 s, 7.71 s. Shortest 1.12 s, 1.33 s, 1.38 s (macro section).
- 0 % under 1 s, 64 % over 3 s. One caption = one shot of 4-8 s; macro section uses a 1.375 s grid.
- 52 % of cuts on audio onsets vs 40 % chance - loosely on the beat (track pulse ~2.05 s per bar).

## Typography (data/specs on screen)
- Tesla's light geometric sans (Gotham-like; closest free: Montserrat Light/Regular), sentence case, white or very light grey, small: ~2-2.3 % frame height per line. No boxes, no lines, no icons.
- Placement: in the empty side of the frame next to the robot (left or right third, roughly at shoulder height in studio shots, lower third in walking shots).
- Animation: soft fade in ~0.4 s, hold 3-5 s, fade out; multi-line facts build line by line (foot sensing: 3 lines in ~3 s). Product name: "Optimus - Gen 2" with "Gen 2" in italic/lighter weight, date line below in smaller size.
- Data visualisation: tactile HUD (two rows of fingertip pad icons labelled "Right"/"Left", "Thumb"/"Index"), pads light up pink in sync with real contact - the only real data on screen.

## Colour/grade
- Clean, neutral daylight on real test footage (studio concrete wall, garage, gym). Macro section: black with blue/white rim light. Post-credit: saturated purple/cyan club lights.

## Camera/shots
- Mostly locked-off or slow gimbal medium-wide shots of the real robot doing one simple action per shot (wave, turn head, walk, squat, pick egg).
- Side tracking shot at foot level for walking (48-52 s).
- Real footage throughout (visible cables-free robot in real rooms); the walking speed may be real-time (no label) - a guess.

## Transitions
- Hard cuts; fades on text and logo. Version timeline uses fade-up/fade-down of dimly lit robots on black.

## Sound
- Electronic beat with steady 16th-note hi-hats (spectrogram 40-80 s), no VO, robot sounds not audible as a feature. Integrated -14.9 LUFS.
- 0.65 s digital silence before the post-credit gag, then the biggest hit.

## What makes it credible / premium
- Version history first (Bumblebee -> Gen 1 -> Gen 2): progress shown as proof.
- One measurable claim per shot ("30% walk speed boost", "10kg total weight reduction", "11-DoF").
- Real rooms, real robot, simple actions, long shots (median 4.5 s) so the motion can be judged.
- Tactile HUD tied to the real contact - data that reacts to the footage.
- Ends with humour (dance) after the logo - personality without hurting the spec section.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Version timeline: black, previous machine images at 25 % brightness, caption `<b>Prototype 1</b><br><small>March 2025</small>` (`font: 500 2.3vh Montserrat`, small 1.5vh), fade .5 s in, 3 s hold, fade .5 s out; alternate left/right.
- Feature shots: 4-8 s each, one action, caption in the empty third: `font: 400 2.2vh Montserrat; color:#f2f2f2`; extra lines `gsap.from(line2,{autoAlpha:0,duration:.4}, '+=1.2')`.
- Sensor HUD: small SVG grid of pads; drive the glow from a CSV/JSON of real sensor values (or keyframe them to the contact moments) - `gsap.to(pad,{fill:'#ff4fa0',duration:.05})`.
- End: logo on black 4 s, 0.6 s silence, then a light-hearted 8 s extra.
