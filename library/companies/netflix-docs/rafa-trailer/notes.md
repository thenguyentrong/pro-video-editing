# Rafa | Official Trailer | Netflix  (Netflix, 2026-05-19, 2:40 file = 147.3 s trailer + 13 s YouTube end screen, 16:9, YouTube / Netflix channel)
URL: https://www.youtube.com/watch?v=tQ31ScZSYFQ
Purpose: trailer for an athlete documentary series (career + retirement)
One-sentence point: the series shows what was behind a legend's career: pain, family and the will to "endure one more ball"; out May 29.

Structure (0–147.3 s):
- 0–8.4 INTIMATE OPEN: phone/handheld home video in a house: the athlete with his child, family voices, burned-in English subtitles. Series bug top-left ("RAFA" with a thin red rule), N top-right.
- 8.5–23 THE ANNOUNCEMENT: shoes on clay, a press-room or stadium address (4.6 s, the third-longest shot), a serve toss on black, an empty stadium at night. Shots 1–4.6 s, subtitles carry his spoken lines.
- 23–35 FLASH OF THE CAREER (densest, 14 cuts in 20–30 s): trophies and camera flashes at 0.17–0.2 s per shot, an MRI scan of a knee (27 s), a wedding photo, the crowd.
- 36–43 CONFESSION: a 7.0 s close interview in low-key light (head bowed, hand at the eyes), a 0.95 s near-silence to -50 dB at 39.5 before his next line.
- 43–45 MID-TRAILER N STING on black (the Netflix brand placed as a chapter break, not only at the end).
- 45–92 THE STORY: TV news report of his comeback (subtitles), home gym, a swimming pool, archive of him as a boy training with his coach (55–65), the coach today in interview, archive matches, bandaged hands, an X-ray, a medical scan, his wife and family interviews, rivals in interview.
- 92.47–94.4 CARD on black "THE FIGHT TO BE A / CHAMPION" (2.0 s).
- 94.5–105.9 RIVALS + GLORY: rival players in interview, archive finals, trophy lifts.
- 105.9–107.8 CARD on black "THE COURAGE TO BECOME A / LEGEND" (1.9 s).
- 108–132.9 CLIMAX: driving to a match, doctors, team on the bench, a boy's face in old home video, wins at four slams, crowd chants; music up to -13…-14 dBFS.
- 133–139 FINAL IMAGE: an overhead of him lying on the clay after a win, racket thrown aside; one subtitle line.
- 139.5–141.5 TITLE "R A F A" thin wide-spaced caps on black; 141.5–143.5 "ONLY ON NETFLIX / MAY 29" on light bars; 144–147 N sting (+18.7 dB at 144.9), fade to silence.

Cut rhythm: 103 shots in 147.3 s, ASL 1.43 s, median 1.13 s (adaptive detector + 2 verified flash cuts at 23.27 / 23.69 added). ASL per quarter 1.15 / 1.84 / 1.05 / 1.94 s. 42 % of shots under 1 s, 5 % over 3 s. Shortest 0.17–0.21 s (trophy flashes 23.5–27 s); longest: final aerial + title + date + N counted as one 14.4 s block, the 7.0 s confession, the 4.6 s announcement. Cuts per 10 s: 4, 5, 14, 8, 4, 6, 7, 9, 9, 8, 9, 6, 8, 5. 31 % of cuts on an audio onset vs 29 % by chance (cut on speech, not on beats).

Typography:
- Burned-in subtitles for all Spanish speech: white sans with a soft shadow, cap ≈3.5 % H, 1–2 lines, centred, bottom at y ≈92 %. They are part of the design: almost every story beat has a line on screen.
- Mid cards: two-size wide-tracked caps on black: small line ≈1.5 % H, tracking ≈0.5 em, over a big word ≈4 % H, tracking ≈0.8 em, light warm grey, centred at y ≈52 %; a classical serif-like display (closest free: Cinzel 400 / Cormorant SC). Fade in/out ≈0.3 s, 1.9–2.0 s each.
- Title: "R A F A" in the same spaced caps, cap ≈4 % H, tracking ≈2 em, centred on black, 2 s.
- Bug: "RAFA" small caps with a red rule top-left in the first seconds; "NETFLIX" wordmark top-right after.

Colour/grade: warm, natural, slightly desaturated present-day footage (homes, interviews in low-key warm light); archive TV and home video left as is (soft, 4:3 sources pillar- or crop-fitted); terracotta clay as the signature colour. Cards and title on pure black. Full 16:9.

Camera/shots: sit-down interviews in very tight, low-key frames (half the face in shadow), observational handheld at home, phone home video, medical imagery (MRI, X-ray) as evidence of pain, decades of broadcast archive, one overhead final image.

Transitions: hard cuts; cards and title cut or fade from black; camera flashes used as natural white flashes inside the trophy burst; mid-trailer N sting as a chapter break.

Sound: (I could not listen; from level data and picture.) Integrated -14.7 LUFS, LRA 8.6 LU, true peak -1.5 dBTP. Opens quieter (-20…-27 dBFS) with home-video sound and speech; builds to -13…-14 in the climax (118–134 s). One planned near-silence (0.95 s to -50 dB at 39.5) in the confession. Biggest rise +18.7 dB on the final N sting.

What makes it premium:
- Intimacy first: home video and a confession before any glory.
- Pain is shown as evidence (MRI, X-ray, taped hands), not described.
- Two quiet cards on black with spaced classical caps split the trailer into "champion" and "legend".
- The last image is one overhead hold of a body on clay, then a single word title.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- Order: home video (8 s) → announcement (15 s) → 10 s flash burst of career highs (0.17–0.25 s each, use camera-flash frames as the cut points) → 7 s confession close-up with a 1 s silence before the key line → brand sting → story 45 s → card → glory 11 s → card → climax 25 s → one 6 s overhead final image → title.
- Subtitles: `font: 500 3.5vh Inter; color:#fff; text-shadow: 0 1px 4px rgba(0,0,0,.6); bottom: 8%`, 1–2 lines, on for the whole spoken phrase.
- Cards: small line `400 1.5vh Cinzel; letter-spacing:.5em` over big word `400 4vh Cinzel; letter-spacing:.8em; color:#d9d4cc`, on `#000`, fade 0.3 s, hold 1.4 s.
- Title: one word `400 4vh Cinzel; letter-spacing: 2em`, 2 s. Date card 2 s. Master -14 to -15 LUFS.
- Stock/own footage queries: `tennis clay court overhead`, `athlete interview low key dark`, `knee mri scan`, `stadium camera flashes trophy`.
