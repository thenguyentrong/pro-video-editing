# Leica M11 Monochrom – A Symphony of Light and Shadow  (Leica Camera, 2023-04-13, 1:33, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=vnXkgEeA62M
Purpose: launch film (narrated), black-and-white camera
One-sentence point: A camera that only sees black and white brings photography back to light, contrast and composition.

Structure:
- 0.0-26.6 product in darkness: a slow light sweeps across the black body (the red dot is the only colour, frames/t003.0s.jpg), the shutter dial macro (t007.0s), the viewfinder window, the rear; four fades through black at 5.3, 9.1, 13.5, 23.9 s. VO starts at 4 s.
- 26.6-38 desert: sculpted rock formations, a woman in traditional dress and mask (t026.0s area), a photographer in the sand, back-lit by a white sky.
- 38-42 the camera on a white plinth in a grey space (t038.5s), a lens macro.
- 43-67 city: New York streets, a woman in headphones (t044.0s), motorbike riders, a portrait in a bar, subway, street photographer with the camera.
- 68-73 desert again: woman with a camel, dunes from above, a rider.
- 73-89 the camera on the plinth: wide, slow orbit, top plate and lens macros, final 3/4 hero (t086.0s).
- 89.1-92.8 red dot logo on black (t090.5s), 3.2 s of silence.

Cut rhythm: 37 shots (adaptive + 4 fades added), ASL 2.51 s, median 1.84 s, 3 % under 1 s, 27 % over 3 s, 24 shots/min. Quarters 5.80 / 1.93 / 1.66 / 2.32 s: a slow dark product overture (shots up to 10.4 s), then a steady 1.5-2.5 s rhythm for the photographs. Cuts on onsets 19 % vs 24 % chance (cut to VO phrases).

Typography: none in the body. End: red dot logo only, ≈ 9 % H, centred on black.

Colour/grade: fully monochrome (median saturation 0 %) - the film looks like the camera's output; the only colour is the red logo dot on the body and the end logo. Median luma 75, contrast p95-p5 134, deep blacks with bright white skies; 32 % of frames dark.

Camera/shots: product: extreme macro, very slow slides with a moving light in a black void (a light sweep over texture), later a white plinth in a soft grey studio, slow orbit. People: real photographers on location, handheld, wide lenses, back-lit silhouettes, street portraits.

Transitions: fades through black in the product overture (0.4-0.6 s each), hard cuts in the people section, a hard cut to the logo.

Sound: male VO from 4 to 90 s, slow, poetic, few words per sentence with pauses; piano/strings score that builds; −16.1 LUFS, LRA 7.1 LU, true peak +0.7 dBTP. The biggest hit (a final chord, rise +28 to +37 dB at 87.2 and 89.0 s) lands on the cut to the logo, then 3.2 s of silence (89.6-92.8 s). Also +28 dB at 15.8 s inside the dark overture. 0.7 s silence at the start.

What makes it premium:
- The film obeys the product: black and white only, with the brand red as the single accent.
- A 26 s product overture in near-darkness: patience as luxury.
- Light does the reveal (sweep across the body), not motion graphics.
- Zero supers; the VO carries meaning, the logo closes.

Recipe (real footage + HTML/GSAP):
1. Grade everything to monochrome: `filter: grayscale(1) contrast(1.15) brightness(.95)`; keep one red element unmasked on a separate layer.
2. Overture (≈ 25 % of runtime): 3-5 product macros of 4-10 s, each lit by a moving light band (`linear-gradient` band, `mix-blend-mode:screen`, x −60 % → 140 % over 6 s, `sine.inOut`), joined by 0.5 s fades through black.
3. Then 1.5-2.5 s cuts of people using the product, matched to VO phrases.
4. Return to the product on a white plinth in a grey void for the last 15 %: slow orbit, 3-5 s per shot.
5. Logo on black, 3 s, in silence. Master −16 LUFS.
