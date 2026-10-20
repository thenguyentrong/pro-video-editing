# Automated CAR-T Cell Therapy for Personalized Cancer Treatment  (Festo, 2026-04-17, 3:25, 16:9, YouTube @festo)
URL: https://www.youtube.com/watch?v=QdkVjBbslio
Purpose: research-partner case film (automated cell-therapy production with a research institute), documentary-cinematic
One-sentence point: Together with a research institute, Festo automates the hand-made production of CAR-T cells so personalised cancer therapy can reach more patients.

## Structure
- 0-7 two lines of white text on near-black (≈3 % H, centred), a short second card.
- 7-26 cinematic open: microscope view of cells, ink-in-water macro, automated cell lab in a glass box, black particle shots, glass atrium of the institute.
- 26-44 professor interview (name super), lab b-roll, two researchers walking.
- 44-63 explainer: white/light-blue 3D animation - body icon, blood drop, "T Cells" in a dish, "CAR-T Cells" with receptors, back into the body (one 18 s animation).
- 63-82 problem: manual lab work in clean rooms, aerial of the campus, ink macro.
- 82-147 research associate interview (super), pipetting, drawings and CAD, chip and microscope macros, orange-lit bioreactor macros, white 3D model of the lab modules.
- 147-197 Festo manager interview (super) in front of the automated system, valve/chip macros, white 3D animation of the module, map pins and many patients (scale idea).
- 197-205.5 end: the system, blue line + "Automation for a world in motion.", FESTO logo on white (4.5 s silence under it).

## Cut rhythm
- 112 shots in 205.5 s, ASL 1.83 s, median 1.12 s, 43 % < 1 s, 12 % > 3 s, 32.7 shots/min. ASL per quarter 2.0 / 1.5 / 1.7 / 2.2 s.
- Many 0.12-0.4 s flash shots in the b-roll bursts (10.5-11.6 s, 90-93 s, 98.8 s); peaks of 8-13 cuts per 10 s (90-120 s). Longest 18.0 s (44 s, explainer animation), 12.5 s and 10.9 s (end). Interview pieces 2-6 s.
- Rhythm = calm interview pieces + percussive b-roll bursts on music accents.

## Typography
- Festo face (closest free: Fira Sans).
- Name super: name semibold ≈7 % H white, bottom-left (x ≈5 %, y ≈72-80 %), a thin blue line under the name that runs in from the left edge, role + institution regular ≈3.3 % in two lines below; hold ≈5 s.
- Opening text: regular ≈3 % H white on near-black, centred, two lines.
- Explainer labels: dark grey semibold ≈8-9 % H, set in 3D on the scene floor ("T Cells", "CAR-T Cells").
- End: blue line + tagline ≈2 % H, FESTO logo blue on white.

## Colour/grade
- Cinematic teal-and-orange: cool teal labs and atrium, warm orange macros of the bioreactor; slight crush and soft contrast. The explainer is the opposite: flat light blue and white.

## Camera/shots
- Real lab footage with cinema lenses: shallow depth of field, slow push-ins, macro through glass, aerial of the campus, interviews off-centre at 35-50 mm with the lab behind. 3D animation only for biology and for the system concept, always on its own clean white/blue look.

## Transitions
- Hard cuts, flash cuts of 3-10 frames in bursts, a few dissolves into macros (7.2, 28-30, 47-58 s).

## Sound
- Interview voices ≈188 s (≈440 words, ≈2.3 words/s) over a cinematic electronic score with hits on the bursts. Integrated -14.3 LUFS, LRA 6.0 LU, true peak -0.5 dBTP. One 0.3 s drop-out at 127.15 s before a +34.5 dB hit; loudest at 91.35 s (the burst). 4.5 s silence under the end card.

## What makes it premium / credible
- Named scientists and a named institute explain the problem; Festo appears as the partner, not the hero.
- A simple 3D explainer makes the biology clear in 18 s.
- Cinema grade and macros make lab hardware look precious.
- Weak: the automated system is shown mostly in macros and CGI; no long take of it working, no throughput number.

## Recipe (real footage + HTML/GSAP)
- Name super: `<div class="ns"><b>Dr. Name Surname</b><i></i><span>Role<br>Institute</span></div>`, `b{font:600 7vh 'Fira Sans'}`, `i{display:block;height:2px;width:20vw;background:#0091DC;margin:1vh 0 1vh -5vw}`, `span{font:400 3.3vh 'Fira Sans'}`; line `scaleX` from 0, 0.4 s, text fade 0.3 s.
- Burst: 4-6 macro shots of 3-10 frames on one music accent, then back to a 3-6 s interview piece.
- Explainer: separate white/light-blue 3D or flat animation, labels in dark grey 8vh, one idea per 4-6 s.
- Grade: `filter: saturate(.85) contrast(1.05)` + teal shadows / orange highlights LUT on lab footage.
