# Learn Canva fast, from anywhere. #CanvaWorldTour  (Canva, 2026-09-15, 30.0 s, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/oLFjRjVrQkc
Purpose: B2B/education promo (free events + online courses), creator-style
One-sentence point: A presenter talks very fast inside a phone frame while the world behind her swaps every half second, joking that the boss wanted it under 30 seconds.

Structure: beats with timestamps
- 0.0-5.0 hook: a white meme pill at the top (the boss wants the video under 30 seconds + running emoji) and a selfie-video phone frame lying on a green rug; she starts talking at 0.0 s.
- 2.1-8.0 events: backgrounds swap to city and event footage (0.5-1.3 s each) while she talks.
- 8.0-15.1 "learn anywhere": she lists places (home, train, cafe, park, lunch); each word gets its own background (0.5-0.8 s).
- 15.1-24.5 new feature: the product UI scrolls behind the frame (2.8-3.2 s each).
- 24.5-30.0 offer + close: free, then a question to the viewer as the last line; no end card, no logo.

Cut rhythm
- 23 shots (background swaps; the presenter is one continuous selfie take), ASL 1.31 s, median 0.97 s, 52 % < 1 s, ≈46 swaps/min. Quarters 0.94 / 0.83 / 1.88 / 1.50 s: fastest on the list of places.
- Swaps land on the listed word (one place = one background).

Typography
- Meme pill: black sentence case on a white rounded pill, cap ≈1.5 % H, 2 lines, at 15-21 % H, on 0-5 s.
- Subtitles: white sentence case with a thin shadow on a faint dark box, cap ≈1.5 % H, 2 lines, at 80.5-84 % H (low, partly in the UI zone). Closest free: Figtree 500 (Canva Sans look).

Colour/grade
- Natural phone colour; backgrounds are mostly top-down lifestyle textures (green rug, gingham blanket, wood table, book pages) in warm greens and browns, plus event and UI footage.

Camera/shots
- Front-camera selfie inside a phone mockup (≈45 % W, 25-77 % H) layered over top-down flat-lays, event clips and UI screen recordings.

Transitions
- Hard swaps of the background only; the phone frame and the face never cut (continuity = trust).

Sound
- Voice + light bed; -16.4 LUFS, peak -4.1 dBTP. Two short music drops (0.55 s at 14.95 s and 28.35 s) before the feature and before the last line.

What makes it premium
- A self-aware meme hook about video length that excuses the fast pace.
- The device (phone frame over swapping worlds) shows "anywhere" literally, word by word.
- Product UI appears as a background, not a lecture.

Recipe (real footage + HTML/GSAP, 1080x1920)
- Record one continuous 25-30 s selfie; mask it into a phone mockup `width:490px; height:1000px; border-radius:60px` centred at y 480-1480 px.
- Backgrounds: 20-25 flat-lay/event clips, `tl.set` swap on each listed word (0.5-1.3 s), UI sections 2.8-3.2 s.
- Pill: `background:#fff; color:#111; font:500 32px Figtree; border-radius:40px; padding:14px 28px`, top y ≈290 px, 0-5 s.
- Subtitles at y ≈1250 px (move up from Canva's 1550 px to stay out of the bottom UI zone).
