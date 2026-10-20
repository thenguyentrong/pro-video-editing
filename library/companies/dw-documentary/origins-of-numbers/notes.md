# From 0 to 9 — the mysterious origins of numbers  (DW Documentary, published 2026-10-06 on dw.com, 51:44 full / first 300 s analysed, 16:9, dw.com + YouTube)
URL: https://www.dw.com/en/from-0-to-9-the-mysterious-origins-of-numbers/video-79556280
Note: downloaded from DW's own site at 640x360; type sizes read from upscaled frames.
Purpose: documentary explainer (history of an idea: narrator, location, experts, animated texture titles)
One-sentence point: The digits everyone uses were born in India, and the film follows their path through temples, manuscripts and scholars.

Analysed: the first 300 s (5 min) of 51:44.

Structure (first 300 s):
- 0.0-11.3 the place: one slow drone shot over a temple complex (11.3 s).
- 11.3-44 temple details: towers, carvings, 3-6 s each.
- 44.2-61.2 the object: a carved grid of old numerals in stone (17 s with a slow move).
- 61-77 the present: a chalkboard sum, city traffic, a calculator keypad, manuscript pages.
- 77.2-103.4 title: a 26 s manuscript shot; "FROM 0 TO 9" in bold white caps fades in and out over it (≈85-92 s).
- 103-133 animated title world: numerals in many scripts as moving 3D texture in red, gold, then blue-violet; the full title "The Mysterious Origins of Numbers" in white (115-121 s); fade to black at ≈125 s.
- 133-180 on location: a woman walks through the temple grounds, a local scholar points at the carved numerals.
- 180-194 dark interiors with sculptures (≈3 s shots).
- 194-247 the scholar again, ceilings, aerial, a man walking.
- 247-261 a mathematician interviewed on a green-grey set, lower third.
- 260.8-283.3 an illustrated manuscript (22.6 s slow pan).
- 283-300 popular culture: film clips and crowds cut at 0.7-1.3 s.

Cut rhythm: 55 shots in 300 s, ASL 5.46 s, median 3.88 s, 2 % under 1 s, 64 % over 3 s, 11.0 shots/min (scene detector + 6 verified cuts in the dark sculpture sequence). ASL per quarter 5.00 / 7.50 / 3.75 / 5.77 s. Cuts per 10 s: 0-4. Longest 27.3 s (title animation), 26.2 s (manuscript + title), 22.6 s (illustrated manuscript). The title section uses dissolves, which are not counted as cuts.

Typography:
- DW roundel top left ≈5.5 % H.
- DW house sans (closest free "Noto Sans"): series title "FROM 0 TO 9" bold caps ≈7 % H white, centred left; full title ≈5 % H sentence case white.
- Lower third, right-aligned, no box: name in bold caps ≈4.5 % H, role ≈3 % H.

Colour/grade: warm sandstone, gold and green for India; title animation saturated red/gold then cyan-violet; interview set desaturated green-grey.

Camera/shots: slow drone moves, macro and detail shots of carvings and manuscripts, a scholar on location pointing at the evidence, a studio-like interview, 3D type animation, film archive.

Transitions: hard cuts in the location sections; dissolves and a fade to black around the title.

Sound: integrated -15.9 LUFS, LRA 4.8 LU, true peak -2.0 dBTP, median RMS -21.4 dBFS. Narration over a continuous score; 8 short drop-outs (0.3-0.7 s), the deepest at 255.05-256.4 s (two dips to -56 and -65 dBFS) before the illustrated manuscript, then +42 to +48 dB. Cuts below chance on onsets (28 % vs 32 %): picture is cut to the narration's phrasing, not to music.

What makes it premium:
- The evidence is physical and old (stone carvings, manuscripts), shot like art objects with slow moves.
- The title comes late (≈85 s) and opens into a designed animated world of numerals, then fades to black.
- An expert on location points at the object, so the claim and the proof share one frame.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Open: one 10-12 s drone move, then 3-6 s details.
- Object hold: 15-20 s slow push `scale 1→1.08 ease:none` on the key artefact.
- Title over a manuscript: `font:800 7vh "Noto Sans";text-transform:uppercase` fade 1 s in, 5 s hold, 1 s out.
- Animated title world: layers of numerals in several scripts as repeating text in CSS 3D (`perspective:800px; rotateY(25deg)`), scroll 10-20 % over 10 s, colour from `#B3122E/#D9A441` to `#2E7BD6/#7A3FD1`; full title `font:600 5vh` held 6 s; fade to black.
- Lower third right-aligned, caps name 4.5 vh, role 3 vh, no box.
- Mix: narration ≈-16 LUFS short-term over continuous score, master -16 LUFS.
