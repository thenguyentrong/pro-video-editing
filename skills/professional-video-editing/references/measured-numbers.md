# Measured numbers from real films (Oct 2026)

Measured from official YouTube uploads at 480p (adaptive cut detection, every Spider-Man cut checked by eye; EBU loudness in 50 ms windows; text sizes as % of frame height H, ±1%). One sample per category here, so treat these as anchors, not laws; the style files add 2–10 measured examples each. Measure your own with `scripts/analyze_video.py`.

| Film | Length | Shots | Average shot length (ASL) / median | ASL by quarter | Silence | Biggest hit |
|---|---|---|---|---|---|---|
| Spider-Man: Brand New Day, new trailer | 154.5 s | 135 | 1.14 / 1.04 s | 1.07 · 1.10 · 1.02 · 1.33 | 0.35 s at −59 dBFS right before the last burst | +31 dB, 2.7 s before the title |
| Avengers: Doomsday trailer | 143 s | 65 | 2.20 / 1.46 s | 3.25 · 1.38 · 1.49 · 5.11 | 2.7 s cut to black, then ~10 s held near −45 dBFS | +28 dB, title cut 0.6 s later |
| Apple iPhone 17 Pro film | 54 s | 39 | 1.38 / 1.40 s | 1.12 · 1.50 · 1.04 · 1.69 | none (music within ±3 LU) | hero push-in at 46 s |
| Apple Watch Series 12 film | 92.5 s | 93 | 0.99 / 0.92 s | 1.10 · 0.93 · 0.86 · 1.01 | 1 s pulse, short black blinks | montage peak at 67 s |
| Nothing Phone (3a) launch | 110 s | 33 | 3.33 / 2.80 s | 3.06 · 3.06 · 2.50 · 3.93 | bed −12 dB under the typed title | +32 dB on the first product cut |
| Johnny Harris documentary (first 90 s) | 90 s | 41 | 2.20 / 1.54 s | 3.21 · 1.32 · 1.61 · 3.75 | 1.6 s at −63 dBFS | +36 dB out of that silence |

## Rules derived from the numbers

**Trailers**
1. Body pace: ASL 1.0–1.3 s; 45% of shots under 1 s, only 1% over 3 s; shortest normal shot ~0.4 s.
2. In these two trailers peak cut density sits at **50–65 % of the runtime** (9–12 cuts per 10 s); across the trailers in `styles/movie-trailer.md` it ranges from 30–75 % (Marvel) to 60–92 % (streaming, A24, Warner, NEON, Pixar). Neither trailer here accelerates into the end: the last 15–25 % slows down (closing scene ASL 1.6–2.4 s, title shot 3.5 s or longer). Build the climax in the middle-late part, then let the ending breathe. The title itself lands at 83–96 % of the runtime in most measured full trailers (73–76 % only when a scene, scare or gag follows it).
3. Two openings: slow (ASL ~3.5 s for ~24 s with 1.6–1.9 s fades to black) or fast (ASL ~1.0 s for ~17 s ending on a +25 dB hit on the logo).
4. Before the title: cut the sound for ~0.35 s (to −51…−59 dBFS), the hit 0.9 s later, the title cut 0.6 s after the hit.
5. Before a closing scene: 2–3 s of black, then ~10 s with the music nearly gone. Comic beats get 0.5–0.85 s of dead air.
6. Text: only 4–6 cards in the whole trailer, 1–4 words, centred. Taglines hold 1.0–1.6 s, title/date 2.4–3.5 s. A date can be typed one token per beat (~0.67 s). Title type: heavy extended caps ~6% H for taglines, title word ~23% H with a small subtitle ~4% H.

**Apple**
7. ASL ~1.4 s, nearly flat across the film (quarters 1.0–1.7 s). Text on screen ~57% of the time; product on black ~43% of shots; the frame is ≥ 70% empty in about half the shots.
8. Body text: 2–5 words, regular/medium weight, normal tracking, cap height ~4% H, centred at 50% height, hold 1.2–1.8 s (~2.5 words/s), words fade grey → white one by one over 0.3–0.4 s, leave with a 0.4 s crossfade, mostly on black.
9. Punch words: one word per card, 0.5–0.65 s, hard cut on the beat, each card 1.5–2× bigger than the last (e.g. 8% → 16% → 22% H).
10. The iPhone 17 Pro film keeps its music steady (about −16 LUFS, within ±3 LU) and only fades for the logo (~1.3 s), but this is not a rule: 5 of the 10 Apple films in the library have short drop-outs of 0.2–1.8 s before the biggest hit or joke. Trailers mix at −14 to −17 LUFS.
11. Lifestyle montage: ASL ~1.0 s (0.78 s in the middle 40%); 72% of cuts land within 0.1 s of a music onset.
12. End lockup: build the last line in 3 chunks on beats ~1 s apart, hold 4 s, fade the logo in over 0.5 s, hold 2.5 s.

**Startup launch / documentary**
13. Product-render launch film (Nothing): ASL ~3.3 s, 42% of shots over 3 s, scene changes by morphing/assembling the product rather than cutting; open with ~6 s of black + typed text, then a +32 dB hit on the first product shot.
14. Documentary: long takes (~3.7 s) under the opening voice, faster (~1.4 s) in the middle, long again in quoted clips; captions build word by word in the lower third, cap height ~3% H; 1–1.6 s of real silence as a reaction beat before a loud return.

## Applying it to a 60–70 s pitch film
Open slow and confident (2–4 shots), run the evidence at ~1.0–1.3 s per shot with its densest part around 55–65% of the film, put a 0.35–2 s silence before the turn, land the turn on the biggest hit, then slow down (2–3.5 s shots) for the solution and end card. Use 4–6 text cards in total, not one per line.
