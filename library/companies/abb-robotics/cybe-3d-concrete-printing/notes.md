# Op bezoek bij CyBe Construction: 3D-betonprinten met ABB-robots  (ABB Robotics, 2026-09-08, 0:56, 16:9, YouTube @ABBRobotics)
URL: https://www.youtube.com/watch?v=UlTf-jIU3JQ
Purpose: social reel / customer visit (construction partner: 3D concrete printing with ABB robots)
One-sentence point: An ABB presenter visits CyBe, a 3D-concrete-printing company that builds its own printers on ABB robots, and shows the printers and printed walls.

## Structure (cut list + English captions; Dutch title, English speech)
- 0.0-9.4 hook: selfie-style piece to camera (phone held at arm's length, she walks; printed concrete wall behind her). "Hello, today I'm at our partner CyBe. CyBe is a technology company that offers an all-in-one solution for building faster, cheaper and more sustainable through 3D printing."
- 9.4-13.5: handheld walk past two ABB industrial robots (one red, one white) in the workshop. Dissolve.
- 13.5-21.5: large white ABB robot on a floor track (the printer), handheld push-in. Dissolve.
- 21.5-29.9: a worker in a helmet at the mortar mixer / printer station.
- 29.9-35.4: selfie again, printed elements behind her ("In the Netherlands they print projects themselves, but worldwide they sell their technology...").
- 35.4-41.7: handheld along a 3D-printed wall element - close on the layer lines and a pipe sleeve inside the print (printed curves, gravel infill).
- 41.7-52.3: gantry printer printing a foundation outline on the floor (10.6 s, the longest shot) with music only.
- 52.3-56.2: CyBe logo on white.

## Cut rhythm
- 9 shots in 56.2 s (6 hard cuts + 2 dissolves found by eye at ~13.5 s and ~21.5 s). ASL 6.24 s, median 6.30 s. ASL per quarter 4.68 / 7.03 / 3.51 / 4.68 s.
- Longest 10.57 s (gantry printing), 9.43 s (selfie), 8.43 s, 8.0 s. 89 % over 3 s. One shot = one location on a walk-through.

## Typography
- No supers, no captions burned in (the speech is the only "text"). Persistent corner bugs: "ABB Robotics" logo in a white box bottom-left (~10 % frame height) and the CyBe logo bottom-right (white, semi-transparent). End card: CyBe logo (orange knot + grey wordmark) on white, centred, ~22 % height.

## Colour/grade
- Ungraded phone/handheld footage: bright industrial hall daylight, slight over-exposure on windows, natural skin tones. The red ABB robot and orange CyBe accents are the only strong colours.

## Camera/shots
- Phone or small camera: selfie walk-and-talk, handheld walk-past b-roll, a handheld close pass along the printed wall, a static-ish wide of the gantry printer at work.
- No slow motion, no drone, no lighting. Whether the gantry shot is sped up can't be told (no label) - the head moves at a plausible print speed.

## Transitions
- 6 hard cuts + 2 dissolves (~0.5 s) between walk-through b-roll shots.

## Sound
- Presenter speech (English) with light background music; music only in the second half. Integrated -17.5 LUFS. Small gaps around 43-48 s are music beats; loudest at 48.65 s.

## What makes it credible (and what is missing)
- Real place, real people, real machines, uncut walk-throughs - it feels like a visit, not an ad.
- Partner logo on screen the whole time (co-branding = endorsement).
- Missing for premium: no hero shot of the print in progress close-up, no data (print speed, wall height, time), no captions for sound-off viewing, no title card. Useful as a "minimum viable" construction-site reel.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Shoot on a phone/gimbal: 1 selfie intro (8-10 s), 4-5 walk-through b-roll shots (6-10 s each), 1 long shot of the machine working (10 s), 1 macro along the finished product.
- Bugs: `<img class="bug left">` your logo bottom-left in a white box (`height:10vh; padding:1vh; background:#fff`), partner logo bottom-right (`opacity:.85`), constant.
- Add what this one lacks: burned-in captions (Inter 600, 3.5vh, white with a 60 % black pill, centre-bottom), one data card ("Wall printed in 4 h 20 min") over the long machine shot, and a 3-frame white flash into the end card.
- Dissolves: `gsap.to(clipA,{autoAlpha:0,duration:.5})` while `clipB` is under it.
