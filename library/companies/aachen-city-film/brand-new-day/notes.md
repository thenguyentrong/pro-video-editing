# Brand New Day | Aachen | Fujifilm X-S20  (independent creator Dev Kabra, 18 Oct 2026, 1:50 / 110.4 s, 2.39:1 picture delivered as 854×358, YouTube)
URL: https://www.youtube.com/watch?v=1D6z-HkgBHs
Purpose: personal city film (a "city as a movie" reel), made with one consumer camera and film-simulation looks
One-sentence point: an ordinary university city, framed like the opening titles of a superhero film, with jokey credits that cast local places and things as the stars and crew.

Structure (cut times from metrics.json; the new sheet labels are exact):
- 0–1.92 black. Music starts at 0.5 s (first onset), so the song plays 1.4 s over black.
- 1.92–5.24 hook: wide street corner, title "BRAND NEW DAY / IN AACHEN" in the centre.
- 5.24–25.4 "production" credits: Marvel-style studio line, "written by", "edited in", featuring ... strangers, students, the two leads who are NOT in the film.
- 25.4–98.7 the "cast": landmarks, a cafe, a canteen, a park with sheep, the weather, a volleyball court, the buses, clothing, plus self-aware jokes ("if you're still watching ...", "slowly running out of things to say"). One credit per shot, 23 shots.
- 98.7–105.3 the authors: camera, lens maker, the creator's name, "edited by also me".
- 105.3–108.3 last card: the franchise title it borrows, as a homage, over a church tower against sky.
- 108.32–110.4 black (2.1 s).

Cut rhythm: 34 shots (32 picture shots + black open + black end). ASL 3.25 s, median 3.32 s, 0 % under 1 s, 91 % over 3 s, 18.5 shots/min. The picture shots are 3.24–3.44 s long: a cut every ≈3.33 s from 1.92 to 108.32, so every 10 s window has exactly 3 cuts (cuts per 10 s: 3,3,3,3,3,3,3,3,3,3,3). ASL per quarter 3.07 · 3.07 · 2.76 · 3.07 (Q3 lower only because a black hold is split). This is a metronome grid; ≈3.33 s equals one 4/4 bar at 72 BPM (my inference, not measured from the beat). Cuts on onsets 9 % vs 8 % by chance: the song has few sharp onsets (0.38 per s), so the grid follows bars, not hits.

Typography (measured on 854×358 frames; % of the PICTURE band height, then of a full 16:9 frame in brackets):
- One two-tier credit block for every card: small role line above a larger name line, all caps, centred on each other, white, no box, no shadow.
- Role line ink 9 px = 2.5 % (≈1.9 % of a 16:9 frame); name line 15 px = 4.2 % (≈3.1 %). Gap between the lines ≈11 px (≈0.7 × name height). Title block uses the same sizes as the credits (title 15 px).
- Face: light-regular geometric sans, wide tracking (≈0.15–0.2 em on names, a bit wider on roles). Closest free font: Montserrat 300–400.
- Width: names 20–28 % of frame width.
- Placement changes with the shot: centre (title, 49 % x), right third (x 70–94 %, y 54–64 %), bottom centre over a dark table (y 82–92 %), upper right in sky (x 57–78 %, y 32–41 %), bottom left, top centre. Always in a calm area: sky, wall, floor, lawn.
- Animation: NONE. Frame strips at 25 fps show the credit fully on from the first frame of the shot to the last; it cuts in and out with the picture.
- 32 text cards in 110 s (one per shot), 2–9 words each.

Colour/grade: warm, soft film-simulation look (creator credits "Fujifilm recipes"): gentle contrast, lifted shadows, slightly teal skies, warm stone. One look for the whole film. 2.39:1 delivered without bars in the file (YouTube adds them in a 16:9 player).

Camera/shots: almost all locked-off. Wides and medium wides of streets, facades, landmarks, a park, a canteen interior; low angles up at towers and facades against sky; one foreground-blur shot through glass; people small and natural. No drone, no gimbal moves, no speed ramps.

Transitions: hard cuts only (soft-transition candidates are motion inside shots). No fade from the picture to black at the end: hard cut to black at 108.32.

Sound: one song, no voice, no SFX. Integrated −18.4 LUFS, LRA 1.8 LU (extremely flat), true peak −5.1 dBTP. The music drops out for 0.8 s under the last card (107.15–107.95, floor −71 dB), then one last note at 108.1, 0.2 s before the cut to black; 0.6 s of silence at the very end.

What makes it premium:
- The grid: 32 shots of the same ≈3.33 s length. The steady rhythm alone reads as "title sequence".
- Cinema frame (2.39:1) plus one warm film look on cheap gear.
- Composition first: every shot has a clean empty area where the credit sits, and the credit moves around the frame to find it.
- The words carry the humour: places credited as cast, the weather as a crew member, a wallet as producer.
- Restraint: no fades, no motion graphics, no voice, no hits.

Recipe (real or licensed footage + HTML/GSAP Hyperframes, 1920×1080):
- Frame: 2.39:1 bars of 138 px top and bottom on 1080p. Grade every clip the same: `filter: contrast(.95) saturate(.92) sepia(.06)` as a start, plus grain at 0.05–0.07 opacity.
- Grid: pick a song at 70–75 BPM (or 140–150); shot length = one bar (4 × 60/BPM ≈ 3.2–3.4 s). Lay all cuts on the bar grid: `t_i = t0 + i * bar`.
- Credit: `.role{font:400 21px/1 Montserrat; letter-spacing:.22em}` (≈1.9 % H) and `.name{font:400 34px/1 Montserrat; letter-spacing:.16em; margin-top:12px}` (≈3.1 % H), uppercase, white. `tl.set(credit,{opacity:1},t_i); tl.set(credit,{opacity:0},t_i+bar)`: on and off with the cut.
- Position each credit in the shot's empty area (store `left`/`top` per shot).
- Open with 1.9 s of black while the song starts; end with the title card, cut the music 1 s before the end of the last shot, one last note on the cut to black, 2 s of black.
- Master the song flat: `loudnorm=I=-16:TP=-1:LRA=4` for online use (the original sits at −18.4).
