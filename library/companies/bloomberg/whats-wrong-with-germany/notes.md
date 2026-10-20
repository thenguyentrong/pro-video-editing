# What's Wrong With Germany?  (Bloomberg Originals, 2026-08-21, 12:29, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=IlbPO9Vmuuo
Purpose: explainer / business documentary (reporter + economist interviews)
One-sentence point: Germany's industrial model (cars, chemicals, cheap energy, exports to China) is breaking, and growth has stalled since 2018.

First 150 s analysed (of 749 s).

Structure: beats with timestamps
- 0–1.4 s flash cold open: 5 shots of 0.25 s each (machine interiors, a lab glove, a robot arm).
- 1.4–5.8 s establishing beats: German flag over a factory chimney in smoke, worker, robot, welding at night.
- 5.8–7.8 s the reporter (Marilen Martin) in an empty concrete warehouse set.
- 7.8–10.2 s Bloomberg TV archive clip as evidence: anchor with the live "INTRADAY Volkswagen 71.28 ▼1.66 2.28 %" box and the red ticker "VW SAYS COMPETITION FROM CHINA INTENSIFYING".
- 10.2–19 s factory b-roll, then two Bloomberg headline cards over darkened footage: "BMW Offers Severance Packages to Employees to Cut 8,000 Jobs" (13 s) and "VW Eyes Cutting 100,000 Jobs and Closing Plants, Report Says" (16 s), each with byline + date and a QR code "Scan to read the full article."
- 19–32.7 s data: "Germany GDP Growth" yellow bar chart composited flat onto an aerial top-down shot of a truck yard; the chart scrolls left through the years as bars grow (13.5 s continuous).
- 32.7–36.7 s workers/laser close-ups; 36.7–39.5 s economist (Martin Ademmer) wide in the warehouse set.
- 39.5–63.5 s observational b-roll: truck stop, protest placards, chemical plant, control room, old loom, punch clock, a second interviewee, pipe bridge, welding.
- 63.5–68 s chapter title "Germany's Industrial Crisis" over a refinery behind a maize field (fade in/out ~0.5 s).
- 69–82 s VW chimneys, factory tunnel, car train, an archive Deutsche Mark banknote in a rounded inset on black, euro notes counted at an ATM.
- 82–93.6 s interview block with lower thirds (economist 82–85 s, reporter 86–88 s), tighter singles 89–93 s.
- 93.6–112 s b-roll montage (Frankfurt towers, steel mill, train, paint robots, bike lane, craftsmen, phone repair).
- 112–124 s reporter, smokestacks, third interviewee (Kamil Kowalczewski, lower third), steel ladle.
- 125–150 s "German Industrial Production" red line chart composited onto a weathered steel container; the line draws and the time axis scrolls 1996 → 2020 with labelled events ("Labor Market Reforms", "Global Financial Crisis", "COVID Pandemic") — 25 s in one shot.

Cut rhythm: 58 shots in 150 s, ASL 2.59 s, median 1.96 s. ASL per quarter 1.97 / 2.21 / 2.21 / 4.69 s. Longest 25.1 s (line chart on the container at 125 s), 13.5 s (GDP bars on aerial at 19 s), 6.4 s. Shortest 0.25 s x 4 (cold-open flashes). 12 % of shots under 1 s, 16 % over 3 s. Densest 0–10 s (10 cuts). Cuts on audio onsets 42 % vs 54 % chance (cut on picture, not on beats). The chart shots are the long holds; b-roll runs at ~2 s per shot.

Typography: (Bloomberg uses its own grotesk; closest free "Inter" / "Neue Haas"-like "Archivo" — guess)
- Headline cards: "Bloomberg" wordmark bold white ~4 % H; headline bold sans white, 3 lines centred, font ~7 % H, tight leading (~1.05); words wipe in orange first and settle to white (inferred from frames at 13 s vs 13.5 s); byline light grey ~3 % H "Tim Loh | July 29, 2026"; QR code + "Scan to read the full article." ~1.5 % H top-left. Background photo darkened ~50 % and blurred slightly.
- Lower third: no box. Name white bold ~3.5 % H with the surname in Bloomberg orange-red (wipe-on), role white regular ~3 % H ("Economist, Bloomberg Economics"); at x 10 %, y 72–80 % H.
- Chapter title: white bold sans ~6.5 % H, centred at 50 % H, sentence/title case, held ~3 s, no box.
- Charts: title bold dark grey ~3.5 % H top-left of the chart; source line ~1.5 % H ("Source: Deutsche Bundesbank"); axis labels regular ~2.3 % H right-aligned on the right; event labels in italic sans ~2.2 % H with a small leader.
- Persistent bug: white Bloomberg "B" icon top-right (x 94 %, y 9 %), ~5 % H.

