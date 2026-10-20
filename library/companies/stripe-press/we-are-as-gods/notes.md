# We Are As Gods – a film about Stewart Brand  (Stripe / Stripe Press with Structure Films, 2021-02-12, 2:21, 16:9, YouTube / Stripe channel)
URL: https://www.youtube.com/watch?v=hixwoe3UnqY
Purpose: trailer for a feature documentary about a counter-culture and tech pioneer, released by a company's publishing imprint
One-sentence point: one man's life links the 1960s counter-culture, the first personal-computer culture and today's ideas about the planet; the film is his story.

Structure:
- 0–4.5 PUBLISHER MARK: "Stripe Press" monogram (a looped S in thin lines) centred on aged cream paper; near-silent (-50 dBFS) with a 1.55 s silence twice.
- 4.5–8.5 STUDIO CREDIT: "STRUCTURE FILMS" in bold caps types/fades on over the same paper (8.5 s on paper in total, the longest shot).
- 8.5–16 FIRST IMAGE: black-and-white photos of the subject as a young man on a roof, shown as a triptych of photo frames side by side; three 0.13–0.33 s flicker cuts at 13.5–13.7.
- 16–43 1960s: colour 16 mm footage (desert, a top hat, a bus), old photo prints laid on paper with hand notes and pencil circles, a tinted (green) archive of an early computer demo with text on screen, office photos, hang-gliding (41–43).
- 43–60 HISTORY CONTEXT: 1960s news footage of politicians, a protest, a nuclear test cloud (53–56, loudest stretch -10 dBFS), contact-sheet strips, wall graffiti.
- 60.85–67.4 a TV studio clip held 6.5 s (archive interview), then a miner, a street.
- 72–83 COMPUTER ERA: an early tech founder and the subject at a desk (archive video), a commencement speech (78–83).
- 83–107 THE CATALOGUE: a group photo of the commune generation, the catalogue cover on a wooden desk (85–88), a magnifying glass moving over catalogue pages (89–92), book diagrams, a geodesic dome, a "SPACE COLONIES" book cover (100–101), illustrated pages.
- 107–119 TODAY: the subject on a cliff over a forest, a green terminal screen, a cluttered office, waves on rocks.
- 119–131 PRESENT-DAY PORTRAIT (densest, 13 cuts in 120–130 s): the subject now at the sea, climbing rocks, reading, colour present-day footage framed inside rounded photo borders on the paper.
- 131.8–140.3 TITLE: the subject seen from behind, hands on hips, on paper (8.5 s); title "WE ARE AS GODS" in serif caps with an underline, right of him; fade to black 140.3–141.2.

Cut rhythm: 71 shots in 141.2 s, ASL 1.99 s, median 1.58 s (adaptive detector). ASL per quarter 2.21 / 2.08 / 2.35 / 1.36 s. 30 % of shots under 1 s (many are photo flicks inside the collage), 15.5 % over 3 s. Cuts per 10 s: 1, 7, 6, 3, 5, 6, 3, 2, 4, 5, 4, 7, 13, 3. Longest: opening paper 8.5 s, title 8.5 s, TV studio clip 6.5 s. 37 % of cuts on an audio onset vs 45 % by chance (cuts follow the narration and music phrases, not beats). Many changes happen inside a shot (photos slide across the paper), so the felt pace is faster than the ASL.

Typography:
- Publisher mark: thin-line monogram + small humanist sans name (cap ≈2 % H) centred on paper.
- Studio credit: bold geometric-humanist caps (closest free: Josefin Sans 700 / Montserrat 700), cap ≈4 % H, warm dark grey with slight colour fringing, centred, fade ≈1 s.
- In-world type does the rest: catalogue covers, book covers with halftone display caps, typed notes, a terminal screen. No added captions, no lower thirds.
- Title: serif caps (closest free: Libre Caslon Text 700 / Playfair Display 700), cap ≈2.5 % H, dark brown, thin underline, placed right of the figure at y ≈52 %, x ≈60–85 %; small and quiet for a title.

Colour/grade: everything sits on one aged cream-paper ground with vignette, scratches and light leaks; archive kept in its own looks (black-and-white, faded 16 mm colour, green-tinted video) but given rounded photo borders, torn edges and paper shadows. Warm sepia overall; one green and one red tinted section.

Camera/shots: almost 100 % archive: photos, 16 mm film, TV news, documents, books; a few present-day shots of the subject (sea, cliff, office) treated to match. Rostrum-style moves: slow pushes over photos and books, a magnifying glass sliding across a page, photos sliding in and out over the paper.

Transitions: hard cuts plus collage moves: photos slide over the paper ground, triptych frames, flicker cuts of 3–4 frames, a fade from black at the start and to black at the end. Many soft transitions inside the paper world (score 0.5–1.2 at 10.0, 10.8, 29.4, 68.3, 70.8 s).

Sound: (I could not listen; from level data and picture.) Integrated -21.4 LUFS, LRA 5.0 LU, true peak -3.1 dBTP. Silent start (-50 dBFS for 4 s), then a steady bed at -20…-25 dBFS (2 s RMS) with archive voices and narration lines. Biggest rises +29 dB at 94.95 (the catalogue section) and +22 dB at 84.8; loudest stretch around the nuclear test footage (52–57 s). Fades to -35 at the title.

What makes it premium:
- One physical world (old paper) holds very different archive sources together.
- A company's name appears only as a small publisher mark; the subject and his ideas carry it.
- Real artefacts (catalogue, books, terminal) are filmed like objects, with a magnifier and hands, not as flat scans.
- Quiet open and quiet small title: confidence instead of hype.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- Ground: a cream paper texture `#efe3cc` with `radial-gradient` vignette to `#b89a72` at the edges, `mix-blend-mode: multiply` scratch/dust overlay at 30 %, a light-leak layer `screen` 15 %.
- Archive cards: each clip or photo in a frame `border-radius: 1.2vh; box-shadow: 0 1vh 3vh rgba(60,40,20,.45)`, filter per era (`grayscale(1) contrast(1.1)` for B/W, `sepia(.35) saturate(.8)` for 16 mm). Slide in `x: 30% → 0` over 0.8 s `power2.out`, slow push `scale 1 → 1.04` over the hold.
- Open: 4 s silence on paper with your mark (`opacity 0→1` 1 s), then a studio credit `700 4vh "Josefin Sans"`.
- Cut 1.5–2.5 s on average, flicker bursts of 3 frames for photo sequences, a 13-cut / 10 s build near the end with present-day footage in the same frames.
- Objects: film books/catalogues on a wooden desk with a magnifier moving across (2–3 s).
- Title over a figure from behind: `700 2.5vh "Libre Caslon Text"; letter-spacing:.04em; color:#3b2a1a; border-bottom:2px solid`, fade 1 s, hold 6 s, fade to black 1 s. Master ≈-18 to -21 LUFS.
- Stock/archive queries (public-domain or licensed): `1960s 16mm counterculture`, `vintage computer 1968 demo`, `old paper texture`, `magnifying glass old book`, `geodesic dome 1970s`.
