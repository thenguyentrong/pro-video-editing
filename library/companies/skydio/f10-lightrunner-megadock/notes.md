# Introducing Skydio F10 Lightrunner + MegaDock  (Skydio, 2026-09-23, 2:13, 16:9, YouTube @Skydio)
URL: https://www.youtube.com/watch?v=mai4evTj4dM
Purpose: product launch film (narrated reveal)
One-sentence point: a docked, robot-launched fixed-wing drone brings fast, long-range aerial views to existing customers, and one person can run several of them.

## Structure (narrated)
- 0.0-12.9 context: the company's existing drones at work (roof dock, live operator screen, a house fire from above, firefighters, utility crews, a power line inspection).
- 12.9-18.1 need: city and field aerials, a fast motion-blurred flight, a fixed-wing silhouette at sunset.
- 18.1-29.3 the dock: a black dock box at night, a robot arm inside loading and launching the drone (8.4 s shot), launch through the roof hatch.
- 29.3-34.5 name: product wordmark ≈12 % H with a widely tracked sub-name, over a real flight past the camera; other scenes (substation, construction site, bridge) under it.
- 34.5-48.1 numbers: a digital map with radius rings; then the speed counts up on real flight shots (three steps to the top speed) and the flight time counts up the same way; numbers centred ≈5 % H.
- 48.1-63 operations: field crew with the drone, hand launch, a hangar, the dock arm again, an operator at a multi-screen station.
- 63-74 design: renders of the airframe on dark grey; a labelled split screen comparing a traditional wing with the product's camera view; real camera close-ups on the wing.
- 72.2-72.6 drop-out, +30.2 dB hit at 73.05 on the people beat: utility worker, firefighters, a driver.
- 74-93 software: operator UI full screen (real recording), a coloured 3D voxel map of the planned route, an aerial of the site.
- 93-103 family: other drones of the brand in flight and a rendered group shot around the dock.
- 103-125.7 hero flights: many short real flights at dawn and dusk, the dock bay.
- 125.7-133.3 wordmark on blue-grey, then on black.

## Cut rhythm
- 62 shots in 133.3 s (adaptive detector; all extra cuts checked by eye). ASL 2.15 s, median 1.35 s. ASL per quarter 1.67 / 1.96 / 2.78 / 2.08 s.
- 29 % under 1 s, 19 % over 3 s. Cuts per 10 s: 11, 4, 3, 6, 1, 7, 4, 5, 4, 1, 8, 5, 2. Longest 10.7 s (93.0, family render), 8.4 s (spec counters), 8.4 s (dock arm).
- 46 % of cuts land on an audio onset (chance 35 %).

## Typography
- Wordmark: wide geometric product logo ≈12 % H + sub-name in caps with letter-spacing ≈.5em, ≈2 % H.
- Numbers: grotesk 500 ≈5 % H, centred, white, soft shadow; the value counts up in 3 steps on 3 shots, the unit word stays. Closest free: Inter 500.
- Split-screen labels: caps ≈1.5 %, letter-spaced, under each panel.

## Colour/grade
- Natural real footage, warm dawn/dusk for hero flights, dark navy UI and renders; one light-blue accent stripe on the airframe.

## Camera/shots
- Mostly real: customer operations, the dock and arm, chase and ground long-lens flight shots, onboard views. Renders: airframe turntable, comparison, the product family; a 3D route visualisation. Real and render are in separate shots.

## Transitions
- Hard cuts; a couple of motion-blur speed transitions; fade to the end wordmark.

## Sound
- Narrator, ≈252 words in ≈124 s (≈2.0 words/s), conversational, with rhetorical questions.
- Integrated -14.0 LUFS, LRA 4.4 LU, true peak -0.8 dBTP. Biggest hits +33.7 dB at 65.7 s (design turn) and +30.2 dB at 73.05 s (after the only drop-out). Ending: button (cut to silence 130.75).

## What makes it premium
- Specs are earned on screen: the counter climbs while the real drone flies.
- The robot dock and arm are shown working in long takes (8.4 s).
- Customer jobs open the film, so the product enters a real need.
- Renders are used only for design and family, never for flight proof; the brand also released a separate real-only cut (f10-real-flights-no-cgi).

## Recipe (real footage + HTML/GSAP)
- 10-13 s of real customer work before the product appears.
- Counter: `gsap.to(obj,{v:100, duration:2.4, ease:'steps(3)', onUpdate:()=>el.textContent=Math.round(obj.v)+' mph'})` across 3 flight shots; Inter 500 5vh centred.
- Wordmark at 25 % runtime over a real fly-by; sub-name 2vh caps letter-spacing .5em.
- Show the operator UI as the real recording for 4-6 s before the autonomy claim.
- 0.4 s drop-out before the human beat; end on a hard button.
