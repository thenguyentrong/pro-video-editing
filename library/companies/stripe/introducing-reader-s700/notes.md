# Introducing Stripe Reader S700  (Stripe, 2023-05-02, 74.1 s incl. 1.4 s black, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=9oieNo53aNY
Purpose: launch film (hardware + software product, told through a customer platform and its café customer)
One-sentence point: A restaurant-software startup and one of its cafés show that the new countertop reader makes ordering and paying feel simple.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-2.0 hook (0-3 %): five 0.36 s shots of the reader in a café (espresso, latte art, hand with the device) — a product flash before any words.
- 2.0-6.0 (3-8 %): flat motion-graphics map on Stripe violet, a pin drops on the city, the partner's logo pops in, the city name types in big condensed caps.
- 6.0-22.0 (8-30 %): two co-founders on a sofa (two-shot + singles). From 9 s the frame splits: interview on the left half, a violet panel on the right with an animated icon + one feature word per panel (four panels, 1-2 s each). The map comes back and zooms out to the whole country (16-22 s).
- 22.0-33.6 (30-46 %): a dark circle mask opens on the café exterior (22 s); café owner interview with lower third, staff and guests, the owner unboxes the reader.
- 33.6-38.0 (46-52 %): three clean product renders on a lavender gradient (front, back, three-quarter) and a UI close-up (sign on screen).
- 38.0-52.6 (52-71 %): the reader in real use: espresso, tap to pay, staff at the counter; small line-art sparkles pop around the device.
- 52.6-56 (71-77 %): split screen again, founder left, product insert right.
- 56-68.5 (77-94 %): founders use the reader in their office; product held to camera.
- 68.5-72.7 (94-100 %): a white wave wipes the frame to an off-white end card (product name + URL, 1.5 s), then a three-logo lockup (customer + platform + Stripe), then 1.4 s black.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 45 shots in 72.7 s (black tail excluded), ASL 1.62 s, median 1.36 s, 31 % under 1 s, 11 % over 3 s, 37 shots/min. Quarters 1.51 / 1.65 / 1.40 / 1.65 s: an even pulse.
- Shortest 0.36 s (opening product flash, five in a row); longest 5.6 s (map zoom-out), 4.7 s (tap-to-pay hero), 4.2 s (end card).
- Densest: 30-40 s (10 cuts / 10 s: unboxing + renders).
- Verified by eye on the contact sheet and the cut pairs; five cuts added that the scene detector missed (map in at 2.0 s, angle changes behind the split screen at 10.0 / 12.2 s, render angle changes at 35.6 / 36.4 s).

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- City name and feature words: tall condensed grotesque, bold caps (free: Oswald 600 or Bebas Neue). City name cap height ≈18 % H, bottom-right; feature words ≈5 % H caps, centred in the violet half under a 2-colour icon, 1-2 words, 1-2 s each. Colour light lavender ≈#b3b0ff on violet, or navy on violet.
- Lower thirds: Stripe's own grotesque (Söhne-like; free: Inter). Thin vertical bar | name (regular, cap ≈3.8 % H) | thin bar | role (≈2.8 % H), white, one line at y ≈83 % H, left edge x ≈6 %. Fade in/out ≈0.3 s, hold 2-3 s.
- End card: product name semibold navy ≈#0f1f2c, cap ≈5.5 % H, centred; URL regular ≈3.5 % H under it; off-white ≈#f5f9fa. Hold 1.5 s.
- Logo lockup: three logos in one row joined by small "+", centred, ≈5 % H.

Colour/grade: palette, contrast, grain, letterbox
- Live action warm and natural (wood, café tan, soft daylight, shallow focus). Graphics in brand violet: map ≈#796af9, panels ≈#5d4df8, renders on lavender gradient ≈#a6a7f7 → #bfc0f9, navy ≈#0f1f2c for icons. No grain, no letterbox.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Interviews: two-camera (two-shot + single CU), soft key, office background. Product B-roll: macro and medium shots with very shallow focus, slow slider moves. Three 3D/studio product renders on gradient. One UI insert (screen content composited flat). Flat 2D motion-graphics maps.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts almost everywhere. Graphic transitions: split-screen panels wipe in (9 s, 53 s), map zoom-out, a circle iris mask from map to the café (22 s), a white wave wipe into the end card (68.5 s). Small line-art sparkles and dots burst around the device on taps (5-6 times).

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Voice: interview sound bites only (two founders + café owner), from 5.5 s to 67.5 s, ≈60 s of speech (≈2.7 words/s); no narrator.
- Music: light upbeat bed under the voices; small UI pops on the graphics. Integrated −19.6 LUFS, LRA 4.5 LU, true peak −2.8 dBTP. No drop-outs; 1.2 s silence at the end. Biggest rise +24.5 dB at 31.3 s (bed swells into the unboxing).

What makes it premium (3-5 bullets)
- The customer tells the story; Stripe only appears in the renders and the end card.
- One graphic system (violet map, icon + one word, iris mask, wave wipe) ties live action to brand.
- Product truth: real hands, real taps, real café; renders only for 4 s.
- Even, calm pulse (quarters 1.4-1.65 s) with one fast product flash as a hook.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920×1080, 70-75 s. Hook 2 s = 5 product shots × 0.36 s. Then city map 4 s, interviews with split screen 13 s, customer site 11 s, renders 4.5 s, product in use 15 s, payoff 15 s, end card 4 s.
- Split screen: interview `clip-path: inset(0 50% 0 0)` left; right panel `#5d4df8`, icon 18 % H navy, word `600 5vh Oswald` caps colour `#0f1f2c`, panel slides in `x:100% → 0` 0.4 s `power3.out`, swap every 1.5 s.
- Lower third: `Inter 400 3.8vh` white, role `2.8vh`, 1 px white bars, `left:6%; top:80%`, fade 0.3 s.
- Iris transition: map layer with SVG circle mask growing `r 0 → 60vmax` 0.8 s `power2.inOut`, navy ring 4 % H around it.
- End: white wave SVG path sweep 0.5 s, then `#f5f9fa` card, product name `Inter 600 5.5vh #0f1f2c`, URL `3.5vh`, hold 1.5 s; logo row 1.5 s; 1 s black.
- Sound: interview bites on top, bed at −20 LUFS integrated, no drops.
