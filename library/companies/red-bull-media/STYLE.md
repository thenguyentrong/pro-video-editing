# Red Bull Media House – athlete short documentaries (2018–2026)

Examples (first 300 s of each measured): `armed-robber-triathlete` (The Way of the Wildcard S1, 2018, 13:46), `mira-rai-trail-runner` (The Way of the Wildcard S2, 2020, 15:59), `rise-of-eileen-gu` (Red Bull Snow, 2026, 13:38). Analysed Oct 2026. This folder is for documentary shorts; Red Bull's vertical action clips are in `companies/redbull`.

## The style in one line
An athlete portrait cut like a feature: a hard cold open, a tiny "presents" credit, a heavy series logo on a drone shot, interviews in low-key light, archive used as evidence, and one strong stylistic device (reconstruction, window-boxed archive, viewfinder frames) per film.

## Measured overview (0–300 s)
| film | shots | ASL | median | <1 s | >3 s | per quarter | LUFS | picture |
|---|---|---|---|---|---|---|---|---|
| Armed Robber (Wildcard S1) | 132 | 2.27 s | 1.14 s | 42 % | 29 % | 2.78 / 1.27 / 5.00 / 2.21 | -22.7 | 16:9, 360p source |
| Mira Rai (Wildcard S2) | 118 | 2.54 s | 2.08 s | 19.5 % | 25 % | 2.34 / 2.21 / 2.88 / 2.59 | -22.2 | 2.35:1 |
| Rise of Eileen Gu | 113 | 2.65 s | 1.68 s | 21 % | 32 % | 3.95 / 1.74 / 3.26 / 2.42 | -15.0 | 16:9 |

## Core idea
Red Bull's long-form docs are about who the athlete is, not the stunt. The series brand (The Way of the Wildcard) is consistent: credit on movement, slab-caps logo on a drone shot, episode card in light spaced caps. Inside that frame each film picks one device that carries the story's hardest part.

## Rules (with numbers)
1. **Cold open with a jolt or a patient take.** 11 cuts in 10 s with 0.12 s flashes and an eye macro (Armed Robber), one 12.9 s locked take (Mira Rai), or the athlete talking to a handheld camera in fog with a 1 s drop before her line (Eileen Gu).
2. **Credit.** "RED BULL MEDIA HOUSE / PRESENTS", cap ≈1.7 % H, tracking ≈0.3 em, centred over movement or a black pupil.
3. **Series logo** ≈9 % H heavy rounded slab caps on a 4–8 s drone shot at 19–50 s; episode card name ≈2.5 % H + light subtitle ≈2 % H, tracking ≈0.4 em.
4. **The past as evidence.** Tabloid headlines, mugshots, CCTV (Armed Robber); 4:3 archive window on black, 56 % of frame width (Mira Rai); career photo wall inside a viewfinder frame (Eileen Gu).
5. **One contrast montage.** 20–25 cuts in 10 s (0.2–0.5 s) for the "other life" (Armed Robber 120–130 s), or 16 cuts in 10 s to start a new chapter (Eileen Gu 290–300 s).
6. **Breaks.** Black holds of 3.3–6.7 s, near-silences of 8–11 s at -40…-48 dBFS, silences of 3.3–3.9 s in reconstructions.
7. **Interviews** low-key, 3/4 profile, 6–13 s holds; subtitles for non-English speech; lower thirds without a box.
8. **Loudness.** Wildcard episodes -22.2 to -22.7 LUFS (quiet, dialogue-led, LRA 8–12); the 2026 film is louder (-15.0, music-led).

## Recipe (real footage + HTML/GSAP, 1920x1080)
- 0–13 s cold open → 3 s credit → 10–12 s promise montage → title on a drone shot → episode card → first interview by ≈60 s.
- Body ASL 2.3–2.7 s; interviews 6–13 s; one contrast montage at 20–25 cuts / 10 s; one stylised device (black-and-white reconstruction with dissolve chains, archive window, viewfinder frame).
- Type: credit `500 1.7vh Montserrat; letter-spacing:.3em`; logo `400 9vh "Bowlby One"`; episode `500 2.5vh` + `300 2vh; letter-spacing:.4em`; viewfinder tag `700 1.8vh Inter`.
