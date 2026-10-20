# How Satellite Images of Big Bend Contradict Border Agency Claims  (The New York Times — Visual Investigations, 2026-09-04, 6:00, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=QX2fq6RsibQ
Purpose: explainer / investigation (reporter at his desk walks through the evidence)
One-sentence point: Satellite images show border construction (roads, barriers) inside and near Big Bend National Park, although the agency told a court nothing was being built.

First 150 s analysed (of 360 s).

Structure: beats with timestamps
- 0–8.4 s cold open: reporter (Christoph Koettl) at his desk, two monitors of grey satellite imagery behind him, talking to camera (wide), then a closer angle.
- 8.4–21 s verité multi-cam: profile, back-of-head over-the-shoulder on the monitors, through-the-glass wide, hand pointing at the screen.
- 21–26 s title card: "VISUAL INVESTIGATIONS" label + "What Satellite Images Show About Construction in Big Bend" in white boxes over a 1948 archive aerial photo (date "7-30-48" burned in, film edge visible).
- 26–43.8 s satellite evidence: archive aerial → screen recording on his monitor → hand on the screen → full-frame grayscale satellite where a new road is traced as a white line (39–43 s).
- 43.8–53 s reporter interview, lower third 45–49 s (box sits beside him, right of centre).
- 53–77.7 s pointing at monitors: wide, OTS, the finger on the satellite image (full-frame push at 69–72 s), reporter explaining with his hands.
- 77.7–105.6 s one map shot (27.9 s): NYT basemap, green park polygon, satellite tiles drop onto the map, orange diamond markers + leader lines "Area 1–4", then a pull-out to a US–Mexico locator map.
- 105.6–110 s reporter.
- 110.3–123.8 s second map: the border line, a crimson "Patrol road" line draws along the park edge, blue "Vehicle barriers" segments appear, area labels return; "Source: Customs and Border Protection / Graphic: The New York Times" bottom-left.
- 123.8–135.6 s the court papers: reporter picks up a printed filing from a green folder on his desk, reads it (close-ups of paper and hands).
- 135.6–150 s the documents digitally: court exhibit pages (Case 3:26-cv-01099) pillarboxed on black, scroll/zoom to emails, key sentences in yellow highlighter ("Does the government still intend to provide us with 30 days notice before construction", "Yes, we still plan to provide notice", "no dates have been set for installation of vehicle barrier …").

Cut rhythm: 31 shots in 150 s, ASL 4.84 s, median 2.87 s. ASL per quarter 3.41 / 3.41 / 7.50 / 5.36 s. Longest 27.9 s (map at 77.7 s), 14.4 s (documents at 135.6 s), 13.5 s (route map at 110.3 s). Shortest 1.13 s. 0 % under 1 s, 45 % over 3 s. Cuts on audio onsets 50 % vs 59 % chance (not cut to music). The first half is people + screens at ~3.4 s per shot; the second half is long graphic holds.
Note: each map/document sequence is one continuous animated shot (zooms, draws, highlights inside it).

