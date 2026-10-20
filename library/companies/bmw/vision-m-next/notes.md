# BMW Vision M NEXT. Official Launch Film.  (BMW, 2019-06-25, 1:37, ≈2.35:1 letterbox in 16:9, YouTube @BMW, source only 640x360)
URL: https://www.youtube.com/watch?v=81wHqxnWeHQ
Purpose: concept-car launch film (fashion-film look, score by a famous film composer)
One-sentence point: The car is made for a driver who wants to be in control and to feel it.

## Structure
- 0-1.0 black. 1-15 **dark tease**: a figure in red light, the headlights, red light lines across the body, wide shot of the car on a mountain road, the car alone in a grey studio. Shots 0.5-2 s.
- 15.2-19.2 **the question**: a model on a solid red background with "WHO ARE YOU?" split around her (16-17 s), then "A DRIVER?" small red on black (18.1-19.2 s, black hold 1.12 s, 0.45-s silence at 18.75 s).
- 19.25 hit; 19-58 **build**: portraits of models (red light stripes on faces, a hand on a cheek, an eye), macro details of the car body, aerials of a serpentine road, a red grass field. Voice-over enters at ≈18 s and runs as a slow poem.
- 58-66 interior UI: yellow boost graphics, a heart-rate line, a gear-shift display.
- 66-88 fastest part: car on the road, faces, wheel macro, aerial, 0.4-0.9 s shots.
- 88.6 "DRIVE" in red over an aerial road (1 word); 89-93 the car drives into the sunset (longest shot 4.5 s).
- 93-95.4 "M NEXT" wordmark on black; 95.4-97.4 BMW roundel plate on black, 2.5 s silence.

## Cut rhythm
- 83 shots in 97.4 s. ASL 1.17 s, median 0.92 s, 54 % under 1 s, 51 shots per minute.
- ASL per quarter 1.43 / 0.94 / 1.06 / 1.22 s.
- Cuts per 10 s: 6, 7, 9, 8, 12, 7, 11, 14, 7, 1; peak 70-80 s.
- Longest 5.04 s (34.96, aerial), 4.50 s (92.92, end), 4.32 s (88.6, "DRIVE" aerial). Shortest 0.24 s.
- Note: dark film; the adaptive detector finds 82 cuts, the scene detector only 35.

## Typography
- Bold grotesque caps (closest free: Inter Bold / Archivo Bold), tight tracking.
- "WHO ARE YOU?": black on red, ≈8 % H, split left/right of the figure at y ≈50 %.
- "A DRIVER?": red on black, ≈2.5 % H, centre (small after big = a whisper after a shout).
- "DRIVE": red, ≈7.5 % H, centre, over landscape.
- HUD graphics in acid yellow (#e6e600-ish) only inside the car.

## Colour/grade
- Black, steel grey and one signal red; acid yellow for the UI only; blue-hour landscapes. High contrast, crushed blacks, letterbox ≈2.35:1 (bars ≈12 % top and bottom).

## Camera/shots
- Fashion-film portraits (models styled with red light stripes), studio car on a grey stage, extreme macro of body lines, aerials of mountain roads, a few tracking shots. Many shots start in darkness and are revealed by light.

## Transitions
- Hard cuts; black hold 1.12 s at 18.1 s; fades only on the wordmarks.

## Sound
- Orchestral-electronic score with a big entrance at 19.25 s after a 0.45 s silence; a calm spoken poem from ≈18 to ≈95 s. Integrated -10.0 LUFS, LRA 8.1 LU, true peak +0.6 dBTP. Loudest 0.5 s at 65.1 s. 2.5 s silence at the end.

## What makes it premium
- Strict three-colour system (black, steel, red) with one extra colour for the digital world.
- A question on screen, then silence, then the music: classic anthem turn at 20 % runtime.
- People are styled like the car (red light lines on skin = red lines on the body).

## Recipe
- Letterbox `clip-path: inset(12% 0)`; grade `contrast(1.25) brightness(.85)`, push reds.
- Question card: solid `#d0021b` background, figure cut-out in the middle, two words left/right at 8vh `Inter 800`; then small red text on black 1.1 s with music cut (`volume: 0` for 0.45 s), hit on the next shot.
- Build 60-70 shots at 0.4-1.5 s, peak at ≈75 % runtime; one red word over the final aerial; wordmark and logo on black with 2.5 s silence.
