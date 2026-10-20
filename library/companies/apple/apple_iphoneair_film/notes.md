# iPhone Air: Incredibly light and thin with pro-level performance  (Apple, 2026-08-20, 0:53 file / 0:48.5 content, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=sKJ0_NNcJzI
Purpose: product ad / launch spot (feature run-down)
One-sentence point: iPhone Air is ultra-thin and light yet has pro power — told as a clean list of one-line feature cards between product shots.

## Structure
- 0-1.7 s **Ident**: " iPhone Air" small, grey, fades in on light grey.
- 1.7-5.6 s **Hook**: "Power in a new light" card → the phone edge rises from the bottom edge of frame, held by fingertips (hit at 4.4 s).
- 5.6-17.9 s **Design**: card / product / card rhythm: "Ultralight titanium design" (the word "titanium" gets a light sweep), dark macro of the side rail (7.5-9 s), "Ceramic Shield front and back", "More durable than any previous iPhone" over the phone turning flat→edge, "Immersive 6.5″ display", blue ProMotion macro with text inside, phone front turning.
- 18-34 s **Camera**: "48MP Fusion camera system" → dissolves to "Two advanced cameras in one", champagne camera macro, 4 photo cuts at 0.67-0.83 s with zoom UI "1× 2" (shutter SFX), "Center Stage front camera", split card "for smarter [phone] group selfies", "Dual Capture video" → skateboard Dual Capture clip with caption over footage.
- 34-41 s **Power**: A19 Pro chip on grey (light sweep), "Pro power and all-day battery life", phone pushes up with a game on screen, "Built for Apple Intelligence" in rainbow gradient text with a glowing rainbow frame edge (40-41 s).
- 41-45.6 s **Payoff**: four colourways lying flat stacked, then the phone held upright between thin outline shapes.
- 45.6-48.5 s **End**: Apple logo turns from grey to black, held in silence; then 5 s black.

## Cut rhythm
- 28 shots/cards in 48.5 s → **ASL 1.73 s**, median 1.70 s (hard cuts + 7 dissolve/push card changes added by eye from a 3 fps strip; hard cuts alone give 22 shots, ASL 2.2 s).
- ASL per quarter 1.73 / 1.21 / 1.52 / 2.02. Densest 20-30 s (8 changes): photo samples at 0.67-0.83 s.
- Longest 3.0 s (skate Dual Capture clip), 2.7 s (upright phone). 14 % < 1 s, 4 % > 3 s.
- Text cards hold 1.4-2.0 s each.

## Typography
- SF Pro Display, medium (~500), sentence case, one line, centred at y ≈ 50 %.
- Size: cap height ≈ 7 % of H (ink incl. descenders 7.1-8.75 % H); line width 50-67 % of W. 3-7 words per card.
- Colour: dark slate text (core #15222f, anti-aliased mean ≈ #4c6176) with one keyword in lighter blue-grey (≈ #7d9bb5): "**Ceramic Shield** front and back", "**in one**", "**Center Stage** front camera", "**Pro power** and all-day…". AI line uses a pink→purple gradient.
- Animation: fade-in 0.3-0.6 s (no slide), keyword light-sweep, cross-dissolve to the next card 0.3-0.5 s, or the product pushes the text out upward. Split card: words sit left and right of the phone.

## Colour / grade
- Light studio sweep: centre #f4f3f6, darker grey band at the top (≈ #d1d5d9) → feels like a lit cyclorama.
- Product sky-blue/silver; colour accents only from UI and the rainbow AI frame.
- 46 % of frames mostly empty, 45 % on light — lots of negative space.

## Camera / shots
3D/CG product renders and macro (side rail, camera plateau), product held by fingertips entering from frame bottom, screen content, sample photos/videos as proof (full frame), chip render. Slow rotations and rises; no handheld.

## Transitions
Hard cuts between product shots, cross-dissolves between text cards, vertical push (product slides up, text exits up) 3×, light sweeps on words.

## Sound
- Music only: "Reverie" by Citizen (captions). No VO.
- SFX: camera shutters under the photo cuts (22.4-25.3 s), "Apple Intelligence tone" at 40.2 s.
- Integrated **−16.1 LUFS**. Biggest rises 4.4 s (+25.5 dB, phone rises) and 5.6 s, 10.5 s.
- Music ends at 45.5 s; the Apple logo is held 3 s in silence.

## What makes it premium
- One idea per card, few words, same position every time → calm, list-like clarity.
- Two-tone text (keyword lighter) instead of bold or colour boxes.
- Huge negative space on a light sweep; product enters from frame edge, held by fingertips (scale and thinness).
- Proof inserts are fast (0.7 s) while cards are slow (1.5-2 s) — contrast in rhythm.
- Silent logo ending.

## Recipe (real footage + HTML/GSAP)
- Background: `radial-gradient(120% 80% at 50% 60%, #f6f5f8 0%, #eeeef1 60%, #d6d9dd 100%)` or real cyc footage.
- Card: Inter Display/SF Pro 500, `font-size: 9.5vh` → cap ≈ 7 % H (≈ 103 px font at 1080; Inter cap ≈ 0.73 em), `letter-spacing: -0.01em`, colour `#1f2d3d`, keyword span `#7d9bb5`.
- Card in: `gsap.from(card,{opacity:0,duration:.45,ease:"power1.out"})`; hold 1.5-1.8 s; out: crossfade 0.35 s into the next card, or `gsap.to(card,{yPercent:-120,duration:.6,ease:"power3.inOut"})` while the product clip slides up from `yPercent:100`.
- Keyword sweep: background-clip text gradient `linear-gradient(90deg,#7d9bb5 40%,#fff 50%,#7d9bb5 60%)`, animate `background-position` 0.8 s.
- Proof inserts: 0.7-0.8 s hard cuts, each with a shutter SFX.
- End: logo fade 0.5 s, music out 0.2 s before, hold 3 s silent.
