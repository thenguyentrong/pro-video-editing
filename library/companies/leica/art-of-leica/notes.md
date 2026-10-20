# The Art of Leica  (Leica Camera, 2026-09-24, 2:09, 16:9, YouTube; ≈ 160 k views)
URL: https://www.youtube.com/watch?v=Sh9jSPuuUQw
Purpose: brand anthem (narrated)
One-sentence point: Photography is the art of seeing, and Leica is the tool that brings each photographer's vision to its fullest.

Structure:
- 0.0-5 black, then one word "Photography" fades in (frames/t001.5s.jpg) over a dark gallery with a framed print; VO starts at 2 s.
- 5-19 photographers at work: street, Tokyo crossing at night, a dancer on stage, people in rabbit masks; first "result" still at ≈ 18 s, a black-and-white print with a white border on black (t018.0s).
- 19-37 street and patience: chess players, a man in sunglasses, a couple in a doorway, a swan in a black frame (t033.0s), a city canyon.
- 37-60 everyday and joy: a kitchen party, dancers in tutus, a studio portrait session on white, a fashion model; stills on black alternate with the footage (t057.0s).
- 60-90 travel and nature: Iceland road, a boat, an old man's face, lightning storm (photographer in silhouette), a husky on white, laughing elders.
- 90-99 craft: hands on a lens, technical drawings, "LEICA M6" box engraving, metal being finished.
- 99-118 community: street crowds, a pigeon still, camera dials, a darkroom in red light.
- 118-125.4 a woman and a man lift the camera to the eye; the camera alone on a table (t124.5s).
- 125.4-129 red dot logo grows from small to full size on black (t127.5s), 2.7 s of silence.

Cut rhythm: 81 shots (adaptive detector + 1 added, checked on the sheet), ASL 1.59 s, median 1.40 s, 16 % under 1 s, 4 % over 3 s, 37.7 shots/min. Quarters 1.70 / 1.34 / 1.47 / 1.70 s: flat, slightly faster in the middle. Longest 5.0 s (opening word), 3.7 s (logo). Cuts on onsets 19 % vs 24 % chance: cut to the VO phrases, not to the beat.

Typography: only one word on screen in the body: "Photography", geometric sans light/regular (closest free: Outfit Light or Jost Light), sentence case, white, cap ≈ 6.3 % H, centred at y ≈ 50 %, fade in ≈ 0.5 s, held ≈ 3 s. No other supers. End: Leica red dot logo, scaling up from ≈ 2 % to ≈ 9 % H.

Colour/grade: each photographer keeps their own look (cool teal night city, warm amber stage, bright white studio, B&W stills), unified by a soft filmic contrast and slight warmth (R-B +5); median luma 53, contrast p95-p5 161, 29 % of frames dark. Photos are presented as prints with a thin white border, centred on black at ≈ 40-70 % of the frame height.

Camera/shots: documentary-style live action, mostly handheld or slow push, shallow depth of field; "photographer → photo" pairs (≈ 12 stills on black); product inserts are rare and short (lens ring, dials, box engraving, camera on a table at the end).

Transitions: hard cuts; the still photos act as a "shutter": footage → the resulting print on black for 0.6-1.5 s.

Sound: male VO from 2 to 127 s, wall-to-wall, in an "It's the art of ..." list rhythm; warm piano/strings bed. −17.7 LUFS, LRA 4.7 LU, true peak −0.2 dBTP. 1.25 s of silence at the start, 2.7 s at the end on the logo.

What makes it premium:
- The brand speaks through other people's photographs: proof by results, not specs.
- One word on screen in two minutes; the logo is the only other graphic.
- The anaphora VO ("It's the art of ...") sets a steady 1.4 s cut rhythm.
- Product shown only as craft details and at the very end.

Recipe (real footage + HTML/GSAP):
1. Collect 10-15 "maker → result" pairs (person at work + the finished photo/object).
2. VO: one repeated sentence opener, one phrase per 1.5-3 s; cut at phrase ends.
3. Still-on-black device: `<figure style="background:#000">` with `<img style="max-height:62vh; border:6px solid #f4f2ee">`, cut in hard, hold 0.8-1.5 s.
4. Single word open: `font: 300 8.6vh 'Outfit'` (cap ≈ 6.3 % H), centred, `opacity 0→1` 0.6 s over black, then reveal the first shot under it.
5. Logo end: `gsap.fromTo(logo,{scale:.25},{scale:1,duration:1.2,ease:'power3.out'})` on black, music out 0.3 s before, hold 2.5 s silent.
6. Master −16 to −18 LUFS for a VO-led anthem.
