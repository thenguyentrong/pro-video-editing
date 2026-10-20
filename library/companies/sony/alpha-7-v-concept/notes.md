# Alpha 7 V Concept | Sony  (Sony Camera Channel, 2 Dec 2025, 3:27 (≈181 s film + 26 s silent recap tail), 16:9, YouTube @ImagingbySony)
URL: https://www.youtube.com/watch?v=tEoVWaISSaA
Purpose: launch concept film (brand + product)
One-sentence point: "Redefine basic" - the new standard camera, told as a fast montage of young photographers catching real moments, cut against white-studio CGI of the sensor and processor.

## Structure (cut times from metrics.json)
- 0-2.1 s: α ALPHA logo on black, then 1.1 s silence.
- 2.1-14.8 s (7 %) cold open: ONE continuous 12.7 s move - a horizon of blue light, a white pavilion, into a metro station, a young man's face in close-up. Sparse VO starts.
- 14.8-26.9 s: "Redefine basic" in black on off-white (≈4 s), then the stacked sensor and processor float in CGI on white with light rays.
- 26.9-57.6 s (17 %) montage 1: photographers in a forest, on a beach, in a jazz club (cymbal, sax), Lisbon alleys, a sprint on the beach that ends in a sand splash; extreme close-up of an eye; a top-down of a person lying in a sand "lens" shape.
- 57.6-97 s (22 %) tech + montage 2: processor CGI with "BIONZ" chip, camera in hands, a portrait take, city rooftops, kids with bubbles; AI tracking shown as a white pose skeleton and boxes over a runner in a forest (88-91 s).
- 97-145 s (26 %) montage 3: concert/jazz, the metro, an exploded CGI camera assembling on white (107-110, 118-122, 128-135 s), photographers framing; the fastest section (up to 13 cuts / 10 s, 0.2 s flashes at 104, 141, 162 s).
- 145-166 s (12 %) product: exploded view assembles into the body, dials and mount macros, an orange ring around the E-mount, final montage of smiling subjects.
- 166-179.2 s (7 %) end: lens front, camera turns on white, "α7V" logo on white (≈4 s), "Redefine basic" (≈3 s); 2.15 s silence; SONY on blue → black (179-181 s).
- 182-207 s: a 25 s silent recap of the end shots (no audio) - not part of the edit, ignore when copying.

## Cut rhythm
- 137 shots in 207.3 s; for the film part (0-181 s) ≈128 shots → ASL ≈1.4 s. Tool ASL 1.51 s, median 0.96 s, 53 % < 1 s, 12 % > 3 s, 40 shots/min.
- ASL per quarter 1.85 / 1.30 / 1.10 / 2.07 s: accelerates to a dense third quarter, then slows for the product end.
- Cuts per 10 s: 0 / 2 / 4 / 9 / 10 / 6 / 6 / 13 / 6 / 7 / 7 / 9 / 8 / 9 / 9 / 12 / 8 / 2 / 2.
- Longest: the 14.8 s opening move, product turn 7.3 s, the silent tail 7.1 s. Shortest 0.21 s (single-frame-like flashes).
- Adaptive and scene detectors agree on 113 cuts; 15 scene-only cuts are flashes and fast whips that were checked on the cut sheets.
- Cuts on music onsets 4 % vs 7 % chance: the edit follows picture and VO, the score is ambient (only 0.36 onsets/s).

## Typography
- Sony's humanist sans (SST, proprietary). Closest free: **Noto Sans Bold** / **Source Sans 3 Bold**.
- Tagline: "Redefine basic" bold, sentence case, no full stop, black (#111) on off-white (#F2F2F2), cap ≈6.7 % H, centred, held 3-4 s, fade in/out ≈0.5 s.
- Product logo: "α7V" logotype cap ≈9 % H, centred on off-white.
- In-picture graphics: thin white AF boxes and a pose skeleton (1-2 px lines) over the subject; an orange ring around the lens mount.
- No feature labels, no specs on screen - the film never lists features.

## Colour / grade
- Two worlds cut against each other: (1) people - teal-green, cool and slightly desaturated filmic grade, soft contrast, warm skin, warm tungsten jazz club; (2) product - high-key off-white studio CGI with soft grey shadows and light rays. Mean luma 0.45.
- Accent: one orange ring (mount) and purple sensor glints.

## Camera / shots
- ≈60 % lifestyle: young photographers in action, handheld, often shot from the subject's side; extreme close-ups (eyes, shutter finger); fast running and sports; top-downs on sand.
- ≈30 % CGI on white: floating sensor, processor, exploded camera assembling, slow orbits.
- ≈10 % product macros (dials, mount, lens front) and logo cards.

## Transitions
- Mostly hard cuts; one-frame white flashes and fast whips between montage and CGI (≈0.2 s); match cuts on shape (round sand shape ↔ lens; eye ↔ lens front). The opening is one in-camera move from landscape into a face.

## Sound
- Sparse narrator: ≈100 words in 180 s (poetic lines, long pauses), not explaining specs.
- Ambient electronic score with SFX (shutter clicks, whooshes on CGI, sand hit).
- Integrated −15.7 LUFS, LRA 8.9 LU, true peak −1.7 dBTP.
- Silences: 1.1 s after the logo (1.0-2.1 s), 2.15 s before the SONY logo (177.05 s); a 2.45 s drop-out at 176.75 s. Hits: +23.3 dB at 38.1 s (jazz club), +17.7 dB at 34.65 s, loudest 77.1 s.

## What makes it premium
- A brand idea in two words, shown twice (start and end) - no feature list.
- Real moments by real photographers; the camera is the tool, the moment is the hero.
- Clean, bright CGI on white between moody teal lifestyle: strong contrast in tone.
- Long opening move and very fast middle: pace as storytelling.

## Recipe (real footage + HTML/GSAP)
- Footage: "photographer running beach sand splash", "jazz club saxophone close up", "young woman photographer street Lisbon", "photographer forest mist", "eye extreme close up", "kids bubbles plaza"; product renders on white.
- Grade lifestyle `contrast(1.05) saturate(.85)` + teal shadows; CGI world `#F2F2F2` with soft rays.
- Tagline card: `background:#F2F2F2; font:700 9.5vh 'Noto Sans'` (cap ≈6.7 % H), black, centred, fade 0.5 s, hold 3.5 s.
- AF overlay: SVG rectangles `stroke:#fff; stroke-width:1.5` that track the subject (GSAP keyframes every 4 frames) + a pose skeleton (lines between 12 points).
- Pace: one 12-15 s opening move, then ≈1.3 s average with bursts of 0.2-0.5 s flashes; slow 4-7 s product shots at the end.
- Mix: ambient score at ≈ −15.5 LUFS, sparse VO, 1-2 s silences before and after the logos.
