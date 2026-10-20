# INSPECT (2026)  (Linear, 2026-08-31, 236.8 s, 16:9, YouTube / customer page)
URL: https://www.youtube.com/watch?v=bRCaSP9x614
Purpose: customer short film (brand documentary about a customer's in-house coding agent; launch support for Linear's agent features)
One-sentence point: An engineering team built its own coding agent that now writes most of its pull requests, and Linear is where that work is planned and reviewed.

Structure: beats with timestamps (% of runtime)
- 0-21.9 s (0-9 %) cold open: a wide of one engineer at a desk in a white-brick loft, warm practical lamp; hands on the keyboard; a mono caption types on bottom-left at ≈15 s (a one-line fact about the company's code volume).
- 21.9-40 s (9-17 %) interview: off-axis close-ups of the engineer (looking off camera, 3/4 profile), cutaways to hands.
- 40-52 s (17-22 %) first graphic: a dark silhouette profile with a mono HUD (a striped progress bar and a short label) typing on in the left third.
- 52-70.9 s (22-30 %) interview + phone/hand inserts.
- 70.9-120.5 s (30-51 %) the mechanism: an eye close-up dissolves (83.2 s) into a soft-focus room plate that carries a 1-px line flow chart (INSPECT box → arrow → TEST with pass/fail check boxes, more boxes added) for 37 s while the interview continues as VO.
- 120.5-152.9 s (51-65 %) interview, a second team member joins (148 s), faster cutting (ASL 3.7 s in Q3).
- 152.9-188.5 s (65-80 %) reflective inserts: notebook, handwriting macro, reading a book on a sofa (one 14 s take).
- 188.5-221 s (80-93 %) interview resolution; a third person with headphones at a laptop.
- 221-235 s (93-99 %) closing wide on the headphones shot; crew credits type on bottom-left in the same mono.
- 235-236.8 s logo mark + wordmark on black, silence.

Cut rhythm (verified)
- Scene detection found 25 cuts; adaptive 40; all 40 checked on before/after pairs and kept. One dissolve added (83.2 s). Several long tilts/racks (57-63 s, 129-132 s, 154-160 s) are single takes, not cuts.
- 42 shots, ASL 5.64 s, median 3.34 s, 4.8 % under 1 s, 59.5 % over 3 s, 10.6 shots/min. Per quarter 5.38 / 9.87 / 3.70 / 4.93 (Q2 holds the 37 s graphic shot). Longest 37.3 s (HUD flow chart), 14.0 s (handwriting), 14.0 s (closing). Shortest 0.71 s.

Typography
- One mono face for everything (caption, HUD labels, credits): white, caps for captions/credits, sentence case inside HUD boxes. Caption cap ≈1.9 % H (line box 2.7 % incl. block cursor) at x ≈6 %, y ≈87 %. HUD labels ≈1.7 % H inside 1-px white boxes ≈23 % W × 13 % H.
- Animation: type-on with a solid block cursor (terminal feel), boxes draw on, progress bars fill; no fades of whole cards.
- Closest free font: IBM Plex Mono or JetBrains Mono (regular).
- End logo: mark + wordmark, centred, line box ≈8.8 % H incl. glow, 1.7 s.

Colour/grade
- Warm tungsten practicals (amber lamp ≈#e8a050) against cool grey-lilac daylight walls (≈#8c88a0); skin warm; blacks slightly lifted, soft contrast, fine grain. Silhouette shots in deep blue-black. Mean luma 0.24.

Camera/shots
- Cinema camera, shallow depth of field, slow handheld/slider drift, off-axis interview framings (subject never looks into the lens), many hand and object inserts, one long locked-off "graphics plate" shot. Real people, real office.

Transitions
- Hard cuts on sentence ends (cuts on onsets 39 % vs 45 % chance: not beat-cut). One dissolve into the graphics plate. HUD graphics appear over picture instead of cutting to full-screen graphics.

Sound
- Interview voice almost wall to wall: speech from 1.4 s to 224 s, ≈632 words, ≈2.8 words/s (measured with speech detection, not transcribed).
- Soft music bed under the voice, RMS steady at −15 to −20 dBFS; a few lifts (+21 to +25 dB rises at 93, 186, 215, 221 s) at section changes. No drop-outs; 1.75 s silence under the logo.
- Integrated −14.2 LUFS, loudness range 4.3 LU.

What makes it premium
- Shot like a short documentary, not a testimonial: off-axis interviews, inserts, real light.
- The product idea (an agent that inspects and tests) is drawn as a minimal mono HUD over a soft plate, not as screen recordings.
- One typeface, one colour (white) for all graphics, terminal type-on as the motion signature.
- Patience: 37 s graphic hold, 14 s inserts, credits at the end like a film.

Recipe (real footage + Hyperframes, 1920×1080, 3-4 min)
- Shoot: 1 main subject, 2 supporting; off-axis interview (85 mm look, f/2), 15-20 inserts (hands, keyboard, notebook, objects), 2-3 wides of the space with practical lamps. Grade warm practicals vs cool daylight, lift blacks to ≈#101014, light grain.
- Cut on sentence ends; ASL ≈5-6 s, median ≈3.3 s; hold 1 graphic plate 20-40 s mid-film.
- Mono HUD: `font: 400 1.7vh 'IBM Plex Mono'`, `color:#fff`; boxes `border:1px solid rgba(255,255,255,.85)`, label set into the top border; draw lines with `strokeDashoffset` 0.5 s; type-on with `steps(n)` at ≈25 chars/s and a block cursor `█` blinking 0.5 s.
- Caption: caps `1.9vh` at `left:6%; bottom:11%`, type-on, hold ≈5 s.
- Credits at the end in the same mono, bottom-left, one line per 0.1 s type-on; logo on black 1.5-2 s in silence. Master −14 LUFS.
