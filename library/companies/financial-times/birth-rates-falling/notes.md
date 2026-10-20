# Why birth rates are falling everywhere all at once | FT  (Financial Times, uploaded 2026-06-11 per yt-dlp, 12:13 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=6lFXmDk-tps
Purpose: explainer (data-journalist presenter + charts, studio)
One-sentence point: Fertility is falling in rich and poor countries at the same time, faster than forecasts, and the data point to fewer couples forming rather than couples choosing fewer children.

Analysed: the first 300 s (5 min) of 12:13.

Structure (first 300 s):
- 0.0-3.6 cold open: the question as the title, white serif on black boxes, over a dark image of a figure made of digits.
- 3.6-17.6 first chart: the presenter keyed in on the right, small multiples "Average number of children born per woman" (yellow lines) on the left, source line under it.
- 17.6-20.8 presenter full frame on a blue-purple digital texture, lower third.
- 20.8-43 the spread: a world map filling cyan for countries below replacement, then a line chart ("Mexico has lower birth rates than America").
- 43-92 presenter blocks (6-13 s) alternating with charts: successive UN projections vs actual births (lines drawn one by one), b-roll (newborn, factory, couple).
- 92.3-116.8 the key chart (24.6 s): small multiples, ideal vs actual children per woman in four countries, gap shaded.
- 117-141 presenter, phones b-roll.
- 141-147 chapter "Why it matters": white sans over a time-lapse montage cut at 0.28-0.6 s (the densest moment, 10 cuts in 10 s).
- 147-235 presenter, crowd and train b-roll, a Japan chart with the presenter keyed beside it, a quoted clip, chapter "It's coupling, not childbearing" over a peacock.
- 236.7-262.4 the longest chart (25.8 s): small multiples with a highlight box moving between panels.
- 262-300 presenter, couples b-roll, chart by education.

Cut rhythm: 57 shots in 300 s, ASL 5.26 s, median 3.12 s, 16 % under 1 s (the two time-lapse chapter montages), 53 % over 3 s, 11.4 shots/min (adaptive detector: presenter-to-chart changes are soft pushes the scene detector misses; + 1 verified cut). ASL per quarter 6.25 / 3.26 / 5.00 / 7.50 s. Cuts per 10 s: 0-5, one burst of 10 at 140-150 s. Longest 25.8 s and 24.6 s (charts), 17.8 s (chart).

Typography:
- "FT" mark top left: serif "FT" on a grey square (≈#8C8C8C, ≈9 % H), always on.
- Title and lower third: Financier-like serif (closest free "Playfair Display" / "Source Serif 4") on tight black (title) or white (lower third) boxes, one box per line; title ≈4.5 % H; name ≈4 % H; role in tracked serif small caps ≈2.6 % H on a second white box.
- Charts: FT Metric-like sans (closest free "Inter" / "Figtree") in white; title regular weight ≈5 % H, top left; panel labels ≈3.3 % H; axis numbers ≈3.3 % H grey; source line ≈2.2 % H grey bottom left; direct labels on the lines in the line colour (no legends where avoidable).
- Chapter card: white sans ≈6 % H, sentence case, centred over footage.

Colour/grade: chart ground dark slate (≈#262A33) with thin grey grid lines; data colours yellow (#F2E300 ≈), cyan (#2FD3F0 ≈), blue (#3D7BFF ≈), crimson (#E0245E ≈), grey for context lines. Presenter backdrop: blue-purple digital texture. B-roll neutral.

Camera/shots: presenter on a keyed studio set (medium and wide, talking to camera, hands active), charts as full frames or with the presenter keyed at the side (≈25 % W, right), stock-like b-roll, time-lapse city montages for chapter cards.

Transitions: presenter-to-chart changes are short pushes/slides (missed by the scene detector, found by the adaptive one); chapter montages are hard cuts of a few frames. Chart elements draw on in place (lines left to right, map fills).

Sound: integrated -27.3 LUFS (very quiet), LRA 5.0 LU, true peak -7.5 dBTP, median RMS -36.1 dBFS. 52 drop-outs of 0.3-0.95 s with floors around -72 to -82 dBFS: the voice sits in near-silence between sentences, i.e. no continuous music bed under the presenter. Cuts not on onsets (46 % vs 57 % chance).

What makes it premium:
- The charts are the film; each holds 15-26 s and builds in steps while the presenter talks through it.
- Direct labels, one idea per chart, a source on every chart.
- The presenter shares the frame with the chart, so the argument and the evidence are seen together.
- Very dry, quiet mix: nothing competes with the voice.

Recipe (presenter + HTML/GSAP charts, Hyperframes):
- Chart frame: `background:#262A33`; title `font:400 5vh Inter;color:#fff;left:7%;top:6%`; axis `font:400 3.3vh Inter;color:#9AA0A6`; source `font:400 2.2vh Inter;color:#9AA0A6;bottom:5%`.
- Lines: `stroke-width:.45vh`, draw each series with `strokeDashoffset` over 2-4 s `power1.inOut`, label at the line end fades 0.3 s after.
- Presenter beside the chart: keyed plate at `right:2%;bottom:0;height:85%`; chart in the left 70 %.
- Title / lower third: `span{background:#000;color:#fff;font:600 4.5vh "Playfair Display";padding:.3vh 1vh;box-decoration-break:clone}`; lower third white box, role `font:600 2.6vh "Source Serif 4";font-variant:small-caps;letter-spacing:.1em`.
- Chapter card: 6 s of 0.3-0.6 s time-lapse cuts + one sentence-case line `font:500 6vh Inter`.
- Pacing: charts 15-26 s, presenter 6-13 s, chapter bursts 0.3-0.6 s.
- Mix: dry voice ≈-22 LUFS short-term, no bed or a bed ≥25 dB under; master -24 LUFS (FT sits at -27; for social master -16).
