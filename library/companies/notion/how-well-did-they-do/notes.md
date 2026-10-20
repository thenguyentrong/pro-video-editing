# How well did they do?  (Notion, 2025-09-26, 23.5 s, 9:16, YouTube Shorts / TikTok)
URL: https://www.youtube.com/shorts/DEewjtcAnlU
Purpose: social reel (event street-interview game: "Can you draw Nosy, the Notion mascot?")
One-sentence point: People at a Notion event try to draw the mascot from memory and get a red X or a green check.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-6.6 hook: wide 2-shot at a wooden event wall, host with mic + guest. Question "Can you draw Nosy?" on top and the answer key (Nosy face in a white disc) under it. Host: "Can you draw Nosy the Notion mascot from memory? Let's put it to the test."
- 6.6-20.7 game: 6 guests, each in 3 beats: wide drawing (1-1.5 s) -> CU proud reveal of the whiteboard (0.8-1 s) -> verdict freeze (0.5 s: B&W, tight on the board, hand-drawn red X or green check, Nosy disc on top). Fails first, passes later (19-23 s).
- 20.7-23.5 payoff: the best drawing with a green check, the guest waves next to the Nosy disc. No end card.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 18 shots, ASL 1.31 s, median 0.87 s, 61 % under 1 s. Quarters 5.88 / 0.84 / 0.74 / 1.18: one long set-up shot, then a very fast game loop. Shortest 0.43 s (verdict freezes).
- Audio drop-outs at 9.5, 12.0, 17.5 (1.5 s) and 23.5 s line up with verdict beats (music cut for the reveal).

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Question: white sans medium, glyph line ~3.6 % H at 10-13.5 % H, 0-6.6 s.
- Reference disc: white circle with the black Nosy line drawing, diameter ~21 % H at 17-38 % H.
- Verdict marks: hand-drawn red double-stroke X across the board, or a green rounded-square check icon (~10 % W) at the board's top edge.
- No dialogue subtitles.

Colour/grade: palette, contrast, grain, letterbox
- Warm wood wall, neutral clothes; verdict freezes switch to black and white so the red/green marks pop.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- One camera, wide 2-shot plus digital punch-ins to CU (from 1440x2560 source); freeze frames.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 17 hard cuts; verdicts are freeze + desaturate + graphic.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Dialogue and laughter over an upbeat bed; integrated -18.9 LUFS; music stops on verdicts.

What makes it premium (3-5 bullets)
- The logo IS the game: brand recall tested in public, and the viewer plays along.
- Answer key on screen from frame 1, so every viewer can judge.
- 3-beat loop per guest (draw / reveal / verdict) at under 1 s per beat.
- Fail-first order builds to a satisfying "pass" ending.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 20-25 s; set-up shot 5-6 s, then per guest 1.2 s wide + 0.9 s CU (punch-in `scale:1.6`) + 0.5 s verdict.
- Question: `500 52px Inter` white, line at y 190-260 px (10-13.5 % H); reference disc 400 px white circle with the logo at y 330-730 px (17-38 % H).
- Verdict: freeze frame `filter: grayscale(1)`, red X as two SVG paths `stroke:#E53935; stroke-width:18; stroke-linecap:round` drawn with `strokeDashoffset` in 0.15 s; pass = 120 px green (#2EB82E) rounded square with a white check, `back.out(3)` pop.
- Cut music to silence for each verdict, back on the next guest.
