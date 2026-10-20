# New 2026 F1 Opening Titles  (FORMULA 1, uploaded 2026-03-05, 57.0 s, 16:9, YouTube / FORMULA 1 channel; the title sequence that opens every race broadcast)
URL: https://www.youtube.com/watch?v=Sks_fMr2Yss
Purpose: broadcast opening titles / season intro (driver roll-call)
One-sentence point: all 22 drivers of the 2026 grid, one hero portrait and one name card each, in 48 s, ending on the F1 logo.

Structure:
- 0.0–1.4 HOOK: macro of a glossy, extruded red F1 logo on red. Music hits at 1.5 s (+17 dB, the only big rise).
- 1.4–49.4 ROLL-CALL: 22 drivers, two per team, in this order: Cadillac (Pérez, Bottas), Alpine (Colapinto, Gasly), Audi (Bortoleto, Hülkenberg), Haas (Ocon, Bearman), Aston Martin (Stroll, Alonso), Racing Bulls (Lindblad, Lawson), Williams (Sainz, Albon), Ferrari (Hamilton, Leclerc), Red Bull (Hadjar, Verstappen), Mercedes (Antonelli, Russell), McLaren (Piastri, Norris). This is the 2025 constructors' order reversed, new team first (my inference); the champion team closes, and Norris carries the number 1 in the corner digits (47.4–49.3).
  - ~2.2 s per driver (48 s / 22). Usually 2 shots: a close portrait (face fills 60–80 % of frame height) and a full-body or 3/4 shot with the name card.
  - CG car-part inserts between some teams as "breathers": white/red car body light-sweep (15.3–17.2), wheel/halo shapes (22.3–24.3), rear rain light (30–31), wheel arch (35.9–37.5).
