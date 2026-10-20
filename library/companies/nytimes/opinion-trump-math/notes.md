# The Damage of 'Trump Math' Is Adding Up  (NYT Opinion, 2026-05-15, 7:39, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=-aJ1WHR5Q9s
Purpose: explainer / video op-ed (argued essay, narrated)
One-sentence point: Federal data quietly guides everyday life (weather, roads, medicine, food), and the administration is deleting or stopping that data.

First 150 s analysed (of 459 s).

Structure: beats with timestamps
- 0–2 s cold open: a split-flap counter flips "13" → "2" → "?" on black (numbers theme set in 2 s).
- 2–15 s glitch montage of archive and data: Obama, a TV wall, scrolling IP-address numbers, Trump on the phone (heavy RGB split), a glass crack on black (9.5 s), data terminals, a weather map, a number matrix. 14 cuts in 15 s.
- 15.5–35 s the central metaphor: an iridescent 3D swim-goggle render on black; footage plays inside the lenses with one big stat each ("135,000 / COWS IN HAWAII", "54 / ICE JAMS IN THE LAST SEVEN MONTHS").
- 35–69 s POV "through the goggles": the lens rim stays visible at the frame bottom with colour fringing; daily-life stock clips (care home, pilgrims, farmer, weather balloon, "Rain stopping in 10 minutes" phone alert, GPS, warehouse, CVS bus stop, school book, lab, spreadsheet, highway, construction) — what the data does for you.
- 69–81 s the goggles fog over (clouds), then go dark (78–81 s, empty rim on black).
- 82–85 s title ident: small "The New York Times" + "OPINION" in serif caps, centred on near-black.
- 85–106 s the turn: glitched rally footage, a golden Trump statue (slow push 91–97 s), Trump shouting at night with a flag; typed text "STEP 1: / CONTROL / ALT / DELETE" in a dot-matrix font (102–106 s).
- 106–129 s the evidence: RGB-split signing footage, a wall of agency logos (EIA, BLS, NCHS, BEA, ERS, BJS, CDC, IRS SOI), scrolling record lists, an FBI "Seeking information" poster, then real web pages: DOJ "Page not found", DAWN dashboard breaking up, EPA Greenhouse Gas Reporting Program page, a "Proposed Reconsideration of the GHGRP" text card, a USDA survey form double-exposed over farm workers, Federal Register "Discontinuance of Information Collections".
- 130–150 s consequences: lab stock, top-down traffic, Capitol at dusk, State of the Union (Trump close-up 140–148 s), pharmacy shelves.

Cut rhythm: 55 shots in 150 s, ASL 2.73 s, median 2.07 s (one false cut on a text-only change at 104.84 s removed). ASL per quarter 2.50 / 2.08 / 4.69 / 2.21 s. Longest 22.5 s (the goggles render at 15.5 s — one continuous 3D shot with footage changing inside the lenses), 9.0 s (fog sequence at 73.5 s), 8.8 s (night speech + typed text at 97.9 s), 8.4 s (speech close-up). Shortest 0.30–0.40 s (glitch flashes). 31 % of shots under 1 s, 31 % over 3 s. Densest 0–10 s (8 cuts) and 110–120 s (6 cuts, the logo/list barrage). One black flash (0.63 s at 9.5 s, the glass crack). Cuts on audio onsets 55 % vs 51 % chance (cut to the voice, not to a beat).
Note: footage changing inside the goggles is counted inside the one 3D shot, so the real "image change" rate in 15–38 s is higher than the ASL shows.

Typography: (fonts guessed)
- Persistent bug top-left: NYT "T" logo + thin vertical rule + "OPINION" in serif caps, cap height ~2.5 % H, at x 3 %, y 7 % — on every frame.
- Typed card: dot-matrix / LED bold caps, centred, two lines, cap height ~6.5 % H, light grey #ddd on black, typed on per word (~0.7 s per word, 102–105 s).
- Goggle stats: number in white sans regular (Franklin-like; closest free "Libre Franklin" 400) ~5.5 % H, label in caps ~2.5 % H under it, centred in the lens.
- Title ident: tiny NYT blackletter wordmark over "OPINION" serif caps (Cheltenham-like; closest free "Source Serif 4" 600), ~3 % H, centred on #111.
- Documents: real web pages and PDFs, cropped to the headline area; no added highlighter.

