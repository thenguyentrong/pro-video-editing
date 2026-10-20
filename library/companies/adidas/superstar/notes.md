# Superstar  (adidas Originals, 2026-02-26, 1:33, 16:9 (≈1.66:1 pillarbox in the colour world), YouTube @adidasOriginals)
URL: https://www.youtube.com/watch?v=I6AxpJHSiY0
Purpose: product heritage anthem (Superstar shoe), celebrity narrator
One-sentence point: The Superstar is a shoe that leaves marks in culture; a narrator drives through memory and finds the people who wore it.

## Structure
- 0-0.33 black. 0.33-12.6 **opening hold**: one B&W shot of the narrator driving at night, locked inside the car (12.3 s, the longest shot). Voice-over starts at 1.5 s; the shot dissolves (7.7-11.6 s) into a long, symmetrical, one-point-perspective corridor in colour.
- 12.6-36 **the corridor world**: a surreal hotel/hall of doors (pale green marble, white floor, red carpets). Narrator in a long coat walks the corridor; each door opens a room with one person (a woman in bed, a man on a staircase, a writer at a desk). Shoes and track tops in close-up. Cuts back to the B&W car twice (25.9, 32.9 s): the car is the "present", the corridor the "memory".
- 36-80 **gallery of characters**: one face or one room per shot, 0.2-1.5 s. Mouth close-ups with grills, a woman shushing, a group on a bed, a DJ, a model in a dark corridor. Two short drop-outs (43.2 s, 80.6 s) before a hit.
- 80-84 snowstorm blows through a room of beds (one long shot, 4.1 s).
- 84-90 back to the B&W car; a skylight, two sneakers on the white corridor floor (the "marks"), the narrator laughs.
- 90.97-92.5 trefoil logo on black (1.6 s).

## Cut rhythm
- 79 shots in 92.5 s. ASL 1.17 s, median 0.83 s, 58 % under 1 s, 51 shots per minute.
- ASL per quarter 2.10 / 0.96 / 0.96 / 1.01 s: a long opening hold, then an even pace.
- Cuts per 10 s: 1, 6, 9, 9, 11, 12, 9, 13, 6, 2.
- Longest 12.26 s (0.33, opening car shot), 4.13 s (79.25, snowstorm room), 3.80 s (63.1). Shortest 0.21 s.
- Cuts on onsets 35 % vs 34 % chance (no beat cutting).

## Typography
- None in the film; the shoe and clothing carry the logo. End: white trefoil logo centred on black, ≈10 % of frame height.

## Colour/grade
- Two worlds: B&W car (present) vs colour corridor (memory). The colour world uses a fixed palette: pale mint/celadon walls, ochre marble, white floor, deep red carpets, royal blue bedding, black tracksuits.
- Some rooms in near-dark with one blue or red key light.

## Camera/shots
- Kubrick-like symmetry: one-point-perspective corridors, camera dead centre at eye height, slow push-ins.
- Wide room tableaux (one person, many objects), extreme close-ups of mouths, shoes and laces, top shots of shoes on the floor.
- Narrator always in the car frame: locked-off, wide-angle, through the windscreen.

## Transitions
- Long dissolve from the car into the corridor (7.7-11.6 s), otherwise hard cuts.
- Match cuts on the corridor axis: every corridor shot uses the same vanishing point in the centre.

## Sound
- One celebrity narrator from 1.5 to 84 s, conversational, with pauses; music and room sound under.
- Integrated -13.8 LUFS, LRA 6.8 LU, true peak -0.6 dBTP.
- Drop-outs 0.7 s at 43.2 s (next hit +42.7 dB at 44.15 s) and 0.9 s at 80.6 s (+30 dB at 81.6 s): silence before a new image world.

## What makes it premium
- One long held opening (12 s) before any cutting: confidence.
- A set (the corridor) as the film's memory palace: every person gets a room.
- Strict palette and strict symmetry make 80 shots of different people feel like one world.
- A narrator who talks, not sells; the product is never explained.

## Recipe (real footage + HTML/GSAP)
- Opening: one locked shot 10-13 s in B&W (`filter: grayscale(1) contrast(1.2)`), voice starts at 1.5 s; cross-dissolve 4 s into the first colour shot (`gsap.to(next, {opacity: 1, duration: 4})`).
- Corridor: same centred one-point composition for every "transition" shot; place a person in each door.
- Palette: limit to 5 colours (mint, ochre, white, red, blue); grade all rooms toward them.
- Gallery: 40-50 portraits/rooms at 0.3-1.5 s; two 0.7-0.9 s silences before new sections.
- End: return to the B&W opening frame, then logo on black 1.6 s.
