# F1 2026 New Season Launch: It's All To Drive For  (FORMULA 1, uploaded 2026-02-22, 60.0 s, 16:9, YouTube / FORMULA 1 channel; campaign spot)
URL: https://www.youtube.com/watch?v=Sj58i-U0o5A
Purpose: season launch promo / brand campaign (:60)
One-sentence point: a host and the drivers pass one spoken line between them, and the season is "all to drive for".

Structure:
- 0.0–7.0 HOOK: host in a black jacket lit by red light (looks like actor Damson Idris, star of the 2025 F1 film; he is not captioned, so this is my identification), crowd, car silhouette with rim light, macro of an eye reflecting the red start lights (5.5 s), screaming fan.
- 7.0–25.0 CHAIN LINES: drivers each say a word or half-sentence to camera, 0.5–1.8 s each (Norris on the Barcelona grid 7–9.5, Hülkenberg + Bortoleto, Pérez, Bottas in Cadillac kit, Sainz, Lawson, Russell, Bearman, Gasly), intercut with a CG red car in a red studio (9, 11, 18, 20 s) and a trophy labelled "MADRID RESERVED" (14 s, the new Madrid race).
- 25.0–39.5 BUILD: fans, sparks under a car (28.5), host on a night street circuit (27, 31, 37), cockpit/onboard, more drivers (Albon, Stroll, Piastri).
- 39.5–46.0 THE BIG NAMES: Hamilton (40–41), Leclerc in front of a giant F1 logo wall (42–43.9), Verstappen (44.6–45.9). A whip pan links Leclerc → Verstappen (44.3–44.6).
- 46.0–55.0 CLIMAX: Ferrari in the gravel, team celebrating, Verstappen helmet, extreme close-up of eyes in a helmet (50), crowd, champagne (52), a champion in a neon-yellow helmet celebrating (53–54).
- 55.3–57.6 RESOLVE: host on the start grid at night under the red start lights, arms wide, says the final line straight to camera (one 2.4 s shot, the longest in the film).
- 57.7–58.2 ENDLINE: onboard car shot with "IT'S ALL TO DRIVE FOR"; 58.2–58.5 the line alone on black.
- 58.5–60.0 LOGO: red F1 logo on pure black (#000000) with two lines of legal text.

Cut rhythm: 72 shots in 60.0 s, ASL 0.83 s, median 0.70 s; 74 % of shots under 1 s, 0 % over 3 s. ASL per quarter 0.79 / 0.79 / 0.79 / 0.83 and 9–14 cuts per 10 s all the way: a completely flat, very fast rhythm (no slow-down even at the climax). Longest shots: host's last line 2.4 s, 42.6 s 2.0 s, 8.1 s 1.8 s. Two whip/smear transitions added by eye (25.15, 44.55). 17 % of cuts on an audio onset (chance 15 %): cut to the dialogue, not to beats.

Typography: almost none. Only the endline: "IT'S ALL TO DRIVE FOR" in a squared techno monospace, all caps, white, cap height 5.0 % of frame height, letter-spacing about 1 em (the line spans 84 % of frame width), centred, cut on (no animation seen at 10 fps), holds 0.8 s. Closest free match: Space Mono Bold or Share Tech Mono with letter-spacing 0.9–1.0em. Small white F1 logo bug top-left throughout (~6 % of frame width). No lower thirds, no driver names: the drivers are expected to be recognised.

Colour/grade: warm, filmic, slightly desaturated real-world footage (Barcelona daylight, paddock, night circuit) mixed with saturated F1-red studio shots (CG car, host in red light). Skin kept natural; the red appears in light and set, not as a filter. 12 % of frames mostly empty.

Camera/shots: shot like a commercial: shallow depth of field, anamorphic-looking flares, low angles on drivers, macro inserts (eye, sparks, helmet visor), handheld fan shots, CG car renders, onboard footage at the end. Lots of faces: roughly 30 of 72 shots are a face to camera.

Transitions: almost all hard cuts; 2 whip/smear transitions (25.0–25.2 push-in blur into the CG car, 44.3–44.6 whip pan). Cut to black before the logo.

Sound: dialogue-led spot over a music bed (host + drivers speaking; I did not listen, the dialogue is inferred from the many talk-to-camera shots and the flat loudness). Integrated −16.2 LUFS, LRA only 2.0 LU (the flattest of the three F1 pieces): momentary level stays between −12 and −18 LUFS for the whole minute, no drop-outs, no silence gaps. Hits at 0.5 s and 4.75 s (opening impacts). Loudest moment at 10 s (−12 LUFS).

What makes it premium:
- One spoken line split across many faces: the edit feels like a relay, so 0.7 s shots still carry meaning.
- Real access (22 drivers, paddock, podium) plus a recognisable host; no graphics needed to explain who is who.
- Endline typography is tiny-but-wide mono caps: understated, techy, very F1.
- Ends on the plainest possible logo card (red on black, legal line) after a busy minute.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Script one sentence of 15–25 words; split it into 15–20 fragments; give each fragment to a different person filmed to camera (85 mm look, f/2, low angle, red practical light behind). Cut each fragment tight to the word: 0.5–1.0 s.
- Between fragments insert 0.3–0.6 s texture shots: macro eye/visor, sparks, crowd, product detail. Keep the presenter for 4–6 returns, and give him the longest shot (2–2.5 s) at the end.
- Whip transitions: on the outgoing clip GSAP x 0 → −35 % and filter blur(0 → 24px) in 0.12 s, incoming clip from +35 % with blur 24 → 0 in 0.12 s, ease "power3.in"/"power3.out".
- Endline: Space Mono 700, uppercase, 54 px on 1080p (5 %), letter-spacing 0.95em, centred, white, appear instantly on a moving onboard shot, hold 0.5 s, cut the plate to black and hold the text 0.3 s more.
- Logo card: logo 37 % of frame width centred on #000, legal text 10 px at the bottom, 1.5 s. Mix: dialogue on top at about −16 LUFS integrated, music bed compressed, no drop-outs.
