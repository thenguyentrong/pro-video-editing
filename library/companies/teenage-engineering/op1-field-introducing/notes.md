# introducing OP-1 field  (teenage engineering, 2022-05-12, 0:28, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=Fab7sp30pg0
Purpose: launch teaser / announcement film
One-sentence point: Ten years after the OP-1, the new OP-1 field is "thinner, louder, better", said in five short lowercase lines and a few quiet macros on white.

Structure:
- 0.0-2.8 hook: black card, small grey lowercase text "the beauty of evolution." (fades up, holds).
- 2.8-6.9 product macros on white: corner of the aluminium body with the "OP-1 [field]" print (frames/t003.2s.jpg, t004.6s.jpg), then white keys with black dots.
- 6.9-9.3 white card, the last word swaps in place: "a decade of ideas" -> "a decade of improvements" -> "a decade of refinements." (one shot, ~0.8 s per word).
- 9.3-11.0 macro: screen with the tape-reel UI, knobs.
- 11.0-13.2 white card: "thinner, louder," -> "thinner, louder, better." (word added in place).
- 13.2-15.4 macro: speaker grille corner, diagonal.
- 15.4-22.0 hero: straight-on product on white, centred, small (~60 % of width), held 6.6 s (screen/LEDs animate).
- 22.0-27.1 end: "the all new" -> logo "OP-1 [field]" (word "field" inside a thin rounded box), legal lines at the bottom, slow fade to grey then black (27.1).

Cut rhythm: 9 shots, ASL 3.12 s, median 2.20 s, quarters 1.75 / 1.75 / 3.51 / 3.50. Shortest 1.68 s, longest 6.6 s (hero) and 6.1 s (end). No shot under 1 s. But the text changes inside shots, so the eye gets a new thing every ~2 s (~14 visual beats in 28 s). Cuts on onset 50 % vs 44 % chance (weak beat link).

Typography: one neo-grotesk (TE's own; free match: Inter or Helvetica Now, Regular 400), all lowercase except the product name, sentence punctuation kept ("refinements."). Small: line height ~3.5 % of frame height incl. ascenders/descenders (x-height ~1.7 %). Dark grey (#222-#333) on off-white, or mid-grey on black. Left-aligned at a FIXED anchor ~35 % from the left edge, so when the last word swaps the start of the line does not move (frames/t007.5s.jpg). Logo ~8 % of frame height, centred; legal 2 lines at ~90 % height, ~1.5 % size. Animations: word swap = hard replace (no slide), card in/out by short fade.

Colour/grade: almost no colour: off-white seamless (median frame luma 218, 75 % of frames brighter than 170) with a soft grey vignette in the corners, product in aluminium/white/black; median saturation 1.3 % (p90 7.6 %). Only the screen and small knob caps add colour (orange/red/blue dots).

Camera/shots: product macros with very shallow depth of field and diagonal framing (corner of the device entering from the top-left), slow drifts/push-ins; one straight-on hero. Probably CG or very clean studio photography (not sure). No hands, no people.

Transitions: hard cuts between macro and card; text changes inside cards; fade to black at the end.

Sound: one upbeat electronic track (likely made on the device; guess), very loud and flat: -8 to -10 LUFS-M the whole film, integrated -10.7 LUFS. Short 0.15-0.2 s gaps at 3.0, 3.55 and 12.85 s followed by hits (+36 dB) = staccato/stutter rhythm. No voice.

What makes it premium:
- Copywriting as design: five lines, lowercase, the last word swaps in place.
- Fixed text anchor (not centred) - feels like a typed spec sheet, not an ad.
- White seamless + product macros: the device looks like an object in a museum.
- The product name is shown first ON the product (printed on the metal) before it appears as a logo.

Recipe (real footage + HTML/GSAP):
1. Background `#f2f2f0` with a radial vignette `radial-gradient(ellipse at center, #f4f4f2 55%, #d9d9d6 100%)`.
2. Text: Inter 400, `font-size:2.6vh` (gives ~3.5 % line box), `color:#2a2a2a`, lowercase, `position:absolute; left:35%; top:48%`. Build the line as spans; swap only the last span with `gsap.set` every 0.8 s (no tween). Hold the final version 1.2 s.
3. Macros: 2-2.5 s each, a slow `scale:1.0 -> 1.04` push on the video/still, framed diagonally (rotate the device 20-30 deg).
4. Hero: centred product at 60 % width for ~6 s, let the screen/LEDs animate.
5. Logo card: product name + small rounded-box tag (`border:1px solid; border-radius:4px; padding:0 .3em`), legal 2 lines 1.4 vh at the bottom, fade to black over 1 s.
6. Music: punchy, -10 LUFS, stutter gaps of 0.2 s just before 2-3 cuts.
