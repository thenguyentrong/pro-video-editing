# How India's Day Retail Traders Lost Billions  (Bloomberg Originals, 2026-09-21, 11:28, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=cndVRiZ9Pdc
Purpose: explainer / business documentary (reporter + expert interviews)
One-sentence point: Millions of Indian retail traders lost a combined $33 billion in options trading, mostly to high-frequency trading firms with faster machines.

First 150 s analysed (of 688 s).

Structure: beats with timestamps
- 0–7.8 s cold open: macro shots of a trading app (prices in red/green), keyboard, candlestick chart with a blue line drawing, a hand on a mouse, a "Buy" button being clicked (6.4 s) — 8 shots in 7.8 s.
- 7.8–11 s the reporter (Chiranjivi Chakraborty) in a grey office, wide then close.
- 11–34 s "the machines": light-trail road, candlesticks, a teal data-centre corridor (dolly, 5.8 s), a cell tower with radio rings, a pixelated eye inside a rounded card over a 3D data terrain, number grids, scrolling code, a red price line.
- 34.5–38.6 s first expert (Donald MacKenzie) in a warm living-room interview.
- 38.6–60 s order books on screens, office facade, a young trader at a laptop on a terrace, a second expert (fintech founder) by a window, silhouette against a glass wall, Mumbai trains.
- 60–68.2 s the crowd: station platform, then a stutter montage of phones in hands — 10 shots of 3 frames (0.125 s) each at 66.15–67.4 s.
- 69.2–74 s the evidence: an article/report page on black, blurred and dark except a central band; the phrase "combined $33 billion over the four years" boxed; "Source: Securities and Exchange Board of India" top-left.
- 74–86.7 s Mumbai: towers, a stock-exchange LED board, the BSE building with a TV screen, the Mumbai bull statue, commuters on a skywalk.
- 86.7–94 s chapter title "India vs. the HFTs" over an aerial of a business district (7.3 s shot, title fades in at ~88 s).
- 94–100.7 s archive: a crowded trading pit, traders on phones (old film look, 4:3-ish crop with black sides).
- 100.7–126.8 s data centres (corridors, cables, aerial of a server farm) intercut with the expert (lower third at 105 s, right-aligned).
- 126.8–135 s staged metaphor: an empty office chair under a single top light in front of a server rack (8.1 s hold).
- 135–137 s glowing number wall; 137–141.4 s reporter with lower third; 141–146 s aerial of a lone ship at sea; 146–150 s red candlestick chart falling on black.

Cut rhythm: 66 shots in 150 s, ASL 2.27 s, median 2.00 s. ASL per quarter 1.56 / 1.63 / 3.41 / 3.41 s (fast first half, calmer second half). Longest 8.1 s (empty chair), 7.3 s (chapter title aerial), 5.8 s (data-centre dolly). Shortest 0.12 s x 10 (the phone stutter montage). 29 % of shots under 1 s (mostly the 10-shot stutter + cold open), 24 % over 3 s. Densest 60–70 s (14 cuts) and 0–10 s (9 cuts). Cuts on audio onsets 45 % vs 48 % chance (cut on picture).

