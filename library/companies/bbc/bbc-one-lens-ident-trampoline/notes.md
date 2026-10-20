# BBC One "Lens" ident – Hall (Trampoline), clean full-length  (BBC One, ident system launched 2022, 40.1 s, 16:9, broadcast ident; uploaded 2022-08-18 by a fan archive channel "Burcica", source given as the music house RESONATE's Instagram – not an official BBC upload)
URL: https://www.youtube.com/watch?v=-YG7LdN7dEw
Purpose: channel ident (between programmes; the long "full-length" version runs under continuity announcements)
One-sentence point: ordinary people in a shared space, and a circular lens briefly opens a window to another shared space – "the spaces we share".

Structure:
- 0.0–1.6 real scene: wide, locked-off shot of a bright sports hall with trampolines and people jumping. BBC blocks top-centre and ONE bottom-centre are on screen from the first frames (~0.4 s).
- 1.6–3.2 the LENS enters from screen right as a thin translucent edge (an ellipse seen side-on), turning toward camera; music has started at 1.2 s (+26.7 dB from silence).
- 3.2–6.4 the lens turns face-on: a large circle (~80 % of frame height) through which we see a different place – an audience on chairs, a dark stage with spotlights and fairy lights, purple/pink light – blended with the hall.
- 6.4–9.0 the lens keeps rotating, its rim turns copper/gold with lights, and it exits screen right; loudest point at ~5.5 s (−8 LUFS momentary).
- 9.0–40.0 the same hall continues with no lens: trampolinists flip and bounce for 31 s. This tail exists so the presentation team can talk over it or cut out at any time.

Cut rhythm: 1 shot, 40 s, no cuts (ASL 40 s). The camera is locked off (no move visible on the sheet). Rhythm comes only from the people jumping and the lens rotation.

Typography / logo:
- BBC blocks (three white squares with dark letters B, B, C, current 2021 logo) top-centre, about 8 % of frame height, ~17 % of frame width, at ~7–15 % from the top.
- "ONE" in white bold sans (BBC Reith Sans Bold; closest free match: Inter 700 / Source Sans 3 Bold), all caps, ~5–6 % cap height, bottom-centre at ~85–90 % from top.
- Logo + channel name are static the whole time (no animation inside the ident – they are part of the composition, not a reveal).

Colour/grade: natural, bright, soft daylight (white walls, blue trampolines, warm wood floor), slightly lifted blacks; the lens brings the only saturated colour (violet, magenta, copper/amber). 0 % empty frames.

Camera/shots: one real-world location, locked-off wide shot, real people (non-actors look), documentary feel. The lens is a VFX element (a reflective/refracting disc) composited into the plate; the other scene inside the lens is a second real plate.

Transitions: none – the "transition" is the lens itself acting as a moving window/mask between two places.

Sound: integrated −11.9 LUFS (loud, broadcast-ident level on this upload), LRA 3.8 LU, true peak −0.7 dBFS. Music starts at 1.2 s, peaks at 4–6 s while the lens is face-on (−8 LUFS), then sits flat at −10 to −12 for the long tail, decaying slightly to −14 by 38 s. No voice. I did not listen; per the uploader the sound comes from RESONATE (music house). There is no separate sonic-logo sting visible in the curve.

What makes it premium:
- One brand device (a circle/lens, heir to BBC One's globe/balloon/circle idents) used once, then gets out of the way.
- Real people and real places (inclusive "spaces we share" idea), not CGI branding.
- Locked-off long take = calm, confident, and practical for continuity (cut out anywhere after 9 s).
- Logo layout is fixed (blocks top-centre, ONE bottom-centre) so every ident in the set feels like one system while the location changes.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Footage: two locked-off wide plates of real shared spaces (A = the main space, B = a different community space, darker and warmer), 40 s of A, 8 s of B.
- Lens: a <div> circle 80 % of frame height with overflow:hidden showing plate B (mix-blend-mode: screen at 0.85 opacity), plus a ring border 6–10 px with a copper gradient (conic-gradient(#f2c08a, #8a4b22, #f7d6a8, #8a4b22)). Fake the 3D turn with GSAP: rotateY 85° → 0° (1.6–4.4 s, ease "power2.out") while x moves 30 % → 0 %, then rotateY 0° → −80° and x 0 → +45 % (6.4–9.0 s, ease "power2.in"); perspective 1400 px on the parent; add backdrop-filter: blur(2px) saturate(1.3) inside the circle for a glass feel.
- Logo layer: static blocks logo top-centre (8 % height) and channel word bottom-centre (Inter 700, 5.5 % cap height), opacity 0 → 1 over the first 0.4 s only.
- Audio: music in at 1.2 s, swell while the lens faces camera, then a steady bed that can be faded anywhere after 9 s.
