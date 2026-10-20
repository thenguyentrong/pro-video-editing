# Sky Sports Cricket: Where Stories Start  (Sky Sports, uploaded 2018-05-15, 40.1 s, 16:9 with ≈2.4:1 letterbox, YouTube / Sky Sports channel)
URL: https://www.youtube.com/watch?v=aIzLRrfQFt4
Purpose: summer-season channel promo (:40) for live international cricket
One-sentence point: the kids playing on a housing estate today are the stars of tomorrow, so every story starts where you watch it.

Structure (times from metrics.json):
- 0.0–9.4 SET-UP: kids on a city housing estate: a boy cycling down a ramp, stumps carried, a girl walking across the courtyard grass, kids running down stairwells; 0.8–3.3 s shots.
- 9.4–19.2 TURN: the estate courtyard becomes a famous test ground: tower-block balconies change into packed stands while the kids keep playing; real broadcast graphics appear on the kids (name strap "Test debut", a player card with a star); a 0.7 s audio drop-out at 13.95 s before the change lands.
- 19.2–35.4 MATCH: a kids' game played like an international: a girl faces a pro bowler with a name strap, a batting stats panel on a boy, a catch, run-out dive; fastest part (10 cuts in 27–33 s, 0.5–0.8 s).
- 35.4–40.0 END: top-down aerial of the green courtyard that rises into a satellite-style aerial of a real stadium (≈4.6 s), with a small line "EVERY ENGLAND HOME TEST, ODI AND T20 LIVE THIS SUMMER" and the channel logo (cricket variant) underneath.

Cut rhythm: 25 shots in 40.1 s, ASL 1.60 s, median 1.0 s, 48 % under 1 s. ASL per quarter 1.67 / 1.67 / 1.11 / 1.43. Cuts per 10 s 6, 5, 11, 1 (the end aerial). Cuts on onsets 33 % vs 24 % chance. Adaptive and scene detectors agreed.

Typography:
- Broadcast graphics used as story devices: the channel's real on-screen strap (light-blue gradient bar with a white crest square, white name ≈3.5 % H in a rounded sans, role line ≈1.6 %), a white stats panel bottom-left. Closest free: Nunito Sans 700 / Source Sans 3 600.
- Endline: thin caps, white, cap ≈1.5 % H, centred at ≈80 % height, with the channel logo ≈4 % H below. Closest free: Montserrat 400 caps, tracking 0.05 em.
- No title card, no talent names besides the kids' straps.

Colour/grade: natural, soft daylight, slightly desaturated brick and concrete, bright green grass; the stadium is the same palette, so the change feels real. Letterbox ≈12.5 % top/bottom.

Camera/shots: commercial cinematography with real kids: eye-level wides, close-ups, tracking shots; seamless compositing of stands into the estate (VFX set extension); a top-down drone and a high aerial for the end.

Transitions: hard cuts; the "turn" is a transformation inside the shot (VFX), not a transition; the end is one continuous rise from courtyard to stadium.

Sound: music + sound effects (bat, crowd swell); integrated −22.9 LUFS (EU broadcast level), LRA 6.3 LU, true peak −10.0 dBTP; quiet start (−26 to −28 momentary for 5 s), build to −19 at 19 s and 35–36 s; one 0.7 s drop-out at 13.95 s (floor −50 dB) then +24 dB at 14.85 s right on the transformation. Not verified by listening.

What makes it premium:
- The broadcaster's own graphics are put on ordinary kids: the brand's on-air language becomes the story.
- One transformation (estate → stadium) carries the idea; no match footage is needed.
- A silence before the transformation, and a calm final rise that matches the start (courtyard) to the end (stadium).

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- Shoot or source a local, real setting (courtyard, school yard) and 20–25 shots of people playing; 1–3 s in the set-up, 0.5–0.8 s in the match.
- Transformation: layer a stadium-stand plate behind a rotoscoped foreground or crossfade `clip-path` from the building edge upward (`inset(100% 0 0 0)→inset(0)`, 1.2 s `power2.inOut`); cut the music for 0.6 s just before.
- Strap: `.strap{height:52px;background:linear-gradient(90deg,#1ea0e0,#5cc8f5);border-radius:2px}` with a 52 px white crest square, name Nunito Sans 700 36 px, role 18 px; slide in `x -30px→0` 0.3 s.
- End: top-down drone → aerial (scale 1.0→0.35 over 4.5 s, `power1.inOut`), endline Montserrat 400 caps 16 px at 80 % height, logo below.
- Stock queries: "kids playing cricket courtyard", "housing estate kids playing", "cricket stadium aerial", "cricket bat ball slow motion", "top down drone grass courtyard".
