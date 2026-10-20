# How Does Your College Choice Affect Your Income?  (The New York Times — Graphics desk Short, 2026-10-10, 1:21, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/GmF0XvpoYzo
Purpose: social reel / data explainer (reporter-hosted)
One-sentence point: New Education Department data shows your major matters more than your school for income, except at the extremes (CMU computer science vs Juilliard music).

Whole video analysed (81 s). Source 480 x 854, 23.976 fps.

Structure: beats with timestamps
- 0–1.7 s hook: reporter seated on a white seamless set, white label tags with school names (University of Florida, Harvard, Dartmouth …) float around her head; caption "Does it matter where you go to college?".
- 1.7–4.4 s title typed on in white boxes, bottom-left: "How Much Does Your College Choice Really Matter?"; caption "We analyzed the data, and the short answer is:".
- 4.4–21.8 s one continuous graphic (17.4 s): a long scrolling list of majors → collapses into a dot-range chart "Earnings ranges for majors across schools" → camera zooms into the top row → hand-drawn arrows explain the encoding ("Earnings range", "Median earnings"); the other rows dim.
- 21.8–37.8 s back on the host: a white chart card with one row (Computer science) slides over her; callouts "$115,980 University of Alabama" vs "$268,121 Carnegie Mellon University"; punch-in jump cuts at 28.0 and 29.7 s; lower third 35–37 s.
- 37.8–48 s full chart again: a white highlight box moves row to row (Finance/Economics/Math = wide ranges; Drama, Mechanical eng., Music, Nuclear eng. = narrow).
- 48–52 s host (medium, then close behind the laptop).
- 52.4–62.8 s chart: all rows dimmed except Music; callout "Juilliard $32,842" vs "Median $43,093".
- 62.8–80 s host, the policy context ("This data came into existence because there's pushback …", "about 98 percent …"); 80–81 s white NYT wordmark over the host.

Cut rhythm: 16 shots in 81 s, ASL 5.07 s, median 2.90 s. ASL per quarter 6.76 / 3.38 / 5.07 / 3.38 s. Longest: 17.4 s (the list→chart graphic at 4.4 s), 10.4 s (chart at 37.8 s), 10.4 s (Juilliard chart at 52.4 s). Shortest 1.29 s. 0 % of shots under 1 s, 44 % over 3 s. Cuts land on voice phrase starts: 73 % on an onset vs 60 % chance. Host shots alternate wide (full body + laptop) and tight (face + laptop edge, often a digital punch-in ~1.4x).
Note: each continuous chart animation (zoom, highlight move, dimming) counts as one shot; the visual change rate inside charts is ~1 change per 1.5–2 s.

Typography: (fonts guessed; NYT uses Cheltenham + Franklin)
- Title: bold serif (Cheltenham-like; closest free "Source Serif 4" 700 / "Libre Caslon Text" 700), black on white boxes, one box per line, font ~3.5 % H, left x 7 %, y 58–72 % H, typed on letter by letter in ~1.5 s.
- Captions (every line of speech): white sans 600 (Franklin-like; closest free "Libre Franklin" 600), font ~2.1 % H, sentence case, on a tight dark translucent box (~#000 @ 45 %), centred at y ≈ 77 % H, 1 line usually, max 2; 3–6 words per caption, ~1–1.5 s each.
- Lower third: white box, name bold serif ~3 % H ("Arfa Momin"), role caps sans ~1.2 % H grey ("NEW YORK TIMES GRAPHICS REPORTER"), left x 7 %, y ~60 % H.
- Chart title bold sans ~2.6 % H top-left (y 13–18 %); axis labels light grey ~2.4 % H; row labels black ~2 % H; source note regular ~1.6 % H at y ~88 %, left 8 %.
- Annotations: bold sans black ~2.4 % H + curved hand-drawn arrow (2 px black).
- Watermark: NYT "T" top-right, white ~50 % opacity, ~6 % W.

Colour/grade: bright, low-contrast, near-white everywhere: white seamless set (#EDEDED-ish), chart background #F2F2F2-ish; one data colour pair: mint/sage bar (~#A8D5C6) and slate-blue median dot (~#5B7A8C, white stroke). Dimmed rows at ~25 % opacity. Host in dark brown top = the only dark mass. No grain, no vignette.

Camera/shots: one locked-off two-camera interview set (wide + tight), digital punch-ins, a laptop as prop. All other screen time = native vertical charts built for 9:16 (not a reframed 16:9 chart).

Transitions: hard cuts between host and chart; inside charts everything is animated (list collapse, zoom, highlight box glide, dimming). No dissolves, no whooshes visible.

Sound: integrated -14.2 LUFS (social-loud), median momentary -13.3 LUFS, flat across quarters (-13.3 / -13.5 / -12.9 / -13.3). Only one dip (5.5–6.0 s to -26 LUFS) and no gap below -50 dBFS → a continuous quiet music bed fills every pause (inference). No big hits (largest rise +14.5 dB at 6 s). Voice = the reporter on camera + VO over charts.

What makes it premium
- The reporter is a real NYT graphics reporter with a name + role; authority without a studio look.
- The chart is designed for vertical: one row per line, big labels, zooms to one row before showing all.
- Explains the chart encoding before using it ("the bar shows the range", "the dot is the median").
- Two concrete names + numbers (Alabama $115,980 vs CMU $268,121) make the abstract range real.
- One data colour pair, everything else grey; highlight = white box + dimming, never red circles.
- Source note always on screen under the chart.

Recipe (real footage + HTML/GSAP, Hyperframes, 1080 x 1920)
- Set: film host on white/grey seamless, two angles; punch in 1.4x in post for every 2nd sentence.
- Captions: `font:600 40px "Libre Franklin"` (2.1 % H), `color:#fff; background:rgba(0,0,0,.45); padding:2px 8px; box-decoration-break:clone`, centred at `top:77%`; swap per phrase (3–6 words) with a hard cut, no pop animation.
- Title boxes: each line `display:inline-block; background:#fff; padding:6px 14px; font:700 67px "Source Serif 4"`; type on with `gsap.from(chars, {opacity:0, duration:.01, stagger:.035})`.
- Chart: background `#F2F2F2`; bars `#A8D5C6` height 3.4 % H, dot `#5B7A8C` r 1.2 % H with 3 px white stroke; title `700 50px "Libre Franklin"` at left 8 %, top 13 %; source `400 30px` at top 88 %.
- Explain encoding: zoom the chart container `scale 1 → 2.2, transformOrigin:"20% 15%"` over 1.2 s `power2.inOut`; arrow SVG path `strokeDashoffset` draw in 0.5 s; dim others `opacity:.25` in 0.4 s.
- Highlight row: white rounded rect (`border-radius:6px; box-shadow:0 2px 12px rgba(0,0,0,.12)`) behind the row, glide `y` to next row in 0.5 s `power2.inOut`.
- Card over host: white card 80 % W, `border:1px solid #ccc; border-radius:6px`, slide up 4 % + fade in 0.35 s `power2.out`; callout numbers `700 2.4 % H`.
- End: white NYT-style wordmark centred over the last host shot for 1 s.
- Mix: voice -13…-14 LUFS short-term, bed ~-30 LUFS continuous, master integrated -14 LUFS.
