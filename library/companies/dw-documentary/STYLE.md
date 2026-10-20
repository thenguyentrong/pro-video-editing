# DW Documentary — house style

## Examples
| Folder | Title | Analysed | Shots | ASL / median | Integrated loudness |
|---|---|---|---|---|---|
| climate-who-pays | The trillion dollar case — Who pays for the climate catastrophe? | first 300 s of 52:03 | 64 | 4.69 / 3.06 s | -16.3 LUFS |
| terror-funding-trail | Tracing the path of funding for Islamist terrorist groups | first 300 s of 41:04 | 71 | 4.23 / 3.84 s | -16.3 LUFS |
| origins-of-numbers | From 0 to 9 — the mysterious origins of numbers | first 300 s of 51:44 | 55 | 5.46 / 3.88 s | -15.9 LUFS |

All three were downloaded from dw.com (DW's own site) at 640x360, the closest rendition to 480p; type sizes are read from upscaled frames.

## In one line
Long (40-52 min) broadcast documentaries that explain through people, places and objects: a fast news or montage open, a late title (1:00-1:45), then slow observational shots, long uncut statements and minimal graphics in one bold sans, with the DW roundel top left and a loud broadcast mix (-16 LUFS).

## Sub-styles
1. **Observational case film** (climate): news clips of other broadcasters, intimate close-ups of protagonists, establishing shots at dawn/dusk/night, a 35 s uncut speech, title in caps over an empty room at 1:34.
2. **Investigative DocFilm** (terror funding): "DocFilm" ident at 2 s, flash montage (0.12-1 s) to 20 s, split-screen title card with a series kicker, officials' statements held 24 s, a 95 s identity-safe recreation of an informant (eye macro, silhouettes, night).
3. **History-of-an-idea film** (numbers): slow drone open (11 s), art-object macro of the evidence (17 s holds), a late title that dissolves into a designed 3D type world (27 s), a scholar pointing at the object on location.

## Measured numbers
| | climate | terror funding | numbers |
|---|---|---|---|
| ASL quarters (s) | 2.59 / 4.41 / 7.50 / 6.82 | 2.50 / 5.36 / 4.17 / 6.25 | 5.00 / 7.50 / 3.75 / 5.77 |
| Shots < 1 s / > 3 s | 0 % / 50 % | 18 % / 59 % | 2 % / 64 % |
| Max cuts per 10 s | 5 | 14 (flash open) | 4 |
| Longest shot | 34.8 s speech | 24.2 s minister | 27.3 s title animation |
| Title at | 94 s | 58 s (card) | 85 s |
| Loudness / LRA / TP | -16.3 / 5.7 LU / -2.8 dBTP | -16.3 / 6.4 LU / -2.2 dBTP | -15.9 / 4.8 LU / -2.0 dBTP |
| Cuts on onsets | 43 % (chance 35 %) | 37 % (45 %) | 28 % (32 %) |

## Type & graphics
- DW roundel logo top left ≈5.5 % H, always on.
- DW house sans (closest free "Noto Sans") for everything.
- Title: bold caps 7-8 % H, white, no box, left of centre over an empty wide; or a split card (kicker black caps on white ≈7 % H + question white bold on black).
- Lower third, no box: name bold (often caps) ≈4.5 % H, role ≈3 % H; right-aligned (climate, numbers) or bottom left (terror); an optional country on the far left.
- Place/date tag bold ≈3 % H bottom right ("The Hague, Netherlands 2024").
- Subtitles for non-English speech: white semibold ≈4 % H on a 60 % black box, max 2 lines.
- Credits "A Film by" bold white on black boxes, one per line.

## Rules
1. Open with energy (other broadcasters' news, a flash montage or one slow drone shot), title only after 1-1.5 min.
2. Let people explain: officials and speakers run 18-35 s uncut.
3. Establish every new place with a wide at a strong time of day; tag place + year once.
4. Recreate sensitive testimony with macro and silhouettes, never a blurred face.
5. Graphics are minimal: titles, lower thirds, tags, subtitles; one designed title sequence at most.
6. Broadcast mix: continuous score or room tone (gaps never below ≈-43 dBFS in the observational film), master -16 LUFS.

## Recipe (real footage + HTML/GSAP, Hyperframes)
```css
.dw{position:absolute;left:3%;top:4%;width:5.5vh;height:5.5vh;border-radius:50%;background:#fff;color:#000;font:800 2.6vh/5.5vh "Noto Sans";text-align:center}
.title{position:absolute;left:12%;top:58%;font:800 8vh/1.05 "Noto Sans";text-transform:uppercase;color:#fff}
.kicker span{background:#fff;color:#000;font:800 7vh "Noto Sans";text-transform:uppercase;padding:0 .8vh}
.lt{position:absolute;right:6%;bottom:9%;text-align:right;color:#fff}
.lt .n{font:800 4.5vh "Noto Sans"} .lt .r{font:600 3vh "Noto Sans"}
.tag{position:absolute;right:3%;bottom:6%;font:700 3vh "Noto Sans";color:#fff}
.sub{background:rgba(0,0,0,.6);font:600 4vh "Noto Sans";color:#fff;padding:.3vh 1vh}
```
```js
tl.set(".title",{autoAlpha:1},t).set(".title",{autoAlpha:0},t+6.5);       // hard on/off title
tl.fromTo(".shot",{scale:1},{scale:1.08,duration:17,ease:"none"},t2);       // object hold
```
Pacing: open 2-3 s (flash montages 0.12-1 s), people 4-8 s, statements 18-35 s; master -16 LUFS.

## Caveats
- 360p source: font sizes ±0.5 % H.
- Only the first 5 minutes of 41-52 min films were measured; the middle acts may differ.
- The terror film needed the adaptive detector (dark recreation); the numbers film got 6 verified dark cuts added.
