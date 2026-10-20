# 38 Matches In 38 Seconds  (Premier League, uploaded 2026-05-25, 38.1 s, 9:16, YouTube Shorts / Premier League channel)
URL: https://www.youtube.com/shorts/Accw1k3wPaI
Purpose: season-review data package (social vertical) — the whole league table of a season as one animated bump chart
One-sentence point: the full season's table, every matchweek, in one continuous move, one matchweek per second.

Structure (one continuous animated shot, no cuts):
- 0.0–1.0 Empty chart: lion + "Matchweek" header, positions 1–20 with crests, matchweek axis on top.
- 1.0–3.0 Chapter label "THE KICK OFF" (vertical, on a mint position column).
- 3.0–16 Lines draw rightward one matchweek per second (≈1.0 s per week), the chart scrolls left so the "now" column stays at ≈70 % of the width; early season = lines cross a lot.
- 16–19 Chapter "FESTIVE FIXTURES" (cyan → violet column).
- 19–29 Mid-season: fewer crossings, the top and bottom settle.
- 29–34 Chapter "THE RUN IN" (orange → magenta → violet column), relegation places marked "R".
- 34–35.3 Chapter "THE FINAL DAY" (dark violet column), champion marked with a trophy icon; final table holds.
- 35.3–38.1 2.7 s digital silence on the final table.

Cut rhythm: 1 shot (no cuts; scene detection finds none; soft "transition" candidates are just chart motion). The pace is set by data: 38 matchweeks in ≈35 s = one step per ≈0.92 s; chapter labels hold 2–5 s.

Typography:
- Header: lion logo + "Matchweek" in the league's geometric sans, bold, ≈2 % of frame height; week numbers ≈1.3 %.
- Position column: rounded pill, white numerals, ≈2 % H, gradient fill that changes per chapter (mint, cyan→violet, orange→magenta→violet, dark violet).
- Chapter labels: "THE" small + main words in heavy geometric caps, rotated 90° clockwise (reads top-to-bottom, set beside the column), ≈25–30 % of frame height long, same gradient as the column. Closest free: Outfit 800 / Lexend 800.
- Crests as the only team labels (no names).

Colour/grade: off-white background with faint white diagonal "lion-mane" stripes; lines 2 px in club colours (red, sky blue, navy, yellow, claret); chapter gradients from the league's secondary palette (mint/cyan #22e3d8, violet #7a2be2, orange #ff5a1f, magenta #e3157a).

Camera: virtual horizontal pan (constant speed, linear), chart height fixed; no zooms.

Transitions: none; chapter changes are recolours of the position column + a new vertical label sliding in.

Sound: a quiet steady bed: integrated −32.1 LUFS (very low for social), LRA 1.5 LU, momentary −30 to −33 all through, then 2.7 s silence. I did not listen (a ticking or soft electronic loop is likely, not verified).

What makes it premium:
- One idea, one move: a bump chart that pans at a fixed speed tells a whole season with no edits.
- Chapters named with the league's own season vocabulary give the data a story arc.
- Club colours only on data lines; brand colours only on the chapter column.

Recipe (HTML/GSAP or D3 in Hyperframes, 1080×1920):
- Data: 20 teams × 38 positions. Draw each team as an SVG path with smooth S-curves between weeks (`d3.curveMonotoneX` or cubic Béziers with horizontal tangents), stroke 4 px in club colour, crest 40 px at the line head.
- Layout: chart area 85 % of width, row height 70 px (20 rows ≈ 1400 px), week spacing 150 px; group `x` from 0 to `-(38*150 - 760)` px over 35 s, `ease:"none"`; reveal each path with `stroke-dashoffset` synced to the pan.
- Column pill at 72 % width, 52 px wide, radius 26 px; gradient per chapter, change with `background` crossfade 0.4 s; label = rotated `writing-mode: vertical-rl` text, 120 px, gradient clip.
- Chapters at weeks 1, 17, 30, 38; hold the final table 2–3 s in silence.
