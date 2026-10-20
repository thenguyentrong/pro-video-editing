# 2025 NBA Tip-Off | START TO FINISH  (NBA, uploaded 2025-10-22, 56.8 s, 16:9, YouTube / NBA channel)
URL: https://www.youtube.com/watch?v=GEohF0W80Kg
Purpose: season-launch campaign spot (opening week), sponsor-titled event lockup
One-sentence point: players train and fans get ready in every city at the same time, because the season runs from start to finish and everyone is in it.

Structure (times from metrics.json):
- 0.0–3.5 HOOK: backlit silhouette of a player under stadium lights, then a tight portrait (face fills ≈90 % of height). Quiet bed (−21 to −23 LUFS momentary).
- 3.5–20 BUILD: training rituals (court dribble, hands, weights, window silhouette) intercut with fans' faces; first hits at ≈7 s and 10 s.
- 20–33 CITY MONTAGE: fans in jerseys of many teams (signs, murals, trains, kids), fastest part, 12 cuts in 20–30 s.
- 33–36 BREATH: shadow of a kid dribbling on a wall, music dips (−16/−19).
- 36–43 PEAK: outdoor hoops against tower blocks, overhead hoop shot, loudest moment at 36.6 s (−7 LUFS momentary).
- 43–49.8 WALK-OUT: two players walk down dark tunnels under strobe light (3.0 s and 2.4 s, the longest live shots).
- 49.8–53.0 WORD CARDS: "START" / "TO" / "FINISH", one huge word over each of three fan close-ups, 0.85 s each (third ≈1.5 s).
- 53.0–56.8 END: league logo + sponsor + event name lockup over a kid's face that turns red with a light bloom; app line; music decays.

Cut rhythm: 45 shots in 56.8 s, ASL 1.26 s, median 1.0 s, 49 % under 1 s, 48 shots/min. ASL per quarter 1.42 / 0.89 / 1.01 / 1.77; cuts per 10 s 5, 9, 12, 9, 6, 3. Six cuts were missed by the scene detector (dark, strobing footage) and added after a frame check; one adaptive-only candidate (45.46 s) was a strobe, not a cut.

Typography:
- Word cards: very condensed heavy italic caps, white, centred, cap ≈50 % of frame height, one word per card, hard on with the cut, no animation. Closest free: Bebas Neue / Oswald 700 with `skewX(-8deg)`, or "Antonio Bold".
- End lockup: league logo (≈26 % H tall) left of a two-line block: sponsor name in wide caps ≈3 % H above "TIP-OFF" in condensed caps, cap ≈19 % H; lockup centred, slightly above middle. App line ≈3 % H, bottom 15 %.
- No lower thirds, no names, no dates in picture.

Colour/grade: teal-and-warm cinema grade (cool blue-green shadows, warm skin), soft contrast, shallow depth of field, some anamorphic-style lens flares. Brand red arrives only at the very end as a light bloom on the last face.

Camera/shots: shot like a commercial, not broadcast: 50–85 mm close-ups, low angles up to the hoop, overhead hoop, silhouettes against windows, handheld fan shots, slow-motion. Real players + real-looking fans. Many faces fill the frame.

Transitions: hard cuts only; text cards sit on footage; end lockup on footage, no black card.

Sound: one track with a build; quiet open (−21/−23), hits at ≈7, 10 and 13 s, steady wall −9 to −13 LUFS momentary 13–32 s, short dip at 33–35 s, peak 36.6 s, plateau −8 to −11 to 52 s, then decay to −21 at the end. Integrated −12.2 LUFS (very loud), LRA 9.9 LU, true peak +1.3 dBTP (over −1: clipping risk). Cuts not on onsets (18 % vs 20 % chance). I did not listen; style of track and whether there is a voice are not verified.

What makes it premium:
- Commercial cinematography (teal/warm, shallow focus) instead of broadcast tape: the league sells feeling, not results.
- The three-word line is the only text and it is enormous (50 % of height), on faces, at the very end.
- Fans and players are given equal weight; every team colour appears in jerseys, so no graphic colour is needed.
- A clear breath (shadow shot + music dip) right before the biggest shot.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- Grade: lift shadows toward teal (`#0f2a2e` at 25 % `mix-blend-mode:soft-light`), keep skin warm; 35 % of shots shallow-focus close-ups.
- Rhythm: 3.5 s calm hook (2 shots) → 1.0 s average for the build → 0.8 s in the city montage → one 2 s breath → 1.5–3 s hero shots → three word cards.
- Word cards: `.word{font:700 italic 300px/0.85 "Bebas Neue";transform:skewX(-8deg);color:#fff;text-shadow:0 0 30px rgba(0,0,0,.35)}` (cap ≈50 % H at 1080), on with the cut, 0.85 s each, footage underneath.
- End: lockup over the last shot, radial red bloom `radial-gradient(circle at 50% 30%, rgba(230,30,40,.65), transparent 60%)` fading in 0.6 s; hold 3.5 s; music decays over 3 s.
- Stock queries: "basketball player silhouette stadium lights", "basketball fans cheering close up", "outdoor basketball hoop city towers", "player walking tunnel dark strobe", "kid dribbling shadow wall".
