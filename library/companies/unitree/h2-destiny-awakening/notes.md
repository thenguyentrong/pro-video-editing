# Unitree Introducing | Unitree H2 Destiny Awakening!  (Unitree Robotics, 2025-10-20, 0:50, 16:9, YouTube @UnitreeRobotics)
URL: https://www.youtube.com/watch?v=eUdBIFkMh-M
Purpose: humanoid launch film (teaser-style product reveal)
One-sentence point: the new 1.8 m class H2 humanoid moves with human-like grace: it dances, does martial-arts kicks and walks a runway next to a human model.

## Structure (measured cut list; no voice found, music only)
- 0.00-0.32 thumbnail frame: robot face close-up + gradient title "Unitree H2 / Destiny / Awakening" (8 frames only; the same trick opens every Unitree film studied).
- 0.32-14.20 ONE 13.9 s orbit: H2 dances on an empty theatre stage, the camera circles it so the backdrop turns into the auditorium seats (checked frame by frame at 7.6-9.0 s: continuous, no cut).
- 14.20-30.60 two more dance takes (10.2 s, 6.2 s) in other halls; crew members stand in the background watching.
- 30.60-36.56 face close-up in a hooded fur jacket, then a fashion-runway walk: H2 in streetwear walks a gold-lit corridor next to a human model (36.6-46.2 s, outfit changes on every cut, 1.0-2.1 s shots).
- 44.24-47.72 martial-arts kick in a stadium hall (2 shots).
- 47.72-48.3 CGI: the robot in a Vitruvian-man pose with four arms inside a purple ring (the only render).
- 48.3-50.0 end card: UNITREE wordmark + a block of safety disclaimers on black.

## Cut rhythm
- 13 shots in 50.0 s (adaptive detector; ffmpeg scene found only 7 in the dark stage footage). ASL 3.84 s, median 2.12 s, 7.7 % under 1 s, 15.6 shots/min.
- ASL per quarter 6.25 / 4.16 / 4.16 / 1.56 s: it opens with long real takes and accelerates into the runway montage (cuts per 10 s: 1, 1, 1, 3, 6).
- Longest 13.88 s (orbit), 10.16 s, 6.24 s. Shortest real shot 1.04 s.

## Typography
- Title (thumbnail frame only): rounded geometric sans (closest free: Poppins Medium / Nunito Bold), sentence case, ≈9 % frame height per line, three lines right of centre, purple-to-gold gradient fill. No other text during the film.
- End card: UNITREE italic wordmark ≈18 % H; first disclaimer lines ≈3.3 % H, bullet lines ≈2.3 % H, white, centred. The block says this is extreme testing that should not be imitated, features vary by version, and buyers should understand the limits of humanoids.
- No speed label, no "autonomous" or "teleoperated" label, no specs.

## Colour/grade
- Theatre: dark blue-grey with warm stage backdrop; runway: warm gold arches, white marble; stadium: cool grey. Mild contrast, no letterbox, clean digital look.

## Camera/shots
- Gimbal orbits and slow tracking at robot height (24-35 mm look), whole body in frame; one face close-up.
- Real people in many frames: crew watching the dance, a human model walking beside the robot. One CGI shot before the end card.

## Transitions
- Hard cuts; one 0.2 s dip to black before the end card (47.7 s).

## Sound
- One electronic track at broadcast-loud level: integrated -6.9 LUFS, loudness range only 0.8 LU, true peak +1.9 dBTP (over the -1 dBTP limit). No drop-outs; music cuts at 48.3 s (1.6 s silence under the end card).
- Cuts on audio onsets 25 % (chance 12 %): loosely on the beat.

## What makes it premium / credible
- The first 14 s is one uncut camera orbit of a full-size humanoid dancing: hard to fake.
- Real venues with real bystanders; the runway pairing with a human shows scale and gait directly.
- Weak spots: no word on how the motions are made (learned policy, motion capture replay or remote control), no speed statement, one CGI shot, very loud master.

## Recipe
- Open on the product doing its most fluid move in one 12-15 s gimbal orbit (`speed ≈ 20°/s`), no title over it.
- Second act: the machine next to a person doing the same thing (walk side by side), 1-2 s shots cut every 2 beats.
- Thumbnail frame: if the platform shows frame 1, put a 0.3 s title card first (Poppins 500, 9vh, gradient `linear-gradient(90deg,#8a5cff,#e8b45a)` with `background-clip:text`).
- End card on black: wordmark 18vh + small honest limits text 2.3-3.3vh. Master at -14 LUFS, not -7.
