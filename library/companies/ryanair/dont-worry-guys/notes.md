# don't worry guys  (Ryanair, 2026-10-02, 6.0 s, 9:16, TikTok cross-posted to YouTube Shorts)
URL: https://www.youtube.com/shorts/cl3kZ7qBD80
Purpose: social reel (topical football banter)
One-sentence point: After a bad result for Manchester City, Ryanair jokes that it can still fly City fans to Luton.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0 hook: a Ryanair 737 on final approach, filmed through an airport fence like a planespotter's phone clip; text "don't worry City fans," is on screen from frame 1 (the target group is named in 3 words).
- 0.0-3.0 build: the plane descends and touches down; the text waits.
- ~3.0 payoff: lines 2-3 appear: "we can still fly you / to Luton" (the joke is in the destination).
- 3.0-6.0: the plane taxis out of frame right. No logo, no end card.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 1 shot, 6.0 s, handheld pan following the plane. Rhythm = one text reveal at the halfway point.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- TikTok in-app "Classic" text: white, thin black outline, lowercase start, centred, cap ~3.3 % H, 3 lines at 18-33 % H (top third, clear of the bottom UI). Two-step block reveal (4 words, then 11), no animation.

Colour/grade: palette, contrast, grain, letterbox
- Flat overcast daylight, grey sky, green grass; ungraded phone footage.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- One handheld phone shot from behind a fence (UGC aesthetic even though it is the brand's own clip).

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- None.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Music bed plus a "Woo!" (auto-captions: "[music] Woo!"); integrated -14.1 LUFS; no VO.

What makes it premium (3-5 bullets)
- Speed: posted the day after the match, reacting to fan culture while it is hot.
- The text is the whole video; footage is just a moving background with the logo on the plane.
- Two-step reveal: set-up first, punch line at 50 % of the runtime.
- Zero production cost: proves tone beats polish on TikTok.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 6 s, one real handheld clip of the product in its natural place.
- Text: `font: 500 60px "TikTok Sans", "Proxima Nova", sans-serif; color:#fff; -webkit-text-stroke: 2px #000; paint-order: stroke fill; text-align:center`, block top at y 340 px, max width 900 px.
- `tl.set(line1,{autoAlpha:1},0); tl.set(lines23,{autoAlpha:1},3.0)`. No logo, no end card; post within 24 h of the news event.
