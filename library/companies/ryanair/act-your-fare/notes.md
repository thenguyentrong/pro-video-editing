# act your fare  (Ryanair, 2026-10-08, 7.5 s, 9:16, TikTok cross-posted to YouTube Shorts)
URL: https://www.youtube.com/shorts/ZvQ4lFWNpWs
Purpose: social reel (meme template: expectation vs reality)
One-sentence point: People who pay €19.99 expect a private jet; the reality is a Ryanair tray table, and the brand laughs at them.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0 hook: stock clip of people boarding a private jet + label "passenger expectations for €19.99:" (the meme format is recognised in under 1 s).
- 0.0-4.2 build: 3 luxury stock shots (boarding 1.4 s, old man with porcelain coffee cup 1.5 s, businessman on the phone signing papers 1.25 s).
- 4.2 turn: label changes to "reality:" on a music hit (+15.6 dB at 4.2 s): handheld phone shot of a Ryanair tray table, whip tilt up to the safety card (5.0-5.1 s, in-camera).
- 5.75-7.1 payoff: a passenger in a Ryanair seat with his hands over his face.
- 7.1-7.5 sting: 0.42 s flash of the plane face laughing. Hard end.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 6 shots (cuts2 found 4, 1 missed hard cut at 5.75 s added by eye), ASL 1.26 s, median 1.35 s. Quarters 0.94 / 0.94 / 0.94 / 0.63.
- Cuts land on audio onsets (100 % vs 19 % chance). Expectation half uses polished stock; reality half uses shaky phone footage: the contrast is in the camera, not only the content.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- TikTok in-app "Classic" white with thin black outline, lowercase, cap ~3.0 % H, centred at 14-22 % H. Two cards only: 5 words (4.2 s) and 1 word (3.3 s). Hard switch, no animation.

Colour/grade: palette, contrast, grain, letterbox
- Expectation: warm, glossy stock (wood, leather, cream). Reality: cool blue-grey cabin plastic + Ryanair yellow. No grade on top.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Stock footage (expectation) vs own phone footage (reality); staged actor face-palm; plane-face composite as sting.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 5 hard cuts + 1 in-camera whip tilt.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Trend-style music with a hit at the "reality:" switch (4.2 s). No VO. Integrated -10.4 LUFS. Track not identified (no music metadata on the cross-post).

What makes it premium (3-5 bullets)
- Uses a known meme template, so the viewer does half the work.
- Self-deprecation as positioning: the low price is the joke and the message.
- The plane-face sting is a 0.4 s brand signature that replaces a logo.
- Two text cards only.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 7.5 s. Part A 0-4.2 s: three glossy stock clips of ~1.4 s. Part B 4.2-7.1 s: two phone clips. Sting 0.4 s.
- Labels: 56 px TikTok Sans / Proxima Nova 500, white, `-webkit-text-stroke: 2px #000`, top at y 270 px; `tl.set(labelA,{autoAlpha:0},4.2); tl.set(labelB,{autoAlpha:1},4.2)`.
- Put the music hit exactly on the label switch; no logo, end on the mascot sting.
