# LEGO Spider-Man swings through NYC! | Stop motion BTS  (LEGO, 2026-09-13, 19.6 s, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/rPUrpJDGhBE
Purpose: behind-the-scenes social cut of a brickfilm (product: buildable Spider-Man figure)
One-sentence point: A stacked split screen shows the animator posing the figure by hand on New York streets (top) and the finished stop-motion result (bottom) at the same time.

Structure: beats with timestamps
- 0.0-2.6 hook: split screen from frame 1 (phone with the figure on screen above, the animated figure below); 3-line title on the seam.
- 2.6-12.8 BTS montage: the animator on sidewalks, a bridge, a library, Times Square; each set-up ≈1-2 s; stop-motion poses step at ≈12 frames per second in the bottom half.
- 12.8-19.3 faster finale: more locations, swinging poses, a "web" line; legal line fades in at ≈17 s at the bottom.
- 19.3-19.6 end: an orange light-leak flash wipes the frame; the clip loops.

Cut rhythm
- Detector: 32 shots, ASL 0.61 s, median 0.33 s, 81 % < 1 s; adaptive finds 54. Both count stop-motion pose steps (≈0.08-0.1 s) as cuts. By eye ≈14 location set-ups in 19.6 s (≈1.4 s each).
- Quarters (detector) 1.64 / 0.41 / 0.55 / 0.45 s: a slower hook, then constant speed.

Typography
- Title "BTS: LEGO Spider-Man in NYC": bold rounded sans, white with a black outline/shadow, 3 lines, cap ≈4 % H, centred at 44-57 % H (sits on the split seam at ≈50 % H), on 0.0-2.6 s. Closest free: TikTok Sans 700 or Nunito 800 with a 3 px black stroke.
- Legal line: white, cap ≈1.2 % H, 3 lines at 85-90 % H in the last ≈2.5 s.

Colour/grade
- Natural summer daylight in the city, phone colour; the red/blue figure is the accent in every frame.

Camera/shots
- Top: handheld phone BTS (hands, animator, phone screen showing the frame). Bottom: locked low-angle phone stop-motion with real city backgrounds.

Transitions
- Hard cuts in both halves; one light-leak flash at the end (loop point).

Sound
- One song with a sung hook (the brickfilm's soundtrack); -12.7 LUFS, peak -0.2 dBTP.

What makes it premium
- Process and result in one frame: the viewer sees the craft and the payoff together.
- Real locations + a toy = scale contrast every second.
- The text says "BTS" in the first frame, so the format is clear instantly.

Recipe (real footage + HTML/GSAP, 1080x1920)
- Two 1080x960 clips stacked (`top:0` and `top:960px`), same timeline; BTS cuts every 1-2 s, stop-motion at 12 fps (hold each frame 2 frames at 24 fps).
- Title `800 76px "TikTok Sans"; color:#fff; -webkit-text-stroke:3px #000; paint-order:stroke fill; text-align:center`, centred on y 960 px, 0-2.6 s.
- End flash: orange radial gradient `autoAlpha 0→1→0` over 0.3 s with `mix-blend-mode:screen`, then loop.
