# Introducing Stripe Radar  (Stripe, 2016-10-19, 100.7 s, 16:9, YouTube; best available 360p)
URL: https://www.youtube.com/watch?v=NWywn0yympA
Purpose: launch film (software product: fraud prevention), customer-story format
One-sentence point: A fast-growing online shop and the Stripe engineers behind the new fraud tool explain how it blocks bad payments without slowing real customers.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-11.0 hook (0-11 %): no title. Macros of a screen-printing press, wide factory shots, staff folding shirts: the customer's physical world.
- 11.0-17.0 (11-17 %): the customer's shop on a laptop (a "shirts sold" counter ticks up), then a wide of the Stripe office with the logo on a wall.
- 17.0-47.0 (17-47 %): Stripe engineering lead interview (lower third at 17.5 s) cut with staff at laptops, a filmed dashboard screen, and a dark, slow shot of code on a laptop (37-43 s, the longest shot, 6.2 s).
- 47.0-80.0 (47-80 %): the customer's risk analyst interview (lower third at 48.5 s) + filmed close-ups of the rules UI (cursor clicks "Add rule", 60-74 s) + office wides. This is the product proof.
- 80.0-90.0 (80-90 %): wider Stripe platform: filmed web pages, an LED logo wall at the customer, code on a monitor.
- 90.0-96.4 (90-96 %): payoff: a phone purchase, shop pages, people wearing the shirts (≈1 s each).
- 96.4-100.7 (96-100 %): end card: violet-pink gradient with angled translucent stripes, white wordmark centre, URL below. Fade to black.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 41 shots, ASL 2.45 s, median 2.17 s, 5 % under 1 s, 24 % over 3 s, 25 shots/min. Quarters 2.29 / 2.80 / 2.10 / 2.10 s: steady documentary pace, a bit slower in the middle (interview-led).
- Longest 6.2 s (code on laptop, 37 s), 5.2 s (end card), 5.0 s (interview). Shortest 0.8-0.9 s (shirt montage, UI angle change).
- Densest 60-70 s (6 cuts / 10 s, the rules UI).
- Verified by eye; two cuts added between filmed UI angles (62.4 / 64.2 s); one false 0.05 s cut on the last frame removed.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Lower thirds: humanist sans (Stripe's 2016 face, Camphor-like; free: Source Sans 3). Name semibold navy, cap ≈3.8 % H; role regular ≈3 % H. Set on 3-4 angled translucent ribbons (lavender, violet, peach gradient) bottom-right, from x ≈52 % to the right edge, y ≈70-95 % H. Ribbons slide in diagonally, hold ≈3 s.
- End card: white wordmark ≈12.5 % H tall, centred at y ≈50 %; URL light white ≈6 % H at y ≈88 % H. Hold ≈4 s.
- No title card, no captions, no on-screen claims. UI text is read from the filmed screen.

Colour/grade: palette, contrast, grain, letterbox
- Natural daylight documentary look: warm interiors (tungsten bokeh behind interviews), cool daylight factory. Brand only in graphics: gradient ≈#8052d9 → #cd7dee with peach accents. No letterbox.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Interviews: single camera, off-axis eye line, shallow depth of field, slow push. B-roll on sliders and handheld. The software is FILMED on real laptops and monitors at an angle with shallow focus (not screen-captured), cursor visible.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts (≈39 of 40). One slow dissolve/rack inside the dark code shot; fade to the end card.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Voice: interview bites only (Stripe engineer + customer analyst), from 1.9 s to 92.8 s, ≈90 s of speech (≈3.5 words/s): wall-to-wall talk. No narrator.
- Music: soft electronic pulse, low under the voice. Integrated −18.1 LUFS, LRA 2.5 LU (very flat), true peak −2.0 dBTP. No drop-outs. Biggest rise +21 dB at 41.3 s (music swell under the code shot).
- Cuts follow sentences, not the beat (40 % on onsets vs 53 % chance).

What makes it premium (3-5 bullets)
- A product nobody can see (fraud scoring) is shown through people, a real shop and real screens.
- Filmed UI, not screen capture: the software lives in a physical, lit world.
- Two voices only, both experts; no announcer, no hype words.
- Brand graphics only twice (lower thirds, end card), both in the same ribbon system.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920×1080, 90-100 s, ASL 2.2-2.6 s. Order: customer world 10 s → product context 6 s → expert 1 (30 s) → expert 2 + filmed UI (33 s) → platform 10 s → payoff montage at ≈1 s/shot 6 s → end card 4 s.
- Shoot the UI on a real monitor, 30-45° angle, f/2 depth, slow slider; or composite a capture onto a monitor plate with `perspective(1200px) rotateY(-25deg)` and a 2 px blur falloff mask.
- Lower third: three `div` ribbons `transform: skewY(-12deg)`, `linear-gradient(90deg,#c9b8f5,#8052d9)` + one peach `#f6a68b` at 60 % opacity; slide `x:+30% → 0` stagger 0.08 s, 0.5 s `power3.out`; name `Source Sans 3 600 3.8vh #1d2a50`, role `400 3vh`.
- End card: `linear-gradient(110deg,#8052d9,#cd7dee)` + 5 translucent skewed bands drifting `x ±3%` over 4 s; wordmark 12.5 % H white; URL 6 % H white 80 %.
- Sound: voice-led, bed at −30 dBFS under speech, master −18 LUFS.