Colour/grade: two worlds. "With data": warm, saturated stock, with prismatic/chromatic fringing at the lens edge. "Without data": heavy RGB channel split (red/green/blue offsets of ~10–20 px at 480p), scan lines, glitch tearing, cyan/magenta casts. Documents are bright white web pages that also glitch. No letterbox.

Camera/shots: almost no original filming in this window — archive news, stock (nursing home, lab, aerial traffic), screen captures of government web pages, a 3D goggle render with footage composited inside, typed text cards. Slow pushes on stills (golden statue).

Transitions: mostly hard cuts; glitch/tear transitions and RGB-split pops in the cold open and the evidence section; a dissolve-like fog-out inside the goggles (69–78 s); one 0.6 s black flash with a crack. soft.py flags 29 soft moments, mostly the fog and glitch moves.

Sound: integrated -18.8 LUFS, median momentary -18.9 LUFS. Pauses only fall to -34…-38 LUFS (19 drop-outs of 0.5–3 s) and only 8 gaps go below -41 dBFS → a continuous music/sound-design bed sits ~15–20 LU under the voice (inference). Loudest -10.9 LUFS at 112 s (the logo barrage: SFX hits +23…+34 dB rise at 106–113 s). Glitch SFX hits at 5.9 s and 10.6 s (+27 dB). Biggest pull-back: 83.5–86.5 s (3 s at -38 LUFS) for the OPINION title.

What makes it premium
- One physical metaphor (goggles = public data) carried for 60 s, then taken away; the argument is visual, not just spoken.
- The "turn" is shown with real evidence: actual government pages ("Page not found", Federal Register notice), not invented graphics.
- Strong grammar for good vs bad: clean warm footage vs RGB-split glitch.
- The title card arrives late (82 s) after the hook — cold open first, brand second.
- Typed instruction "CONTROL / ALT / DELETE" as the one big text moment; everything else stays small.

Recipe (real footage + HTML/GSAP, Hyperframes)
- Bug: `position:absolute; left:3%; top:5%; font:600 2.5vh "Source Serif 4"; letter-spacing:.06em; color:#fff; opacity:.9` + 1 px vertical rule.
- Glitch state: three copies of the video in `mix-blend-mode:screen` with `filter` channel masks (or one canvas shader), offset x ±1.2 % / 0, animate offsets with `gsap.to(..., {x:"random(-2,2)%", duration:.06, repeat:8, yoyo:true, ease:"steps(1)"})`; add a scan-line `repeating-linear-gradient(0deg, rgba(0,0,0,.25) 0 1px, transparent 1px 3px)`.
- Goggle metaphor: transparent PNG/WebM render of the object over #000, footage inside via `mask-image` of the lens shape; stat centred in the lens: number `400 5.5vh "Libre Franklin"`, label `500 2.5vh` caps, fade up 0.4 s `power2.out`, hold 2–3 s.
- Typed card: dot-matrix font (e.g. "DotGothic16" or a LED font) caps `700 6.5vh`, `#ddd` on `#000`; reveal per word with `gsap.from(words, {opacity:0, duration:.01, stagger:.7})`.
- Document evidence: screenshot of the real page cropped to the headline, `scale 1 → 1.04` over 2 s `none`; to show deletion, run the glitch state for 0.3 s then cut.
- Double exposure: form PNG at `opacity:.55; mix-blend-mode:screen` over the photo, slow drift x -1 % over 2 s.
- Mix: voice -16…-18 LUFS short-term; bed 15–20 LU under; glitch SFX hits up to +25 dB rise; drop the bed ~3 s before the title card.
