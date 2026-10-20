# *Just a normal day for Caitlin Clark.  (Nike, 2026-09-22, 30.0 s, 9:16, YouTube Shorts / TikTok / Reels)
URL: https://www.youtube.com/shorts/im_a9GsANvw
Purpose: social reel / launch teaser (Caitlin 1 signature collection, "*Just ..." series)
One-sentence point: A deadpan narrator insists Caitlin Clark is "just a normal girl from Iowa" while the text proves she is not; then "NOTHING SPECIAL TO SEE HERE*".

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-2 hook: an almost empty off-white frame; tiny Caitlin at a desk eating cereal on a round rug (bottom 70-90 % H). "*Caitlin" types on top-left with the narrator's first word. Empty space + small figure + tiny text = you lean in.
- 2-21 build: the paragraph grows word by word with the VO: "...normal girl from Iowa. Raised to do normal stuff: Cereal for breakfast. Football on Sundays. Golf on her days off. Eventually, she grew up and got a job. At this job, she sells out a variety of arenas, shoots from distances previously considered unnecessary, and wears shoes with her own name on them."
- 21-26.7 turn: "The media finds all of this extremely interesting. But to her, this is all totally normal." (the text block now reaches her head).
- 26.7-29.0 payoff: hard cut to a blank card; "NOTHING / SPECIAL / TO SEE HERE*" builds word by word in huge condensed caps.
- 29.0-30.0 end card: CC monogram + swoosh, small, centre.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 3 shots: one locked 26.7 s shot, 2.3 s type card, 1.0 s logo. ASL 10.0 s. All motion comes from the type (about 2.8 words/s) and her small eating actions.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Body: condensed transitional serif (Times / Tiempos Headline Condensed-like), black on off-white #F2F2F0, sentence case, tracking about -2 %, cap 2.7 % H, line height 4.3 % H, left-aligned ragged block x 8-88 % W from 14 % H down to ~70 % H (13 lines). Hanging asterisk in the margin.
- Reveal: word-by-word in perfect sync with the VO, words stay (the paragraph accumulates to ~75 words).
- Payoff: Nike Futura Condensed ExtraBold caps, black, cap ~6 % H, leading ~100 %, centred at 40-61 % H; one word every 0.17-0.33 s; the asterisk closes the "*Just" joke.

Colour/grade: palette, contrast, grain, letterbox
- Off-white seamless, soft top light, the figure and props in natural colours (yellow shoes); no grain.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- One locked extreme-wide studio shot (subject ~20 % of H, isolated "diorama" on a rug), no camera move.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 2 hard cuts.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Deadpan male narrator (auto-captions identical to the on-screen text), soft bed, small cereal/spoon sounds. Integrated -24.0 LUFS, dialogue level.

What makes it premium (3-5 bullets)
- Understatement as flex: "normal" + proof in the same sentence.
- Editorial print typography in a feed full of bold captions: it looks like a magazine page.
- The text IS the subtitle, so it works with and without sound.
- Negative space: 70 % empty frame makes the tiny athlete the focal point.
- Series device (*Just) and asterisk payoff link all episodes.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 30 s. Background #F2F2F0; real footage of the subject shot wide on a seamless and keyed/cropped to a 360 px tall figure at y 1450-1760 px.
- Paragraph: `font: 400 52px "Tiempos Headline", "Times New Roman"; font-stretch: condensed; letter-spacing:-0.02em; line-height:82px; color:#111`, box left 86 px, top 270 px, width 860 px. Wrap each word in a span, `tl.set(word,{autoAlpha:1}, vo_word_time)` from a transcript.
- Payoff card: `font: 800 120px "Futura Condensed ExtraBold" / "Bebas Neue"; text-transform:uppercase; line-height:1`, centred at y 960 px, words added every 0.25 s; logo card 1.0 s.
- Mix VO at about -24 LUFS with a quiet bed; no music hit.
