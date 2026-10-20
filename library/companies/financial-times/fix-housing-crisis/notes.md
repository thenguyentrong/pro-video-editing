# How to fix the housing crisis | FT  (Financial Times, uploaded 2026-08-11 per yt-dlp, 14:31 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=kAcFiHtTDDg
Purpose: explainer (data-journalist presenter, on location + studio + charts)
One-sentence point: High housing costs come from too few homes being built, so popular fixes like rent controls ease the pain for some but do not solve the shortage.

Analysed: the first 300 s (5 min) of 14:31.

Structure (first 300 s):
- 0.0-20.9 cold open on location: the presenter walks and talks to a handheld camera through a London housing estate; title "How to fix the housing crisis" on black serif boxes at ≈2-5 s, lower third at ≈5-9 s; two wides of the estate.
- 20.9-30 studio: presenter keyed on a blue wire-frame "blueprint" backdrop.
- 30.2-39.2 chart: share of 25-34-year-olds living with parents, three panels, national vs city lines.
- 39.2-53.7 quote card: round portrait + name/role on the left, the quote typed on word by word on the right, image credit bottom left (14.5 s).
- 53.7-63.8 presenter + street b-roll.
- 63.8-80.5 a city mayor's press conference with lower third (16.7 s).
- 80.5-105 presenter in studio, then walking on location again (89.3-105 s).
- 105-145 b-roll montage of cities (bridges, skylines, suburbs aerial), 3-5 s each.
- 144.6-164.9 presenter, longest take (20.2 s).
- 165-178 chart again, presenter.
- 178-183 chapter card "Affordability vs shortages": white sans beside a small paper house on a grey sweep.
- 183-235 presenter, interview clips, rent-protest footage, a second typed quote card (204-217 s), presenter.
- 235.7-243 chapter card "Other well-intentioned moves can also prove counter-productive" (same paper house).
- 243-300 research-paper pages with a yellow highlight (blurred margins), suburb aerials, night city, presenter.

Cut rhythm: 56 shots in 300 s, ASL 5.36 s, median 4.24 s, 4 % under 1 s, 66 % over 3 s, 11.2 shots/min (adaptive detector: presenter/chart changes are soft). ASL per quarter 5.36 / 5.00 / 5.00 / 5.00 s: flat. Cuts per 10 s: 0-5. Longest 20.2 s (presenter), 16.7 s (mayor clip), 15.8 s (walk).

Typography:
- "FT" grey square mark top left ≈9 % H.
- Title / lower third: serif on black (title) and white (lower third) boxes as in the other FT explainers; name ≈4 % H, role in tracked small caps ≈2.6 % H.
- Charts: Metric-like sans, title ≈5 % H two lines top left, subtitle grey ≈3.5 % H, direct line labels, source ≈2.2 % H.
- Quote card: slate ground, round portrait ≈25 % H, name ≈2.8 % H, role ≈1.8 % H grey under it, quote in white sans ≈5 % H in curly quotes, typed on word by word; "Image credit: ..." ≈1.9 % H bottom left.
- Chapter card: white sans ≈6.5 % H, sentence case, left half; object on the right.
- Documents: real paper page full frame, edges blurred, one sentence on a yellow highlighter (≈#F5FF3C), credit bottom left.

Colour/grade: chart slate #262A33 with blue (#3D7BFF ≈) and crimson (#E0245E ≈) lines; studio backdrop blue wire-frame (#1D4F73 ≈); location footage natural, overcast; chapter cards grey sweep with one paper object.

Camera/shots: handheld walk-and-talk on location (wide lens, presenter centred), keyed studio presenter, charts, typed quote cards, agency clips of politicians and protests, drone/aerial city b-roll, real research papers.

Transitions: hard cuts and short pushes between presenter and graphics; words appear by type-on. No dissolves seen.

Sound: integrated -23.6 LUFS, LRA 3.1 LU (very even), true peak -8.3 dBTP, median RMS -29.2 dBFS. 32 drop-outs of 0.3-0.85 s with floors around -55 to -92 dBFS between sentences: mostly dry voice, little or no bed. Cuts not on onsets (49 % vs 57 % chance).

What makes it premium:
- The data reporter takes the argument out of the studio: the location walk proves he is talking about real places.
- Quotes from experts are rebuilt as clean typed cards with portrait and credit instead of screenshots.
- Chapter cards are a single object (a paper house) with one sentence, reused for every chapter.
- The pace is flat and calm (ASL 5.0-5.4 s every quarter).

Recipe (presenter + HTML/GSAP, Hyperframes):
- Open on location: 15-20 s handheld walk-and-talk, title boxes at 2 s, lower third at 5 s.
- Quote card: `.q{font:500 5vh/1.25 Inter;color:#fff;left:30%;width:60%}` typed with `tl.from(".q .w",{autoAlpha:0,duration:.01,stagger:.18})`; portrait `border-radius:50%;width:25vh`.
- Chapter card: grey sweep `radial-gradient(circle at 70% 60%,#9a9a9a,#3a3a3a 70%)`, one object photo, sentence `font:500 6.5vh Inter` left; hold 5-7 s.
- Document: page full frame, `mask-image:radial-gradient(ellipse 70% 60% at 50% 50%,#000 60%,transparent)` over a blurred copy; highlight `background:#F5FF3C` wipe 0.5 s.
- Pacing: 4-6 s shots, presenter takes up to 20 s, charts 9-13 s.
- Mix: dry voice ≈-20 LUFS short-term, no bed under the presenter; master -24 LUFS (web: -16).