- 49.4–51.0 PAYOFF: red light streaks collapse into the F1 logo (full-frame red glow 49.4–50.4), logo shrinks to centre.
- 51.0–57.0 END CARD: red F1 logo static on F1 carbon black (#16141f measured, brand #15151E). Music decays 52–54 s, last 3 s are silent (broadcast handover).

Cut rhythm: 43 shots in 57.0 s, ASL 1.33 s, median 1.00 s; 49 % of shots under 1 s, 9 % over 3 s. ASL per quarter 1.43 / 0.89 / 1.10 / 2.04 (the logo end card is the only long shot, 7.6 s). Cuts per 10 s: 8, 8, 9, 9, 8, 0 = a steady machine-gun rhythm with no build. About 4 of the 42 detected boundaries are graphic-layer changes over the same plate (giant letters snapping in at 5.56, 9.80, 39.40, 39.52); counting only plate changes the ASL is ~1.5 s. Cuts 40–50 s are motion-blur smears that the hard-cut detector missed; I added 8 by eye (41.1, 41.8, 43.4, 44.0, 45.2, 46.1, 47.1, 49.4).

Typography (the name-card system, very consistent across all 22):
- First name: brush/marker script (yellow-white or red), tilted ~-8°, ~10 % of frame height including swashes, overlapping the left edge of the surname. Closest free match: "Mrs Saint Delafield" or "Allison" (thin fast script).
- Surname: extra-bold, wide, all-caps sans (F1's own Formula1 Display Wide/Black). Cap height 8.5–9.5 % of frame height (STROLL 8.8 %, NORRIS 9.4 %, HULKENBERG 8.3 %), width 30–48 % of frame. Closest free match: Archivo Black / Archivo Expanded 900, or Unbounded 800. White on dark sets, near-black on the light grey set.
- A red colour wipe runs through the surname left→right during the reveal; mid-frame you see the word half white/half red (HUL|KENBERG, NORRI|S, 11.8 s and 47.9 s).
- Giant background surname: the same wide caps at 40–75 % of frame height, cropped by the frame edges, as thin grey outlines (light sets) or solid red (Bottas 5.5 s, Bearman 17.6 s), drifting sideways.
- Data labels: car number in a squared techno numeral (~2 % of frame height) repeated in 3–4 corners; team name in widely tracked monospace caps (~1.7 %), e.g. "ASTON MARTI", "MCLAREN". Closest free match: Space Mono Bold / Share Tech Mono, letter-spacing ~0.4em.
- Animation: surname slides/smears in with heavy motion blur (~0.2 s), script writes on, background letters slide slowly; exits are smears or giant glyphs wiping across the frame (20.3 s, 39.4 s).

Colour/grade: three set colours that rotate: F1 red studio (#5c020c–#750211 background with bright red light streaks), light grey cyclorama (#cdcbce), and black/charcoal with hard rim light. Red is the only saturated colour besides the team suits. High contrast, crisp, glossy; 14 % of frames mostly empty (dark). No letterbox.

Camera/shots: studio portraits (shot on a volume/cyc), slow push-ins, a few fast whip pans; drivers pose (arms crossed, holding helmet, adjusting gloves). Close-ups with the face filling the frame for the bigger names (Bottas, Hamilton). CG car renders in a white/red light tunnel as inserts. No race footage at all.

Transitions: hard cuts (~30), motion-blur smear pushes (~8, mostly 40–50 s), giant-letter/glyph wipes (~4), and one light-streak morph into the logo. No dissolves.

Sound: driving, steady score (very likely a version of Brian Tyler's F1 theme, the official theme since 2018; I did not listen, so this is not verified). Measured: music in at 1.5 s, then a flat wall −12 to −16 LUFS momentary for 48 s (LRA 3.4 LU, very compressed), loudest at 50–51 s (−9 LUFS) exactly on the logo, then a 3 s decay and 3 s of silence. Integrated −14.1 LUFS, true peak +0.2 dBFS. Only 17 % of cuts land on an audio onset (chance 13 %): the picture is cut to a grid, not to individual hits.

What makes it premium:
- A strict template repeated 22 times (portrait → name card → wipe) so the speed feels designed, not chaotic.
- Type is the hero graphic: giant cropped surname + script first name + mono data = three type layers with clear jobs.
- Only one brand colour (red) on neutral sets; team colours come from the suits, not the graphics.
- The logo is the loudest and longest moment; everything before is a build to it.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Footage: shoot each person in front of one plain backdrop (grey paper or black), 2 shots each: tight portrait (slow push-in) and full body (hands on helmet). Grade: crush blacks, keep skin natural, add a red key light or a red gradient background (#5c020c → #e10600).
- Layout per person (1920×1080): giant surname behind the subject, font-size 520–700 px, Archivo 900, letter-spacing −0.02em, colour rgba(255,255,255,0.12) stroke 2 px (light set) or #e10600 fill, x drifts −6 % over 2.2 s (ease "none"). Foreground surname 96 px cap height (≈9 %), Archivo Expanded 900 uppercase, white; script first name 110 px, rotate −8°, overlapping the surname's first letter by ~20 px. Corner numbers 22 px Space Mono Bold; team label 18 px Space Mono, letter-spacing 0.4em.
- Motion: surname from x +120 px, filter blur(18px) → 0, duration 0.25, ease "power4.out"; red wipe = clip-path inset(0 100% 0 0) → inset(0 0 0 0) on a red copy above the white text, 0.35 s, then the red copy wipes out to the right; script = SVG stroke-dashoffset write-on 0.4 s.
- Exit: one of (a) giant white glyph wipe (a 1.5× frame-height letter shape moving across in 0.2 s, ease "expo.inOut"), (b) motion-blur smear: scaleX 1 → 1.4 + blur 0 → 30 px in 0.15 s, cut on the blur peak.
- Rhythm: 2.2 s per person, 1.0 s median shot, no slow-down until the logo. End: logo 37 % of frame width on #15151E, light-streak collapse 1 s, hold 6 s, music out after 3 s.
