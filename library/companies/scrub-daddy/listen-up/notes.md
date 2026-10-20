# LISTEN UP!!!  (Scrub Daddy, 2025-08-13, 15.1 s, 9:16, YouTube Shorts / TikTok-style reply)
URL: https://www.youtube.com/shorts/qxAnHS6QWw8
Purpose: social reply to a creator's complaint (stitch format) + product push
One-sentence point: A creator says the sponges are too big and people cut them in half; the brand replies: don't cut them, buy the small version.

Structure: beats with timestamps
- 0.0-5.0 hook: the creator's own selfie clip, untouched (kitchen, mug, sponge in hand), her complaint audible from 0.3 s. No brand text over it.
- 5.0-6.0 reply starts: top-down on marble, the product box slides in.
- 6.0-9.0 caption 1 at the top: a plain instruction not to cut the sponges.
- 9.0-12.5 slow push-in to a macro of the small sponges; caption 2 in the upper-middle names the smaller product.
- 12.5-15.1 pull back to the full box; "Buy Now" larger in the centre. Hard end.

Cut rhythm
- 2 shots: 5.0 s stitched clip + 10.1 s product shot with an in-shot push-in and pull-out (the camera move replaces cuts). ASL 7.53 s.
- The single cut is on the end of her sentence (no music sync; cut-to-onset 0 %).

Typography
- TikTok Classic look: white sentence case, thin dark outline/shadow, centred. Caption 1: 3 lines, cap ≈3.0 % H, at 10.5-21 % H (partly inside the top 14 % that the strict safe zone keeps clear). Caption 2: 2 lines, cap ≈2.6 % H, at 32-37 % H. "Buy Now": 1 line, cap ≈4.5 % H, at ≈43 % H.
- Closest free: TikTok Sans 500 with a 2 px black stroke.

Colour/grade
- Phone footage as shot: warm home kitchen (stitch), then cool white marble with the orange/yellow/blue package as the only colour.

Camera/shots
- UGC selfie + overhead product on marble, handheld push-in to macro and back.

Transitions
- One hard cut (stitch boundary).

Sound
- Creator's voice, then a trending/brand sound under the reply; -18.7 LUFS with LRA 22.4 LU (the reply is much quieter than the stitched voice). Peak -0.7 dBTP.

What makes it premium
- Answers a real customer within the platform's own format; the complaint is the free hook.
- One shot with one camera move instead of a cut sequence.
- Three captions, each one job: rule, product, action.

Recipe (real footage + HTML/GSAP, 1080x1920)
- 12-16 s: 4-5 s stitched clip (untouched), then one 8-10 s product shot.
- Captions `500 56px "TikTok Sans"; color:#fff; -webkit-text-stroke:2px #000; paint-order:stroke fill`; caption 1 at y 270-400 px (keep below 270 px for the strict safe zone), caption 2 at y 620-710 px, CTA `500 84px` at y ≈820 px; hard `tl.set` switches at 6.0 / 9.0 / 12.5 s.
- Digital push-in if the shot is locked: `scale 1 → 1.8` over 3 s `power1.inOut`, back to 1 in 0.8 s.
