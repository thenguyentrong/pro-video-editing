# Financial Times — house style (video explainers and FT Film)

## Examples
| Folder | Title | Analysed | Shots | ASL / median | Integrated loudness |
|---|---|---|---|---|---|
| birth-rates-falling | Why birth rates are falling everywhere all at once | first 300 s of 12:13 | 57 | 5.26 / 3.12 s | -27.3 LUFS |
| fix-housing-crisis | How to fix the housing crisis | first 300 s of 14:31 | 56 | 5.36 / 4.24 s | -23.6 LUFS |
| ai-chip-black-market | Silicon shadows: inside the black market for AI chips (FT Film) | first 300 s of 19:22 | 101 | 2.97 / 2.08 s | -14.8 LUFS |

## In one line
Two registers under one grey "FT" mark: a quiet, chart-first explainer where a data journalist shares the frame with clean slate charts and speaks over near-silence, and a loud cinematic FT Film with a montage open, acid-yellow place cards and archive.

## Sub-styles
1. **Data-reporter explainer** (birth rates, housing): presenter keyed on a textured backdrop or walking on location; charts on dark slate (#262A33) held 9-26 s, built step by step; typed quote cards with a round portrait; chapter cards (one sentence + one object, or a time-lapse burst); serif title and lower-third boxes. ASL ≈5.3 s; no continuous music bed; -24 to -27 LUFS.
2. **FT Film documentary** (AI chips): 40 s montage before any explanation, serif "FINANCIAL TIMES" ident at 2 s, title at 1:47 and one-word place cards ("WASHINGTON", "TAIPEI") in acid-yellow geometric caps, low-key interviews with coloured back light, black-and-white archive for history, one 28 s grey map. ASL 3.0 s; continuous score; -14.8 LUFS.

## Measured numbers
| | birth rates | housing | AI chips (FT Film) |
|---|---|---|---|
| ASL quarters (s) | 6.25 / 3.26 / 5.00 / 7.50 | 5.36 / 5.00 / 5.00 / 5.00 | 2.27 / 2.78 / 2.42 / 5.77 |
| Shots < 1 s / > 3 s | 16 % / 53 % | 4 % / 66 % | 9 % / 27 % |
| Max cuts per 10 s | 10 (chapter time-lapse) | 5 | 10 (montage) |
| Longest shot | 25.8 s chart | 20.2 s presenter | 28.2 s map |
| Drop-outs | 52 × 0.3-0.95 s to ≈-80 dBFS (no bed) | 32 × 0.3-0.85 s to ≈-65 dBFS | 8 × 0.3-0.65 s |
| Loudness / LRA / TP | -27.3 / 5.0 LU / -7.5 dBTP | -23.6 / 3.1 LU / -8.3 dBTP | -14.8 / 4.1 LU / -0.3 dBTP |
| Cuts on onsets | 46 % (chance 57 %) | 49 % (57 %) | 42 % (48 %) |

## Type & graphics
- Mark: serif "FT" on a grey square (≈#8C8C8C), top left, ≈9 % H, always on.
- Explainer titles and lower thirds: Financier-like serif (closest free "Playfair Display" / "Source Serif 4") on tight boxes, one box per line: title white on black ≈4.5 % H; name black on white ≈4 % H; role in tracked small caps ≈2.6 % H on a second white box.
- Charts: Metric-like sans (closest free "Inter" / "Figtree"): title regular ≈5 % H top left, subtitle grey ≈3.5 % H, axis ≈3.3 % H grey, source ≈2.2 % H bottom left; direct labels in the line colour; slate ground #262A33; data colours yellow, cyan, blue, crimson, grey for context.
- Quote card: round portrait ≈25 % H left, quote ≈5 % H white sans typed on word by word, "Image credit" ≈1.9 % H.
- Chapter card: white sans ≈6-6.5 % H sentence case, over a time-lapse burst or beside one object on a grey sweep.
- Documents: real page, blurred edges, one sentence on yellow (≈#F5FF3C), credit bottom left.
- FT Film: acid yellow (≈#E4F53C) heavy geometric caps (closest free "Jost" ExtraBold / "League Spartan"): title ≈9 % H, place cards 12-17 % H; lower third without box (serif name ≈3.5 % H + small-caps role ≈2.6 % H); tiny "Credit: ..." bottom right ≈1.9 % H.

## Rules
1. In the explainer, the chart is the long shot: 9-26 s, one idea, built in steps; the presenter talks over it, often keyed in beside it (≈25 % W, right).
2. Source line on every chart; direct labels instead of legends.
3. Keep the voice dry: no music under the presenter; 0.3-0.9 s silences between sentences.
4. Quotes become typed cards with portrait and credit, not screenshots.
5. Chapters: one sentence + a time-lapse burst (0.3-0.6 s shots) or one object on grey, 5-7 s.
6. FT Film: montage first (30-40 s), title late (≈1:45), one-word yellow place cards for each new location, black-and-white archive for history, master loud (≈-15 LUFS).

## Recipe (HTML/GSAP, Hyperframes)
```css
:root{--slate:#262A33;--grid:#3A3F4A;--axis:#9AA0A6;--yellow:#F2E300;--cyan:#2FD3F0;--blue:#3D7BFF;--crimson:#E0245E;--acid:#E4F53C}
.ftmark{position:absolute;left:3%;top:4%;width:9vh;height:9vh;background:#8C8C8C;font:600 5vh/9vh "Playfair Display";color:#222;text-align:center}
.chart{background:var(--slate)} .chart h2{font:400 5vh Inter;color:#fff} .chart .src{font:400 2.2vh Inter;color:var(--axis)}
.tbox span{background:#000;color:#fff;font:600 4.5vh "Playfair Display";padding:.3vh 1vh;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.lt .n{background:#fff;color:#111;font:600 4vh "Playfair Display";padding:.3vh 1vh}
.lt .r{background:#fff;color:#111;font:600 2.6vh "Source Serif 4";font-variant:small-caps;letter-spacing:.1em;padding:.3vh 1vh}
.place{font:800 15vh "Jost",sans-serif;color:var(--acid);text-transform:uppercase;text-align:center}
```
```js
series.forEach((s,i)=>tl.fromTo(s,{strokeDashoffset:len[i]},{strokeDashoffset:0,duration:3,ease:"power1.inOut"},t+i*3.5)); // lines one by one
tl.from(".q .w",{autoAlpha:0,duration:.01,stagger:.18},t2);   // typed quote
tl.set(".place",{autoAlpha:1},t3).set(".place",{autoAlpha:0},t3+5);  // FT Film place card
```
Mix: explainer = dry voice ≈-20 to -22 LUFS short-term, no bed, master -24 LUFS (FT sits at -24 to -27; for social -16). FT Film = continuous score, master ≈-15 LUFS, TP ≤ -1 dBTP.

## Caveats
- Fonts (Financier, Metric, the FT Film display face) are proprietary; free stand-ins named.
- Presenter-to-chart changes are soft pushes: the scene detector missed them, so the two explainers were measured with the adaptive detector.
- Both explainers have the same presenter; the FT's other explainer hosts were not measured.
- Only the first 5 minutes of each film were measured.
