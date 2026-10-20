# Feel the system  (Sonos, 2026-09-14, 0:30, 16:9, YouTube; ≈ 0.9 M views)
URL: https://www.youtube.com/watch?v=LVm_zZ_HCTo
Purpose: brand campaign ad (whole product system)
One-sentence point: Sonos is not a pile of speakers but one system that makes you feel things in every room.

Structure:
- 0.0-2.4 product grid: speakers pop on and off a cream paper background, handwritten red model names beside them (frames/t001.0s.jpg); 7 changes in 2.4 s.
- 2.4-6.2 the grid thins out, then a hand-drawn diagram of arrows between the products; three words appear in purple highlight boxes one by one (t005.5s).
- 6.2-7.3 a laughing face, extreme close-up (real footage).
- 7.3-10 orange card "AWE IN THE LIVING ROOM": soundbar line drawing with arrows and a small inset video (t008.5s).
- 10-14.5 a kiss close-up, then a green card "LOVE IN THE BEDROOM" with two speakers and the kiss as a cut-out photo; a lilac card with stereo arrows.
- 14.5-19.3 headphones collage on red and beige: "JOY IN THE KITCHEN", "WHILE YOU MICROWAVE A BURRITO" (t016.5s).
- 19.3-23 spreadsheet paper with circled engineering words, then a purple psychedelic ripple pattern (t021.0s).
- 23-25.6 a head cut-out with the ripple inside, products around it, two purple highlight labels (t024.5s).
- 25.6-28 handwritten "Love the sound" on blue, "Feel the system" on lilac, small SONOS wordmark (t026.5s).
- 28-30 a giant red-and-brown "N" crop, then SONOS wordmark on orange (t029.5s).

Cut rhythm: 33 shots, ASL 0.91 s, median 0.33 s, 67 % under 1 s, 66 shots/min. Quarters 0.68 / 1.25 / 0.68 / 0.94 s. Most "cuts" are collage pop-ins of 4-8 frames (0.17-0.33 s) inside a held layout; the layouts themselves last 2-5 s (longest 4.75 s). Cuts on onsets 44 % vs 41 % chance.

Typography: two systems. (1) Labels: heavy condensed grotesk caps, black, cap ≈ 2.5-3.5 % H, set on the card edges like a magazine; key words in purple or orange highlight boxes (marker style). (2) The end lines are handwritten in black marker, very large (≈ 25 % H line), lowercase/uppercase mix. Wordmark SONOS in its own wide geometric caps, ≈ 4 % H. Closest free: Barlow Condensed ExtraBold / Anton for labels; a marker font is not a good substitute (shoot or scan real handwriting).

Colour/grade: bright paper world (median luma 201), warm (R-B +28), flat paper colours: cream, orange, mint green, lilac, red, sky blue, brown. Real footage close-ups are warm and grainy.

Camera/shots: stop-motion-style paper collage, cut-out photos of products, hand-drawn arrows and diagrams, extreme close-ups of faces (laugh, kiss, smile). No product beauty shots, no rooms.

Transitions: hard cuts and pop-ins; colour-card changes; no dissolves.

Sound: female VO from 0.5 to 27.5 s, dry and playful, over an upbeat track; −15.1 LUFS, LRA 1.9 LU (very compressed), true peak −2.2 dBTP. No drop-outs; rises at 6.3 (laugh) and 18.7 s.

What makes it premium (and why it is NOT Apple precision):
- It is the opposite of the product-precision look: a zine collage that jokes about "calibrated acoustics" and sells feelings.
- Discipline still shows: one paper texture, one label typeface, one highlight colour family, one VO.
- Handwritten end lines feel human and owned.
Use it as the counter-example: a premium brand can drop precision when the message is emotion and the whole system, not one object.

Recipe (HTML/GSAP):
1. Cream paper background `#f3ead8` with a subtle paper-grain overlay (`mix-blend-mode:multiply`, 20 %).
2. Products as cut-out PNGs; pop each in with `scale:.92→1, opacity 0→1, duration:.08` on music onsets, 4-8 frames apart.
3. Labels `font: 800 3.8vh 'Barlow Condensed'; text-transform:uppercase`; highlight words in `background:#c9a3f5; padding:0 .25em`.
4. Arrows as SVG paths drawn on with `strokeDashoffset` over 0.4 s.
5. Real face close-ups as 1-1.3 s inserts between cards.
6. End: scanned handwriting full-screen on a flat colour, 1.2 s per line, then wordmark on orange. VO-led master −15 LUFS.
