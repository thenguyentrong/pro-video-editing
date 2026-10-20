# The Rise of Eileen Gu  (Red Bull Snow, 2026-01-23, 13:38, 16:9, YouTube / Red Bull Snow channel)
URL: https://www.youtube.com/watch?v=BVzP_NXZowM
Measured: first 300 s only (of 818 s). Everything below is about 0:00–5:00.
Purpose: athlete documentary (portrait of a champion freeskier who is also a student and model), released before a Winter Olympics
One-sentence point: the film follows one athlete across training, competition and her public life to show how she combines all of it.

Structure (first 5 min):
- 0–13 COLD OPEN IN FOG: the athlete in helmet and goggles talks to a handheld camera at the top of a foggy slope (≈1 s drop-out to -43 dB at 6.6 before her line); she drops in, small in a white frame.
- 13–37 THREE WORLDS INTRODUCED: an empty white halfpipe, a photo wall of her career (framed prints shown inside a white "viewfinder" border with crosshair and corner marks), a sit-down interview outdoors on a lawn (shallow focus, 3/4 profile), the helmet talk again.
- 37–100 TRAINING: slow, patient shots: skis on snow, a 10.3 s helmet close-up with goggles (45.8), long wides of her running the pipe in fog (56–72, cuts every 5–10 s), interview inserts.
- 100–160 COMPETITION (densest, 6–8 cuts per 10 s): viewfinder inserts with a location tag (place name in small bold caps top-left), slopestyle and big-air runs, GoPro and broadcast angles, podiums, sponsor walls, interviews in the finish area.
- 160–180 back to the photo wall and the helmet close-ups (180–190 in the start gate).
- 190–250 a halfpipe final at night: broadcast-style follow shots, crowd, press zone, medal.
- 250–288 PUBLIC LIFE: a city skyline over water, then a hosted sit-down interview on a terrace (11.9 s and 12.8 s holds, the longest shots).
- 288–300 a 16-cut burst (0.28–0.4 s shots): cars, crowds, phones, a new chapter starts.

Cut rhythm (0–300 s): 113 shots, ASL 2.65 s, median 1.68 s (adaptive detector; the scene detector found 91, missing cuts in white fog). ASL per quarter 3.95 / 1.74 / 3.26 / 2.42 s. 21 % of shots under 1 s, 32 % over 3 s. Cuts per 10 s: 2, 4, 3, 3, 1, 1, 2, 3, 3, 5, 6, 6, 6, 7, 8, 5, 2, 3, 2, 3, 1, 3, 4, 2, 2, 2, 1, 1, 5, 16. Long holds on the person (10–13 s), fast only in competition and in the closing burst. 35 % of cuts on an audio onset vs 32 % by chance.

Typography:
- Inserts framed as a camera viewfinder: footage or photos at ≈76 % width on a white ground, thin white corner ticks, a centre crosshair, small dots; a location tag in bold sans caps ≈1.8 % H top-left inside the frame (closest free: Inter 700).
- No big titles in the first 5 min; no lower thirds for the athlete (she is the film). Broadcast graphics and sponsor walls appear as they were filmed.

Colour/grade: two looks: white, low-contrast fog and snow (almost monochrome, the athlete's dark suit as the only shape), and saturated competition colour (blue sky, sponsor colours, night lights). Interviews warm and soft. 16:9.

Camera/shots: handheld talk-to-camera on the mountain, helmet close-ups, long-lens wides of runs, POV/GoPro, broadcast follow cams, sit-down interviews (outdoor lawn, hosted terrace), observational public-life footage.

Transitions: hard cuts; the viewfinder frame acts as a graphic transition (footage scales into the white frame).

Sound: (I could not listen; from level data.) Integrated -15.0 LUFS, LRA 5.6 LU, true peak -0.1 dBTP (too hot): music-led and fairly loud for a doc; -14…-21 dBFS in every 10 s window. One clear drop-out (1 s, -43 dB) in the cold open before her first line. Biggest rises +18–19 dB at 169.0 and 179.3 (competition).

What makes it premium:
- The athlete speaks first, to camera, on the mountain, before any polish.
- White fog used as a design: a near-blank frame with one dark figure.
- A simple graphic system (viewfinder frame + location tag) for all inserts and archive.
- Pace follows the life: slow in training, fast in competition, very fast in public life.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- Cold open 13 s: handheld talk-to-camera, a 1 s drop before the first line, the drop-in as a small figure in a white frame.
- Viewfinder insert: stage `#f7f7f7`; clip at `width:76%` centred; 4 corner ticks (2 px white lines 3 % long), crosshair `⊕` 1.5 % H; tag `700 1.8vh Inter; text-transform:uppercase; left:3%; top:3%`; clip scales from 100 % → 76 % in 0.5 s `power2.inOut`.
- Training: 5–10 s wides and 10 s close-ups; competition: 1–1.5 s; closing burst 16 cuts in 10 s.
- Hosted interview holds 12–13 s. Master -15 to -16 LUFS, true peak ≤ -1 dBTP.
- Stock queries: `freeskier halfpipe fog`, `ski goggles helmet close up`, `big air skier blue sky`, `city skyline terrace interview`.
