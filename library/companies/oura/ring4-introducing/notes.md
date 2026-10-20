# Introducing Oura Ring 4: Sleeker. Smarter. Made for you.  (ŌURA, 2024-10-03, 0:30, 16:9, YouTube; ≈ 4.4 M views)
URL: https://www.youtube.com/watch?v=lCE7dmBojyg
Purpose: launch spot (music only)
One-sentence point: A tiny ring quietly measures your sleep, activity, recovery, stress and heart.

Structure:
- 0.0-1.7 linen curtain, the word "Meet" appears centred.
- 1.7-5.2 the ring on an oak bedside table, "Oura Ring 4" with the 4 in a circle (t002.5s); then the inside of the ring with its sensors, "Incredible accuracy" (t005.0s).
- 5.2-7.4 an empty bedroom, olive bedding: "For your best sleep".
- 7.4-9.7 the ring lands on a white pillow.
- 9.7-12 a rolled olive yoga mat, the ring drops through it: "Your activity" (t010.5s).
- 12-14 lips breathing out, close-up: "Your recovery" (t013.0s).
- 14-18.3 the ring rolls on the table; folded hands wearing it: "To check your stress".
- 18.3-23.5 olive fabric swirl with the ring, a hand on the chest: "And listen to your heart" (t022.0s).
- 23.5-25 phone with a heart-health screen (t024.5s).
- 25-26 the ring spins past the lens (motion blur).
- 26-30 end card on beige satin: "Oura Ring 4 / Sleeker. Smarter. Made for you.", then ŌURA wordmark top and "Shop now at Oura" bottom (t027.5s, t029.5s).

Cut rhythm: 15 shots, ASL 2.0 s, median 2.0 s, 0 % under 1 s, 30 shots/min. Quarters 1.50 / 1.50 / 1.88 / 1.88 s. Longest 4.0 s (end card). Very regular: almost every shot is 1.7-2.3 s and carries exactly one word-built line. Cuts on onsets 14 % vs 29 % chance: cuts follow the text, not the beat.

Typography: a neo-grotesk sans (closest free: Inter) for the line, with the key word set in a light italic serif (closest free: Instrument Serif Italic): "Incredible *accuracy*", "Your *recovery*". White, sentence case, cap ≈ 3.8 % H, centred at y ≈ 48-50 %. Word build: the sans part appears first, the italic keyword fades in ≈ 0.5-0.8 s later and the line re-centres. Product name ≈ 5 % H with the model number in a small circle; end tagline ≈ 2.5 % H in the same sans; "Shop now at Oura" ≈ 1.8 % H at y ≈ 90 %.

Colour/grade: warm neutral home palette (R-B +40): oatmeal linen, light oak, beige satin, olive green as the one accent (bedding, mat, fabric, T-shirt). Bright (median luma 132), soft contrast (p95-p5 136), no dark frames. The silver ring is the only metal.

Camera/shots: real product macro + CG-like product moves (the ring drops, rolls, spins), extreme close-ups of body parts (lips, hands, chest), one phone screen. Shallow depth of field, slow pushes.

Transitions: hard cuts; one motion-blur spin past the lens as a hidden transition into the end card.

Sound: music only, soft and sparse; −23.8 LUFS integrated (very quiet), LRA 2.9 LU, true peak −11.5 dBTP. Small sound hits on the ring actions (+28 dB at 1.8 s, +42 dB at 19.6 s measured from near-silence).

What makes it premium:
- One line per shot, built in two steps, with an italic serif keyword: editorial and soft.
- One accent colour (olive) in a beige home world.
- The product is shown small, in human places (pillow, mat, hands), never loud.
- Mixing so quiet it feels like a whisper (but too quiet for platforms).

Recipe (real footage + HTML/GSAP):
1. Shot list: one ring/product shot per benefit, each in a home texture (linen, wood, satin, yoga mat), plus 2-3 body close-ups.
2. Line component: `<p class="l"><span class="a">Your</span> <em class="b">recovery</em></p>`; `.l{font: 400 5.2vh 'Inter'; color:#fff; text-align:center}` `.b{font-family:'Instrument Serif'; font-style:italic}`; `tl.from(a,{opacity:0,duration:.4}).from(b,{opacity:0,duration:.5},"+=.5")`.
3. Rhythm: 2.0 s per shot ±0.3 s, one line per shot, 12-15 shots in 30 s.
4. End card: product on beige satin, name 7vh, tagline 3.5vh, wordmark top centre, CTA bottom 10 %; hold 4 s.
5. Master at −16 LUFS (the original's −24 is too quiet for social).
