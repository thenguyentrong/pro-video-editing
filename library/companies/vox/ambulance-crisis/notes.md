# How the US created an ambulance crisis  (Vox, 2025-06-03, 6:51 full / first 150 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=pWRlDIBoQW4
Purpose: explainer (policy/health, sponsored "presented by T-Mobile"), narrator-led with expert interviews
One-sentence point: Ambulances are not funded like fire trucks or police, so millions of Americans live in "ambulance deserts" where help takes too long.

Structure (first 150 s):
- 0.0–3.3 cold open: night drone top-down of a road, typed white caps line "LET ME ASK YOU A QUESTION." with a text cursor, then aerial of an ambulance and fire truck.
- 3.3–9.3 animated "response-time clock": big blue disc on a pale grid, an ambulance icon rides a pink hand; a pink tag counts 03:27 → 19:21 "RESPONSE TIME" while the camera punches in (cut at 5.6 s is a punch-in inside the graphic).
- 9.3–15.4 real crash-scene drone top-down, night street.
- 15.4–16.1 expert flash (Joshua Brown, MD, 0.67 s), back to the clock: now a yellow tag "08:00" and a green wedge = the target time.
- 20.7–22.2 three 0.5 s punch-ins on a red county choropleth (Washington, Oklahoma…), then 22.2–28.5 the full map with the study's real title "Number of people living in ambulance deserts by county, 2021–2022", citation "Jonk, et al. | May 2023"; yellow highlighter wipes across "ambulance deserts" word by word (24–27 s).
- 28.5–31.0 author on webcam with lower third "Yvonne Jonk / Deputy director, Maine Rural Health Research Center".
- 31.0–43.0 the report itself: "Prepared by" page (highlight on her name), cover, state maps, Executive Summary page zoomed so it runs off the right edge; the line "4.5 million people live in an ambulance desert" gets a yellow highlight (39–43 s). 7 cuts in 30–40 s = densest stretch.
- 43.0–57.0 drone shots of an ambulance on rural roads at dusk (4 shots, 4–5 s each).
- 57.0–62.0 flat illustration: ambulance on a winding road (dark navy).
- 62.0–67.5 expert grid: one, two, then three webcam interviewees side by side on black.
- 67.5–72.9 chapter title typed over the road illustration: "HOW CAN WE FIX IT?" + cursor, then Vox wordmark "presented by T-Mobile".
- 72.9–111.2 sponsor read (38.4 s, one talking-head shot with a magenta progress bar along the bottom). Excluded from the editorial numbers below.
- 111.2–121.9 b-roll: fire aerial, police car, fire-rescue crew.
- 121.9–150 flat blue explainer graphic (road, fire truck + police car, red "ESSENTIAL" rubber stamps, green "TAXES" / "INSURERS" / "PATIENTS" icons with "+$" coins), cut with expert Joshua Brown MD (lower third at 125 s).

Cut rhythm: raw 37 shots in 150 s (ASL 4.05 s). Editorial only (sponsor read removed): 36 shots in 111.7 s, ASL 3.10 s, median 2.48 s, 17 % under 1 s, 44 % over 3 s. Raw ASL by quarter 1.97 / 4.17 / 18.75 (sponsor) / 3.75 s. Cuts per 10 s: 4 3 5 7 2 2 2 1 0 0 0 3 3 3 1. The open is fast (ASL ~2 s for 40 s), then the drone b-roll settles at 4–5 s shots. Fast moments are punch-ins on the same graphic (three 0.5 s map zooms at 20.7–22.2 s) rather than new footage. Cuts on audio onsets = chance (56 % vs 56 %).

Typography:
- Typed lines (cold open + chapter title): white heavy grotesque caps, cap height ~6.3 % H, centred, with a visible text cursor "|"; typed on letter by letter, no box. Closest free: Archivo Black / Inter Black (guess).
- Chart titles: bold serif (Vox house serif; closest free Source Serif 4 Bold) ~5 % H, black on white, two lines, left aligned; citation line in sans ~2.5 % H under it ("Jonk, et al. | May 2023"). Legend bottom left in small sans.
- Highlighter: flat yellow #FFFF00 box behind the words, no rounded corners, wipes left→right over ~1 s.
- Graphic labels: monospace-like digits on pink/yellow pill tags ("13:15 RESPONSE TIME"), small caps label under the number; icon labels in spaced caps sans ("TAXES", "INSURERS").
- Lower third: same as Vox house — thin yellow rule left, bold serif name ~5 % H, small sans role.
- Bug: white "Vox" serif wordmark top right; replaced by "PRESENTED BY T-Mobile" (white) during sponsored parts.

