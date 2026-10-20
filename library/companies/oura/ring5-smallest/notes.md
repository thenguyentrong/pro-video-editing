# Introducing Oura Ring 5: The World's Smallest Smart Ring  (ŌURA, 2026-05-28, 0:30, 16:9, YouTube; ≈ 13 M views)
URL: https://www.youtube.com/watch?v=8C8dC9yQ7m8
Purpose: launch spot (music only)
One-sentence point: The next ring is 40 % smaller but tougher, waterproof and still research-grade.

Structure:
- 0.0-3.1 a dark ring on a light grey seamless; the ŌURA wordmark appears huge with the ring passing through the O (frames/t002.0s.jpg).
- 3.1-5.6 "The next big thing" over a black ring macro, then "is small" over the ring on a rock with a red flower (t004.5s).
- 5.6-7.2 a hand: "40%" then "40% smaller" (t007.5s area).
- 7.2-11.3 sensors: "Redesigned sensors", then a black ring with glowing green/red LEDs: "Research-grade accuracy" (t011.0s).
- 11.3-14.4 an iceberg, a scratch on ice: "Tougher to scratch".
- 14.4-18.5 an exploded view of the ring; a water splash: "Fully waterproof" (t017.5s).
- 18.5-21.6 a desert at night with cacti: "1 charge lasts a week".
- 21.6-24.8 two rings float, hands: "No alerts", a misty forest: "No distractions" (t022.5s).
- 24.8-27.7 sensor macro, a butterfly lands on the ring, "Barely ..." line; two rings side by side with a small line (t027.0s).
- 27.7-30 product name "Oura Ring 5" with the 5 in a circle, ring centred (t029.0s).

Cut rhythm: 22 shots, ASL 1.36 s, median 1.12 s, 36 % under 1 s, 44 shots/min. Quarters 1.50 / 1.07 / 1.25 / 1.07 s. Longest 3.1 s (logo open). Each claim takes two shots (setup word on shot A, completion on shot B) ≈ 2.5-3 s per claim. Cuts on onsets 5 % vs 6 % chance.

Typography: neo-grotesk sans regular (closest free: Inter Display 400), white, sentence case, tight tracking (≈ −0.02 em), cap ≈ 7 % H, centred at y ≈ 48 % (mid-frame, over the product), one line, 1-4 words. Two-step builds: the second half of the line is added on the next shot ("Research-grade" → "Research-grade accuracy"). Wordmark ŌURA at the start ≈ 13 % cap H. Small lines ("The world's smallest smart ring") ≈ 1.5 % H. Name card ≈ 6 % H with circled model number.

Colour/grade: neutral light-grey seamless (median luma 170, saturation 8 %, R-B +3), crisp contrast (p95-p5 134); world inserts are desaturated toward grey-blue (ice, night desert, mist), so the warm gold/rose ring finishes and the green/red sensor LEDs are the colour.

Camera/shots: CG and macro product on grey and black, slow rotations; metaphor stock-style inserts (iceberg, water, desert, forest, butterfly) that each prove one claim; hands as scale.

Transitions: hard cuts only; the text line continues across the cut (completion on the next shot) which links shots like a match cut.

Sound: music only, pulsing and bright; −13.2 LUFS, LRA 4.4 LU, true peak −1.0 dBTP. No drop-outs, no single big hit.

What makes it premium:
- Apple-like grammar (one claim per card, white sans, light seamless) but warmer finishes.
- The two-shot line build: the sentence finishes on a new picture, so text and image change together.
- Metaphor inserts instead of spec graphics: iceberg = tough, splash = waterproof, desert night = battery.
- Big wordmark open, small name close.

Recipe (real footage + HTML/GSAP):
1. Write 7-9 claims of 2-4 words; split each into "setup | completion".
2. Pair each claim with one product shot (setup) and one metaphor shot (completion), 1.0-1.6 s each.
3. Text: `font: 400 9.6vh 'Inter Display'; letter-spacing:-.02em; color:#fff; top:48%`, the completion word `opacity 0→1` 0.25 s on the cut; the setup part stays in place (no re-centre jump: pre-layout the full line, hide the second span).
4. Grade metaphor stock `saturate(.55) brightness(1.05)` so the product finish stays the colour.
5. Open with the wordmark huge (cap ≈ 13 % H) and the product passing through a letter; close on the name card 2.3 s. Master −14 LUFS.
