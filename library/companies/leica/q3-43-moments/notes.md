# LEICA Q3 43 - Moments, just as your eye sees them.  (Leica Camera, 2024-09-26, 0:55, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=GvXb98qeDTU
Purpose: product film (CG, music only)
One-sentence point: The camera is built in front of you, lens element by lens element, in a calm sunlit room.

Structure:
- 0.0-5.1 a single glass lens element floats and turns above a light oak table, soft leaf shadows on a beige wall (frames/t001.0s.jpg).
- 5.1-8.5 more elements join: an exploded lens stack, then the stack breaks into floating rings and glass (t006.0s).
- 8.5-16.2 assembly: the sensor body drops onto the table, rings and lens elements fly in and lock into place, the camera is complete (t012.0s).
- 16.2-22 details: the side of the body in soft focus, the top plate, a macro of the red logo dot and the lens markings (t020.5s).
- 22.0-43.4 one long orbit (21.4 s) with hidden changes: 3/4 hero on the table, lens hood swap (silver ↔ black), a special-edition top plate, the camera on a charging stand (t031.0s), the rear screen showing a live picture of the camera itself (t038.0s), back to the hero angle.
- 43.4-48 black: "LEICA Q3 43" small caps, centred, fades in and out (t045.5s).
- 48-54.7 red dot logo on black (t050.0s), last 1.7 s silent.

Cut rhythm: 6 shots, ASL 9.1 s, median 6.7 s, 0 % under 1 s, 100 % over 3 s, 6.6 shots/min. The real rhythm is inside the CG: a new event every ≈ 2-4 s (element arrives, ring locks, hood swaps, plate changes). By eye ≈ 15 events in 43 s ≈ 2.9 s each.

Typography: "LEICA Q3 43" in thin-to-regular wide-tracked caps (closest free: Jost Light / Outfit Light, tracking ≈ +0.08 em), white on black, cap ≈ 4 % H, centred at y ≈ 48 %, fade 0.5 s in / 0.5 s out, held ≈ 3 s. Red dot logo ≈ 9 % H.

Colour/grade: warm daylight interior (R-B +26), beige wall, oak table, leaf-shadow gobo (dappled light), median luma 119, crisp contrast (p95-p5 173). The camera is dark grey/black; the only saturated colour is the red dot (and one green-gold edition accent).

Camera/shots: photoreal CG product animation; table-top hero at a low 3/4 angle, macros of glass and engravings, an exploded view that assembles itself, slow continuous orbit; the screen-in-screen shot (the camera shows itself).

Transitions: 4 visible cuts; the rest are object transitions inside the take (parts fly in, a hood or plate swaps while the camera orbits). Cut to black for the name, fade to the logo.

Sound: music only, minimal electronic with mechanical clicks on each lock-in; −9.0 LUFS integrated (very loud), LRA 4.0 LU, true peak +1.2 dBTP. Rise +23 dB at 22.2 s when the long orbit starts. Logo ends in 1.7 s of silence.

What makes it premium:
- Construction as spectacle: the camera assembles from its optics, so the lens is the hero.
- Calm, sunlit "home" set with dappled light instead of a black studio: warm luxury, not tech.
- Few cuts; the camera never stops moving, events every 2-4 s.
- Name card and logo separated, each alone on black.

Recipe (CG or HTML/GSAP 2.5D):
1. Shoot or render: product parts as separate PNG layers (lens elements, rings, body), plus a sunlit table plate with a leaf-shadow gobo.
2. Assembly: each part `gsap.from(part,{y:-120, rotation:gsap.utils.random(-25,25), opacity:0, duration:1.1, ease:'power3.out'})`, staggered 0.25-0.4 s, with a click SFX on each landing.
3. Orbit: a 15-25 s clip (real turntable or CG); swap accessories during the move with a 0.3 s cross-fade masked to the part.
4. Gobo light: an overlay `<img>` of leaf shadows at `mix-blend-mode:multiply; opacity:.35`, drifting x ± 2 % over 10 s.
5. Name card: `font: 300 5.5vh 'Jost'; letter-spacing:.08em; text-transform:uppercase`, black background, 3 s; then logo 5 s, last 1.5 s silent.
6. Master −14 LUFS for social (the original −9 LUFS is louder than platforms play back).
