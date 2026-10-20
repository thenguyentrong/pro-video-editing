# time to do your streakity  (Duolingo, 2026-10-07, 7.5 s, 9:16, YouTube Shorts / TikTok cross-post)
URL: https://www.youtube.com/shorts/3OTzXpz0rOw
Purpose: social reel (foreign-language audio meme + translation)
One-sentence point: A viral Russian meme song, translated word by word in app tiles, turns a brainrot trend into a tiny language lesson.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0 hook: no intro. Frame 1 is already the gag: Duo is the rope in a tug-of-war between a Minecraft-Steve look-alike (left half: Minecraft screenshot) and a pirate bear (right half: yellow Backrooms wallpaper). Russian lyric "Верити" + tile "Verity's" pop on at 0.0 s.
- 0.0-3.9 line 1: "Верити с Майнкрафта" -> tiles "Verity's / from / Minecraft" (complete at 1.5 s), held 2.4 s while the tug continues.
- 4.0-6.6 line 2: "Ему место в Бэкрумс" -> "He / belongs / to / Backrooms" (one tile per word, 4.0, 5.0, 6.0, 6.5 s).
- 6.6-7.5 end: same pose as frame 1, so the video loops seamlessly. No logo, no CTA.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 1 shot, 7.5 s (ASL 7.5). The rhythm comes from the word tiles (7 pop-ons in 6.5 s, ~1 per 0.9 s) and the looping 2D tug animation, not from cuts.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Layer 1, the original lyric: Feather Bold / Nunito ExtraBold-like, no box, teal (line 1) and yellow-orange (line 2) with a thin dark outline, cap 2.3 % H, at ~22 % H.
- Layer 2, translation: Duolingo word-bank tiles (white, grey bottom edge), tile height 6.3 % H, text cap 2.3 % H, row at 25-31.5 % H, x 7-91 % W. Word-by-word, synced to the sung word.
- Max 1 lyric line + 4 tiles (about 8 words). All text in the upper third, away from the platform UI at the bottom and right.

Colour/grade: palette, contrast, grain, letterbox
- Two worlds split by a vertical torn edge at ~42 % W: grey-green Minecraft left, flat yellow Backrooms right. Characters are flat 2D cut-outs with thick black outline. Full-bleed.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- 2D cut-out animation (limited animation, characters bob ~2 poses/s) over game-screenshot backgrounds. Locked frame, no camera move.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- None.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Russian meme song with vocals is the whole soundtrack; integrated -11.5 LUFS, 2.1 onsets/s; no VO, no SFX. Trending-audio play: the brand adds the translation, which is its product.

What makes it premium (3-5 bullets)
- Rides a trending foreign sound but adds a reason only Duolingo has: the translation.
- Two caption layers (source + translation) read like a lesson in 7 s.
- Single shot that loops perfectly: watch time can exceed 100 %.
- Internet references (Minecraft, Backrooms) stacked in one frame for the core Gen Z/Alpha audience.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 7.5 s, one locked shot (real footage: two locations split with a torn-paper mask at x 450 px, or one location + a 2D sticker layer).
- Lyric line: font Nunito 900, 44 px cap (2.3 % H) at y 420 px, color #1CB0F6 then #FFC800, `-webkit-text-stroke: 3px #3C3C3C`. Reveal per word with `tl.set(word,{autoAlpha:1}, t)`.
- Tile row under it at y 480-600 px, tile height 120 px, gap 16 px, text Nunito 700 44 px #3C3C3C, pop-on `from {y:12, autoAlpha:0, duration:0.06}`.
- End frame = first frame (hold the same pose) so the loop is invisible; no logo.
