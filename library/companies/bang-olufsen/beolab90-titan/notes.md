# Beolab 90 Titan Edition  (Bang & Olufsen, 2026-04-02, 1:00, 16:9 file with a 1.90:1 picture (854x450), YouTube)
URL: https://www.youtube.com/watch?v=7zj8pNacjYQ
Purpose: limited-edition product film / craft film
One-sentence point: A huge speaker is made by hand from raw aluminium in the Struer factory, and the finished object is the reward.

Structure (times from metrics.json; sheet labels are correct):
- 0.0-4.0 hook: wide shot of an empty white warehouse, a man pushes the raw speaker shell on a blue workshop crane; "BANG & OLUFSEN / Est. 1925" wordmark centred over it (frames/t001.0s.jpg).
- 4.0-22.2 raw making: grinding wheel on aluminium with sparks and dust (t005.0s), metal close-ups, gloved hands flattening a disc on a workbench (t012.5s), wide workshop, parts hung on a rack, ratchet, disc turned by hand. A 0.44 s cream-white flash at 21.8-22.2 marks the turn.
- 22.2-34 precision: polished edge macro, wooden jigs holding parts (t024.5s), a technician in silhouette at a lit test bench (blue room), logo engraved into the part.
- 34-39 first object shots: one part alone on black (t034.5s), grilles laid out in rows on a light table.
- 39-48 assembly: crane lifts the cabinet, screws laid out on white gloves, hands fit the driver bolts (t045.0s).
- 48-56 reveal + macro run: the finished speaker on the grey floor (49.2), then 7 macro shots of drivers and grilles at 0.5-1.1 s each, light sweeping over the metal.
- 55.7-58.5 title: the speaker in the empty hall, "Beolab 90 / Titan Edition" fades in over it (t057.5s); the lights dim at ≈58 s.
- 58.5-60 wordmark on black (t059.0s), 0.45 s silence at the very end.

Cut rhythm: 42 shots, ASL 1.43 s, median 1.32 s, 19 % under 1 s, 2 % over 3 s, 42 shots/min. Quarters 1.50 / 1.25 / 1.25 / 1.36 s: very even. Longest 4.0 s (opening wide), 2.4 s. Shortest 0.44 s (white flash) and the 0.5-0.7 s driver macros near the end. Cuts on onsets 15 % vs 15 % chance: cut to picture actions (grinder, hand moves), not to the beat. Cut list was checked by eye (3 cuts added in the dark macro run, 3 flash false-positives removed).

Typography: Wordmark "BANG & OLUFSEN" in wide-tracked caps, cap ≈ 9 % H, centred at y ≈ 47 %, with "Est. 1925" ≈ 3 % H under it. Product title: "Beolab 90" in a geometric sans, sentence case, cap ≈ 7 % H, white, centred over the product; "Titan Edition" under it in an italic serif, ≈ 4 % H. Closest free fonts: Jost (sans) + Libre Caslon Italic / Instrument Serif Italic (edition line). Fade in/out ≈ 0.5 s. Only two text moments in the film.

Colour/grade: cool, clean, low saturation (median 13 %, R-B −10 = slightly blue), crisp contrast (p95-p5 168), median luma 107. Silver aluminium, white gloves, beige workwear; the blue crane and blue test room are the only colour. Product macros on black are near-monochrome.

Camera/shots: real factory footage, mostly locked or slow slider; macros of metal, sparks, tools; overhead hands on workbench; one silhouette wide; product hero shots low and centred in an empty hall (symmetry, lots of empty floor and ceiling).

Transitions: hard cuts only; one cream-white flash frame (0.44 s) as a section marker; light changes inside shots (light sweep on metal, hall lights dim before the logo).

Sound: music only (no VO), steady instrumental bed with mechanical texture; −16.8 LUFS integrated, LRA 6.6 LU, true peak +0.2 dBTP (hot master). No drop-outs; 0.45 s of silence on the wordmark.

What makes it premium:
- The making is the proof: raw metal, sparks, gloved hands, jigs, then the perfect object.
- Even, calm rhythm (≈1.3-1.5 s every quarter), no speed-ramps or effects.
- White gloves and an empty white hall = museum treatment of a product.
- Two text moments only: wordmark at the start, product name at the end, both small and centred.
- A dimming of the lights instead of a "whoosh" before the logo.

Recipe (real footage + HTML/GSAP):
1. Shoot or license: factory/workshop macros (grinding, polishing, CNC, gloved hands), one empty hall wide, 6-8 macros of the finished product with a moving light.
2. Order: process (raw → precise → assembled) for ≈80 % of runtime, reveal at ≈80 %, macro run, title, logo.
3. Cut every 1.2-1.6 s, flat across the film; end the macro run with 0.5-0.7 s shots.
4. Title over the hero wide: `font: 500 9.6vh 'Jost'` (cap ≈ 7 % H) + italic serif line at 5.5vh, centred, `opacity 0→1` 0.5 s `power1.out`; dim the video `brightness(1 → .55)` over 1 s before cutting to the wordmark on black.
5. One white flash (0.4 s, `#f3ecdc`) between "raw" and "precise" sections only.
6. Music only, master −16 LUFS, true peak ≤ −1 dBTP (the original is hotter).
