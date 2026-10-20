# Introducing Figma's new glass effect  (Figma, 2025-07-17, 29.6 s, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=H_HN0nwdox0
Purpose: launch film / social feature reel (one feature, music only)
One-sentence point: A new glass effect with light, refraction, depth and dispersion, shown on six very different designs in 24 seconds.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-3.8 hook (0-13 %): a glass lens slides over the dark settings panel and magnifies it; pull back to the panel.
- 3.8-7.6 (13-26 %): glass sphere on black-and-white op-art stripes; the cursor drags the depth slider and the rainbow edge grows. The clearest "what it does" shot.
- 7.6-11.4 (26-39 %): glass controls on a music-player UI over blue waves; the cursor types a refraction value.
- 11.4-15.2 (39-51 %): a frosted glass card over a yellow flower photo; the effect panel beside it.
- 15.2-18.3 (51-62 %): glass frame on violet in the full editor.
- 18.3-20.2 (62-68 %): an orange app with a glass toolbar.
- 20.2-22.0 (68-74 %): a rainbow gradient slider pill.
- 22.0-23.7 (74-80 %): a glass pill moves over a paragraph of text, bending and splitting the letters.
- 23.7-29.6 (80-100 %): coloured shapes bounce in on black and settle into the logo (5.8 s, longest shot).

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 9 shots, ASL 3.29 s, median 3.77 s, 0 % under 1 s, 67 % over 3 s, 18 per minute.
- A strict, accelerating grid: 3.8 / 3.8 / 3.8 / 3.8 s, then 3.1 / 1.9 / 1.8 / 1.7 s, then a 5.8 s logo. The music bar sets the shot length (62 % of cuts on onsets vs 29 % chance).
- Verified by eye: four cuts added that the scene detector missed (7.6, 11.4, 22.0, 23.7 s) because the dark UI frames are similar.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- No title, no claim, no end line. The only words are UI labels (Light, Refraction, Depth, Dispersion, Frost) zoomed to ≈4-6 % H, and the sample designs' own text. The logo ends it.

Colour/grade: palette, contrast, grain, letterbox
- Dark UI (≈#1e1e1e panels on near-black) against bright, high-contrast test patterns (stripes, blue waves, yellow flower, orange, rainbow). Rainbow chromatic fringes are the accent. Mean luma 0.19 (dark film).

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Rendered UI at 200-300 % zoom, slow virtual push or drift in every shot, glass objects moving across the background. Cursor drags sliders in time with the music.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts on the bar (8 of 8). The glass lens itself acts as a moving reveal inside shots. Shapes morph into the logo at the end.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- No voice. One bright, compressed electronic track. Integrated −9.0 LUFS (very loud), LRA 1.2 LU, true peak +0.1 dBTP. No drop-outs. Hits +19 to +22 dB at 11.5, 18.9 and 26.3 s (scene changes and logo).

What makes it premium (3-5 bullets)
- One feature, one film: the property names are the only words, so the viewer learns the controls by watching.
- Test patterns chosen to show the physics (stripes for refraction, text for distortion).
- A musical grid that speeds up toward the logo.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920×1080 (also works 1:1 or 9:16), 25-30 s. Four shots of 3.8 s (≈ two 4/4 bars at ≈126 BPM, inferred from the grid, not measured), then 3.1 / 1.9 / 1.8 / 1.7 s, logo 5-6 s.
- Glass in HTML: a rounded `div` with `backdrop-filter: blur(2px) saturate(1.4)`, an SVG `feDisplacementMap` (scale 30-60) for refraction, and three offset copies in R/G/B with `mix-blend-mode:screen` (offset 2-6 px) for dispersion; move it `x` across 3 s `sine.inOut`.
- Panel: dark `#1e1e1e` card with real labels, sliders animate with the cursor (`power2.out`, 0.6 s) on the beat.
- Logo: five coloured shapes drop in with `back.out(2.5)`, stagger 0.12 s, settle into the mark, hold 2 s.
- Sound: one loud track (−9 to −12 LUFS for social), cut on the bar, no VO.
