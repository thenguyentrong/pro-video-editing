# Greatness. It Only Takes Everything | Rafael Nadal  (Nike, 2024-11-19, 1:00, 16:9 file with ~1.44:1 pillarbox, YouTube @nike)
URL: https://www.youtube.com/watch?v=X0xbNUMZCvk
Purpose: ad / tribute film (Nadal's retirement)
One-sentence point: Greatness is not one big moment but every second of a life given to the sport.

## Structure (cut list + English captions)
- 0.0-2.1 hook: low-angle profile close-up of Nadal with headband against a pale sky (2.1 s).
- 2.1-12 ritual: textures of the clay court - the line sweeper net dragged over the clay, shoes and long shadow, top-down drone of a lonely court in pines, net close-up. VO 6.7 s "When the dust settles, you'll know you've given more than anyone."
- 12-24 the work: night court, single ball in the dark, sweat, racket, a hand with taped fingers. VO "Chased down every game, shot, point. And put it all on the line for one more win."
- 24-27 archive memory: real broadcast footage - Nadal lying on the clay after a win (24.6), crowd hugging (25.9).
- 27-48 the litany: VO "Not once, but every second, minute, hour, day of your life" - one word per shot. Cuts accelerate (15 cuts in 40-50 s; 41.08-41.36 is a 0.28 s shot).
- 47.96 black hold 0.64 s, then a single ball in the dark (48.6).
- 49.9-51.7: overexposed white portrait, Nadal looking down (the only high-key shot).
- 51.68-60.0 end: one held 8.3 s wide shot - fog rolling over a clay court in the pine trees, Nadal walking away into it. Text over it: "Greatness." (52.5-53.9), empty fog (~1.3 s), "It only takes everything." (55.25-56.3), empty (1.7 s), white swoosh (58.0 to end).

## Cut rhythm
- 50 shots in 60 s. ASL 1.20 s, median 0.94 s. ASL per quarter 1.50 / 1.00 / 0.79 / 1.67 s.
- Longest 8.32 s (end shot), then 2.12 s (opening), 2.04 s. Shortest 0.28 s (41.08), 0.40 s (46.40).
- 54 % of shots under 1 s, 2 % over 3 s. Acceleration curve: 6 -> 8 -> 9 -> 10 -> 15 cuts per 10 s, then 1.
- Cuts are on the voice, not on music onsets (6 % on onset vs 7 % chance).

## Typography
- Small, quiet text. A light book serif (Nike uses a custom serif here; closest free: EB Garamond or Libre Caslon Text), sentence case, white, centred.
- Text height ~4 % of frame height (cap + descender), width ~29 % of frame for "It only takes everything.". Placed at ~49 % height, on top of the walking figure.
- 1-4 words per card. Hold 1.0-1.5 s. Hard on / hard off (no fade visible at 4 fps), each card followed by ~1.3-1.7 s of empty fog.
- Swoosh: white, ~11 % of frame width, centre at ~50 % x, ~54 % y, hard on at 58.0 s with an audio hit.

## Colour/grade
- Black and white, soft vintage lens look: strong vignette, soft/smeared edges, some barrel distortion (looks like a Petzval or tilt lens - a guess). Heavy grain.
- Picture is pillarboxed to ~1.44:1 (x 81-773 px of 854) - a square-ish "film archive" frame.
- Mostly low-key night shots with one hard light; the 49.9 s portrait is blown-out white as a contrast beat.

## Camera/shots
- Extreme details and textures (clay, net, shadows, taped hands) > faces. Top-down drone at 10 s. Low angles on the hero.
- Motion-blur "speed" plates (24.5 s: the camera rushing low over the clay).
- Archive: only 2 real broadcast shots (24.6-27.9 s), graded mono so they blend in.
- Slow motion on the ball and on the body in a few shots; mostly normal speed.

## Transitions
- Hard cuts. One 0.64 s black hold (47.96) as a breath before the last act. No dissolves found by soft.py besides camera moves.

## Sound
- Male English VO, measured and slow; music builds under it. Integrated -10.7 LUFS (loud), loudest 0.5 s at ~50 s (-7.4 LUFS momentary).
- Biggest hit: 30.0 s (+18 dB rise) - the start of the "Not once, but every second" litany.
- End hit at 58.05 s (+17.5 dB) on the swoosh. Then silence from 59.0 s.

## What makes it premium
- A tiny copy line ("Greatness. / It only takes everything.") on a huge, quiet image.
- One consistent optical look (mono, vignette, odd pillarbox) makes staged + archive feel like one memory.
- Rhythm built from the VO: one word = one shot in the litany.
- 8.3 s ending shot - the longest - after the fastest section.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Frame: 1920x1080 stage, a `<div class="frame">` 1555x1080 (1.44:1) centred, black around it. Every clip inside: `filter: grayscale(1) contrast(1.2)` plus a radial vignette overlay (`radial-gradient(ellipse at center, transparent 45%, rgba(0,0,0,.75) 100%)`) and a grain layer.
- Shots: texture details of your work (for construction: formwork, rebar, dust, hands, boots), one drone top-down, one or two real archive moments.
- Cut on each VO word in the litany: shots of 0.3-0.7 s, then one black hold of 0.6 s, then the slow end shot of 8 s.
- End text: `font-family: 'EB Garamond'; font-size: 3.2vh; color: #fff; text-align: center; top: 47%`. Timeline: `tl.set(t1, {autoAlpha:1}, 0.8).set(t1, {autoAlpha:0}, 2.2).set(t2, {autoAlpha:1}, 3.6).set(t2, {autoAlpha:0}, 4.6).set(logo, {autoAlpha:1}, 6.3)` relative to the end shot start. Hit SFX on the logo.
