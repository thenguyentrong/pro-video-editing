# New York City's Hottest Day in 14 Years  (Casey Neistat, 2026-07-03, 9:33 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=B-46uG6raX4
Purpose: event / experiment vlog (a heat wave measured around the city)
One-sentence point: On a record-heat day Casey crosses the city with an infrared thermometer to find the hottest surface and test whether an egg really cooks on the street.

Data note: first 300 s analysed (trimmed with ffmpeg). Cuts from the adaptive detector plus three verified scene-only cuts (91.47, 187.02, 260.18 s: hand-over-lens and whip cuts). Speech timings from a local speech-to-text pass (±0.5 s).

## First 30 s (hook)
- 0.0–8.1: one locked-off wide at street level: Casey cracks an egg on the asphalt and crouches next to it; his first line (a question about the heat) at ≈2.1 s, the egg premise at ≈4–6 s.
- 8.1–22.4: sunrise world montage: a ferry against the sun, then 5 drone aerials of the city in haze (1.3–4.8 s each) under a collage of radio/TV news voices about the heat (≈7.6–21.6 s). The context is told by others' voices, not by the host.
- 22.4–23.9: title card over the sun (3 lines, see typography), 1.5 s; biggest rise near it (+29.9 dB at 21.9 s).
- 23.9–26.2: frontal wide of Casey on his skateboard in a bike lane (gear-up start).
- 26.2–31.9: four 1.2–1.5 s inserts: drawing the infrared thermometer from a belt holster like a pistol; loudest moment of the film at 31.7 s (−8.1 dBFS, music hit).
- (after the hook) 32–44 skating down the avenue, top-down drone shots of intersections; the measuring task is put to camera at ≈43.5 s; first reading with a big white arrow at 52.9 s.
- Cuts in 0–30 s: 11 (the densest opening of the three).

## Structure (first 300 s)
- 0–32 hook (above). 32–60 first measurements on the street (phone, thermometer, white arrow on the reading).
- 60–80 the egg check (macro of the egg, wide static of the street).
- 80–100 a park and a subway entrance (reading on the railing).
- 100–136 subway: stairs, turnstile, platform, readings with the thermometer close to the lens, train arrives.
- 136–153 the public library steps with a crowd; 153–175 inside a building, dark interior readings.
- 175–190 Times Square, readings; 186.3 hand-over-lens cut to a market stall.
- 190–245 Central Park: drone over the lawn, talk to camera (11.7 s, longest shot), a runner interviewed while running.
- 245–285 drone top-down of a fountain plaza, kids in a fountain, aerial over the city, walking talk on a street.
- 285–296.5 an appliance shop (air-conditioner box), talk to camera.
- 296.5–298.5 "YESTERDAY" card over a whip-blur, on 2.0 s of digital silence, then the story jumps back.

## Cut rhythm
93 shots in 300 s, ASL 3.23 s, median 2.63 s, 7.5 % under 1 s, 43.0 % over 3 s, 18.6 shots/min — the fastest of the three and very even: ASL by quarter 3.4 / 3.0 / 3.0 / 3.1 s. Longest 11.7 s (197.9 s park talk), 8.9 s (104.4 s subway), 8.5 s (260.2 s). Shortest 0.42 s (104.0 s), 0.62 s, 0.67 s. Cuts per 10 s: 1–6, peaks of 6 at 20–30, 130–140 and 280–290 s (measurement insert bursts). Cuts on onsets 43 % vs 38 % chance.

## Typography
- Title card: Helvetica-style bold grotesque caps (closest free: TeX Gyre Heros Bold / Inter Bold), white, no shadow, three lines justified to the same width (≈8–68 % W), flush left at x ≈8 % W, block from ≈51 % to 87 % H; cap heights ≈9 % H ("city" line), ≈12.5 % H (the key line, horizontally condensed), ≈10 % H (date line); tight leading; hard cut on and off, 1.5 s, over a telephoto sun.
- Time card: "YESTERDAY" in a regular-weight Helvetica-style caps, white, centred, cap height ≈16.7 % H, spanning ≈12–88 % W, over darkened (≈−40 %) whip-blurred footage, ≈2 s, in silence.
- Annotation: a flat white block arrow ≈26 % W pointing at the thermometer reading, cut on/off with the shot, no animation.

## Colour/grade
Sunrise orange haze for the world montage; hard midday sun, saturated and contrasty on the streets; subway cooler and greener; no letterbox, no grain.

## Camera/shots
Locked-off wide of himself (egg open), drone aerials (sunrise and top-down), fisheye selfies at arm's length, macro inserts of the thermometer pointed at the lens, a handheld follow of a runner, 360/top-down plaza shot, appliance-shop wide.

## Transitions
Hard cuts; hand-over-lens cut (186.3 s), whip cuts (260.2 s), a time card with silence (296.5 s).

## Sound
−12.7 LUFS integrated (loudest of the three), LRA 7.1 LU, true peak +0.8 dBTP (480p re-encode). RMS median −17.5 dBFS. Music is under almost everything: p10 sits only 3–9 dB under the median in most 10 s windows. Radio-news collage over the opening montage. One designed silence: 2.0 s digital silence under the "YESTERDAY" card (296.5–298.5 s). Hits +15…+21 dB at measurement reveals (e.g. 44.95, 102.7, 190.65 s).

## What makes it premium
- A simple measurable question (how hot is it, really?) turns a weather day into a mission with a number every 20–30 s.
- Other people's voices (news radio) set the stakes in 14 s so the host doesn't have to.
- One bold, well-set title card instead of many graphics.
- The thermometer pointed at the lens is a recurring, readable visual.

## Recipe (real footage + HTML/GSAP)
- 0–8 s: one locked-off wide of the premise action; first line at ≈2 s.
- 8–22 s: 5–6 aerial/b-roll shots of 1.3–4.8 s under a news-voice collage, music rising.
- Title card 1.5 s: `.t{position:absolute;left:8%;bottom:13%;font:800 var(--s)/0.92 "TeX Gyre Heros",Inter,sans-serif;color:#fff;text-transform:uppercase}` with line sizes 12.6vh / 17.5vh (scaleX .9) / 14vh to get cap heights ≈9 / 12.5 / 10 % H; cut on with a music hit, cut off.
- Gear-up: 4 inserts × 1.2–1.5 s, last one on the loudest hit.
- Readings: insert with the number held 2–4 s; optional static white arrow (`clip-path` block arrow, 26 % W).
- Time jump: blur + darken the last shot, "YESTERDAY" `font:400 23vh` caps centred, mute all audio for 2 s.
</content>
</invoke>
