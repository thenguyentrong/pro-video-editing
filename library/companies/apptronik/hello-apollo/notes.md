# Hello Apollo  (Apptronik, 2023-08-23, 0:44, 16:9, YouTube Apptronik)
URL: https://www.youtube.com/watch?v=uJOA5IDaL5g
Purpose: launch teaser (humanoid reveal)
One-sentence point: meet Apollo, a friendly humanoid that already walks, carries boxes and works with people in a warehouse.

## Structure (studied from the sheet and metrics)
- 0.0-6.3 hook on black: a chat "typing" bubble (1 s), then "hello" types on letter by letter (2-4 s), "APOLLO" appears below (5-6 s) - the robot greets the viewer like a message.
- 6.3-12.6 reveal: dissolve into a dark warehouse; Apollo walks out of the shadow towards camera, lights come up (7-10 s), leg tracking shot (10-12 s).
- 12.6-37.1 capability montage: walks down an aisle; takes a box from a person's hands (14-16 s); places a box on a roller conveyor (16-18 s); carries a box in a wide (18-20 s); stacks boxes (21-25 s); top-down of the hands holding a box (24-25 s); carries a tote to a cart (25-28 s); gripper close-ups on a tote at a workstation (28-30 s); with a worker at a bench (30-33 s); waves and gives a thumbs-up to camera (33-37 s).
- 37.1-41.8 out: wide in the aisle, the lights go out, silhouette.
- 41.8-44.0 logo: glitch/audio-waveform transition into the symbol + APPTRONIK wordmark on black.

## Cut rhythm
- 20 shots in 44.0 s after adding 6 verified cuts the scene detector missed in the dark footage (6.30 dissolve, 20.31, 30.36, 32.37, 33.70, 39.08); a 26.7 s adaptive candidate was the robot walking across frame and was dropped.
- ASL 2.2 s, median 1.96 s; per quarter 3.67 / 1.83 / 1.22 / 2.2 s. 5 % under 1 s, 27.3 shots/min. Shortest 0.71 s (24.7). Longest 6.3 s (title on black), then 3.8 s (reveal walk).
- Cuts per 10 s: 1 / 5 / 7 / 5 / 1 - a classic arch: slow open, dense middle, slow out.

## Typography
- "hello": thin lowercase geometric sans, white, ≈11 % H (ascender height), centred at y ≈40 %. Closest free: Raleway ExtraLight / Quicksand Light.
- "APOLLO": wide tracked caps with an open "Λ" A (no crossbar), ≈11.5 % H, letter-spacing ≈.3em, centred below. Closest free: Michroma or Montserrat Medium with letter-spacing .3em (draw the A as Λ).
- Typing: one letter per ≈0.25 s after a chat-bubble "…" icon; hold ≈1.5 s, then fade.
- End: symbol ≈11 % H + APPTRONIK wide caps ≈5.5 % H.
- No captions, specs, speed or autonomy labels.

## Colour/grade
- Dark, moody warehouse: low-key top light, warm cardboard browns, the white robot as the brightest object. Mean luma 0.20. Lights-up reveal and lights-out ending.

## Camera/shots
- Cinema camera on gimbal/slider; medium shots and close-ups of hands; low tracking on legs; one top-down; robot faces camera for the gesture.
- People: one worker hands over a box, one works at a bench. Real robot, real set; whether moves are autonomous or teleoperated is not stated.

## Transitions
- Dissolve from the title into the first shot (≈0.5 s), hard cuts in the montage, lights-out in camera, glitch into the logo.

## Sound
- Music-led trailer with UI sounds on the typing; no voice heard. Integrated -10.2 LUFS (loud), LRA 12.5 LU (quiet open, big body), true peak -0.1 dBTP. Silence 0.5-1.7 s (before the bubble) and 43.25-44.0 s. Biggest hit +30.9 dB at 2.05 s (the first letter).

## What makes it premium
- The greeting idea: the robot speaks through type before you see it.
- Dark-to-light reveal and light-to-dark exit bookend the film.
- Friendly gestures (thumbs-up, wave) and hand-overs with a person make it a coworker, not a machine.

## What it does not prove
- No task duration (shots ≤3.8 s), no speed label, no autonomy statement, no named site or customer.

## Recipe (real footage + HTML/GSAP)
- Open on black: chat bubble (3 dots bounce, 0.6 s), then type "hello" at 4 chars/s in Raleway 200 11vh; second line in Michroma 11vh letter-spacing .3em fades in 0.4 s.
- 0.5 s dissolve to a dark wide; let the machine walk into a pool of light (4 s).
- Montage 15-20 shots of 1-3 s, 5-7 cuts per 10 s, each shot one action (take, carry, place, gesture).
- End: lights off in camera (or `filter:brightness` to 0 over 1 s), 0.2 s RGB-split glitch into the logo.
- To make it proof: add one 20-40 s uncut take and a corner label (speed + autonomy).
