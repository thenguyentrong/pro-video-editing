# All the launches at Config 2025  (Figma, 2025-05-07, 81.1 s, 16:9, YouTube; best available 360p)
URL: https://www.youtube.com/watch?v=NHodnYFUT_I
Purpose: keynote sizzle / launch recap (four new products + several features from the annual conference, as rendered UI)
One-sentence point: Four new products in 80 seconds, each with its own title card and its own mini-world, all ending in one line: everything now lives in one tool.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-3.1 hook (0-4 %): white wordmark on deep maroon ≈#6b141c, letters type on with a selection box; a colourful collage of shapes builds around the logo.
- 3.1-4.5 (4-6 %): letters scatter into a grid on black and resolve into chapter card 1 (white product name on black).
- 4.5-26.8 (6-33 %): product 1 (website builder): live websites at three breakpoints, templates, responsive resize, a CMS grid that flips colours (grey → green → violet → yellow, 0.4-0.6 s each), a hover state, a collection page.
- 26.8-35.4 (33-44 %): chapter card 2 (rainbow-glitch name) → product 2 (AI prompt-to-app): an image is dropped into a prompt, the prompt types, a "Thinking" state glitches, the generated app appears.
- 35.4-56.1 (44-69 %): chapter card 3 (name with a yellow hand-drawn underline) → product 3 (illustration and type tools): brush strokes, a mascot drawing, type on a path, a big red display word stretched with handles, vector butterfly → shader-filled art → festival poster (the visual peak).
- 56.1-71.0 (69-88 %): chapter card 4 (name inside a magenta outline frame) → product 4 (brand templates at scale): fields fill in a poster, a sneaker ad, a data table feeds a bulk export ("Export assets" button).
- 71.0-77.3 (88-95 %): a wall of generated cards rearranges (6.3 s, longest shot), the end line in two lines (black + red) on a pastel gradient, a collage of shapes.
- 77.3-81.1 (95-100 %): logo on a pastel gradient, then on dark grey; 1.75 s silence at the end.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 45 set-ups, ASL 1.80 s, median 1.50 s, 18 % under 1 s, 13 % over 3 s, 33 per minute. Quarters 1.56 / 1.35 / 1.84 / 2.25 s: fast start, slower end.
- Cuts per 10 s: 5, 7, 8, 5, 6, 4, 6, 3. Densest 18-20 s (colour-flip grid, 0.4-0.6 s).
- Longest 6.3 s (card wall), 5.0 s (shader art), 4.8 s (template build).
- Verified by eye on the cut pairs: 27 detector cuts dropped (UI animations, resize steps, glitch frames, a 0.17 s card shuffle that is one animation), 3 added (18.7, 62.6, 68.2 s). Rendered-UI boundaries are partly a judgement call; treat counts as ±10 %.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Chapter cards: the brand grotesque (free: Inter 500), white on pure black, sentence case "brand + product", cap ≈11 % H, centred. Hold 1.2-2.1 s. Each card gets ONE treatment that shows the product: letters typing in a selection box, rainbow glitch, hand-drawn yellow underline drawn on, magenta frame outlines. The opening wordmark on maroon: cap ≈8.8 % H.
- End line: two lines, centred, cap ≈15.6 % H, black first line, red ≈#e5384b brand word; pastel gradient ≈#dcddf2 → pale green. Hold ≈1.5 s, then shapes burst over it.
- All other words are inside the UI or the sample designs (serif headlines in website templates, display type in posters).

Colour/grade: palette, contrast, grain, letterbox
- Multicolour brand world: maroon opener, black chapter cards, then each product scene uses its sample designs' colours (sage, khaki, lime, coral, magenta). Pastel gradient for the end. No grain, no letterbox.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- 100 % rendered UI and sample designs. Virtual camera: slow pushes, push-ins on details, slides; UI windows float on coloured backgrounds; cursor with name tags (multiplayer). No people, no live action.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Mostly hard cuts on colour changes; glitch transition into product 2; letter-scatter morph into the first chapter card; shapes morph into the logo. Chapter cards act as the act breaks.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- No voice (one sung or sampled word at ≈2 s). Upbeat electronic/pop track with UI ticks. Integrated −15.6 LUFS, LRA 7.0 LU, true peak +0.1 dBTP. No drop-outs; 1.75 s silence at the end. Biggest rise +35.9 dB at 23.9 s (music re-enters after a thin passage), +25.9 dB at 47.5 s.
- Cuts on onsets 59 % vs 53 % chance: loosely on the music.

What makes it premium (3-5 bullets)
- Four products, four chapter cards, one card system: the viewer never gets lost.
- Each chapter card hints at the product with one small effect (type-on, glitch, underline, frame).
- Sample designs are art-directed like a magazine (serif sites, festival poster, sneaker ad), so the UI looks desirable.
- No voice, no feature list on screen: the work in the tool is the argument.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920×1080, 75-85 s, ASL ≈1.8 s. Opener 3 s → per product: chapter card 1.2-2 s + 7-20 s of UI scenes at 1.5-2 s → end line 1.5 s → logo 3 s → 1.5 s silence.
- Chapter card: `#000`, `Inter 500 11vh #fff`, centred. Effects: type-on with a 2 px blue selection box (`#0d99ff`) around the growing word, 0.06 s/char; glitch = 3 RGB-split copies `x ±6px` for 0.2 s; underline = SVG path `stroke:#f5d90a; stroke-width:6` drawn 0.5 s; frame = 3 nested magenta `#ff24bd` outlines scaling in 0.4 s.
- UI scenes: real HTML mocks; virtual camera via `scale/x/y` tweens 1-2 s `power2.inOut`; colour-flip grid = `set()` background every 0.45 s.
- End line: `Inter 500 15vh`, line 1 `#000`, brand word `#e5384b`, gradient `linear-gradient(180deg,#dcddf2,#effbe0)`.
- Sound: one upbeat track at −15 to −16 LUFS, UI ticks, hit on each chapter card, silence on the last 1.5 s.
