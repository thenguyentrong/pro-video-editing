# 2026 NBA Finals | History Is Calling  (NBA, uploaded 2026-06-03, 30.5 s, 16:9, YouTube / NBA channel)
URL: https://www.youtube.com/watch?v=o6VOHPzR1-8
Purpose: tune-in promo (:30) for Game 1 of the Finals, the same spot that runs on the network
One-sentence point: two team crests become trophies, both teams' stars flash past, and the card tells you the night, the time and the channel.

Structure (cut times from metrics.json, verified on the sheet):
- 0.0–0.5 black, music in at 0.5 s.
- 0.5–6.0 HOOK, CG: a Knicks centre-court crest on a wood floor that rises into a gold trophy-shaped plinth (one slow camera move), hard switch at 3.3 s to the same move with the Spurs crest. Two teams = two identical CG shots, 2.8 s each.
- 6.0–10.5 BUILD: four atmosphere shots (locker-room huddle, huddle with a purple grade, low-key face, star praying hands), 0.9–1.3 s each.
- 10.5–26.3 ACTION: 19 shots, 0.13–1.5 s, game action alternating team A / team B; overhead rim-cam dunks, floor-logo camera, wide arena shots; densest 10–20 s (12 cuts).
- 26.3–30.5 END CARD 4.2 s: "Finals" wordmark, "GAME 1", "KNICKS vs SPURS", "TONIGHT 8:30 PM ET", network bug; trophy right; thin gold court lines on black.

Cut rhythm: 26 shots in 30.5 s, ASL 1.17 s, median 0.88 s, 65 % under 1 s, 51 shots/min. ASL per quarter 1.90 / 0.85 / 0.69 / 1.52 (last includes the 4.2 s card). Cuts per 10 s: 5, 12, 8. Four cuts (3.27, 7.27, 8.48, 9.64) were found only by the adaptive detector and added after checking by eye.

Typography (end card only; no text over action):
- "Finals" = brand script wordmark beside the league logo, ≈12 % of frame height. Closest free: a bold upright script such as "Yellowtail" (only for mock-ups; the real one is a logo).
- Teams: condensed bold caps, cap ≈9 % of frame height, gold with a light top-to-bottom gradient, small "vs" in lower case at ≈4 %. Closest free: Oswald 700 or Barlow Condensed 800.
- "GAME 1" and "TONIGHT 8:30 PM ET": same family, white, cap ≈2.7–3 %; time in heavier weight than the label.
- Everything centred on the left 55 % of the frame; trophy fills the right side at ≈60 % of frame height.
- Animation: the card arrives as one hard cut; only a soft glow moves.

Colour/grade: game footage stays natural but warm and contrasty; atmosphere shots get one colour each (purple, deep red/orange haze). End card black + gold (#c8b07a-ish) only, gold court lines at ≈1 px.

Camera/shots: CG floor crest with a slow crane; broadcast action from the main camera, rim-cam overhead (looks straight down into the hoop), floor-logo low angle, slow-motion celebrations. No interviews, no voice lines.

Transitions: hard cuts only; one hard switch between two identical CG moves; end card on a hard cut.

Sound: one trailer-style cue (whether a voice-over sits on top was not verified), music starts at 0.5 s and stays flat: −13 to −18 LUFS momentary every second, LRA 3.3 LU, integrated −16.9 LUFS, true peak −6.0 dBTP. Loudest 0.5 s at 26.8 s = the end card arrival, then a 2 s fade (−21 at 29 s, −33 at 30 s). Cuts are not on onsets (14 % vs 13 % chance). I did not listen; the music character is a guess, levels are measured.

What makes it premium:
- Symmetry: team A and team B get the same CG shot, the same number of action shots, alternating.
- Brand world first (CG crest → trophy) for 6 s, then only real game footage.
- One-colour end card (black + gold) with a strict hierarchy: brand → game → teams → time → network.
- The loudest point is the card, so the information lands on the peak.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- 0–6 s: two identical CG or photo moves (a team crest as an SVG laid on a wood-floor plate, CSS `perspective:1200px; rotateX(55deg)`, camera move `scale 1.0→1.25`, `y 0→-8%`, 2.8 s `power1.inOut`); hard cut between them.
- 6–10 s: four atmosphere clips of ≈1.1 s, each graded to one colour (purple `#5a2a8a` overlay at 35 % `mix-blend-mode:color`).
- 10–26 s: 18–20 action clips, 0.6–1.0 s, alternating sides, 12 cuts in the busiest 10 s; one 0.13 s flash shot for energy.
- 26–30.5 s: end card. Background #000 with thin gold court lines (SVG stroke 1.5 px #b89b5e, 60 % opacity); wordmark 12 % H; team line Oswald 700 caps 96 px (≈9 % cap) with `linear-gradient(#efe0b8,#b8975a)` text fill; label lines 30 px white; trophy image right at 60 % H. Card on a hard cut at the music peak, 4 s hold, music fades 2 s.
- Stock queries: "basketball dunk slow motion arena", "basketball court overhead hoop", "team huddle locker room", "athlete portrait dark arena light".
