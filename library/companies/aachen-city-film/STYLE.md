# Aachen city film — "opening credits" city reel

One film measured at 480p (analyze_video.py, adaptive detector, cross-checked by the scene detector: 33 vs 33 cuts, no disagreements; credit timing checked on 25 fps strips; text measured in px on 854×358 frames). The creator has no other public city films, so this folder holds one example; the grammar is compared with visit-oslo/is-it-even-a-city, which uses the same composed ≈3.3 s tableaux.

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) / LRA | Aspect |
|---|---|---|---|---|---|---|---|
| [Brand New Day, Aachen (2026)](brand-new-day/notes.md) | 110.4 s | 34 (32 picture) | 3.25 / 3.32 | 3.07 · 3.07 · 2.76 · 3.07 | 0 % / 91 % | −18.4 / 1.8 | 2.39:1 |

## Core idea
Treat an ordinary city like the opening titles of a big studio film. The pictures are calm, composed and locked-off; the credits do the storytelling and the humour. Everything else is removed: no voice, no effects, no fades, no hits.

## Rules with numbers
- **Metronome grid**: every picture shot 3.24–3.44 s (one bar at ≈72 BPM). Exactly 3 cuts in every 10 s window from start to end. No acceleration, no slow ending.
- **One credit per shot**, on for the whole shot, hard cut in and out with the picture (no fades).
- **Two-tier credit**: role 2.5 % / name 4.2 % of the picture band (≈1.9 % / 3.1 % of a 16:9 frame), caps, light geometric sans with wide tracking; gap ≈0.7 × name height.
- **Text placed in the empty area** of each shot, so the position changes almost every card (centre, right third, bottom centre, upper sky).
- **Credit order like a film**: title → studio line → writer/editor → "featuring" → leads (here: the stars who are NOT in it) → places → crew jokes → camera and lens → creator → borrowed franchise title as the final card.
- **2.39:1**, one warm film-simulation grade.
- **Sound**: one song, flat (LRA 1.8 LU), −18.4 LUFS; 1.4 s of song over black at the start; 0.8 s drop-out under the last card, one note on the cut to black, 2.1 s black tail.

## Recipe
1. Choose a 70–75 BPM song (or 140–150 half-time). Bar length = 240/BPM s. Plan `N = runtime / bar` shots (110 s → 32–33 shots).
2. Write N credits in film order; make at least half of them about real local places, and 3–5 self-aware jokes.
3. Shoot or pick locked-off wides with a big calm area. Low angles against sky give clean space for text.
4. Frame 2.39:1 (bars 138 px on 1080p). Grade all clips the same, warm and soft.
5. Credits as in the notes recipe: Montserrat 400, 21 px / 34 px on 1080p, tracking .22 / .16 em, `tl.set` on at the cut, off at the next cut.
6. Start on 1.9 s of black with the song already playing; end on the title, kill the music ≈1 s before the last cut, one final note, 2 s of black.
