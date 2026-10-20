# All 20 of the 2026/27 Premier League Goal Animations  (Premier League, uploaded 2026-08-21, 13.1 s, 9:16, YouTube Shorts / Premier League channel)
URL: https://www.youtube.com/shorts/-G9DoPu8G0Q
Purpose: graphics-package reveal: the score bug's club-specific "GOAL" animation for every club, shown as two stacks of ten
One-sentence point: every club gets its own goal moment inside the same score bug.

Structure (one continuous animated graphic, no cuts):
- 0.0–1.0 grey background, empty.
- 1.0–2.0 Stack A: ten resting score bugs (clubs A–F alphabetically), centred.
- 2.0–2.3 neon gradient wipe (lime → cyan) runs across every bug.
- 2.3–3.3 each bug turns its club colour; the league lion in the middle becomes the club crest; a club-specific icon (e.g. a cannon, a bird, a cherry) wipes across the wing.
- 3.3–5.0 "GOAL" (or a club chant word) in white heavy caps on the wing, ≈1.7 s hold.
- 5.0–5.3 neon wipe back; the score now reads 1–0.
- 5.3–6.6 staggered exit to the right with a slight motion trail, bottom bug last; the stack shrinks.
- 7.0–12.3 Stack B (the other ten clubs), same sequence 1.1 s faster: rest 7.0–8.6, GOAL state 9.0–11.2, score update ≈11.4, exit 12.0–12.6.
- 12.6–13.1 empty grey.

Cut rhythm: 1 shot (no cuts). The goal animation itself lasts ≈3.3 s from first wipe to updated score (≈0.3 s wipe in, ≈1 s club reveal, ≈1.7 s GOAL hold, ≈0.3 s wipe out).

Typography (score bug anatomy, measured on the 480×854 upload, bug ≈ 54 % of frame width):
- Left tab: 3-letter club code, white heavy caps on the club colour, cap ≈1.5 % of frame height.
- Centre: score digits white, heavy, ≈2.5 % H, either side of the lion/crest disc; clock "00:00" in a dark purple tab below, ≈1.3 % H.
- Right wing: purple-to-violet gradient (#3d0a6b → #8a2be2); in the goal state it becomes the club colour with "GOAL" in white heavy caps ≈2.3 % H, right-aligned. Some clubs replace "GOAL" with their own word (e.g. a chant).
- Closest free: Outfit 800 / Lexend 800 for codes and GOAL; Barlow Semi Condensed 700 for the clock.

Colour/grade: neutral light-grey stage (#e8e8e8); bug in league purple; neon lime/cyan for the transition wipe; each club's own colour in the goal state.

Transitions: gradient wipe in, icon wipe, text slide, gradient wipe out, staggered exit. Everything moves left-to-right.

Sound: a loud, flat sting loop: integrated −9.0 LUFS, LRA 0.5 LU, true peak +0.3 dBTP; first hit at 0.7 s; momentary −7 to −9 for the whole clip (not verified by listening).

What makes it premium:
- A template with a personal slot: one fixed bug, 20 different goal moments (crest, icon, word, colour).
- The goal moment changes only the wing; the score and clock positions never move, so viewers can still read the game.
- The same neon wipe opens and closes every state: one transition, used everywhere.

Recipe (HTML/GSAP in Hyperframes):
- Bug 580×64 px at 1920×1080 (or 54 % of width on vertical): `.code` 96 px tab in club colour, `.score` 150 px with digits 44 px + 56 px crest disc, `.wing` 260 px `linear-gradient(90deg,#3d0a6b,#8a2be2)`, `.clock` 120×28 px #2a0730 below.
- Goal timeline (3.3 s): neon wipe = overlay `linear-gradient(90deg,#d6f23a,#22e3d8)` with `clip-path: inset(0 100% 0 0)→inset(0 0 0 0)→inset(0 0 0 100%)` 0.3 s `power2.inOut`; under it swap wing to club colour and lion → crest; club icon SVG `x -120%→120%` 0.6 s; "GOAL" `x 30px→0, opacity 0→1` 0.25 s `power3.out`; hold 1.7 s; reverse wipe; digit `0→1` swap under the wipe.
- Exit: each bug `x 0→110%` 0.35 s `power2.in`, stagger 0.05 s bottom-first.
