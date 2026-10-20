# Formula 1: Drive to Survive - Season 8 | Official Trailer | Netflix  (Netflix, 2026-02-12, 2:04 file = 113.8 s trailer + 10 s YouTube end screen, 16:9, YouTube / Netflix channel)
URL: https://www.youtube.com/watch?v=T3nrpj38zSk
Purpose: trailer for a sports documentary series (season 8)
One-sentence point: in the sport's 75th year a wave of rookies arrives, a champion team is in turmoil and three drivers fight for the title; the new season is out February 27.

Structure (0–113.8 s):
- 0–8 COLD OPEN in a team party / garage: magenta and blue club light, phones filming, a rookie close-up. Netflix series bug top-left ("FORMULA 1: DRIVE TO SURVIVE SEASON 8" with a red rule) and the N top-right, then "NETFLIX" wordmark top-right from ≈5 s.
- 8–16 THE WORLD: aerial of a harbour circuit city, a speedboat, paddock walks, a train with drivers. 1–1.5 s shots.
- 16–24 ROOKIE BEAT: sit-down portraits on a black studio void; 7 shots of 0.16–0.5 s at 17.0–17.6 s (rookies clapping slates, side profiles against a light grid), then 1-second smiles at camera.
- 24–37 LIFESTYLE + STAKES: car rides, fans, a helicopter over a capital city (29–31 s), a team boss on the pit wall, a tennis court.
- 37–56 RACING: onboard and track-side cars, a Ferrari halo POV, a street circuit, a rain crash (55 s). Interviews on black intercut.
- 55.7–56 dip to black; 56–61 STORM: dark sky over a skyline, palms in wind (a tone change).
- 61–70 TURMOIL: a team principal in profile on black, a reflection macro in a driver's sunglasses (62–64, 2.8 s, one of the longest shots), a car sliding, the champion looking down; 69.2 dip to black.
- 70–100 TITLE FIGHT MONTAGE (densest: 15 cuts in 90–100 s): starts, podiums, jets, a desert, a pool, hugs, a team boss shouting, burnout smoke, celebrations.
- 100.8–101.3 black; 101–107 BUTTON: quiet interview of a former team principal, then a wide of him alone in a dark studio with the lights and stands in frame (105–107); a 0.85 s drop to -54 dB at 104.45.
- 107.2–110.2 TITLE over a top-down pit-stop shot: "FORMULA 1 / DRIVE TO SURVIVE / SEASON 8" in white geometric caps, letters wiping on, 3.0 s.
- 110.2–112.4 "ONLY ON NETFLIX / FEBRUARY 27" on magenta-purple light bars; 112.4–113.8 N sting; sound ends 113.3.

Cut rhythm: 102 shots in 113.8 s, ASL 1.12 s, median 1.00 s (adaptive detector). ASL per quarter 1.05 / 1.05 / 1.19 / 1.05 s: flat and fast the whole way. 46 % of shots under 1 s, only 1 % over 3 s; shortest 0.16–0.2 s (slate flashes at 17.1–17.4), longest 3.04 s (title) and 2.76 s (sunglasses macro). Cuts per 10 s: 6, 13, 8, 11, 9, 7, 5, 11, 8, 15, 6. 36 % of cuts on an audio onset vs 31 % by chance (loose beat cutting; dialogue lines decide most cuts).

Typography:
- Series bug (first ≈5 s): white sans caps, 2 lines, cap ≈1.8 % H, with a thin red vertical rule, top-left (x ≈3 %, y ≈4–7 %); N monogram top-right. Then "NETFLIX" wordmark (condensed bold caps, cap ≈3 % H, grey-white) top-right on every footage shot.
- Title: show logo in wide geometric caps (closest free: Montserrat 600 / Outfit 600), 3 lines, "FORMULA 1" cap ≈6 % H, "DRIVE TO SURVIVE" ≈4.5 % H, "SEASON 8" ≈3 % H, centred at y ≈40 %, over footage, letters revealed by a wipe/mask in ≈1 s.
- Date card: "ONLY ON NETFLIX" light caps ≈3 % H over "FEBRUARY 27" bold ≈7 % H, centred, on Netflix light bars.
- No names or lower thirds for anyone: the audience is expected to know the drivers; the reveal is in the faces.

Colour/grade: punchy and saturated; club magenta/blue in the open, clean daylight paddock, studio interviews on a black-grey void with a single soft key, storm-blue mid-section. Full 16:9, no letterbox.

Camera/shots: observational handheld in garages, paddocks and homes; studio sit-down portraits on black (two set-ups: frontal close-up and profile against a light grid); aerials (helicopter, city, desert); race broadcast-style track shots and onboards; macro details (sunglasses reflection, helmet). Lots of people looking at people.

Transitions: hard cuts; three short dips to black (0.3–0.5 s at 55.7, 69.2, 100.8) mark the act changes; mask wipe for the title; light-bar wipe into the N.

Sound: (I could not listen; from level data and picture.) Integrated -15.1 LUFS, LRA 7.4 LU, true peak -1.7 dBTP. Body steady at -13…-20 dBFS (2 s RMS); dialogue from interviews over music. Two clean drop-outs: 0.85 s to -54 dB at 104.45 (before the last interview line) and 0.75 s to -52 dB at 110.95 (before the date card). Biggest rise +19.7 dB at 41.8 s (race engine entry).

What makes it premium:
- Real access: studio portraits, homes, garages and the track in one rhythm, so the trailer feels like a drama.
- A dedicated micro-beat for a theme (rookies): 7 slate flashes of 4–5 frames each.
- Act changes marked by short dips to black and a weather change (storm) rather than cards.
- Ends on a quiet human button (one man alone in a studio) before the title.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- 100 shots for 114 s: 40 % observational handheld, 20 % studio portraits on black, 25 % action, 15 % aerial/macro. Cut 0.8–1.3 s; let dialogue lines decide the cut point.
- One theme micro-beat: 6–8 shots of 4–5 frames (0.16–0.2 s) of the same action (slates, helmets on), then 1 s smiles.
- Act breaks: 0.3–0.5 s dip to black, then a mood shot (storm sky, empty track) of 2–3 s.
- Before the title: 0.8 s drop to ≈-50 dBFS, one quiet line, a 2 s wide of the speaker alone.
- Title over action (top-down shot): `font: 600 6vh Outfit; letter-spacing:.05em` + smaller lines, reveal with `clip-path: inset(0 100% 0 0) → inset(0 0 0 0)` 0.8 s `power2.out`, hold 2 s. Date card 2.2 s. Master -14 to -15 LUFS.
- Corner bug first 5 s: `600 1.8vh Inter`, uppercase, 2 lines, 3 px red rule left, top-left.
- Stock queries: `race car pit stop top down`, `helicopter over city aerial`, `studio interview black background portrait`, `storm clouds city skyline timelapse`.
