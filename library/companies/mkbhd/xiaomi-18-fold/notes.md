# Xiaomi 18 Fold: How Does This Happen?  (MKBHD / Marques Brownlee, 2026-10-02, 10:47 full / first 300 s analysed, 2:1 frame inside 16:9 player, YouTube)
URL: https://www.youtube.com/watch?v=3iRUwVzRDZQ
Purpose: tech review / first impressions (single product, creator-led)
One-sentence point: a phone maker has shipped a foldable with the same shape and screen ratio as an Apple foldable that is not even out yet, and Marques shows where it copies and where it does better.

Data note: first 300 s analysed (trimmed with ffmpeg after download). Frame is 854x428 at 480p = 2:1, the channel's usual aspect. One cut added by eye at 2.4 s (end of the logo sting, iris reveal). The image-wall stretch at 135.5–147.5 s fires the 0.15 scene threshold 9 times; it is one scrolling/zooming screen capture, not cuts, so it was left as one shot.

## First 30 s (hook)
- 0.0–2.4 channel logo sting: glossy red 3D logo strokes and wireframes on black, shrinks to the small red-white mark (1.5–2.4 s dip to black). Loudest 0.5 s of the sting at 0.85 s.
- 2.4–2.9 circular iris opens from the logo centre onto the first shot.
- 2.4–22.2 one continuous 19.8 s overhead hands-on take on a white desk (orange-accent keyboard in the corner): the phone is picked up, unfolded, turned, folded, the back colour shifts in the light. No talking at first.
- 2.4–14.9 music only, stop-start: hits every ≈2.2 s (4.8, 7.0, 9.2, 11.45, 13.65 s) with two digital-silence gaps of 0.9 s (3.55 s) and 0.95 s (12.4 s). Loudest 0.5 s of the 300 s is at 13.65 s, right before the voice.
- ≈14.9 s host voice-over starts over the same take; the product is named at ≈19.7 s (a "this is not X, this is Y" reveal).
- 22.2 first cut (new angle, grey desk), 27.2 cut. Cuts in 0–30 s: 3 (2.4, 22.2, 27.2).
- Host on camera first at 41.5 s; no title card, no sponsor, no chapter card in the hook.

## Structure (first 300 s)
- 0–22 sting + silent-then-voiced overhead hands-on (above).
- 22–41 hands-on angles, side by side with the comparison device.
- 41.5–47 talking head (red wall, lamp, colourful props, plant).
- 47–58 evidence: event photo, then the maker's press-release web page scrolled with the cursor visible (52.5–58.4 s).
- 58–77 talking head 18.9 s.
- 77–100 maker's keynote footage (presenter on stage, product renders).
- 100–135 talking head 13.9 + 21.3 s.
- 135–147 wall of image-search results (leaks of the rival device) scrolled as one screen capture.
- 147–175 talking head; 175–209 product on colour backdrops (pink, blue), colour variants (orange, green) side by side.
- 209–223 talking head; 223–250 hands-on outdoors/gallery; 250–257 phone on a kitchen scale (weight proof); 257–266 thickness detail.
- 266–282 talking head; 282–300 warm interior hands-on of the unfolded screen. A subscribe ask sits mid-film at ≈273 s.

## Cut rhythm
38 shots in 300 s, ASL 7.89 s, median 5.91 s. 2.6 % of shots under 1 s, 89.5 % over 3 s, 7.6 shots/min. ASL by quarter 6.82 / 8.33 / 7.5 / 6.82 s. Longest 21.3 s (talking head, 114.2 s), 19.8 s (opening overhead take, 2.4 s), 18.9 s (talking head, 58.4 s). Shortest 2.4 s apart from the sting and the tail. Cuts per 10 s: 0–3, never more. Cuts on audio onsets at chance (59 % vs 59 %): cut on sentences.

## Typography
None of the channel's own type in the first 300 s. All text on screen is borrowed: the maker's press-release page (black bold sans headline on white), the image-search grid. Proof is shown as the real page, full frame, with the cursor.

## Colour / grade
Clean, neutral, slightly cool; high clarity, no grain, no vignette. Product sets are neutral surfaces (white desk, grey felt, blue desk) with one coloured accent (orange keycaps). Host set: deep red wall + warm practical lamp + saturated toy-like props. Shallow depth of field everywhere.

## Camera / shots
Overhead and 45° desk shots with smooth, slow, motion-control-like moves; hands in frame doing the demo. Locked-off, centred talking head at eye level. Product on colour backdrops, scale/weight shot top-down. Screen captures of web pages. Borrowed keynote footage.

## Transitions
Hard cuts only after the sting. One iris (circle) reveal out of the logo at 2.4–2.9 s.

## Sound
Integrated −17.9 LUFS, LRA 4.4 LU (very steady), true peak −0.1 dBTP. Voice median −24.7 dBFS (50 ms RMS), p10 −53.5 dBFS → pauses ≈29 dB under the voice: no bed under talking. 15.2 % of 50 ms windows below −45 dBFS. Music only in the cold open and under product b-roll. Biggest designed sound move: the stop-start music open with two 0.9 s digital silences.

## What makes it premium
- The hook is a silent product demo in one long, smooth take: you study the object before anyone tells you what it is.
- Neutral surfaces + one accent colour make the product the most saturated thing in frame.
- Proof is the primary source itself (press-release page with cursor, rival leak images, a scale).
- Talking head runs long (13–21 s) because the opinion is the product.

## Recipe (real footage + HTML/GSAP)
- Logo sting 2.4 s, then `clip-path: circle(0% at 50% 50%) → circle(75% at 50% 50%)` over 0.5 s `power2.out` onto the first shot.
- First shot: one overhead take of 15–20 s, slow drift `scale 1 → 1.04` `ease:none`; music-only for 10–12 s with stop-start hits every ≈2.2 s and 1–2 cuts to digital silence of ≈0.9 s; voice enters at ≈12–15 s and names the product within 5 s.
- Talking head: locked, centred, 2:1 frame (`aspect-ratio:2/1` with 16:9 letterbox 6 % top/bottom), hold 6–21 s.
- Evidence: real web page full frame with cursor, slow scroll `y: 0 → -30%` over 5 s `ease:none`.
- Mix: voice dry, −18 to −20 LUFS integrated, no bed under talking; music −20 dB under voice only under b-roll.
