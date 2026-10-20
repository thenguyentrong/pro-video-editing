# Mattress Assembling | FANUC & Hollander Techniek and Auping | GET IT DONE. TOGETHER!  (FANUC Europe, 2026-05-12, 3:16, 16:9, YouTube @FANUCEurope)
URL: https://www.youtube.com/watch?v=2tj13F8j7lM
Purpose: application demo (integrator series "GET IT DONE. TOGETHER!"; a real production cell, no talk)
One-sentence point: Several FANUC robots in an integrator's cell assemble mattress frames and parts automatically - just watch the cell run.

## Structure
- 0-5.2 sting: flat yellow card, white kinetic words "GET IT DONE" → "WITH" → "FANUC" (red logo), one word group per ≈1 s, music hit on each.
- 5.2-31.2 one 26.0 s take: a heavy arm picks a large frame and places it on the line.
- 31.2-59.9 six shots of 2.4-5 s from different angles (cell overview, gripper, conveyor, second station).
- 59.9-133.7 4 shots of 12.8-18.2 s: robots handling foam blocks and frames, close-ups of the gripper at work.
- 133.7-192.5 three long takes: 27.4 s (frame turned and placed, the longest), 6.9 s, 24.5 s (wide of the whole cell with several arms).
- 192.5-196.5 the yellow sting again ("GET IT DONE WITH FANUC").

## Cut rhythm
- 19 shots in 196.5 s, ASL 10.34 s, median 5.17 s, 0 % < 1 s, 84 % > 3 s, 5.8 shots/min. ASL per quarter 7.0 / 6.1 / 16.4 / 12.3 s: gets slower towards the end.
- Longest 27.4 s, 26.0 s, 24.5 s. Shortest 2.37 s.
- 0-3 cuts per 10 s; 8 of 20 windows have no cut. Cuts ignore the music (6 % on onsets vs 18 % chance).

## Typography
- Only the sting: bold DIN-style caps (closest free: Barlow Bold), white on FANUC yellow, ≈5 % H, centred; "DONE" white bold vs "GET IT" lighter; FANUC wordmark red. No captions, no labels, no names, no speed label inside the film.

## Colour/grade
- Neutral factory light, natural colours: yellow robots, blue conveyors, steel frames. No grade effects.

## Camera/shots
- Locked-off tripod and very slow slider moves at 1-3 m; mostly high three-quarter views that show gripper + part + target; a few low close-ups. Real time.

## Transitions
- Hard cuts only; cut in and out of the yellow sting.

## Sound
- Music only (no VO), upbeat corporate electronic, mastered loud: -10.9 LUFS integrated, LRA 5.3 LU, true peak +1.0 dBTP (clips). Silences 0.35-0.8 s inside the stings (1.2, 3.2, 191.8, 193.8, 195.7 s) - each word slam lands after a short silence.

## What makes it credible
- Long real-time takes of whole handling cycles (24-27 s), no speed-up visible, nothing hidden.
- The integrator and end customer are named in the title.
- Weak: no text at all - viewers do not learn cycle time, payload, robot model or what each station does; no people, no site.

## Recipe (real footage + HTML/GSAP)
- Sting: yellow `#FFD800` full frame; words `font:700 5vh Barlow; text-transform:uppercase`, shown one group at a time with `tl.set` every 1 s, a 0.35-0.45 s silence before each, then a hit; red logo last.
- Body: 3-4 takes of 20-30 s, locked off, each one full cycle; fill the middle with 2-5 s detail shots only where the long takes repeat.
- Add what the series lacks: one lower-left line per take ("Robot · task · cycle time"), `font:600 3vh Barlow` white, and "Real time" in a corner.