Typography: (Bloomberg's own grotesk; closest free "Inter" 600/700 — guess)
- Lower thirds: no box. Name bold ~4.2 % H font, role regular ~3 % H, two lines ("Reporter, Bloomberg News"; "Professor of Sociology / University of Edinburgh"). Placed on the open side of the frame: left x 10 % for a subject on the right, right-aligned x 90 % for a subject on the left; y 74–84 % H. Revealed by a colour sweep (red → magenta → white gradient passes through the text, ~0.6 s), then plain white. Held ~4 s.
- Chapter title: white semibold sans ~5 % H, centred, sentence case "India vs. the HFTs", fade in ~0.5 s, held ~5 s.
- Document focus: real article text at ~4 % H, everything blurred (~3 px) and darkened except one band; the key phrase sits in a light box; source line "Source: …" white ~2.2 % H top-left at x 6 %, y 7 %.
- Persistent bug: white Bloomberg "B" icon top-right (x 94 %, y 9 %).
- No captions/subtitles.

Colour/grade: dark, cinematic, teal-and-black for "machines" (data centres, cables, black screens with red/green prices), warm and soft for human interviews (living room, window light), neutral grey for the reporter. Crushed blacks, gentle highlight roll-off, mild contrast; no letterbox. Accent colours come from the subject itself (red/green candles), not from added graphics.

Camera/shots: cinema-camera b-roll with very shallow depth of field (macro screens, hands, phones), slow dollies down server aisles, drones (city, server farm, ship), interviews on two sizes (wide + close, often profile-ish), a staged metaphor shot (empty chair + spotlight), stock-style abstract renders (pixel eye on 3D terrain, number walls), archive trading-pit film.

Transitions: hard cuts only; the stutter montage acts as a transition into the evidence; chapter title fades. No graphics-driven wipes.

Sound: integrated -19.6 LUFS (quiet; median momentary -19.2, flat by quarter: -19.1 / -19.1 / -19.5 / -19.0). Pauses dip only to -31…-41 LUFS and nothing below -50 dBFS → a continuous score under everything (inference). Biggest moments: +24 dB rise at 103 s (after a 2 s dip at 101–103 s, into the data-centre section) and +28 dB at 137.5 s (reporter returns after a -41 LUFS dip). Small 0.5 s dips before section changes.

What makes it premium
- Feels like a tech thriller, not a news package: macro, shallow focus, dark teal grade, staged metaphor shots.
- Evidence is focused, not dumped: one phrase from the regulator's study, everything else blurred.
- The stutter montage (10 x 3 frames) turns "millions of traders" into one image in 1.25 s.
- Lower thirds sit in the subject's open space and use the brand colour only during the reveal.
- Calm second half (ASL 3.4 s) after a fast first half (ASL 1.6 s).

Recipe (real footage + HTML/GSAP, Hyperframes)
- Grade: `filter: contrast(1.08) saturate(.85)` + teal shadows (LUT or `mix-blend-mode:color` layer `#0d2a2e` at 15 % for "machine" shots); keep interviews warm.
- Document focus: page screenshot full-frame on #000; two copies: back copy `filter: blur(3px) brightness(.35)`; front copy masked to a horizontal band (`mask-image: linear-gradient(transparent 38%, #000 44%, #000 56%, transparent 62%)`); key phrase box `background:#e9e9e9; color:#111; padding:.1em .25em` scales in `scaleX 0 → 1, transformOrigin:"left"` 0.5 s `power2.inOut`; push the page `scale 1 → 1.05` over 4 s `ease:"none"`; source label `600 2.2vh` top-left.
- Stutter montage: 8–12 clips of the same action from different people, 3 frames each at 24 fps, hard cuts, then one 1 s hold on the last.
- Lower third: `font:700 4.2vh "Inter"` name, `400 3vh` role, white, no box; reveal with `background:linear-gradient(90deg,#fff 0 33%,#ff3b5c 50%,#ff8a00 66%,#fff 100%); background-size:300%; -webkit-background-clip:text; color:transparent`, animate `backgroundPosition 100% → 0%` 0.6 s `power2.out`; place at `left:10%` or right-aligned `right:10%` on the subject's open side, `top:74%`; hold 4 s, fade 0.3 s.
- Chapter title: `600 5vh` centred over a 7 s drone shot, fade in at +1.5 s, out 0.5 s before the cut.
- Pace: first half ASL ~1.6 s, second half ~3.4 s; one 8 s metaphor hold per section.
- Mix: voice ~-17 LUFS short-term, score always under (-25…-30 LUFS), dip the score to ~-40 LUFS for 0.5–2 s before each new section, then let it rise +20 dB.
