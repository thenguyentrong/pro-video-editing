# DJI Osmo Pocket 4 is here - redefining what a pocket camera can do  (DJI, 16 Apr 2026, 1:46, 16:9, YouTube @DJI)
URL: https://www.youtube.com/watch?v=EbebFc9PHcU
Purpose: launch film (product introduction)
One-sentence point: a pocket gimbal camera for everyone's everyday story - a narrator ticks off ≈18 features in 95 s, each one a 2-4 shot mini scene with a two-line label.

## Structure (cut times from metrics.json, adaptive detector)
- 0-5 s (5 %) hook: the camera held in hands against night bokeh and a sunset skyline; VO from 0 s.
- 5-7 s name card: "INTRODUCING / OSMO POCKET 4" centred over two girls running through a yellow rapeseed field.
- 7-93 s (81 %) feature run, ≈18 features at 3-6 s each: 1-inch sensor, slow motion (skateboarder on a coast road), built-in storage (on-screen dialog), 10-bit D-Log (CGI sensor with the image inside), HDR, 3-axis stabilisation (safari truck, giraffe), 2x zoom (lions), wireless mic, gesture control, surround sound (CGI sound rings on a road), subject tracking ("Subject Registered" on the screen), live stream (a designer streams from her studio, stream UI composited), beauty mode, fast charging, joystick, fast transfer, low light, built-in fill light (night harbour selfie).
- 93-98.4 s: summary hero shots (girl in the field, friends on a cliff), then the camera turns on black and its fill light switches on.
- 98.4-101 s: "OSMO POCKET 4 / THE WORLD IN MY POCKET" on black (cap ≈3 % H + small tagline).
- 101-105.7 s: DJI logo on black (silence from 97.7 s).

## Cut rhythm
- 90 shots in 105.7 s, ASL 1.17 s, median 0.96 s, 52 % < 1 s, 51 shots/min. Without the black end (from 98.4 s): ≈89 shots in 98.4 s → ASL ≈1.1 s.
- ASL per quarter 1.15 / 1.15 / 1.06 / 1.20 s: completely flat - a metronome feature run.
- Cuts per 10 s: 11 / 8 / 5 / 8 / 10 / 10 / 7 / 10 / 13 / 7 / 0. Longest real shot 5.6 s (built-in storage UI take), shortest 0.2 s.
- The adaptive detector found 12 cuts the scene detector missed (fast pans, similar greens); checked on the sheet.
- Cuts on music onsets 45 % vs 37 % chance.

## Typography
- Same DJI system as Mini 5 Pro (see dji/mini-5-pro-meet): name card = thin tracked "INTRODUCING" (cap ≈2 % H) over a medium-weight product name cap ≈5.8 % H, centred at ≈50 % H; free stand-in **Montserrat** Light/Medium.
- Feature label (two lines): bold caps title cap ≈2.6 % H ("LIVE STREAM*") + regular sentence-case subline ≈2.4 % H ("Anywhere, Anytime"), left at x ≈6.5 % W, y ≈75 % H. Free stand-in **Open Sans** Bold/Regular.
- "SHOT ON / OSMO POCKET 4" watermark top-left on every shot filmed with the product (≈1 % + 3 % H).
- Real device UI on the 2" screen is shown big in close-ups (dialogs, check marks, live-stream overlays composited around the person).
- Legal micro-text at the bottom (≈1.2 % H) when a label has an asterisk.

## Colour / grade
- Bright, warm, saturated holiday colours: yellow rapeseed, blue sky, golden safari light; night scenes with warm bokeh. Mean luma 0.35. Clean, no grain.
- Studio scenes in soft white daylight. Close on pure black.

## Camera / shots
- ≈50 % people filming themselves or friends with the product in hand (front-facing, smiling, moving), ≈35 % the product's own footage ("shot on"), ≈10 % product macros and CGI (sensor, sound rings), ≈5 % screen UI close-ups.
- Lots of motion: running, skateboarding, safari vehicles, walk-and-talk.

## Transitions
- Hard cuts on the beat; whip-pans between scenes; CGI push into the sensor; UI elements animate on the device screen. No flashes.

## Sound
- One upbeat female narrator from 0 to ≈94 s, ≈177 words (≈113 words/min): one short sentence per feature, every spec said aloud.
- Light, bouncy pop bed with claps; cuts on its beat.
- Integrated −16.9 LUFS, LRA 3.0 LU (very flat), true peak −1.0 dBTP.
- Drops: 0.45 s at 4.2 s (before the name card, then +33.2 dB at 5.45 s), 0.35 s at 38.5 s, 1.2 s at 95.6 s (before the product on black). Hits +16-22 dB on feature starts.

## What makes it premium
- A huge feature list stays light because every feature is a tiny human scene, not a spec card.
- Real people filming their own lives: the product is always in a hand.
- The same two-line label in the same place for every feature - the viewer learns the system in seconds.
- A short drop before the name card and before the final product shot.

## Recipe (real footage + HTML/GSAP)
- Shoot/source 18 micro-scenes of 2-4 shots each ("girl running rapeseed field", "skateboarder coastal road slow motion", "safari jeep giraffe", "lions resting grass", "fashion designer live stream studio", "friends selfie cliff sunset", "night harbour selfie light").
- Pace: ≈1.1 s per shot, flat; 3-6 s per feature; VO ≈110 words/min, one sentence per feature.
- Label: `.t{font:700 2.6vh 'Open Sans'; text-transform:uppercase} .s{font:400 2.4vh 'Open Sans'}`, `left:6.5%; top:75%`, cut in/out with the shot.
- Name card over a lifestyle shot: eyebrow `font:300 2vh Montserrat; letter-spacing:.3em`, name `font:500 5.8vh Montserrat`, centred, fade 0.5 s.
- End: product on black with its light turning on (`filter: brightness(.3 → 1)` on a light layer, 0.4 s), name card 2.5 s, logo 4 s.
- Mix: VO-led at ≈ −17 LUFS, flat bed, 0.4-1.2 s drops before the name card and the end.
