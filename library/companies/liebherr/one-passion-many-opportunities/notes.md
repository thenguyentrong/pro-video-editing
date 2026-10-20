# Liebherr - One Passion. Many Opportunities.  (Liebherr, 2023-06-27, 1:48, 16:9 with ≈2.35:1 letterbox, YouTube @Liebherr)
URL: https://www.youtube.com/watch?v=He-cWehTCyc
Purpose: employer-brand / recruiting film
One-sentence point: Passion for machines and technology is what people at Liebherr share; the group offers room to grow, freedom to act and a team that holds together.

## Structure (one inner-monologue VO in German, subtitles burned into the lower black bar)
- 0.0-2.9 (0-3 %) logo on white, silent (1.9 s digital silence).
- 2.9-7.9 (3-7 %) drone above a sea of fog at sunrise, factory roofs below. VO asks how you recognise passion.
- 7.9-13.2 (7-12 %) flash cluster: black dip, extreme close-ups of eyes (0.12-1.3 s each, machine reflected in an iris) - "a light in the eyes".
- 13.2-24.2 (12-22 %) people at work: scrapyard excavator from above, engineer looking up at a crane, welder, large ring part, crane operator, a young man on a dirt site with an excavator behind.
- 24.2-31.8 (22-29 %) value-word flicker: big white words (cohesion, fascination, freedom to act, consistency) flash over shots and change every 0.2-1.3 s; tower crane against clouds, server/blue lights, a manager in a hall.
- 31.8-47.6 (29-44 %) "I want to contribute / this is me / I belong here": office whiteboard, workshop, apprentice with a saw, crane cab, a woman inside a machine, simulator, eye again.
- 47.6-66.0 (44-61 %) opportunities and growth: VR headset, crane cab POV, bucket, a woman putting on a hard hat, a figure on a crane boom at sunset, a woman in an appliance plant, drone over a yard of cranes, word "Handlungsfreiraum" (freedom to act) held 2-3 s over a sunrise drone of a crane factory.
- 66.0-89.4 (61-83 %) cohesion: words "Beständigkeit" and "Zusammenhalt" over a team portrait, high-fives in hi-vis, a hook block swinging, workers smiling to camera (diverse), people walking through the plant, low-angle team in front of a row of crawler cranes (hero).
- 89.4-94.9 (83-88 %) drone over the plant at sunrise: "this is what I am looking for".
- 94.9-108.4 (88-100 %) white end card: claim (≈4.5 s), careers URL (≈2.5 s), logo (≈6 s).

## Cut rhythm
- 97 shots in the 94.9 s before the end card (86 detected + 11 verified by eye: a dissolve at 2.9 s, flash cuts and whip cuts the scene detector missed; 4 adaptive-only candidates were false and left out). ASL 0.98 s, median 0.76 s, 69 % of shots under 1 s.
- ASL per quarter 1.13 / 0.85 / 0.99 / 0.88 s. Longest 5.54 s (final drone, 89.4 s), 5.02 s (fog drone opener), 2.96 s. Shortest 0.12 s (eye flashes).
- Cuts per 10 s: 4 / 12 / 9 / 16 / 9 / 12 / 6 / 14 / 13 - the pace breathes only for the "freedom to act" sunrise (60-70 s).
- End card 13.5 s (white, three text states).

## Typography
- Value words: bold condensed grotesk (Liebherr house face; free: Barlow Condensed 700 or Barlow Semi Condensed 700), white, ≈13 % H cap height, sentence case, centred horizontally at ≈45-55 % height, no box, no shadow. Hard cut on/off, words replace each other on the shot cuts (0.2-1.3 s per word); the strongest one holds 2-3 s.
- Subtitles: the VO line burned into the bottom letterbox bar, white regular grotesk (free: Barlow 400) ≈3.5 % H, centred, one sentence per card.
- End card: claim in bold condensed ≈7 % H, black on white, centred; URL ≈2.5 % H; wordmark logo ≈5 % H.

## Colour/grade
- Cinematic teal-orange: golden-hour sun, haze, fog, lens flares, warm skin, teal shadows; blue/green tech shots (servers). Letterbox ≈2.35:1 (bars ≈12 % H each). Slight softness/bloom; no visible grain.

## Camera/shots
- Drone: fog sea, crane factory at sunrise, overhead of crane yards and scrapyard - about 10 drone shots in total. Many extreme low angles up booms; macro eyes; gimbal walks with people; portraits to camera (subjects look into the lens, smile). Real employees in work clothes, PPE where the job needs it (hard hats, hi-vis).
- No product claims, no data, no UI, no timelapse; real footage only.

## Transitions
- Hard cuts, flash frames (0.12-0.2 s), whip pans used as cuts, black dip 0.2 s at 7.9 s, dissolve from the logo card. Text flicker as rhythm device.

## Sound
- Epic emotional build (piano/strings into drums), single male VO, close and intimate. Integrated -15.5 LUFS, LRA 6.9 LU, true peak +0.3 dBTP (clipping risk). Silence 0-1.9 s on the opening logo; 1.35 s silence at the very end.
- Hits: +16 dB at 94.45 s (cut to the claim card), +24 dB at 101.4 s (logo), +15 dB at 12.35 s (eye flash cluster). Cuts are not on music onsets (11 % vs 14 % chance) - the edit follows the VO phrases and its own flash rhythm.

## What makes it premium
- Machine scale as emotion: a person tiny on a crane boom at sunrise, a team in front of a row of crawler cranes.
- Value words as huge type, flashed on the cut - a statement without a speaker on screen.
- Faces that look into the lens; diverse real staff instead of actors (looks real, unpolished smiles).
- Teal-orange golden-hour grade and letterbox make a factory look like a feature film.

## Recipe (real footage + HTML/GSAP)
- Shoot at sunrise: 3 drone shots (fog/haze, factory, yard from above), 6 low angles up machines, 8 portraits to camera (3 s each), 6 macro eyes/hands, 1 team hero in front of machines.
- Letterbox `box-shadow: inset 0 12vh 0 #000, inset 0 -12vh 0 #000`; subtitles inside the bottom bar `bottom:4vh; font:400 3.5vh Barlow; color:#fff`.
- Value word: `font:700 13vh 'Barlow Condensed'; color:#fff`, `tl.set(word,{textContent:'Freedom'},t)` on each cut, 0.2-1.3 s per word, the last one held 2.5 s.
- Cut 0.5-1.2 s; insert 3-5 flash shots of 0.12-0.2 s at each VO question; let one 5 s drone breathe at 60 % and at the end.
- End card on white: claim 4.5 s -> URL 2.5 s -> logo 6 s, hard cuts, hit on the claim.
