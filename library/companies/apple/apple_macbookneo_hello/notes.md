# Hello, MacBook Neo  (Apple, 2026-03-04, 3:50 file / 3:41.7 content, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=u3SIKAmPXY4
Purpose: launch film (playful product walkthrough)
One-sentence point: MacBook Neo is a fun, colourful, affordable Mac — every feature is shown as a hand-made "magic trick" on a white tabletop.

## Structure (VO lines from the official captions)
- 0-9 s **Hook**: "This is MacBook Neo. An amazing all-new Mac at a surprising price." Two hands swap colours (silver → pink → citrus) with whip moves, then the citrus Neo opens to a bright wallpaper.
- 9-27 s **Build**: a raw aluminium slab (knock SFX) is shaped in the hands into a laptop; "most recycled material of any Apple product".
- 27-37 s **Display**: dark set, the hands stretch a purple light like dough; it snaps into the screen.
- 37-56 s **Keyboard**: a marble is flicked away, hands clap, keys explode into the air (snap, thud, clatter) and rain onto the keyboard.
- 56-72 s **Trackpad / Touch ID**: a rocket from a game flies out of the screen into confetti; finger on Touch ID, Apple Pay chime, UI cards float.
- 72-103 s **Ports, camera, mics, speakers**: side ports, glass disc/marble, black frame with the camera dot (89-90 s), car-chase movie on screen with engine and shouting SFX.
- 103-126 s **Colours**: Silver, Indigo, Blush, Citrus swapped in the hands; colour-matched rubber feet pop off and back; A18 Pro chip is tossed in.
- 126-204 s **Software**: hands on keyboard with app demos, Apple Intelligence, app icons as physical tiles pinched between fingers (Finder, lock), Dock as a strip, Continuity with iPhone.
- 204-221.7 s **Close**: "So that's MacBook Neo. Everything you'd expect of a MacBook… at a price you wouldn't." Lid closes; "MacBook Neo" wordmark on the lid, a hand wipes it off and plays with the Apple logo; legal.

## Cut rhythm
- Detector: only 12 hard cuts → ASL 18.5 s over 221.7 s. This is NOT the real feel: almost every change is hidden in a hand move, whip, colour swap or VFX.
- By eye on a 2 fps strip of 0-60 s: **~16 camera set-ups → ASL ≈ 3.7 s** (estimate). Many "takes" are 10-40 s continuous tabletop moves.
- 55 % of the few hard cuts sit on an audio onset (chance 34 %).

## Typography
- Almost none. Only the end wordmark "MacBook Neo": a wide/extended heavy grotesk (not SF Pro; closest free: Archivo Expanded ExtraBold / Unbounded Bold — guess), black on the brushed-aluminium lid, ink 5.2 % H (cap ≈ 4.5 %), x 31-69 %, 212-215 s, wiped off by a hand.
- No feature supers; the VO names every feature.

## Colour / grade
- Bright white seamless tabletop (high key), neutral grade, soft shadows; product colours (citrus yellow-green, indigo, blush) and the purple/green wallpaper carry all colour.
- One dark interlude (27-37 s) with purple glow; one moody grey section for the movie (152-158 s).
- 11 % of frames mostly empty.

## Camera / shots
Locked or slow-moving camera over a white table at 3/4 overhead; one pair of hands as the "performer"; practical tricks + VFX (stretchy light, exploding keys, objects popping off, icons as physical tiles); screen content composited live on the display; close-ups of keys, ports, feet.

## Transitions
Hidden cuts in whips and hand passes (colour swaps at ~1.8 s and ~2.7 s), VFX morphs (light → screen, keys → keyboard), hand wipes (title wiped off). Very few visible hard cuts.

## Sound
- VO: friendly, casual first-person-plural ("we built in…", "because you know… details"). Music: "Presto" by Hark Madley.
- Dense foley for every trick (captions: whirring, knocks, snap, thud, rapid thuds, clatter, whoosh, pop, puff, Apple Pay chime, keystrokes, alert tones, slam).
- Integrated **−15.9 LUFS**. Three 0.15-0.2 s drop-outs at 86-90 s (stop-start rhythm around the camera/mic section), hit at 86.35 s (+31.8 dB). 0.7 s silence at 214.2 s while the hand wipes the title.

## What makes it premium
- One clear device: hands + white table + magic. Every feature becomes a physical gag.
- Long, confident takes; the editing hides itself.
- Sound design makes the tricks tactile (every touch has a sound).
- Joyful colour on a pure white stage.

## Recipe (real footage + HTML/GSAP)
- Shoot on a white table, locked-off 3/4 overhead, 24 fps, 1/50 shutter for motion blur; plan whip/hand-pass hides every 3-5 s to swap objects.
- Composite the screen with HTML: place a `<video>` or UI mock in the display area with CSS `transform: matrix3d(...)` corner-pinned to the lid; animate content with GSAP.
- "Magic" beats in HTML/GSAP: icons as tiles with `box-shadow: 0 12px 24px rgba(0,0,0,.15)`, `gsap.from(tile,{scale:.2,y:80,rotation:-15,duration:.5,ease:"back.out(2)"})`; confetti with 60-120 small rectangles, `gsap.to(..,{y:"+=400",rotation:"random(-360,360)",duration:1.6,ease:"power1.in"})`.
- End: product wordmark in an extended heavy grotesk, cap ≈ 4.5 % H, centred on the lid; wipe off with a `clip-path: inset(0 0 0 X%)` following the hand, 0.7 s silence.
- Mix: VO −16 LUFS, music bed −24 to −20 LUFS, one foley hit per action.
