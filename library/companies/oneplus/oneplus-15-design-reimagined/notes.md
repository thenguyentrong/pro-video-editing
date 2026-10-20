# Introducing OnePlus 15 | Design Reimagined  (OnePlus, 30 Oct 2025, 0:52, 16:9, YouTube @OnePlusTech)
URL: https://www.youtube.com/watch?v=ZS9o0adDUew
Purpose: launch design film (teaser)
One-sentence point: the design told in pairs - every shot is a split screen of two panels with a two-word label each ("outside / inside", "dust / deep", "Power On / Limits Off").

## Structure (cut times from metrics.json)
- 0-4.9 s: black, a rim light slowly draws the camera module; first label appears.
- 4.9-14.2 s (18 %) build: split screens - the phone back | an X-ray of its insides, rounded corners | a CNC cutter, frame parts orbiting a ring (CGI), electric arcs | glowing orange metal ("Micro-arc oxidation").
- 14.2-26 s (23 %) colour 1 (Sand Storm): bead-blasted sand finish, the phone floating, bezels measured by red laser lines | a hand holding the larger screen.
- 26-34.6 s: durability pairs: hands gaming | heat and frost, the phone falling through dust | underwater.
- 34.6-39 s: colour 2 (Ultra Violet) macros in lilac light.
- 39-45.3 s: colour 3 (Infinite Black) with red laser lines in the dark.
- 45.3-48.3 s: sign-off pair "Power On" | "Limits Off" over two phone macros.
- 48.3-52 s: "OnePlus 15 / Power On. Limits Off." on black, launch date line, wordmark.

## Cut rhythm
- 21 shots in 52.1 s, ASL 2.48 s, median 2.37 s, 14 % < 1 s, 38 % > 3 s, 24 shots/min.
- ASL per quarter 1.86 / 3.25 / 1.63 / 2.60 s. Cuts per 10 s: 4 / 4 / 4 / 5 / 3.
- Each split-screen panel changes on its own: the two halves are cut at different times (the detector counts a full-frame change only), so the felt rhythm is about twice as fast.
- Cuts on music onsets 0 % vs 12 %: timing is set by the moves, not the beat.

## Typography
- OnePlus Sans (proprietary). Closest free: **Inter** / **Manrope** Regular.
- Labels: sentence case, two words, white, cap ≈3 % H, centred in each panel at ≈50 % H (one label per panel); fade in 0.3 s, held as long as the panel.
- End: product name cap ≈2.5 % H with a tiny tagline under it; date line ≈1.8 % H; wordmark.

## Colour / grade
- Product-colour worlds per section: warm sand/champagne, lilac violet, black with red laser lines; CGI orange heat and blue arcs for the material story. Mean luma 0.29.
- Very clean CGI, studio-white macros.

## Camera / shots
- ≈70 % CGI and product macros (X-ray, exploded parts, materials), ≈20 % hands with the phone, ≈10 % test scenes (dust, water, heat).
- Slow pushes and orbits inside each panel.

## Transitions
- The split itself is the device: panels slide in, one half changes while the other holds; a red laser line can cross from one panel into the other.

## Sound
- Music + SFX only (speech detection found no lines). Electronic with impacts on the material shots.
- Integrated −9.6 LUFS (very loud), LRA 8.4 LU, true peak +0.9 dBTP. Biggest hit +25.8 dB at 0.55 s (first sound), +15.6 dB at 11.45 s (arc/heat). 1.15 s silence on the logo.

## What makes it premium
- One graphic system for the whole film: two panels, two words.
- Pairs make opposites feel designed ("Minimalist outside | Mastery inside").
- Material science (micro-arc oxidation) shown as beautiful CGI, not a chart.

## Recipe (real footage + HTML/GSAP)
- Layout: `display:grid; grid-template-columns: 1fr 1fr; gap: 0` (or 60/40), each panel its own clip; labels `font:400 3vh Inter; position:absolute; top:50%; left:50%; transform:translate(-50%,-50%)`.
- Cut the two panels at different times (offset 0.4-1 s) so the image keeps moving.
- Footage: product macros, "cnc machining aluminium", "electric arc macro", "molten metal glow", "phone falling dust slow motion", "phone underwater bubbles".
- Mix: music + SFX, loud (≈ −10 LUFS), true peak ≤ −1 dBTP.
