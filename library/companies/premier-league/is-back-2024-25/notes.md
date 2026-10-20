# The Premier League is BACK! ("The Kick Off" 2024/25)  (Premier League, uploaded 2024-08-12, 67.7 s incl. a 7.7 s end screen, 16:9, YouTube / Premier League channel)
URL: https://www.youtube.com/watch?v=Fi5OWvIii-8
Purpose: season-launch campaign spot (comedy narrative + highlight montage + identity end card)
One-sentence point: the whole country gets ready for the new season, down to the haircut, so it starts on the named date.

Structure (content 0–60.0 s; times from metrics.json):
- 0.0–6.4 HOOK: one slow 6.4 s shot past a barbershop window with a "price list" of famous players' haircuts on the wall; fans in many club shirts queue outside.
- 6.4–15.5 SET-UP: a fan in the chair asks for a haircut (dialogue scene in medium close-up, 1–2 s shots); a 0.4 s campaign-wordmark flash on a pitch at 10 s; a burst of club-crest and lion-logo inserts 11.6–14.2 s (tattoos, murals, shirts, a crest shaved into hair) at 0.12–0.3 s each.
- 15.5–41.0 MONTAGE: drop-out at 15.4 s, then the season's material at 0.3–0.6 s per shot: goals, celebrations, fans, new signings and managers as paper cut-outs on neon green with duotone echo copies, a "spectrum" heat-map cut-out, a fantasy-app phone screen, barbershop reaction shots between.
- 41.0–55.2 PAY-OFF: the campaign show on the shop TV (diegetic brand), the barber reveals the cut (4.4 s and 4.2 s shots, the longest of the body), big stars celebrating, the fan's grin.
- 55.2–60.0 END CARD 4.8 s: ball flies through to a purple card: lion logo, "THE KICK OFF" wordmark, date pill. Then 0.85 s silence, a purple league logo card, and the end screen.

Cut rhythm (0–60 s): 76 shots, ASL 0.79 s, median 0.38 s (!), 83 % under 1 s, 76 shots/min. ASL per quarter 0.79 / 0.60 / 0.68 / 1.15. Cuts per 10 s: 3, 21, 18, 16, 8, 9: slow hook, a very dense middle (21 cuts in 10–20 s), slower comedy pay-off. Union of the adaptive and scene detectors (22 scene-only cuts in the logo burst checked by eye: all real).

Typography:
- Campaign wordmark: geometric heavy sans caps "KICK OFF" with a small rotated "THE" stacked vertically before it, lime-to-cyan gradient (#d6f23a → #22e3d8), cap ≈16 % of frame height, centred; the O carries a centre-circle mark. Closest free: Outfit 800 or Lexend 800.
- Date pill: rounded rectangle with the same gradient, ≈7 % H tall, digits in dark purple, cap ≈3.5 % H, centred under the wordmark.
- Lion logo white, ≈18 % H, centred above.
- No supers on the footage; brand text only on cards and on the in-shop TV.

Colour/grade: commercial grade for the barbershop (warm wood, tungsten, shallow focus); match footage natural; graphic layer = league purple (#37003c family, here #3d0a6b–#7a2be2 diagonal stripes) + neon green (#00ff85 family) + lime/cyan gradient. Cut-outs: white torn-paper border, duotone lime echo copies stepping back.

Camera/shots: scripted comedy scene (barber, client, onlookers), close-ups and reaction shots; macro inserts of crests and tattoos; broadcast match footage; stills of players turned into animated cut-outs; a phone screen recording.

Transitions: hard cuts; a whip-pan blur into the montage (≈33 s); the ball flying into lens wipes to the end card (55–56 s); cut-out pops on cuts.

Sound: dialogue scene + music + match atmosphere. Measured: very loud, integrated −11.0 LUFS (whole upload), true peak +0.1 dBTP; momentary max −8 to −10 LUFS through the montage, peak −3 at 16 s right after a 0.35 s drop-out (15.35–15.7 s, floor −38 dB, then +32 dB); a second 0.5 s drop-out at 48.55 s before the reveal; a dip at 42–43 s (−19/−23) for a dialogue beat; 0.85 s digital silence before the logo card. LRA 8.3 LU. I did not listen; lines and music style are not described.

What makes it premium:
- A human, local story (a barbershop) carries the season promo; the football is the punchline, not the whole film.
- The brand appears inside the world (tattoos, shirts, a shop TV) before it appears as a graphic.
- One strong colour system (purple + neon) used for cut-outs, cards and wordmark.
- Two short silences (0.35 s and 0.5 s) before the two biggest moments.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- Script a 60 s scene with one setting and one hero; 6 s slow establishing shot, then 1–2 s dialogue shots.
- Logo burst: 8–10 inserts of your mark in the wild at 0.12–0.3 s (hard cuts).
- Montage: 0.3–0.6 s shots for 25 s; drop the music to silence for 0.35 s at the start (`gain 1→0` in 0.05 s, back on a hit).
- Cut-out card: PNG of a person with `filter: drop-shadow(0 0 0 #fff)` + an 8 px white outline (SVG `feMorphology dilate`), 3 echo copies behind with `filter: grayscale(1) sepia(1) hue-rotate(40deg) saturate(4)` stepping `x -9%` each, on a #00ff85 plate with darker diagonal stripes; pop in 0.15 s `back.out(2)`.
- End card: purple #3d0a6b with 6 diagonal stripes (`repeating-linear-gradient(115deg, …)`), logo 18 % H, wordmark Outfit 800 caps 170 px with `background: linear-gradient(90deg,#d6f23a,#22e3d8); -webkit-background-clip:text`, date pill 74 px tall radius 12 px; hold 4 s, then 0.8 s silence and the logo card.
- Stock queries: "barbershop customer laughing", "football fans queue street", "football tattoo close up", "football fans celebrating stadium", "paper cut out collage texture".
