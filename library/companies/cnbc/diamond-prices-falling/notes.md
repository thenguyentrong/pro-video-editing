# Why Diamond Prices Are Falling So Fast  (CNBC, uploaded 2026-09-27 per yt-dlp, 4:26, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=xrg6QCGzQGc
Purpose: explainer (business-news explainer, reporter-hosted, CNBC digital format)
One-sentence point: Lab-grown stones and weaker demand have pushed natural diamond prices to multi-year lows, and the big miners are cutting output.

Analysed: the full film (266 s, including a ≈11 s end card).

Structure:
- 0.0-11.4 cold open: one animated line chart "Price of 1-carat diamonds" on the house dark-teal ground, the line draws and falls; source line bottom left (11.4 s, one shot).
- 11.4-15.1 reporter stand-up on the balcony of CNBC's newsroom, lower third.
- 15-31 first evidence: diamond macro, a headline card (outlet name, byline, date, headline with one phrase on a gold highlight, 6 s), the diamond district, tweezers, reporter.
- 31.4-39.8 series title: "CNBC | Are diamonds losing their luster?" over a blurred macro of a ring (≈8 s with the move).
- 39.8-61.5 mechanism: lab footage with labels, then a 16.6 s 3D animation of a growth reactor (longest shot).
- 61-133 the market: trays of stones, store fronts, a wedding-industry report page with one highlighted sentence, two experts on clean interview set-ups with lower thirds, more headline cards; the reporter returns every 20-30 s for 3-5 s.
- 133-182 supply: headline card about conflict diamonds, a grading lab, expert, mine aerials with labels, a world map of the top five producers (166-178 s, pill labels with percentages).
- 182-224 the miners: headline cards (Reuters, a trade title), De Beers store, a "30 %" label over a stone, a bar chart of one miner's output (219-224 s).
- 224-255 close: reporter, last headline card, expert, hands with rings.
- 255-266 end card: CNBC logo, credits block, subscribe line.

Cut rhythm: 45 shots in 266 s, ASL 5.91 s, median 5.09 s, 0 % under 1 s, 84 % over 3 s, 10.2 shots/min (scene detector + 1 verified cut; headline cards and charts are single shots with internal motion). ASL per quarter 5.54 / 5.11 / 5.54 / 6.04 s: completely even. Cuts per 10 s: 0-3, never more. Longest 16.6 s (3D reactor), 13.4 s (end card), 12.0 s (map). Shortest 1.54 s.

Typography (CNBC digital system):
- Bug: "CNBC" wordmark top right, white, ≈3.8 % H, always on.
- Font: geometric sans (CNBC uses a Proxima-Nova-like face; closest free "Montserrat" / "Figtree") for everything.
- Lower third: gold vertical bar (≈#F2B400, ≈0.6 % W wide, ≈10 % H tall) left of the name; name bold white ≈5.5 % H; role/outlet regular ≈3.3 % H ("CNBC"). Placed at x ≈55 % W, y ≈73-85 % H for the stand-up; for experts flush right with the bar on the right.
- Headline card: dark-teal ground; gold vertical rule at x ≈15 % W; outlet name in tracked caps ≈2.8 % H; byline + date ≈2.4 % H between two thin white rules; headline bold ≈6.5 % H, 2-3 lines, one phrase on a gold highlight box with dark text. Held 4-6 s with a slow push.
- Series title: logo | gold bar | two-line question in bold white ≈8 % H, centred over blurred footage.
- Charts: title bold white ≈5 % H centred top, unit/date range ≈3 % H under it; rounded panel slightly lighter than the ground; cyan line/bars (≈#3EC1E6) with a glow; y-axis labels on BOTH sides; source + note bottom left in grey ≈2 % H under a short rule.
- Map: blue world map in a rounded cyan-outlined panel; producers filled gold; white pill labels "Country | %" with leader lines.

Colour/grade: house ground = dark teal radial gradient (≈#0E4A5C centre to #06202B edge); accents gold #F2B400 (highlight, bars, map fills) and cyan #3EC1E6 (data); footage clean and bright, interviews neutral. No grain, no letterbox.

Camera/shots: reporter stand-ups in the newsroom (locked medium), clean two-camera expert interviews (medium + close), b-roll of products/stores/labs, 3D animation for the process, aerials, screen-captured documents.

Transitions: hard cuts; cards and charts open with a short push-in (≈1.05× over the hold, judged at 1 fps). No whips, no dissolves found.

Sound: integrated -24.0 LUFS, LRA 9.2 LU, true peak -5.7 dBTP; median RMS -33.5 dBFS. Reporter VO over a soft music bed; 10 short drop-outs (0.3-0.6 s) between sentences, the clearest at 222.55 s (0.6 s) before a +41.5 dB re-entry. Cuts not on onsets (45 % vs 58 % chance).

What makes it premium:
- One branded graphics world (dark teal + gold + cyan) for chart, map, headline and title, so evidence from many outlets looks like one film.
- Other outlets' reporting is quoted as clean headline cards with outlet, byline and date, the key phrase highlighted.
- The reporter is a host, not a subject: 3-5 s stand-ups between pieces of evidence.
- Calm, even pacing (ASL 5-6 s in every quarter) that lets each number be read.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Ground: `background:radial-gradient(ellipse at 50% 30%,#0E4A5C 0%,#082F3B 55%,#06202B 100%)`.
- Headline card: `.hc{position:absolute;left:15%;top:28%;width:58%;border-left:.6vh solid #F2B400;padding-left:3vh}` `.src{font:600 2.8vh Montserrat;letter-spacing:.2em;text-transform:uppercase}` `.by{font:500 2.4vh Montserrat;border-top:1px solid #fff9;border-bottom:1px solid #fff9;padding:1vh 0}` `.hl{font:700 6.5vh/1.2 Montserrat}` `.mark{background:#F2B400;color:#0B2530;padding:0 .6vh}`; push `scale 1→1.05` over the 5 s hold.
- Lower third: `.lt{border-left:.6vh solid #F2B400;padding-left:1.6vh}` `.n{font:700 5.5vh Montserrat}` `.r{font:500 3.3vh Montserrat}`; slide 2 vh from the bar in 0.3 s, hold 3-4 s.
- Chart: panel `background:#0F5366;border-radius:1.5vh`; line `stroke:#3EC1E6;stroke-width:.5vh;filter:drop-shadow(0 0 .8vh #3EC1E6)` drawn by `strokeDashoffset` over 6-8 s; source `font:400 2vh Montserrat;color:#9FB6BE`.
- Pacing: shots 4-6 s, max 3 cuts per 10 s; one 3D or chart shot of 11-17 s per minute; reporter 3-5 s every 20-30 s.
- Mix: VO ≈-20 LUFS short-term, bed ≈15 dB under; 0.3-0.6 s gaps between paragraphs; master -24 LUFS (web: -16).
