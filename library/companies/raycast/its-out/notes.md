# It's out  (Raycast, 2026-05-14, 160.6 s, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=uJ70iGerYzE
Purpose: launch film, founder/team-led (the rebuilt Raycast opens as a public beta)
One-sentence point: The new Raycast is out today as a public beta; here is what changed, how to switch, and where to learn more.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-2.1 (0-1 %) cold open: the presenter (a Raycast team member speaking for the company) to camera, one line.
- 2.1-7.0 (1-4 %) proof: the new website hero ("The next generation of Raycast is here") as a screen insert.
- 7.0-24.9 (4-16 %) why: presenter explains the rebuild, cutting between two camera angles.
- 24.9-38.1 (16-24 %) how to get it: download page with the beta button, the app window, the "Transfer your data" screen.
- 38.1-63.5 (24-40 %) what is in it: presenter; a "Public Beta" title card with the glowing app icon (47.3-50.7); a three-item feature list set beside the presenter (54.5-58.5).
- 63.5-84 (40-52 %) the launcher in use: two screen-recording inserts of typing and results, presenter between them.
- 84-106 (52-66 %) presenter only, longer takes.
- 106-114 (66-71 %) the new online manual (site scroll inserts).
- 114-143 (71-89 %) presenter, the two longest takes (13.4 s and 11.0 s).
- 143-148 (89-92 %) the release blog post.
- 148-160.6 (92-100 %) sign-off to camera. No end card, no logo.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 31 shots (verified on the cut sheet; 2 insert cuts added from the adaptive detector at 26.8 and 109.7). Camera-angle changes on the presenter count as cuts.
- ASL 5.18 s, median 4.38 s, 0 % under 1 s, 81 % over 3 s. Quarters 3.65 / 4.46 / 5.02 / 6.69 s: the film slows down as it goes.
- Shortest 1.9 s (website insert), longest 13.4 s (presenter at 114 s).
- Screen inserts: 8 blocks, ≈43 s in total = ≈27 % of the runtime; presenter on screen ≈73 %.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- The house sans (closest free: Inter). No lower third with name or title.
- "Public Beta" card: Inter 400, white with a slight grey gradient, cap ≈9 % H, left of centre at ≈50 % H, the app icon (≈22 % H) to the right with a soft red glow (#ff6363 family) and a "BETA" pill. The icon arrives first (47.3 s), the words 3.3 s later; hold ≈3.4 s.
- Feature list over the presenter: Inter 500, white, sentence case, cap ≈5.5 % H, 3 lines left-aligned at x ≈66 %, y ≈37-66 %, built line by line (≈0.5 s apart), hold ≈4 s, while the shot is reframed so he sits left.
- All other words are inside the real UI or web pages.

Colour/grade: palette, contrast, grain, letterbox
- Presenter: warm home studio, amber practical lamp at frame left (#9c8e83 wall, #32211b shadows), white T-shirt, a red object as accent; shallow depth of field.
- Inserts: near-black product world (#000000-#0f1011, UI greys #383b3e) with the red brand accent. The cut between warm room and black screen is the film's colour rhythm.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Two locked cameras on the presenter: A frontal medium (eye-line to lens), B a slightly tighter angle; cuts A/B every 3-15 s on sentence ends.
- Inserts are clean screen recordings and website captures, some with a slow push; one rendered title card.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- All hard cuts (30). No graphics transitions.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Voice from first to last second (speech detected 0.0-159.9 s, ≈3.3 words/s, measured with a speech detector, not transcribed). The 32 short "drop-outs" (0.3-0.85 s) are breath pauses between sentences. A soft music bed may sit under the voice; the level data cannot confirm it.
- Integrated −14.2 LUFS, LRA 2.1 LU (very even voice), true peak −0.8 dBTP. The big "rises" (+34 to +46 dB) are voice restarts after pauses, not musical hits.

What makes it premium (3-5 bullets)
- A real person from the company speaks plainly to camera, like a creator video, not an ad.
- Two-camera coverage hides the edits in the talk and keeps the pace without jump cuts.
- Warm human room vs black product screen: every insert is a clear visual break.
- Only two designed graphics in 160 s; the product and the website do the rest.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920x1080, 2-3 min. Shoot the speaker with two locked cameras (A medium at eye level, B 15-30° off-axis and tighter), warm practical lamp in the background, key from the window side, f/2-2.8.
- Cut A/B on sentence ends every 3-8 s at the start, 8-14 s later on. Insert a screen recording every 15-25 s (2-8 s each); inserts ≈25-30 % of runtime.
- Title card: `#000`, app icon `scale .9 → 1` + glow `box-shadow 0 0 120px rgba(255,99,99,.35)` in 0.6 s; 3 s later `400 96px Inter` text `autoAlpha 0 → 1` with a `linear-gradient(90deg,#fff,#bbb)` text fill; hold 3.4 s, hard cut.
- Side list: reframe the speaker to the left third (`scale 1.15, x -12%`), then 3 lines `500 52px Inter` white at `left:66%`, stagger 0.5 s `y 12 → 0, opacity 0 → 1`, hold 4 s.
- Voice at −14 LUFS integrated, music bed (if any) 20-25 dB under the voice; no end card needed.
