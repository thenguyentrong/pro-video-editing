# House of the Dragon Season 2 – Opening Credits  (HBO, uploaded 2024-06-17, 114.2 s file = 98.9 s sequence + 5 s Max card + 10 s YouTube end screen, 16:9 file with 2:1 letterbox, YouTube / HBO Max channel)
URL: https://www.youtube.com/watch?v=9Dk3OOgXlzo
Purpose: main title sequence (series opening credits)
One-sentence point: the family history is an embroidered tapestry, and the camera reads it panel by panel until the title appears in the dark.

Structure:
- 0.0–4.6 HOOK: extreme macro of red and white yarn stitches (a tapestry being made); first star card EMMA D'ARCY bottom-right. Music starts at frame 1 (first hit at 0.6 s, no silent lead-in).
- 4.6–34 BUILD 1 (history): one panel per shot, each ~4.3 s: castles, a dragon, mother and child, stitched branches, battle with dragons. Cast names in groups of 1–3.
- 34–43 BUILD 2: darker, faster panels (2.1–3.0 s shots): dragon wings, "MUSIC BY RAMIN DJAWADI" at 39–41 s.
- 43–56: the city in red thread between two dragon jaws (45 s), the Targaryen three-headed-dragon sigil (52–55 s), Dragonstone.
- 56–90 TURN (the current conflict): gold-thread royal figures, skeletal figures, a woman in green, a crown lying in a red stain (73.5–75.7 s), the Iron Throne with swords radiating (76–82 s), a manuscript panel with hands (82–90 s, longest content shots 8.1 s and 8.8 s).
- 90–94: two dragons fighting in stitched thread.
- 94.0–98.9 PAYOFF: dark, misty night landscape, lit castle window at top, title HOUSE OF THE DRAGON fades up in metallic gold.
- 99.1–104 Max card on bright blue ("max / THE ONE TO WATCH", then "PLANS START AT $9.99/MONTH"); 104+ YouTube end screen.

Cut rhythm: 24 shots in 99 s, ASL 4.12 s, median 4.21 s. Very regular: 15 of 24 shots are 4.1–4.6 s long, like a metronome (my guess: two bars of the theme per panel; not verified against the score). ASL per quarter 4.1 / 2.8 / 3.5 / 5.0 s: denser in the second quarter (2.1–2.2 s shots at 37–44 s), slower at the end (8–9 s shots). No shot under 2 s. Inside every shot the camera glides and racks focus over the fabric.

Typography:
- Credits: classical inscriptional serif, all caps with small caps for first letters (Trajan-like; closest free match: Cinzel 400), very wide tracking (~0.25–0.3 em), warm parchment-gold colour (~#d8c29a) with low contrast to the cloth. Cap height ~2.5–3 % of frame height (estimated from frames, the measuring tool cannot separate it from the bright cloth).
- Groups of names are stacked and staggered (each line indented differently, 14 s), not centred blocks. Role labels ("PRODUCTION DESIGNER", "EXECUTIVE PRODUCER") are the same serif at ~60 % size, above the name.
- Placement: lower-left, lower-right or upper-right, wherever the cloth is empty. Animation: soft fade (~0.5 s), no movement.
- Title: the GoT-family wordmark "HOUSE of the DRAGON" (small stacked "OF THE" between the words), metallic gold with soft glow, centred, ~10 % of frame height, ~60 % of frame width, fades up over ~1 s over the dark landscape.

Colour/grade: warm sepia parchment (~#c9b28c) under a single low raking light, deep brown-black shadows, thread colours restricted to oxblood red (~#8e2a1f), gold (~#c79a3e), dark teal for dragons (~#2e4a4a) and bone white. Floating ember/dust particles (53 s, 74 s). Letterbox: 26 px bars top and bottom of 480 (5.4 % each) = 2:1 frame inside 16:9. Almost no "empty" frames (1 %), the cloth fills everything.

Camera/shots: CG (or photographed) embroidery, macro lens look, shallow depth of field, slow lateral glides and push-ins, raking light so every stitch casts a shadow. No live action, no actors.

Transitions: 23 hard cuts between panels plus slow focus pulls inside the shots. Final title shot is a hard cut to dark. No dissolves, no wipes.

Sound: Ramin Djawadi's House of the Dragon / Game of Thrones theme (orchestral, cello-led; known music, I did not listen). Measured: wall-to-wall and flat — momentary loudness stays between −11 and −17 LUFS for the full 99 s, LRA only 3.2 LU, integrated −15.4 LUFS, true peak 0.0 dBFS. No drop-outs, no silence, no big hit after the first downbeat (0.6 s). Cuts are not on onsets (13 % vs 6 % chance), so the editing follows phrase length, not beats. No voice.

What makes it premium:
- A single material metaphor (needlework) used for every shot, so 24 cuts still feel like one object.
- Metronomic shot length (~4.2 s) gives a ceremonial, reading-a-chronicle pace.
- Raking light + macro shallow focus make the craft tactile; embers add life without extra elements.
- Inscriptional serif with wide tracking = history/royalty; tiny size keeps the art the hero.
- Restricted palette (parchment, oxblood, gold, teal) across the whole piece.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Footage: shoot real embroidery/tapestry/fabric with a macro lens, one hard side light at ~15° (raking), f/2.8, slow slider moves (2–3 cm per shot). 20–24 shots. Grade warm: shadows #1a120c, mids #c9b28c, keep reds desaturated toward #8e2a1f.
- Frame: 2:1 letterbox inside 16:9 (bars 5.4 % top and bottom, pure black).
- Cut every 4.2 s (or 2 bars of your music); allow 2–3 s shots in the middle third and two 8 s shots before the title.
- Inside each shot: GSAP on the video wrapper scale 1.04 → 1.10, x 0 → −2 %, duration = shot length, ease "none"; add CSS blur 2px → 0 over the first 0.6 s to fake a focus pull.
- Particles: 20–30 small radial-gradient dots (#ffb15a, 2–4 px, blur 1px) drifting up 40–80 px over 6 s with random opacity 0.2–0.8.
- Credits: Cinzel 400, uppercase, letter-spacing 0.28em, 30 px on 1080p (2.8 %), colour #d8c29a; labels 18 px; stagger multi-name groups with left indents of 0 / 40 / 16 px. Fade in 0.5 s, hold 2.5–3 s, fade out 0.5 s.
- Title: hard cut to a dark misty plate; wordmark in metallic gold (linear-gradient #f0d28a → #8a6a2e, background-clip:text) at ~10 % of frame height, opacity 0 → 1 over 1.0 s, slow scale 1.00 → 1.03 over 5 s.
- Audio: one orchestral theme, already at full level from the first second, compressed flat (LRA ~3), no SFX.
