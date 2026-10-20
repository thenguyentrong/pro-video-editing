# CNBC — house style (digital explainers)

## Examples
| Folder | Title | Analysed | Shots | ASL / median | Integrated loudness |
|---|---|---|---|---|---|
| diamond-prices-falling | Why Diamond Prices Are Falling So Fast | full 4:26 | 45 | 5.91 / 5.09 s | -24.0 LUFS |
| ai-kill-switch | Why It's So Hard To Build An AI Kill Switch | first 300 s of 10:20 | 59 | 5.09 / 3.96 s | -23.4 LUFS |
| inside-man-fed-spies | Inside Man: How Chinese Spies Used Lies, Romance And Betrayal To Target The Federal Reserve | first 300 s of 21:13 | 48 | 6.25 / 5.23 s | -23.7 LUFS |

## In one line
A reporter hosts from CNBC's newsroom, and every source (other outlets' headlines, posts, press releases, event clips, recordings) is retyped into one dark-teal + gold card system; the pace is calm and even (ASL 5-6 s, never more than 3-5 cuts per 10 s).

## Sub-styles
1. **Business "Why ..." explainer** (diamonds): cold open on an animated chart, reporter stand-up, headline cards, 3D mechanism animation, interviews, map and bar chart, end card. Flat pacing (ASL 5.1-6.0 s in every quarter).
2. **Tech series explainer** (AI kill switch, "AI Insights"): kinetic-type cold open from headlines, event clips inside a gold-outlined frame, a glitch transition into a series title at ≈1:47, data-centre b-roll, many remote interviews.
3. **Long-form investigation** (Inside Man): dark slate world, real interview recordings with teal subtitle boxes, painted/drawn recreations instead of actors, a correspondent on a dark set, series title at 2:39, typed chapter labels.

## Measured numbers
| | diamonds | AI kill switch | Inside Man |
|---|---|---|---|
| ASL quarters (s) | 5.54 / 5.11 / 5.54 / 6.04 | 4.41 / 4.41 / 4.69 / 6.25 | 5.36 / 5.77 / 6.25 / 6.25 |
| Shots < 1 s / > 3 s | 0 % / 84 % | 8.5 % / 71 % | 0 % / 90 % |
| Max cuts per 10 s | 3 | 5 (cold open) | 3 |
| Longest shot | 16.6 s 3D animation | 19.7 s framed clip | 17.4 s |
| Reporter on screen | every 20-50 s, 3-8 s | every ≈45-60 s | every 60-90 s |
| Drop-outs | 10 × 0.3-0.6 s | 12 × ≤0.4 s + 1.55 s | 10 × 0.35-0.55 s |
| Loudness / LRA | -24.0 / 9.2 LU | -23.4 / 8.0 LU | -23.7 / 6.9 LU |
| Cuts on onsets | 45 % (chance 58 %) | 50 % (55 %) | 36 % (49 %) |

## Type & graphics
- Bug: "CNBC" wordmark top right ≈3.8 % H, always on.
- One geometric sans for everything (Proxima-Nova-like; closest free "Montserrat" / "Figtree").
- Ground: dark-teal radial gradient (≈#0E4A5C centre → #06202B edge); the investigation uses charcoal/slate instead.
- Accent gold ≈#F2B400: lower-third bar, highlight boxes, frame outlines, arrows; data cyan ≈#3EC1E6.
- Lower third: gold vertical bar + bold white name ≈5.5 % H + role ≈3.3 % H; flush left for the reporter, right-aligned with the bar on the right for guests.
- Headline card: gold rule left, outlet in tracked caps ≈2.8 % H, byline + date between thin rules, bold headline ≈6.5 % H, one phrase on gold.
- Framed clip: gold outline around the clip (≈80 % W), event | date above it.
- Recording subtitle: white semibold ≈3.6 % H on a dark-teal box; source block of 3 lines top left.
- Charts: centred title ≈5 % H + unit line, rounded lighter panel, glowing cyan line/bars, y labels on both sides, source bottom left ≈2 % H.
- Series title: logo + wide caps (≈11-13 % H) + bold subtitle, 6-8 s, after the hook (≈12-17 % into the film).

## Rules
1. Open on evidence (a chart, headlines in motion, a recording), then the reporter within 11-70 s.
2. Retype every outside source into the house card system; never show raw screenshots full frame without the card styling (exception: long articles on white).
3. Keep it even: 4-6 s shots, ≤3 cuts per 10 s outside the cold open.
4. Give the long shots (11-20 s) to the mechanism: 3D animation, chart draw, framed clip, map.
5. One gold highlight per card; cyan only for data.
6. Bring the series title after the stakes are set (1:45-2:40 in), with a transition effect only there.
7. Investigations: real recordings + illustrated recreations, never actors.

## Recipe (real footage + HTML/GSAP, Hyperframes)
```css
:root{--teal-a:#0E4A5C;--teal-b:#06202B;--gold:#F2B400;--cyan:#3EC1E6}
.ground{background:radial-gradient(ellipse at 50% 30%,var(--teal-a) 0%,#082F3B 55%,var(--teal-b) 100%)}
.bug{position:absolute;right:3.5%;top:4%;font:800 3.8vh Montserrat;color:#fff}
.lt{position:absolute;left:55%;bottom:14%;border-left:.6vh solid var(--gold);padding-left:1.6vh;color:#fff}
.lt .n{font:700 5.5vh Montserrat} .lt .r{font:500 3.3vh Montserrat}
.hc{position:absolute;left:15%;top:28%;width:58%;border-left:.6vh solid var(--gold);padding-left:3vh;color:#fff}
.hc .src{font:600 2.8vh Montserrat;letter-spacing:.2em;text-transform:uppercase}
.hc .by{font:500 2.4vh Montserrat;border-top:1px solid #fff9;border-bottom:1px solid #fff9;padding:1vh 0}
.hc .hl{font:700 6.5vh/1.2 Montserrat} .mark{background:var(--gold);color:#0B2530;padding:0 .6vh}
.frame{position:absolute;left:10%;top:11%;width:80%;aspect-ratio:16/9;outline:.4vh solid var(--gold);outline-offset:.6vh}
.rec-sub{background:rgba(31,74,87,.85);font:600 3.6vh Montserrat;padding:.6vh 1.4vh;color:#fff}
```
```js
tl.fromTo(".hc",{scale:1},{scale:1.05,duration:5,ease:"none"},t);          // card push over the hold
tl.from(".lt",{x:-20,autoAlpha:0,duration:.3,ease:"power2.out"},t2);        // lower third from the bar
tl.fromTo(".line",{strokeDashoffset:len},{strokeDashoffset:0,duration:7,ease:"power1.inOut"},t3); // chart draw
```
Mix: VO ≈-20 LUFS short-term, bed ≈15 dB under, 0.3-0.6 s gaps between paragraphs; master -24 LUFS (web/social -16).

## Caveats
- Fonts and hex values read off 480p frames.
- Framed clips and slow pushes hide picture changes inside one "shot"; ASL is higher than the felt pace.
- AI kill switch and Inside Man numbers cover only the first 5 minutes.
