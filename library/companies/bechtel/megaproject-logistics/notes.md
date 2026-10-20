# Logistical challenges of building mega projects  (Bechtel Australia, 2013-10-29, 1:32, 16:9, YouTube, Bechtel Australia channel)
URL: https://www.youtube.com/watch?v=zFsvFLQ9F0s
Purpose: project case study / internal-external explainer (a joint procurement team supplying three LNG megaprojects on an island)
One-sentence point: One central procurement team buys and ships every piece of material for three LNG projects on an island, from a mainland laydown area that is itself a giant operation.

Source note: uploaded in 2013, available only at 360p; frames are upscaled.

## Structure (92.4 s)
- 0-6 (0-6 %) 3D globe logo spins in on black.
- 6-11 (6-12 %) question card "WHAT IS PJET?" over a sky with sun flare (time-lapse clouds).
- 11-29 (12-31 %) answer: three staff interviews on the laydown yard in PPE (hard hat, hi-vis shirt, safety glasses), each with a name super; b-roll of pipe spools, forklifts, container stacks.
- 29-33 (31-36 %) office: procurement staff at screens.
- 33-53 (36-57 %) numbers spoken: workforce size and 39 hectares of laydown over about 11 sites; b-roll of a crane lift, pipe racks, cable drums.
- 53-70 (57-76 %) to the island: loader and trucks, barge ramp, ferry, then three project location labels over site shots (GLNG, AUSTRALIA PACIFIC LNG, QUEENSLAND CURTIS LNG).
- 70-87 (76-94 %) "first of its kind": a coordinator interview, drone/helicopter over the island, barge loading.
- 87-92 (94-100 %) logo spin on black, 1.7 s silence.

## Cut rhythm (6 dissolves added by eye: 6.0, 46.2, 50.1, 51.6, 74.8, 86.9)
- 37 shots, ASL 2.50 s, median 1.72 s, 5.4 % under 1 s, 24 shots/min. ASL per quarter 3.85 / 2.10 / 1.54 / 2.89 s.
- Longest 6.6 s (first interview), 6.0 s (logo), 5.5 s (logo end). Interviews 3-6 s; b-roll 1.0-2 s.

## Typography
- Name super: name in letter-spaced caps (≈5.5 % cap height) over role line in mixed case (≈3.5 %), white with drop shadow, right-aligned at x ≈95 %, bottom ≈87 %; fades in ≈0.5 s, stays for the whole bite. Humanist sans (Gill Sans/Myriad look; free: Cabin or Source Sans 3).
- Location label: wide letter-spaced caps ≈7 % cap height, bottom-left x ≈10 %, y ≈85 %, white with shadow, fades in.
- Question card: "WHAT IS PJET?" caps ≈5 %, white over sky.

## Colour/grade
- Broadcast-TV look of 2013: punchy saturation, bright tropical sun, hi-vis yellow dominates; no grade style.

## Camera/shots
- Tripod interviews on the yard (staff placed left or right third, materials behind them). Telephoto b-roll of stacked material for density, aerials of the island and port, handheld office shots.
- PPE everywhere: white hard hat with logo, yellow hi-vis shirt, safety glasses.

## Transitions
- Hard cuts plus ≈0.25-0.5 s dissolves into and out of interviews (supers dissolve with them). Logo animations top and tail.

## Sound
- Interview voices over a corporate bed; integrated -21.1 LUFS, LRA 7.2 LU, true peak -0.9 dBTP. No drop-outs; 1.0 s silence at the start, 1.7 s at the end. Hits at 25.9 s and 39.9 s on speaker entries.

## What makes it useful
- Real staff with full names and job titles on the real site - the "we did this" proof.
- Scale through material: thousands of pipe spools, cable drums, container walls.
- Location labels name each megaproject.
- Dated: 3D logo spin, drop-shadow text, 360p.

## Recipe (real footage + HTML/GSAP)
- Interview on site with the material behind (telephoto, 70-100 mm), PPE on, lavalier.
- Super: `right:5vw; bottom:9vh; text-align:right`; name `font:600 4.5vh 'Source Sans 3'; letter-spacing:.12em; text-transform:uppercase`; role `font:400 2.8vh 'Source Sans 3'`; `text-shadow:0 .2vh .6vh rgba(0,0,0,.6)`; `tl.from(sup,{autoAlpha:0,duration:.5})`, hold the whole bite.
- Location label: `left:10vw; bottom:10vh; font:500 5vh 'Source Sans 3'; letter-spacing:.15em`.
- Modern lift: drop the 3D logo; open with the question as plain type; add one number card for the spoken figures (39 ha, 11 sites).
