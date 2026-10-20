# Avengers: Doomsday — Official Trailer, vertical cut  (Marvel Studios, 20 Jul 2026, 2:26 (145.8 s, 143.3 s before the trailing black), 9:16, YouTube Shorts / social)
URL: https://www.youtube.com/watch?v=iFl4YeX6jmc (posted the same day as the 16:9 trailer `irVNGjRFZGk`)
Purpose: social reel (vertical version of the main trailer)
One-sentence point: the same trailer as `../avengers-doomsday-official-trailer/`, re-framed for a phone.

## Structure (beats with timestamps)
Identical to the 16:9 trailer (see its notes): one-shot cold open with the Xavier's School plaque (0–6.3 s), black, Professor X at the burning window, black, Doom's shoulder (7.3 s), Marvel Studios logo (24.4–29.9 s), roll-call montage (30–99 s), 2.7 s black, near-silent Thor / Steve Rogers scene (102–118.6 s), title (118.6–~129.5 s), "SEE IT IN INFINITY VISION" (~129.5–131.5 s), typed date (~131.5–137.5 s; "12.18.26 IS" is on screen at 134.5 s), countdown (~137.5–143 s). Nothing was added or removed for vertical; there are no captions and no extra hook in the first second.

## Cut rhythm
- 66 shots, **ASL 2.17 s**, median 1.38 s, quarters 3.26 · 1.43 · 1.38 · 5.12 s (16:9: 65 shots, ASL 2.20 s, 3.25 · 1.38 · 1.49 · 5.11 s).
- After eye checks the cut list matches the 16:9 version within ±0.15 s. One extra 0.25 s pink flash shot at 88.5 s shows up here (it may exist in the 16:9 too, merged there by the detector — unsure).
- Cuts per 10 s: 2 · 4 · 2 · 3 · 7 · 9 · 6 · 5 · 9 · 10 · 2 · 6 · 0 · 0 · 0.
- Detector note: the raw detector missed 10 real boundaries on the tight vertical crop (dark fades, fast purple fight) and added 2 false ones (a lightning flash, camera shake), so vertical footage needs the same eye check.

## Typography
- **Studio logo**: the red Marvel Studios logo is not enlarged; it spans the full width at mid-height inside a red field (24–29 s).
- **Title** (125.5 s frame): the Avengers Doomsday lockup scaled to ~79% of the frame width, centred, at ~29–47% of the height (a bit above centre). The vertical frame shows the *whole* A-shaped green window behind it, so the background itself becomes the Avengers "A" — a composition that does not exist in the 2.39:1 version.
- **Date**: "12.18.26 IS DOOMSDAY" typed token by token, left-aligned at x ≈ 12%, y ≈ 42%; cap height ~2.6% of the height (= 4.6% of the width), condensed chrome caps, wide tracking. With 9:16 the line no longer fits as a centred line, so it starts left.
- **Countdown** at ~43% height; "THIS FILM IS NOT YET RATED" + "© 2026 MARVEL" at ~79–82% height; the bottom ~15% stays empty (platform UI zone).

## Colour / grade
Same grade as 16:9 (dark, one hot source per frame, per-world colour). No bars: the picture fills 9:16.

## Camera / shots (how it was re-framed)
- Subject-centred crop. Close-ups fill the frame and look stronger than in 16:9 (Shuri 43 s, Thor 106–110 s).
- Wide ensemble shots lose their sides: the 38 s hall keeps only the centre group (Fantastic Four + a few heroes) of ~15 characters.
- More picture above and below than the 2.39:1 version (33.5 s: the whole round door frame and the ceiling lights are visible), so the vertical was re-extracted from a taller master, not just cut out of the scope frame (inferred from the frames).
- The plaque in the opening is readable here ("XAVIER'S SCHOOL FOR GIFTED YOUNGSTERS"); the NYC aerial puts the Avengers "A" tower near the centre.

## Transitions
Same as 16:9: hard cuts, three long black holds (1.9, 1.6, 2.7 s), fades around them.

## Sound
Same mix as 16:9: integrated −14.1 LUFS, loudest −8.4 LUFS M at 54.5 s, 13.5 s of near-silence 101–114.5 s (−10 → −45 LUFS), a 0.35 s gap at −50 dBFS at 117.15 s and the hit at 118.05 s (title cut 118.62 s). Countdown ticks, fade to silence.

## What makes it premium
- Marvel did not make a "social edit": it trusts the full 2.5-minute trailer on a phone and only re-frames it.
- Re-extraction from a taller master instead of a crop keeps close-ups clean and composed.
- The end card is re-composed for 9:16 (title above centre, the A-window as a background frame, billing high enough to clear the UI).

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Keep the 16:9 edit and timing; build a 1080×1920 composition that plays the same clips with `object-fit: cover` and a per-shot `object-position` (keyframe it when the subject moves: `gsap.to(video, {objectPosition:"38% 50%"})`).
2. For wide group shots, pick the 2–4 most important faces and centre them; accept losing the rest.
3. Title: scale the logo to ~80% of the width, centre it at ~38% of the height; use a background element that frames it vertically.
4. Text lines that are too long for 9:16: left-align at 12% and let them type in (`span` per token, 1 s apart).
5. Keep all text between 15% and 82% of the height (`top: 15%; bottom: 18%` safe box); nothing in the bottom 15%.
