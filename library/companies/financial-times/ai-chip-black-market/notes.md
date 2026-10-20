# Silicon shadows: inside the black market for AI chips | FT Film  (Financial Times, uploaded 2026-07-14 per yt-dlp, 19:22 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=kFcWmQevQo8
Purpose: documentary explainer (FT Film: narrated investigation with interviews, archive and maps)
One-sentence point: US export controls created a black market for advanced AI chips, and the film follows how chips reach China and why Washington cannot close the gaps.

Analysed: the first 300 s (5 min) of 19:22.

Structure (first 300 s):
- 0.0-2.0 chip-making machine macro.
- 2.0-4.0 ident: "FINANCIAL TIMES" in a white serif over blue-lit footage.
- 4-41 cold open montage: data centres, AI billboards, a military parade and fighter jets, chip renders on black, a CEO keynote, warehouses (4-6 cuts per 10 s).
- 41-60 first voices: interviews in dark rooms with a blue back light, tech expo, robots, chip renders, archive of the Chinese leadership.
- 60-107 the stakes: a close interview of a researcher, hands at a red-lit laptop, night cities, data halls, explosions, diplomatic meetings; the densest stretch (90-100 s, 10 cuts).
- 107-111 title "SILICON SHADOWS: INSIDE THE WORLD OF CHIP SMUGGLING" in acid-yellow geometric caps over a night aerial of Beijing.
- 111.7-120 place card "WASHINGTON" (huge yellow caps) over the Capitol at sunset.
- 120-152 hearings with lower thirds, meetings, speeches.
- 152-182 history: black-and-white Cold War archive (parades, aircraft, signings), cut at 1-3 s.
- 182-235 smuggling scenes, the White House, an AI app on a phone, an analyst interview.
- 235.5-263.7 the supply chain on a map (28.2 s, the longest shot): grey satellite world, a chip box labelled "DESIGN" linked to a Taiwan inset by a dashed white line.
- 263.7-285 analyst interview.
- 285-292 place card "TAIPEI" over a night skyline; drone show.

Cut rhythm: 101 shots in 300 s, ASL 2.97 s, median 2.08 s, 9 % under 1 s, 27 % over 3 s, 20.2 shots/min (scene detector; the adaptive one found 21 more, mostly inside fast montages, not added). ASL per quarter 2.27 / 2.78 / 2.42 / 5.77 s (the map and interview slow the last quarter). Cuts per 10 s up to 10. Longest 28.2 s (map), 13.3 s, 13.0 s (interviews). Shortest 0.17 s.

Typography:
- "FT" grey square mark top left ≈9 % H.
- Ident: "FINANCIAL TIMES" in a wide high-contrast serif ≈11 % H, white, centred.
- Title and place cards: acid yellow (≈#E4F53C) heavy geometric caps (Futura-like; closest free "Jost" ExtraBold / "League Spartan"); title ≈9 % H (line 1) and ≈6.5 % H (lines 2-3), centred; place cards ≈12-17 % H, one word, centred, over a wide establishing shot.
- Lower third (film version): no box; name in white serif ≈3.5 % H, role in tracked serif small caps ≈2.6 % H, 2 lines max, left of the subject.
- Credits: tiny white sans "Credit: Nvidia" bottom right ≈1.9 % H on borrowed footage.
- Map labels: wide-tracked white caps ≈2.5 % H in thin white boxes ("DESIGN", "TAIWAN").

Colour/grade: cinematic, contrasty, cool; interviews low-key with coloured back light (blue, red); archive black and white; title cards acid yellow, the only graphic colour; map desaturated grey.

Camera/shots: shot interviews (dark rooms, shallow focus, slow push), macro of hardware, aerials of cities, staged inserts (hands on a laptop), news archive, Cold War archive, a 2D/3D grey map with inset boxes.

Transitions: hard cuts; no dissolves seen; montage bursts of 0.17-0.6 s at the turns.

Sound: integrated -14.8 LUFS (loud, film-trailer level), LRA 4.1 LU, true peak -0.3 dBTP, median RMS -20.6 dBFS. Continuous score under narration; 8 short drop-outs (0.3-0.65 s); the biggest re-entries (+43 to +47 dB from the gap floor) cluster at 265-281 s inside the analyst interview. Cuts not on onsets (42 % vs 48 % chance).

What makes it premium:
- It opens like a feature: 40 s of montage before any explanation, the title only at 1:47.
- Place cards with one huge acid-yellow word set the geography; the colour appears nowhere else.
- Archive is used for history (black-and-white Cold War export controls) so the present looks like a repeat.
- The one diagram is a calm 28 s map move in a neutral grey world.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Cold open: 30-40 s of 1.5-3 s shots, music-led, no captions except credits.
- Place card: `font:800 15vh "Jost",sans-serif;color:#E4F53C;text-transform:uppercase;letter-spacing:.01em;text-align:center`; cut on with the shot, hold 4-8 s, slow drone move underneath.
- Title: same face, 9 / 6.5 vh lines, over a night aerial, 4 s.
- Lower third: `.n{font:500 3.5vh "Source Serif 4";color:#fff}` `.r{font:600 2.6vh "Source Serif 4";font-variant:small-caps;letter-spacing:.12em}`, no box.
- Map: greyscale satellite still `filter:grayscale(1) brightness(.8)`, inset boxes `border:.2vh solid #fff`, dashed link `stroke-dasharray:6 6` drawn over 1.5 s; one continuous move 20-28 s.
- Mix: score continuous, narration on top, master about -15 LUFS (web/social) with true peak ≤ -1 dBTP.