Colour/grade: natural, slightly cool and desaturated b-roll; interview set = pale grey concrete warehouse, soft window light, shallow depth of field (85 mm-ish look). Chart colours: Bloomberg yellow bars (~#E8C33F) on grey concrete; crimson line (~#D0263A) with yellow/orange event dots and a dashed yellow highlight segment. Text white or near-black #333 depending on the surface. No letterbox, no grain.

Camera/shots: cinema-camera b-roll on sticks and slider (factories, robots, workers), drone top-downs as chart canvases, three-quarter interviews on two cameras (wide + tight), in-house TV archive, archive film inset, macro close-ups.

Transitions: hard cuts; chapter title fades; charts move inside the shot (scroll, draw). No whips, no flashes after the cold open.

Sound: integrated -16.6 LUFS, median momentary -16.0 LUFS, steady by quarter (-15.8 / -16.8 / -15.3 / -16.7). No gap below -50 dBFS → continuous music bed under all voice (inference). The one big breath: 65–72.5 s drops to -44 LUFS for 7.5 s around the chapter title (music/voice pulled out), then back to -14. Hits are modest (+18 dB at 35 s, +16 dB at 116.5 s) — no trailer-style slams.

What makes it premium
- Own-brand evidence: Bloomberg TV ticker clips and Bloomberg News headline cards (with byline, date and QR) prove the claim and advertise the newsroom.
- Charts live in the world: data drawn onto real surfaces (aerial yard, steel container) instead of a flat slide.
- One accent colour family (yellow/orange/crimson) on neutral, desaturated footage.
- Clean interview set (empty warehouse) repeated for every speaker = visual consistency.
- Chapter title with a 7 s audio breath — rare, so it lands.

Recipe (real footage + HTML/GSAP, Hyperframes)
- Headline card: footage `filter: blur(2px) brightness(.5)`; stack centred: wordmark `700 4vh`, headline `700 7vh/1.05 "Inter"` white with a colour wipe `background:linear-gradient(90deg,#fff 50%,#F5A623 50%); background-size:200%; -webkit-background-clip:text` animating `backgroundPosition 100% → 0%` in 0.6 s `power2.out`; byline `300 3vh #bbb`; QR `top:6%; left:5%` at 12 % H. Hold 2.5–3 s.
- Chart on a surface: shoot a static top-down or a flat wall; place an SVG chart with `mix-blend-mode:multiply` (dark text) or normal (white text) and a 4 % opacity noise; draw the line with `strokeDashoffset` over 20–25 s `ease:"none"` while the inner group scrolls `x` left at the same speed; event dots pop `scale 0 → 1` 0.25 s `back.out(2)`, italic label fades 0.3 s.
- Bars: `#E8C33F`, grow `scaleY 0 → 1, transformOrigin:"bottom"` 0.4 s `power2.out`, stagger 0.25 s, container drifts left over the full shot.
- Lower third: no box, `left:10%; top:72%`; name `700 3.5vh` white with surname in `#FF5A2C`, mask-wipe in 0.5 s; role `400 3vh`. Hold 3 s.
- Chapter title: `700 6.5vh` white centred over a wide landscape, fade 0.5 s in / 0.5 s out, duck music to ~-44 LUFS for 5–7 s.
- Pace: b-roll 1.5–2.5 s per shot, charts 13–25 s in one shot, 3–5 flash frames (6 frames each) only in the cold open.
- Mix: voice -15…-16 LUFS short-term, bed always on ~12–16 LU below, integrated ≈ -16.5 LUFS.
