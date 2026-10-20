# Turning elements into GLASS?! | LEGO glass blowing challenge  (LEGO, 2026-09-07, 37.6 s, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/61HV2u3SIqw
Purpose: social collab / craft challenge (with a glass museum)
One-sentence point: Glass artists make giant glass versions of three LEGO elements (brick separator, frog, flower) and each result is shown next to the real piece.

Structure: beats with timestamps
- 0.0-2.5 hook: a three-way stacked split (three finished glass elements in the fire), title over the middle panel.
- 2.5-10.8 element 1/3: counter card on the work, fast craft shots (flame, cutting, shaping, glory hole) of 0.5-1.7 s.
- 10.8-13.6 reveal 1: split screen, top = the glass piece, bottom = real brick separator next to it; label + emoji on the seam.
- 13.6-22.4 element 2/3: slower craft shots (2.9 s and a 5.9 s blow), then reveal 2 (frog) at 22.4-24.6 s with label + emoji.
- 24.6-34.7 element 3/3: craft shots; reveal 3 (flower) from 34.7 s to the end with label, emoji and legal line. Hard end on the result.

Cut rhythm
- 20 shots, ASL 1.88 s, median 1.50 s, 30 % < 1 s, ≈32 shots/min. Quarters 1.17 / 1.88 / 1.88 / 1.88 s: fastest at the start.
- Each element: ≈8-10 s of process, ≈2-3 s reveal. Cut-to-onset 5 % (picture-driven, not on the beat).

Typography
- Title "LEGO / but make it glass": light italic sans, white, "LEGO" cap ≈6 % H, subtitle ≈2.2 % H, centred at 46-54 % H.
- Counter "ELEMENT 1/3": light italic caps, cap ≈3 % H, number bold, centred at 49-55 % H.
- Reveal labels ("BRICK SEPARATOR", "FROG ELEMENT"): light italic caps, cap ≈3 % H, on the split seam at ≈47 % H, emoji row (1-3) just below at ≈52 % H.
- Closest free: Montserrat Light Italic (or Poppins Light Italic).

Colour/grade
- Dark workshop with hot orange glass and blue-white flame; reveal shots on warm wood. Strong orange/blue contrast.

Camera/shots
- Close handheld craft shots (flame, tools, hands), one wide of the artist; reveals locked on a table.

Transitions
- Hard cuts; split screens are hard-cut in and out.

Sound
- Upbeat track, little natural sound; -9.7 LUFS (loud master), LRA 1.1 LU, peak +0.8 dBTP.

What makes it premium
- A clear counter (1/3, 2/3, 3/3) gives a 37 s video a progress bar.
- Reveal = comparison: the real element sits next to the glass one, so the scale is obvious.
- Craft close-ups with fire and molten glass give motion without camera tricks.

Recipe (real footage + HTML/GSAP, 1080x1920)
- 3 rounds × (8-10 s process at 0.5-3 s per shot + 2-3 s split reveal).
- Split reveal: two 1080x960 layers; label `italic 300 52px Montserrat; text-transform:uppercase; color:#fff; text-shadow:0 2px 8px rgba(0,0,0,.5)` at y ≈900 px, emoji 48 px at y ≈1000 px, both `tl.set` on.
- Counter card: `ELEMENT` 300 italic 52 px + `1/3` 700 italic 52 px, centred y 940-1050 px, 1.5 s.