Colour/grade: two worlds. Live footage: night drone, dusk drone, natural grade, a bit cool. Graphics: flat vector, limited palette per scene — clock scene royal blue #2362A9 disc on pale ice-blue #E1F6F7 grid, pink #F1627E tags, a yellow tag for the target value, green wedge for target; maps in a white field with a 5-step red sequential scale (pale pink → dark red); later scene on the same solid blue #2362A9 with mint-green #2CE67B icons, a charcoal road #2E302D and red stamps; the chapter card sits on dark navy #213745. Documents are shown as real grey-on-white PDF pages, slightly blurred toward the edges.

Camera/shots: lots of top-down drone (night and day), aerial ambulance tracking shots; experts are remote webcam captures (home office, bookshelf) used honestly, plus one in-person interview (doctor in white coat, two-camera). No host on camera in this one; the voice is a narrator.

Transitions: hard cuts; inside graphics the "cut" is a scale punch-in (clock 5.6 s, map 20.7/21.2/21.7 s). Soft detector fires mainly on graphic moves (63.2 s grid assemble, 144.9 s graphic slide). No dissolves between footage.

Sound: integrated −18.8 LUFS, loudest −10.4 LUFS momentary at 117 s (fire b-roll). 50 ms RMS: median −26.1 dBFS, p10 −40.6 → a quiet bed ~14 dB under the voice. One true silence: 1.1 s at −70 dBFS (71.75 s) between the chapter card and the sponsor read; 1.0 s dip at 5–6 s inside the clock graphic. Sharp SFX-like rises of 30–35 dB at 31.3, 38.5, 43.3, 51.2 s (document page and drone cuts) — probably whooshes/sound design (guess; I cannot hear it).

What makes it premium:
- The proof is the primary source: the actual study map, its title and citation, the author on camera, then the report page with the one sentence highlighted.
- The highlighter is yellow and used on exactly the words the narrator says, nothing else on the page is marked.
- Graphics turn a number into a picture you can feel (response-time clock that keeps running) before any chart.
- Typed questions with a cursor work as chapter breaks; the same font appears only twice.
- Expert credibility via plain webcam frames rather than staged interviews — fast and honest.

Recipe (real footage + HTML/GSAP):
- Document shot: render the real PDF page to PNG at 2× and place it at `width:150%` so it runs off the right edge; `filter:blur(0)` on the line you discuss and a second copy with `filter:blur(2px)` masked to the edges (`mask-image: linear-gradient(90deg, #000 70%, transparent)` inverted). Slow push `scale:1→1.05, duration:4, ease:'none'`.
- Highlighter: absolutely positioned `<span>` behind the words, `background:#FFFF00`, `transform-origin:left`, `gsap.fromTo(hl,{scaleX:0},{scaleX:1,duration:0.9,ease:'power1.inOut'})` timed to the spoken words; text stays black on top (`mix-blend-mode:multiply` on the highlight).
- Chart card: white ground, title `700 5vh 'Source Serif 4'`, citation `500 2.4vh Inter` "Author, et al. | Month Year", choropleth from real data with a 5-step red ramp (#FBE3E4, #F4A3A8, #E8565F, #C81E2B, #7E0F19). Punch-in sequence = three `scale` sets of 0.5 s each (hard, no ease) before the full map.
- Typed chapter line: `font:900 6.3vh 'Archivo Black'; color:#fff; text-transform:uppercase`; reveal characters with `gsap.from(chars,{opacity:0,duration:0.01,stagger:0.045})` plus a blinking `|` (`repeat:-1, yoyo:true, duration:.4`). Over drone footage darkened by 25 %.
- Metric clock: SVG disc #2362A9 on #E1F6F7, pink pill #F1627E with `font:700 5vh 'IBM Plex Mono'` counter driven by `gsap.to(obj,{val:1161,duration:5,ease:'none',onUpdate})` (mm:ss).
- Pacing: 2 s shots in the first 40 s, then 4–5 s b-roll; drop all music for ~1 s before a chapter/sponsor change.
