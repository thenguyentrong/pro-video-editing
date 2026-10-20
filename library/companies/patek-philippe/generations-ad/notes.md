# Patek Philippe airs new "Generations" ad  (Patek Philippe, 2016-10-06, 1:00, 16:9, YouTube @PatekPhilippeGeneva)
URL: https://www.youtube.com/watch?v=hjfXUpVtINE
Purpose: luxury TV ad (60 s cut of the Generations campaign) with a product end
One-sentence point: Five cities, five parent-child moments, one watch you look after for the next generation.

## Structure
- 0-10 **Los Angeles**: a classic convertible on a coastal road (2.6 s opening), father and son laughing in the car, the watch on the wheel hand. City name in italic serif, lower right.
- 10-20 **Bangkok**: a flowered arch, mother and daughter, a flower garland passed by hand, the daughter's smile.
- 20-29 **Sydney**: harbour aerial, a cricket ground, a boy in whites, father's hand.
- 29-39 **Geneva**: the lakeside garden and jetty (shots reused from the long film).
- 39-47 **New York**: night window, bare feet, dinner, mother and daughter hug.
- 46.96-51.96 text card: black-to-silver side gradient, logo cross, the campaign line in two serif lines (5.0 s).
- 51.96-57 product: the chronograph turns from caseback to dial on the dark side of the gradient; wordmark and model name stacked at the right.
- 57-60 logo card with "Begin your own tradition."

## Cut rhythm
- 37 shots in 60 s. ASL 1.62 s, median 1.16 s, 19 % under 1 s, 37 shots per minute.
- ASL per quarter 1.36 / 1.15 / 1.25 / 3.75 s.
- Cuts per 10 s: 5, 8, 9, 6, 7, 1, 0.
- Longest 8.06 s (51.96, product turning into the logo card, dissolve), 5.0 s (text card), 3.16 s (35.24). Shortest 0.56 s.
- Faster than the long film (median 1.16 s vs 2.0 s) by trimming each vignette to 8-10 s.

## Typography
- City captions: italic serif (closest free: EB Garamond Italic), white with soft shadow, cap height ≈4.6 % H, right-aligned at x ≈90 %, y ≈80 %; held for the whole vignette.
- Campaign line: serif, sentence case, ≈3 % H, white on the dark side of the gradient, centred.
- Product card: wordmark sans caps ≈3 % H, model name in serif ≈3.5 % H, right column at x ≈73-98 %, vertically centred.

## Colour/grade
- B&W vignettes (soft, bright); the product is the only colour shot of the film (blue dial), on a black-to-silver gradient.

## Camera/shots
- As the long film: lifestyle wides, two-shots, hand and wrist close-ups; one aerial per city. Product: CGI or motion-control turntable.

## Transitions
- Hard cuts; dissolves on the card sequence (product → logo).

## Sound
- No voice; piano/strings. Integrated -13.8 LUFS, LRA 9.9 LU, true peak -0.4 dBTP. No drop-outs.

## What makes it premium
- A place name is the only text in the film: the world is the luxury.
- B&W people, colour product: the watch is the only colour in 60 s.
- The line comes before the product, so the product reads as the proof.

## Recipe
- 5 vignettes × 8-10 s, 5-8 shots each; caption `font: italic 400 4.6vh 'EB Garamond'; right: 10vw; bottom: 18vh` per vignette.
- At 78 % runtime: text card 5 s, then the product turntable 5 s in colour (`gsap.to(watch, {rotationY: 180, duration: 5, ease: 'power1.inOut'})`), logo card 3 s.
