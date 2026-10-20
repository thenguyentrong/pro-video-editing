# Introducing CMF Phone 2 Pro - Wonderful by design  (CMF by Nothing, 2025-05-02, 0:37, 16:9, YouTube; source only 360p)
URL: https://www.youtube.com/watch?v=fvpb6P0bkB8
Purpose: launch ad (sub-brand, younger and louder than Nothing)
One-sentence point: A pop music-video ad in a saturated orange set: the phone is fresh, focused, fast and funky, sung and written on screen as "CALL ME ...".

Structure:
- 0.0-7.8 hook: orange wall; a circular hole opens (iris-in, 0.25 s) and an eye looks through it; inside the circle the picture cuts to her face (2.6 s), then to a wide of her in a dark corridor behind the hole (4.1 s); she walks out through the hole (7.3 s).
- 7.8-12.2 product: the green phone floats over a white light line; dot-matrix title "CMF PHONE 2 PRO" (frames/t008.5s.jpg); she holds the phone up and it swaps colour green -> black -> white -> orange in three 0.28 s cuts (11.36-12.2) under "CALL ME FRESH".
- 12.2-21.1 camera chapter: camera bump macro "CALL ME FOCUSED"; she poses in the orange tunnel; phone screen camera UI in the foreground; small mono spec labels top-left ("ADVANCED 3-CAMERA SYSTEM / 2X ZOOM", "50 MP MAIN CAMERA", "0.6X ULTRA-WIDE"); whip pans between set-ups.
- 21.1-25.7 performance chapter in a dark room with a spotlight: tiny figure on an orange disc, "CALL ME FAST", gaming on the phone ("SMOOTH 120 FPS").
- 25.7-29.4 chip: zoom through the orange board to a MediaTek Dimensity 7300 chip render ("PROCESSOR / UP TO 2.5 GHZ / UP TO 16 GB RAM BOOST").
- 29.4-33.5 accessories: "CALL ME FUNKY", lanyard/accessory, she smiles to camera, holds the phone.
- 33.5-37.0 end: four colours fanned out on orange + "PHONE 2 PRO", then "cmf by NOTHING" lock-up (frames/t035.5s.jpg).

Cut rhythm (with 8 hand-verified soft transitions added: 2 mask cuts, 5 whip pans, 1 zoom-through): 23 shots, ASL 1.61 s, median 1.36 s, quarters 1.85 / 1.03 / 1.16 / 2.31. 30 % under 1 s, 13 % over 3 s. Shortest 0.28 s (the colour-swap triple, 7 frames each). Densest 10-20 s (9 cuts). Hard cuts only (cuts2): 15 shots, ASL 2.47. Cuts on onset 29 % vs 31 % chance (the song drives the TEXT timing, not the cuts).

Typography:
- Display: heavy dot-matrix caps made of big round dots (CMF's own face; free match: Doto 900 or "DotGothic16" in caps), white, bottom-centre, cap height ~9-11 % of frame height, spanning up to 13-87 % of frame width. 1-3 words. It builds word by word on the sung words: "CALL" -> "CALL ME" -> "CALL ME FOCUSED", ~0.25-0.5 s per word, then holds 1-2 s. This is lyric typography.
- Labels: monospace caps (free match: IBM Plex Mono / Space Mono), wide tracking (~0.15 em), top-left at ~5 % margins, ~2.5 % height, two lines: grey category + white spec. They type on.
- Logo bug "cmf by NOTHING" top-right on almost every frame (~4 % height).

Colour/grade: one loud brand colour. Orange-red set, walls and floor (median saturation 79 %, p90 93 %, R-B +150), a white neon light line running across the set, mint-green / black / white / orange phones as the only other colours, plus a dark grey spotlit room for the "fast" chapter. Median luma 91. Clean, bright, no grain.

Camera/shots: studio set with a circular portal and a curved tunnel, talent performing to camera (lip-sync/smile), product floating in CG over the set, product held to lens, screen UI in the foreground with the talent blurred behind, chip/board 3D render. Moves: whip pans, push-ins, orbit around the floating phone.

Transitions: iris-in circle at the start, cuts INSIDE a circular mask (the circle stays, content changes) at 2.6 and 4.1, colour-swap jump cuts (3 x 0.28 s), whip pans (14.3, 16.6, 18.4, 20.3, 21.1), zoom-through into the board (25.7).

Sound: a pop song with vocals (whisper heard "Call me fresh... focus..."), the on-screen words follow the lyric. Level very steady at -9 to -12 LUFS-M (loudest 29.25 s), fade at 34-37 s. Integrated -12.2 LUFS. No separate voice-over.

What makes it premium (in a "fun" way):
- One brand colour owns every frame; the products are the only other colours.
- The song lyric IS the feature list (fresh/focused/fast/funky).
- Big dot-matrix type, used like a music video caption, still clearly from the Nothing family.
- Graphic transitions (portal mask, colour swaps) instead of generic dissolves.

Recipe (real footage + HTML/GSAP):
1. Set: one saturated colour (sampled #e6350d) on walls and floor, one white light line. Talent wears the same colour. Shoot product-in-hand, product-to-lens, screen-in-foreground, and a few CG/packshot floaters.
2. Caption: `position:absolute; bottom:5vh; width:100%; text-align:center; font: 900 10.5vh 'Doto'; text-transform:uppercase; letter-spacing:0.02em; color:#fff`. Words as spans; `gsap.set(word,{autoAlpha:1})` exactly on each sung word (no tween), clear the line on the next phrase.
3. Spec label: top-left at 5vw/6vh, mono 2.4vh caps, letter-spacing 0.15em; type-on with a stepped `clip-path: inset(0 100% 0 0) -> inset(0 0 0 0)`, `ease:"steps(20)"`, 0.5 s.
4. Portal open: circle mask `clip-path: circle(0% at 50% 45%) -> circle(14% at 50% 45%)` 0.25 s `power3.out`; swap the video inside while the mask holds.
5. Colour-swap beat: 3 cuts of 7 frames (0.28 s at 25 fps) on the same framing, one per colourway.
6. Logo bug top-right all film; end lock-up = product fan left + name right, 1.5 s, then logo 1.5 s.
