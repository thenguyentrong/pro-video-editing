# Inside Man: How Chinese Spies Used Lies, Romance And Betrayal To Target The Federal Reserve  (CNBC, uploaded 2026-09-30 per yt-dlp, 21:13 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=9PNuDD5VHtI
Purpose: explainer / investigation (long-form CNBC investigation, correspondent-led, illustrated recreations)
One-sentence point: A senior Federal Reserve adviser was cultivated over years by Chinese intelligence, and the film rebuilds how it happened from recordings, court papers and interviews.

Analysed: the first 300 s (5 min) of 21:13.

Structure (first 300 s):
- 0.0-4.5 cold open: audio of an official interview recording over a painted, desaturated still of the Fed building; subtitle of the question; a three-line source block top left (agency / office / date).
- 4.5-17.5 a phone "RECORDING" graphic with a waveform, the answer subtitled in a teal box; an illustrated recreation of the interview room (drawn figure seen over two dark shoulders).
- 17.5-38 who he is: Fed exterior, a photo card with an arrow callout and a gold name box, photos of him teaching, more illustration.
- 38-48 the charge: Department of Justice press-release card (house headline card on footage of the Fed, 10 s).
- 45.7-68 context: archive of Beijing, the indictment pages, a port aerial.
- 68.4-76.7 the guide: CNBC correspondent standing on a dark grey set, lower third.
- 76.7-158 the case: a defence lawyer and an ex-agent in dark interview set-ups, recordings with subtitles, illustrated recreations (hands on a phone, a man at a desk), browser screenshots, photos.
- 158.7-164.6 series title: "CNBC / INSIDE MAN" with a Fed-building icon and an arrow line, subtitle with the full title, over an illustration (≈6 s, at 2:39 = 12 % of the full film).
- 165-177 chapter 1 "Building the relationship": label typed on with a gold cursor bar over a Shanghai aerial.
- 177-300 illustrated recreations under subtitled recordings, a former investigator, photos of the handlers, archive of China, the correspondent closes the section (268-300 s).

Cut rhythm: 48 shots in 300 s, ASL 6.25 s, median 5.23 s, 0 % under 1 s, 90 % over 3 s, 9.6 shots/min (scene detector + 10 verified dark-footage cuts from the adaptive cross-check). ASL per quarter 5.36 / 5.77 / 6.25 / 6.25 s. Cuts per 10 s: 0-3. Longest 17.4 s (244.8 s), 15.6 s, 14.3 s; shortest 1.63 s. Many shots are slow pushes on stills or illustrations, so the picture moves while the shot is long.

Typography (CNBC digital system on a dark variant):
- "CNBC" bug top right ≈3.8 % H.
- Geometric sans (closest free "Montserrat"/"Figtree").
- Source block for recordings: three lines of bold white ≈3 % H top left (who recorded / office / date).
- Recording subtitles: white semibold ≈3.6 % H on a dark-teal box (≈#1F4A57, 85 %), one line, centred at ≈80 % H; questions use a darker box.
- Photo callout: photo card with rounded corners, a gold arrow and a gold box with the name in dark bold ≈4.5 % H, role in white ≈3 % H right-aligned.
- Correspondent lower third: gold bar + name ≈5.5 % H + "CNBC" ≈3 % H, bottom left.
- Headline card (DOJ release): tracked caps source ≈3 % H, office + date between thin rules, bold headline ≈6.5 % H, gold vertical rule, over darkened footage.
- Series title: logo, wordmark "INSIDE MAN" in heavy caps ≈11 % H split by a thin line that ends in an arrow, a row of dots, subtitle ≈4 % H.
- Chapter label: bold white ≈6 % H, two lines, typed on with a gold cursor bar.

Colour/grade: dark charcoal and slate everywhere (sets, illustrations, stills darkened ≈40 %); gold #F2B400 for names, arrows and bars; teal subtitle boxes. Illustrations: painted, desaturated, sepia-grey with soft vignettes.

Camera/shots: correspondent stand-ups on a dark set; dark interview set-ups (key light, black background); drawn/painted recreations (no actors); photo and document cards with slow pushes; archive and aerials.

Transitions: hard cuts; slow push-ins inside long shots; the chapter label is typed on. No whips.

Sound: integrated -23.7 LUFS, LRA 6.9 LU, true peak -3.9 dBTP, median RMS -31.7 dBFS. Real interview recordings carry the story, under a low suspense bed; 10 short drop-outs (0.35-0.55 s), the deepest at 97.4 s (to -84.5 dBFS) before a +64 dB re-entry into the next recording. Cuts sit below chance on onsets (36 % vs 49 %): cuts fall in pauses, not on sounds.

What makes it premium:
- Real recordings are the spine; illustrations replace actor recreations, so nothing looks staged.
- Every recording has its source and date on screen.
- One house system (gold + teal + slate) holds documents, photos, titles and subtitles together.
- The series title waits until the hook and the main character are set (2:39).

Recipe (real material + HTML/GSAP, Hyperframes):
- Ground: stills darkened `filter:brightness(.6) saturate(.4)` with a vignette; slow push `scale 1→1.06` over the shot (6-15 s).
- Recording: phone mock-up with an SVG waveform whose bars scale with the audio; subtitle `.sub{background:rgba(31,74,87,.85);font:600 3.6vh Montserrat;padding:.6vh 1.4vh}`; source block top left `font:700 3vh Montserrat;line-height:1.15`.
- Callout: photo card `border-radius:1.2vh`, gold arrow drawn with `strokeDashoffset` 0.4 s, then name box `background:#F2B400;color:#111;font:700 4.5vh Montserrat`.
- Chapter label: type on per character `stagger:.04`, gold bar `width:.5vh` blinking twice.
- Pacing: 5-7 s shots, never more than 3 cuts per 10 s; correspondent every 60-90 s.
- Mix: recordings ≈-20 LUFS short-term, bed 15-20 dB under; 0.4-0.5 s silence before each new recording; master -24 LUFS (web: -16).