Typography: (fonts guessed — NYT Cheltenham/Franklin; closest free "Source Serif 4" + "Libre Franklin")
- Title card: label "VISUAL INVESTIGATIONS" black caps sans, tracked ~0.08em, ~2.5 % H, on a white box; title bold serif black on white boxes (one per line, 3 lines), font ~5.4 % H, left x 8 %, y 60–87 % H. Held ~5 s.
- Lower third: same white-box system, name bold serif ~3 % H + role caps sans ~1.4 % H ("VISUAL INVESTIGATIONS REPORTER"), placed in empty space next to the subject (here right of him at x 57–70 %, y 50–58 %), not in a fixed corner.
- Map labels: country names grey caps tracked ~2.7 % H ("UNITED STATES", "MEXICO"); park name white bold ~2.8 % H on the green; feature labels bold in the line colour (crimson "Patrol road", blue "Vehicle barriers") ~2.8 % H; marker labels black bold ~2.8 % H on leader lines.
- Source line: ~1.3 % H grey, bottom-left, two lines ("Source: … / Graphic: The New York Times").
- Documents: the real page typography; highlight = flat yellow (#FFE600-ish) bar behind the sentence.

Colour/grade: neutral, soft office daylight, black shirt + grey walls; a red mug the only warm spot. Satellite imagery kept grayscale/natural. Map palette: pale cream-green terrain basemap, park fill mid green (~#8CC063), patrol road crimson (~#A3122E), barriers blue (~#3D5BA9), markers orange-red diamonds (~#F05A23) with thin black leaders. Documents white on black pillarbox.

Camera/shots: 3 cameras on the reporter (wide, close, profile/OTS), shallow focus, slight handheld drift; inserts of hands pointing at monitors and handling paper; screen captures of satellite tools; archive aerial film scan; animated maps; scanned court exhibits.

Transitions: hard cuts; inside the maps: tiles drop and scale, lines draw, camera pulls out; documents scroll and zoom. No dissolves, no whips.

Sound: integrated -17.0 LUFS, median momentary -16.2, flat by quarter (-16.3 / -15.9 / -16.4 / -16.6). Pauses dip to -28…-44 LUFS; the 10 short gaps floor at -40…-48 dBFS (never near-silent) → a quiet bed or room tone stays under the voice (inference; softer use of silence than the Iran weapon piece). Biggest rise +29 dB at 71.5 s (after the full-frame satellite push).

What makes it premium
- The method is the story: the reporter at his real desk, pointing at the pixels, then holding the printed court filing.
- Evidence chain in order: archive 1948 aerial → today's satellite → map context → official court emails that contradict it.
- Maps are restrained: 3 data colours (green park, crimson road, blue barriers) + orange markers, everything labelled directly, source line always visible.
- Long holds (28 s map) let viewers read.
- Yellow highlighter used only on the documents, only on the exact sentence.

Recipe (real footage + HTML/GSAP, Hyperframes)
- Shoot: reporter at a desk with real screens; 3 angles (wide 35 mm, close 85 mm, OTS on screens); inserts of a finger touching the screen and paper handling.
- Title card over archive: white boxes `background:#fff; padding:.15em .35em; display:inline-block`; label `600 2.5vh "Libre Franklin"; letter-spacing:.08em; text-transform:uppercase`; title `700 5.4vh/1.15 "Source Serif 4"; color:#111`; left 8 %, top 60 %; boxes reveal line by line `clipPath inset(0 100% 0 0) → inset(0 0 0 0)` 0.4 s `power2.out`, stagger 0.12 s.
- Map: static basemap image (cream/sage), park polygon `fill:#8CC063`; satellite tiles drop `from {scale:1.3, opacity:0}` 0.5 s `power2.out`; markers = rotated squares `#F05A23` 1.4 % H with 1 px black leader lines drawn `scaleY 0 → 1` 0.3 s; labels `700 2.8vh` black.
- Route lines: SVG paths `stroke:#A3122E; stroke-width:.45vh` draw with `strokeDashoffset` over 3–4 s `power1.inOut`; barriers `#3D5BA9` segments pop 0.2 s each; label in line colour next to the line end.
- Locator pull-out: scale map group 6 → 1 over 4 s `power2.inOut`.
- Source line: `400 1.3vh #666`, bottom 4 %, left 3 %, two lines, visible for the whole graphic.
- Documents: page image centred on #000 at 95 % W; scroll `y` 0.8 s `power2.inOut` between passages; highlight `background:#FFE600` bar grows `scaleX 0 → 1, transformOrigin:"left"` 0.6 s `none` behind the line; blur the page outside the passage (`filter:blur(2px)` on a masked copy).
- Mix: voice -15…-16 LUFS, quiet bed/room tone ~-40 dBFS in pauses, integrated ≈ -17 LUFS.
