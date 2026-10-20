# Power, reimagined | OnePlus 15  (OnePlus, 24 Oct 2025, 1:00, 16:9, YouTube @OnePlusTech)
URL: https://www.youtube.com/watch?v=A_Jf522wJi0
Purpose: pre-launch brand anthem / teaser
One-sentence point: performance is about the first step, not the finish line - a sprinter in the blocks, then 50 s of athletes taking off, with the phone almost absent until the last 3 s.

## Structure (cut times from metrics.json)
- 0-2.7 s: an empty photo studio with a camera dolly track leading to a white plinth under a square softbox (the "benchmark set").
- 2.7-14 s (19 %) setup: light beam, a red running track, an eye, a sprinter in starting blocks, the studio again; spoken lines subtitled at the bottom.
- 14-33.5 s (33 %) ignition montage: skater, BMX at night, runner's shoes, skateboard in a car park, a burning ring, a woman's profile, swimmers diving (from below), dancers in a warehouse; 0.12-0.8 s shots.
- 33.5-45 s (19 %) the flight: motocross jump against clouds, car drifting in smoke, skater in the air, a phone glimpse on a gimbal rig.
- 45-55 s: callbacks (studio, red-lit face, phone macro), fastest flashes (0.2-0.3 s), the sprinter again.
- 55-57.6 s: "Power On" over the sprinter, "Limits Off" over the phone on the plinth in the studio.
- 57.6-60 s: "OnePlus 15 / Coming Soon" and the logo on black (2.4 s).

## Cut rhythm
- 76 shots in 60.0 s, ASL 0.79 s, median 0.64 s, 74 % < 1 s, 0 % > 3 s, 76 shots/min - the fastest film in this set.
- ASL per quarter 0.75 / 0.56 / 1.15 / 0.79 s. Cuts per 10 s: 12 / 16 / 17 / 7 / 10 / 13.
- Longest 2.7 s (opening studio), shortest 0.12 s (3 frames).
- Cuts on music onsets 12 % vs 14 % chance: the cut follows the spoken lines and motion peaks, not the beat.

## Typography
- OnePlus Sans (proprietary). Closest free: **Inter** or **Manrope** Regular.
- Captions of the spoken lines: sentence case, no full stop, white, cap ≈2.5 % H, centred at ≈86 % H (subtitle position), 2-6 words, changing with every line (≈1-2 s each).
- Sign-off: "Power On" / "Limits Off" as two separate words-pairs, cap ≈3 % H, centred on the subject.
- End: "OnePlus 15" cap ≈2.5 % H + "Coming Soon" ≈1.3 % H, then the wordmark, centred on black.

## Colour / grade
- Dark, high-contrast, filmic: deep shadows (mean luma 0.24), saturated red accents (running track, red-lit face, red room), cool grey studio, sky-blue jump shots. Light grain feel, no letterbox.

## Camera / shots
- ≈85 % athletes and movement (handheld, low angles, from below water, fast pans), ≈10 % the studio set, ≈5 % phone (glimpses only).
- Motion blur and smear are kept, not avoided.

## Transitions
- Hard cuts, many on motion peaks; smear frames act as whips. No graphic transitions.

## Sound
- A calm, intense male voice speaks the manifesto (≈110 words, subtitled), over a driving hybrid track with impacts.
- Integrated −9.2 LUFS (very loud), LRA 2.1 LU (compressed wall), true peak +0.9 dBTP. No silences; hits only +15-16 dB because the bed never drops.

## What makes it premium
- A manifesto, not a feature list; the product earns its place in the last 3 s.
- One recurring set (studio + dolly track + plinth) bookends the chaos.
- Subtitled VO keeps the words readable at this speed.

## Recipe (real footage + HTML/GSAP)
- Stock: "sprinter starting blocks low angle", "motocross jump sky", "skateboarder air clouds", "swimmers diving underwater from below", "dancers warehouse", "car drift smoke", "red running track macro".
- Pace: 0.5-0.8 s shots, flashes of 3-6 frames; one 2-3 s establishing shot to open and one to close.
- Captions: `font:400 2.5vh Inter; bottom:12%; text-align:center`, swap per spoken line, no animation.
- Grade: `contrast(1.2) saturate(1.1)`, crush blacks, push reds.
- Mix: loud and compressed (≈ −9 to −10 LUFS), but keep true peak ≤ −1 dBTP.
