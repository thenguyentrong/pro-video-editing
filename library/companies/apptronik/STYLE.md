# Apptronik - style

Examples (official Apptronik YouTube uploads):
| Example | Date | Length | Shots | ASL | Median | <1 s | Shots/min | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|---|
| [hello-apollo](hello-apollo/notes.md) | 2023-08 | 0:44 | 20 | 2.20 s | 1.96 s | 5.0 % | 27.3 | -10.2 | launch teaser: typed greeting, dark warehouse reveal, gesture montage |
| [tote-picking](tote-picking/notes.md) | 2023-08 | 0:48 | 1 | 48.24 s | 48.24 s | 0 % | 1.2 | silent | raw one-take lab demo, 3 task cycles, no text, no sound |
| [robot-park](robot-park/notes.md) | 2026-06 | 1:14 | 34 | 2.19 s | 1.88 s | 2.9 % | 27.5 | -17.0 | brand + Apollo 2 film: kids → product macro → coworkers → warehouse hero |

## Sub-styles
1. **Launch teaser (2023):** greeting typed on black ("hello" + wide caps name), 0.5 s dissolve into a dark warehouse, robot walks into light, 15-20 shots of 1-3 s (take, carry, place, wave, thumbs-up), lights out, glitch logo. Cuts per 10 s 1 / 5 / 7 / 5 / 1. Loud (-10.2 LUFS, LRA 12.5).
2. **Raw proof clips (same day as the teaser):** 20-50 s locked-off single takes per task (tote picking, case picking, trailer unloading, palletising - titles on the channel), no music, no text.
3. **Brand film (2026):** human-first story (child dreaming of space, kids, office staff, an engineer), product macro with the robot's chest display, carmaker logo banner as proof, warm cinema grade, end line "Robots for humans." on black.

## House rules
- **Friendly humanoid:** face-like head plate, gestures to camera (wave, thumbs-up), hand-overs with people; the robot is always a coworker in frame with humans.
- **Dark, warm cinema look:** low-key light, shallow focus, amber practicals, light reveals in camera (lights on / lights off).
- **Diegetic UI:** the robot's own chest display shows status, battery, task name and progress % - no overlay graphics.
- **Minimal type:** greeting or one brand line; thin lowercase + wide-tracked caps with an open Λ "A" (closest free: Raleway ExtraLight + Michroma); end line in a light grotesk (Inter Light ≈5 % H).
- **Montage at 2 s:** ASL 2.2 s, median 1.9-2.0 s, <1 s shots only 3-5 %; arch-shaped density.

## How they show a real machine working / keep it credible
- The proof sits in separate raw clips, not in the films: one 48 s uncut tote-picking take with three cycles and a human resetting the tote.
- No speed labels, no autonomy or teleoperation statement in any of the three films. In the raw clip a person holds a tablet the whole time; its role is not explained.
- Social proof by logo (carmaker banner on set, 2026) rather than by named site text or a customer speaking.
- Real robot in every shot studied; no CGI product shots seen.

## Contrast with other makers in the library
- Closer to Figure's design-led teasers than to ANYbotics' or Boston Dynamics' engineering records: emotion, people and light first, proof outside the hero film. Compared with Tesla's labelled demos it never says "autonomous" or "1x" on screen.

## Recipe (real footage + HTML/GSAP)
1. Make two deliverables: a 40-75 s hero film and 1-4 raw single-take clips (30-60 s each) that prove each task.
2. Hero: open on black with a typed greeting (Raleway 200 11vh at 4 chars/s after a 0.6 s "…" bubble), name in Michroma 11vh letter-spacing .3em; 0.5 s dissolve to a dark wide; machine walks into light.
3. Montage: 1-3 s shots, one action each, 5-7 cuts per 10 s at the peak; keep a person in at least every third shot.
4. Machine state: film the device's own screen in macro, or a chest-style status card (labels 1.2vh caps grey, values Inter 600 3vh white, progress counter).
5. End: lights out in camera, then one brand line on black (Inter 300 5vh, hold 4 s) and the logo 5 s.
6. Raw clips: tripod medium-wide, full task area in frame, 3+ cycles, room sound kept, and a corner label `AUTONOMOUS · 1X` or `TELEOPERATED · 1X` - the part Apptronik leaves out.
