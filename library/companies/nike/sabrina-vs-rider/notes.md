# Sabrina vs. The Rider | Nike  (Nike, 2026-09-02, 27.5 s, 2:3 (720x1078) posted as a Short, YouTube Shorts / Reels)
URL: https://www.youtube.com/shorts/jx3yiH1M0lc
Purpose: social reel / launch tease (Sabrina 4 "The Switch"), comedy sketch
One-sentence point: Sabrina Ionescu turns pressing the elevator button into a competitive race with a stranger: "No moment is too small to win."

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-2.1 hook: black title cards "NIKE BASKETBALL PRESENTS:" (0-1.0 s) and "Sabrina vs. The Rider" (1.0-2.1 s): framed as a match, so you wait for the contest.
- 2.1-2.8: CU finger presses an elevator button.
- 2.8-8.3 set-up: high-angle CCTV wide, a woman in black alone in a wood-panelled elevator; Sabrina (pink hoodie, basketball) steps in at 4.9 s.
- 8.3-15.8 build: CU deadpan Sabrina, both reach for the panel, tension.
- 15.8-23.4 turn/payoff: VHS-glitch race to the buttons, shoe insert (pink Sabrina 4 at 16.3 s), the rider's bag on the floor, Sabrina leaves victorious.
- 23.4-27.5 end cards on black: "ANYTIME ANYWHERE", "SABRINA 4" logotype, swoosh.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 11 shots, ASL 2.50 s, median 2.13 s, 18 % under 1 s. Quarters 1.38 / 2.29 / 1.72 / 3.44. Longest is the CCTV wide (5.6 s); product insert 1.0 s.
- Cuts land on audio onsets 70 % (vs 45 % chance): dings and stings.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Title cards: white-to-purple/pink gradient type on pure black, a tiny purple square bullet before the text. "NIKE BASKETBALL PRESENTS:" condensed bold caps; "Sabrina vs. The Rider" a serif upper/lower. Line box 3.3-3.8 % H (cap ~2.5 % H), centred at 50 % H, ~1 s each, hard cut on/off.
- End: "ANYTIME ANYWHERE" extended bold caps gradient, "SABRINA 4" logotype, swoosh with RGB split.
- No subtitles (no dialogue).

Colour/grade: palette, contrast, grain, letterbox
- Warm orange wood elevator, magenta hoodie and shoes, low-fi CCTV look: soft, slightly washed, chroma bleed and VHS tracking lines at 2.5, 14-15 and 17 s.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Fixed security-cam wide (fish-eye high corner) + handheld CU inserts (face, hand, shoe). Real athlete as actor.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts, plus glitch frames inside shots.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Room tone, elevator ding, music stings at the race; 2 drop-outs (6.0 s, 27.0 s). Integrated -19.7 LUFS. No VO.

What makes it premium (3-5 bullets)
- Big-sport framing ("presents", "vs.") applied to a tiny everyday moment = the joke and the brand line.
- Found-footage CCTV makes a celebrity sketch feel like a viral clip.
- Product appears once, in a 1 s insert, in the hero colour.
- Clean black title/end cards bracket a messy middle.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1620 (2:3) or 1080x1920 with the same layout; 27 s, ~11 shots.
- Title cards: black 1.0 s each; `font: 800 44px "Barlow Condensed"` caps, `background: linear-gradient(90deg,#fff,#B07CFF 60%,#FF4FD8); -webkit-background-clip:text; color:transparent`; second card in `500 44px "Tiempos"`.
- CCTV look on real footage: `filter: saturate(.8) contrast(.9) blur(.4px)`, barrel distortion via SVG displacement, and a VHS glitch layer: 3-6 px tall horizontal bands offset `x: ±12px` for 2-3 frames at chosen beats; timestamp optional.
- End cards: extended bold caps (Archivo Expanded 900) gradient, swoosh/logo with red/blue `drop-shadow(-3px 0 #f0f) drop-shadow(3px 0 #0ff)`.
