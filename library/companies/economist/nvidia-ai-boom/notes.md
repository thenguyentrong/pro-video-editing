# Nvidia is funding an AI boom. Will it trigger a financial crash?  (The Economist, uploaded 2026-09-07 per yt-dlp, 7:19 full / first 150 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=VF1JES8Sv5U
Purpose: explainer in the studio-discussion format, with one house-style chart
One-sentence point: Nvidia's revenue explosion is being recycled into its own customers, and four Economist writers debate whether that makes a crash more likely.

Structure (first 150 s):
- 0.0-6.7 hook: deputy editor Edward Carr asks the question; lower third on the RIGHT (he looks left), "Edward Carr / Deputy editor, The Economist".
- 6.7-25.4 set-up: business editor Henry Curr explains (lower third 9-13 s, right side), one 18.7 s take.
- 25.4-38.1 the evidence: full-screen Economist chart "Nvidia, quarterly revenue, $bn" (red bars on near-black, 2015-26, "Source: FactSet"), hard cut in, static, held 12.6 s while Henry talks over it.
- 38.1-56.3 the same chart stays visible on the big studio screen behind the table in the wide 4-shot (41.4-56.3 s, 14.8 s) - the chart becomes part of the set.
- 56.3-82.8 Henry again, one 26.5 s take (the longest shot).
- 82.8-139.8 debate: Edward Carr, global business writer Shailesh Chitnis (lower third 89-93 s), a side two-shot (107.7 s); takes of 3-20 s.
- 139.8-144.6 archive: Sam Altman on stage (4.8 s, no lower third, no credit in this window).
- 144.6-150 back to Shailesh, then Edward.

Cut rhythm: 17 shots in 150 s, ASL 8.82 s, median 4.88 s (cuts2, checked on the sheet and with a 5 fps strip at 24.4-26.8 s). ASL per quarter 12.5 / 9.38 / 9.38 / 4.17 s - faster in the last quarter as the debate heats up. Cuts per 10 s: 1,0,1,1,1,1,0,0,2,0,1,2,2,2,2. Longest: 26.5 s (56.3 s), 20.0 s (87.7 s), 18.7 s (6.7 s), 14.8 s wide with chart (41.4 s). 88% of shots over 3 s.

Typography (854x480 frames):
- Bug: white circle with serif "E" top-left (~7% H), stays on over the chart too.
- Lower third: black bar ~9.6% H (white serif name + Economist-red dot) over a grey bar ~6.5% H (white sans title "..., The Economist"), flush to the frame edge on the side the speaker faces away from.
- Chart: near-black background (~#121212); a red dot + bold serif title "Nvidia, quarterly revenue, $bn" top-left at y ~7% H, cap ~3.6% H, left-aligned with the bug; bars in Economist red (~#E3120B) with a hairline gap; thin grey horizontal gridlines; y-axis numbers on the RIGHT (0-100), light grey ~2.6% H; x labels "2015 16 17 ... 26" with tick marks; axis note "Financial years beginning February" centred under the axis; "Source: FactSet" bottom-left ~2.4% H. Title typeface looks like the Economist serif (closest free "Source Serif 4" Bold), labels look like Econ Sans/Milo (closest free "Fira Sans").
- No captions, no subtitles.

Colour/grade: same studio (cream walls, black shelves with gold-spined books, Economist-red table and mugs); the chart repeats the brand red on black, so the cut from studio to chart feels like the same palette. Archive clip keeps its own warm red-orange stage colour (matches by luck or by choice - guess).

Camera/shots: 3-4 locked studio cameras (single side mediums per speaker, side two-shot, wide 4-shot with the screen), one full-screen chart, one archive event clip.

Transitions: hard cuts only. The chart does not build (no animation) - it appears complete and holds.

Sound: integrated -22.3 LUFS (broadcast level). Dialogue only - 52 inter-phrase gaps with a median floor of -61.8 dBFS and some at digital silence; no music under the chart either. Loudest moment 4.5 s (-15.2 LUFS momentary, the opening question). Median momentary level -20 to -23 LUFS per 30 s, very flat.

What makes it premium:
- One chart, in house style, does the whole evidence job - and it is held long enough (12.6 s) to actually read, then kept in the background of the wide shot for another 15 s.
- The chart and the set share one palette (black + Economist red), so data and people feel like one product.
- Sourcing on the chart ("Source: FactSet") but no decoration: no animation, no glow, no 3D.
- Long takes (median 4.9 s) of named experts; cutting speeds up only near the end.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Chart card (HTML/SVG, 1920x1080): `background:#121212`; title `font:700 3.6vh "Source Serif 4";color:#fff;position:absolute;left:9%;top:5%` with a `::before` 1.6vh red dot `#E3120B`; bars `fill:#E3120B` gap 15% of bar width; gridlines `stroke:#3a3a3a;stroke-width:1`; y labels right-aligned on the right edge `font:400 2.6vh "Fira Sans";color:#bdbdbd`; x labels + axis note `#bdbdbd 2.4vh`; source bottom-left `2.4vh #9a9a9a`. Keep the "E" bug on top.
- Motion: none needed - hard cut in, hold 10-13 s under the voice-over. (If you want a build, keep it to bars `scaleY 0->1` staggered 0.02 s, total < 1 s, `power2.out`, and then hold.)
- Put the same chart on a screen/monitor in the wide shot (composite it into the screen area with a 4-corner pin and `filter:brightness(.9)`) so the evidence stays visible during the discussion.
- Lower thirds flush to the edge opposite the speaker's eyeline; never on top of the chart.
- Mix: dialogue only, -22 LUFS integrated (or -16 for social), no music under data.
