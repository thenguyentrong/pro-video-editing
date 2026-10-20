# Turning An F1 Car Into A TRAIN  (Red Bull, 2026-10-10, 10.6 s, 9:16, YouTube Shorts / TikTok)
URL: https://www.youtube.com/shorts/4UjamzoAlJA
Purpose: social reel (stunt reveal + behind the scenes; 5.0 M views)
One-sentence point: A Red Bull F1 car rolls out of a metro tunnel on train wheels: "fastest commute ever?"

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-1.5 hook: locked phone shot of an empty metro platform, caption "fastest commute ever?" (the question sets the expectation).
- 1.5-3.5 payoff first: headlights in the tunnel, the F1 car rolls along the rails (2.0-2.5 s) and passes the camera in a motion blur (3.0-3.5 s).
- 3.5-4.7: it continues down the platform.
- 4.7-10.6 behind the scenes: crew lifts a wheel (4.7 s), fits rail wheels (6.3 s), driver in the cockpit (8.0 s, CU 9.0 s). Ends abruptly.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 5 shots, ASL 2.13 s, median 1.62 s. Quarters 2.67 / 1.33 / 1.33 / 0.89: one long reveal shot (4.7 s), then accelerating BTS cuts (1.6, 1.7, 1.0, 1.6 s).

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Bold italic sans, white, soft shadow, lowercase question, centred at 65.6-67.8 % H, x 20-80 % W; glyph line 2.3 % H (cap ~1.7 % H). One card, 0-4.7 s, gone when the BTS starts.

Colour/grade: palette, contrast, grain, letterbox
- Fluorescent metro light, blue ceiling, white tiles; navy/red/yellow livery pops. No grade.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Locked phone wide for the reveal (vanishing-point composition, car enters from the tunnel), handheld BTS mediums and a CU.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 4 hard cuts.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Engine and rail noise, station ambience; integrated -13.8 LUFS; sparse onsets (0.47/s). No VO, no music detected.

What makes it premium (3-5 bullets)
- Absurd juxtaposition readable in one frame (F1 car + metro).
- Question caption invites comments; the answer is shown, not told.
- Payoff first, explanation after: viewers stay for "how".
- Short (10.6 s) and ends abruptly on BTS, so the replay starts on the empty platform again (loop).

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 10-11 s: 1 locked reveal shot 4.5-5 s (subject enters from depth and passes the lens), then 4 BTS shots of 1.0-1.7 s.
- Caption: `italic 700 40px Poppins`, white, `text-shadow 0 2px 6px rgba(0,0,0,.5)`, centre y 1435 px, only during the reveal.
- No end card; cut out on a mid-action BTS frame for a seamless loop.
