# PlayStation 5 Pro Console - Reveal Trailer  (Sony Interactive / PlayStation, 10 Sep 2024, 1:05, 16:9, YouTube @PlayStation)
URL: https://www.youtube.com/watch?v=6HaRMiTfvks
Purpose: hardware reveal trailer (product launch)
One-sentence point: a dark, slow product tease turns into a burst of colour - three tech claims, each one a CGI light metaphor with a big caps title, then the console on a rainbow light floor.

## Structure (cut times from metrics.json)
- 0-0.5 s: PlayStation logo on blue (ident), 0.4 s silence.
- 0.5-21.4 s tease (33 %): black, then grazing-light macros of the console edges, one blue light line on the body; caps titles fade in and out one by one: "INTRODUCING" (8-10 s), "THE NEXT LEAP" (12-13 s), "IN CONSOLE GAMING" (14-16.5 s). Every shot is a slow move on one detail (2.5-3 s per shot).
- 21.4-22.3 s reveal: the console stands in a beam of rainbow light (the music hits +29 dB at 20.45-21.55 s).
- 22.3-52.6 s three claims (47 %): "ENHANCED WITH" over a projector beam -> pixel wall turns into "PLAYSTATION SPECTRAL SUPER RESOLUTION" (claim 1, 7.4 s continuous shot); a lens/tunnel spiral -> "HIGH FRAME RATES" over a speed meter (claim 2); glowing orange comets skid over dark tiles -> glass cone, sphere and PlayStation shapes catch rainbow reflections -> "ADVANCED RAY TRACING" (claim 3).
- 52.6-62.6 s end (15 %): light beams rise from the floor and form the rainbow light-speed floor, white flash (57 s), console + controller on the floor; PS5 Pro logo + "WITNESS PLAY UNLEASHED" left (10 s shot).
- 62.6-64.6 s: "PLAY HAS NO LIMITS" on PlayStation blue, then the face-button symbols glow on blue.

## Cut rhythm
- 18 shots in 64.6 s, ASL 3.59 s, median 3.0 s, 11 % < 1 s, 50 % > 3 s, 16.7 shots/min.
- ASL per quarter 2.31 / 3.23 / 3.23 / 4.04 s: the film slows down as it goes - the opposite of a montage trailer.
- Cuts per 10 s: 3 / 4 / 3 / 1 / 4 / 1 / 1. Longest: end hero 10.0 s (52.6 s), Spectral pixel wall 7.4 s, tunnel 5.5 s.
- Cuts checked by eye on the cut sheet (17 real cuts). Many of the shots are one continuous CGI camera move that changes scene inside the shot (pixel wall -> title, beams -> floor), so the visual change rate is higher than the cut count.
- Cuts on music onsets 18 % vs 14 % chance: the CGI moves set the timing.

## Typography
- Heavy wide geometric caps (PlayStation's own SST family style). Closest free: **Montserrat ExtraBold** caps or **Archivo ExtraBold** (semi-expanded).
- White, all caps, tracking ≈ +0.02 em, centred.
- Tease titles: cap ≈7 % H, one line ("INTRODUCING" ≈41 % W), held 1.5-2.5 s, fade in 0.5 s, fade out 0.5 s, on black or over a dark macro.
- Claim titles: two lines, cap ≈8 % H each, centred, placed INSIDE the CGI scene (the pixel wall assembles behind it); smaller "ENHANCED WITH" eyebrow cap ≈4 % H above a light source.
- Legal micro-text under each claim (≈1.5 % H, centred bottom, two lines).
- End lockup: PS5 Pro logo + "WITNESS PLAY UNLEASHED" (cap ≈4.2 % H, two lines) as a left-third block beside the product; small legal line bottom centre.
- Tagline card: "PLAY" huge (cap ≈10 % H) over "HAS NO LIMITS." small, white on PlayStation blue (#0070D1 to #003791 gradient).

## Colour / grade
- First third: near black (mean luma 0.19 for the whole film), graphite console with one blue edge light; titles are the only bright thing.
- From the reveal: hyper-saturated spectral rainbow (orange, magenta, violet, cyan), light beams and pixels on black. The rainbow floor is the product's world.
- Close: PlayStation blue.

## Camera / shots
- 100 % CGI. Grazing-light macro slides along the console, slow dolly-ins; projector beams; pixel walls; a spiral tunnel fly-through; comets; abstract glass shapes (cone, sphere, cross, cube) with refracted rainbow light.

## Transitions
- Hard cuts on black in the tease; the white light flash at 57 s; in-shot morphs (pixels assemble into the title wall; beams become the floor). About a third of the scene changes happen inside a continuous move, not at a cut.

## Sound
- Music only, no voice (speech detection found 0 words). Electronic/orchestral build.
- Integrated −14.0 LUFS, LRA 9.3 LU (wide: quiet tease, loud claims), true peak −0.3 dBTP.
- Hits: +29 dB at 20.45 s into the reveal, +19-20 dB on each claim start (2.2, 44.0 s), +18.9 dB at 21.55 s, +17.5 dB at 52.75 s (finale). Loudest 48.9 s (ray-tracing claim). 0.4 s silence after the ident.

## What makes it premium
- Restraint first: 20 s of dark macros and three small caps words before any colour.
- One big colour event (the rainbow) that becomes the product's world and the end-card floor.
- Each claim = one CGI metaphor with the title living in the scene, not pasted on top.
- Long shots (50 % over 3 s) and a pace that slows down to the end.

## Recipe (real footage + HTML/GSAP)
- Tease: 6-7 shots of 2.5-3 s, product macros under one raking light on black (shoot with a single strip softbox or LED tube; `filter: contrast(1.2) brightness(.8)`), one coloured edge light. Titles in `font: 800 7vh Montserrat; text-transform: uppercase; letter-spacing: .02em`, `opacity 0 -> 1` 0.5 s, hold 2 s, out 0.5 s.
- Reveal hit: cut to the product in a light beam exactly on the music hit; 0.4-1 s silence or a low drone before it.
- Claim scenes: stock CGI loops ("abstract pixel grid colourful", "light tunnel spiral purple", "rainbow light speed floor", "glass shapes refraction rainbow"), 5-7 s each, titles two lines cap 8 % H centred, eyebrow cap 4 % H, legal 1.5 % H at 92 % H.
- End: product on a rainbow floor 8-10 s, logo + two-line tagline in the left third (cap 4 % H), then a 2 s brand-colour tagline card.
- Mix: −14 LUFS, music only, a +20 dB hit on each claim.
