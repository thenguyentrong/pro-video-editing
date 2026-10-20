# Gatto | Teaser Trailer  (Pixar, 11 Jun 2026, 58.6 s, 2.39:1 file (1080×452), YouTube)
URL: https://www.youtube.com/watch?v=NIKfR_uF_d0
Purpose: teaser for an original animated film, 9 months before release (a "scene teaser": one comic scene instead of a montage)
One-sentence point: in a city of canals, a gang of cats interrogates the wrong cat about missing tuna, and it goes badly.

## Structure (beats with timestamps; % of 58.6 s)
- 0.0–7.6 **establishing shot with the studio claim**: night rooftops of a canal city, a slow move over the roofs; "FROM THE STUDIO THAT BROUGHT YOU" + two earlier film logos fade in over the picture (≈1.0–4.5 s), cats on the roof below. Quiet bed (−21…−24 dBFS).
- 7.6–8.7 black (1.1 s).
- 8.7–33.2 **one locked 24.5 s take** (42 % of the runtime): a big white cat questions a small black cat under one hanging bulb; the comedy is in timing and acting, not in cutting. Hits only on the jokes (+16…+24 dB).
- 33.2–42.9 **slapstick fight in 8 shots of 1.0–1.4 s**, each separated by a 0.2–0.3 s flash of black (the bulb going out), loudest moment at 37.55 (−11.1 dBFS); a 0.4 s drop-out at 38.95 then +28.2 dB.
- 42.9–44.4 black (1.5 s).
- 44.4–52.7 **title "GATTO"** with the studio names above (8.3 s, at 76 %): a cat runs through the letters, knocks one letter out and the title rebuilds (a character gag inside the logo).
- 52.7–55.0 "IN THEATERS / MARCH 2027" (2.3 s). 55.0–58.6 black, sound out.

## Cut rhythm
- 13 shots, **ASL 4.51 s**, median 1.50 s; no shot under 1 s, 31 % over 3 s; 13.3 shots per minute (the slowest piece in the trailer set).
- ASL per quarter 7.32 · 14.64 · 1.63 · 3.66 s (the long take fills Q1–Q2).
- Cuts on audio onsets **58 % vs 29 % chance**: every cut in the fight lands on a hit.
- Speech in ≈55 s of 59 s by the detector (dialogue plus effort sounds; not checked line by line).

## Typography
- Studio claim over the picture in small serif caps (≈2.5 % H) above two film logos (≈8 % H), placed top left over the sky, faded in and out.
- Title: the film's own brush-textured logo in light blue (≈30 % H) with a small "DISNEY · PIXAR" line above, on a deep blue night gradient. Animated: a character runs through it.
- Date: soft condensed caps (closest free: Oswald 500), light blue with a glow, two lines ≈13 % H each, centred.

## Colour / grade
Deep blue night, one warm bulb as the only light in the scene, orange cat against white cat; all cards keep the night blue.

## Camera / shots
One establishing move, one locked wide for the whole scene, then close fight shots. No montage of the world.

## Transitions
Black between the three parts (1.1 s and 1.5 s); 0.2–0.3 s black flashes between fight shots; title animation instead of a cut.

## Sound
- Integrated **−14.1 LUFS**, LRA 6.3 LU, true peak −1.0 dBTP.
- Dialogue-led: music low under the scene, hits on punchlines, louder fight (−11…−16 dBFS), title music, fade to silence on black.

## What makes it premium
- It trusts one scene: 24.5 s without a cut.
- The studio's past films are the "from the makers of" card, shown inside the first shot.
- The title is a gag with the main character, so even the logo is funny.
- Every fight cut lands on a sound hit (58 % on onsets).

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. 0–7.5 s: one establishing move (`scale 1→1.05`, `ease:"none"`), studio claim faded in over the sky (`opacity 0→1` 0.8 s, hold 2.5 s, out 0.8 s).
2. 1 s of black.
3. One 20–25 s locked scene with dialogue; sound hits on each joke.
4. 8–10 s of fast action, shots of 1.0–1.4 s with 0.25 s black flashes between them, each cut on a hit.
5. 1.5 s black, title 8 s with a character animation through the letters (animate one letter `rotation`/`y` out and back in), date 2.3 s, black 3.5 s.
6. Master −14 LUFS, true peak −1 dBTP.
