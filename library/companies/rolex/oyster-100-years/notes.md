# Worn on the Wrist of History for 100 Years - The Oyster  (Rolex, 2026-04-13, 3:56, 16:9, YouTube @ROLEX)
URL: https://www.youtube.com/watch?v=RuvG8SD0aUw
Purpose: brand film (100-year heritage of the Oyster case)
One-sentence point: One idea from 1926 - the waterproof Oyster case - travelled with a century of human firsts, and it is still made with the same care.

## Structure (cut list + English captions)
- 0.0-1.0 film leader: projector-style flashes with the Rolex crown (0.12-1.04 s).
- 1-17 "1900: the whole century was moving forward" - newsreel archive in a rounded film gate (black surround, ~70 % width): light bulbs, crowds, cars, trains, radio, factories. Flash montage at 16.2-17.5 s (0.2 s shots).
- 17.5-26 title: "A story by" (small italic) + ROLEX crown wordmark over a dark macro of a movement (18-22 s), warm light sweeps across.
- 26-44 the idea: CGI exploded view of the Oyster case (crystal, bezel, case, crown separate and assemble, 27-29 s), macro on the screw-down crown and dial, the 1926 watch on black (41-43 s).
- 44-60 archive print ads collage ("The Rolex three ways protected against water", 44-47 s), a pressure-test machine, then a catalogue: one watch per cut on white, 1926 to today (51-60 s, ~0.5 s each).
- 60-180 a century of firsts: Mercedes Gleitze Channel swim (her real voice, 68 s), Everest (Hillary, 99 s), Submariner (117 s), Apollo lift-off (139 s), MLK "I have a dream" (129 s), Day-Date macro "SUNDAY / MONDAY" changing (142-145 s). Real archive voices and vintage ad narrators carry the audio.
- 180-216 today's manufacture: workshops, watchmakers with loupes, an automated high-bay warehouse (194 s), a robot arm in a glass test cell (212 s), water-resistance test, diamond setting. VO "Rolex combines modern industrial methods and the skills of a craftsman... Certified to the very highest standards".
- 216-228 legacy: modern Oyster Perpetual dial "100 YEARS" (218 s), gloved hands placing it in the box, then testimonials: Sylvia Earle, a conductor, tennis/golf trophies, Scorsese with Oscar - one every 0.45 s (222.4-228.5 s).
- 228.48-236.2 end card (7.6 s): off-white, "100 years of the OYSTER", then ROLEX crown logo (233 s).

## Cut rhythm
- 301 shots in 236 s. ASL 0.78 s, median 0.56 s. ASL per quarter 0.84 / 0.97 / 0.78 / 0.61 s. Verified by eye for 0-20 s: all detected cuts are real.
- Longest 7.56 s (end card), 5.56 s (17.52, the "A story by Rolex" title shot), 4.8 s, 3.84 s. Shortest 0.12 s (flash frames in the leader and at 35 s).
- 79 % of shots under 1 s, 3 % over 3 s. Densest 170-210 s (17-23 cuts per 10 s) in the manufacture section.
- Metronomic stretches: catalogue (~0.5 s per watch) and the testimonial run (0.45 s per person).

## Typography
- Almost none during the film; archive ads and real dials supply the text ("Rolex Oyster", "28", "SUNDAY").
- Opening title: "A story by" small italic serif + ROLEX wordmark with crown, centred, ~3 % height.
- End card: black on off-white (#f2f2f2 with a soft vignette). "100 years of the" italic serif ~3 % height over "OYSTER" roman serif caps ~4.6 % height, block width ~14 % of frame, dead centre (closest free: EB Garamond / Cormorant Garamond). Then the crown + ROLEX logo, same size and place. Fades between cards.

## Colour/grade
- Three layers: (1) B&W and faded-colour archive inside a rounded film gate; (2) warm dark macro (gold, amber, deep brown/black) for the product; (3) clean cool white/steel for the modern catalogue and manufacture.
- No letterbox. Gate surround is pure black.

## Camera/shots
- Macro product: crown, bezel teeth, dial printing, date wheel flipping - slow sliders and rotations; CGI exploded views for the construction story (clearly renders, 27-29 s).
- Archive newsreels and print ads (real).
- Manufacture: wide workshop shots, extreme close-ups of hands/tools, automated warehouse and robot cells - real footage, cool grade.

## Transitions
- Hard cuts; match cuts on round shapes (movement -> dial -> crown); archive gate appears and disappears with cuts. Fades only on the end card.

## Sound
- Continuous orchestral score; archive voices (newsreel narrators, Gleitze, Hillary, NASA, MLK) and vintage Rolex ad VOs collaged on top - no single narrator.
- Integrated -14.1 LUFS, loudest 0.5 s at 139.05 s (the Apollo lift-off). No drop-outs - the score never stops; emphasis comes from archive voice entries. Final hit 230.15 s (+15.5 dB) under the end card.

## What makes it premium
- Real history as proof - the brand stands next to the moments, it does not shout.
- Extreme speed (median 0.56 s) but very quiet compositions: one object, centred, clean background.
- Product truth shown in three ways: CGI construction, macro of the real part, test machine.
- Off-white end card with a tiny serif - no claim, no CTA.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Archive gate: `<div class="gate">` 70vw x 70vh, `border-radius: 4%`, black stage around it; inside the clip `filter: grayscale(1) contrast(1.15)` + flicker `gsap.to(gate, {opacity: .92, repeat: -1, yoyo: true, duration: .08})`.
- Flash montage: 6-8 archive clips at 0.2 s each, then a 5 s title shot.
- Catalogue: same object type centred on white, one per 0.5 s, same scale every time (for robots: each robot generation on the same white sweep, same camera height).
- Testimonial run: 12 faces at 0.45 s each right before the end card.
- End card: `background: radial-gradient(#f5f5f5, #e9e9e9); color:#111; font-family: 'EB Garamond'`, italic line 3vh, caps line 4.6vh letter-spacing .04em, `gsap.from(card, {autoAlpha:0, duration:.6})`, hold 4 s, cross-fade to the logo 3 s.
