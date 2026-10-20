# National Geographic – nature and expedition documentaries (2018–2026)

Examples: `africa-earths-wild-home-trailer` (series trailer, 2026, 72.5 s), `ghost-elephants-trailer` (feature-doc trailer, 2026, 132.6 s), `forty-days-darkness` (Short Film Showcase, 2018, 224.6 s film). All on the National Geographic YouTube channel; channel end screens and closing credits excluded. Analysed Oct 2026.

## The style in one line
The yellow frame is the only brand device, and it goes into the world (inside a waterfall, inside a festival laurel, on a black card); the footage is hero nature or intimate observational life, and the type is either warm gold caps (blue-chip series) or classical spaced serif caps (auteur doc) or quiet small sans (short film).

## Measured overview
| film | length | shots | ASL | median | <1 s | >3 s | per quarter | LUFS |
|---|---|---|---|---|---|---|---|---|
| Africa: Earth's Wild Home trailer | 72.5 s | 62 | 1.17 s | 0.92 s | 56.5 % | 5 % | 1.29 / 1.07 / 1.21 / 0.95 | -19.2 |
| Ghost Elephants trailer | 132.6 s | 97 | 1.37 s | 1.04 s | 42 % | 8 % | 2.21 / 1.38 / 1.33 / 0.92 | -16.6 |
| Return of the Sun (40 days of darkness) | 224.6 s | 51 | 4.40 s | 4.08 s | 2 % | 76.5 % | 5.62 / 3.74 / 4.01 / 3.74 | -16.6 (TP +1.8) |

## Core idea
Two speeds. Trailers sell spectacle with a steady 1-second pulse that accelerates to 0.33–0.9 s at the end; short films sell patience with 4-second holds and one long hero shot. Both use credits (brand, narrator, director, festival) as big cards on the most graphic shots.

## Rules (with numbers)
1. **Brand mark in the world.** The yellow frame placed inside the first aerial (Africa, 1–3.5 s), as a "DOCUMENTARY FILMS" card on black (Ghost Elephants, 2 s), or in a festival-style laurel ≈25 % H (Short Film Showcase).
2. **Credit cards on graphic shots.** "FROM NATIONAL GEOGRAPHIC" on a dune; narrator credit over running silhouettes; director credit over a night sky; 1.2–2 s each.
3. **Trailer acceleration.** Quarter ASL falls to 0.92–0.95 s; the last 10 s use 0.33–0.4 s shots; 10–15 cuts per 10 s at the peak.
4. **Breath.** Dips to black of 0.5–1.8 s between sections (Ghost Elephants), one 3.1 s black with 2.2 s digital silence after the title.
5. **Short film patience.** Median 4.1 s, nothing under 1 s, one 11.7 s hold on the story's symbol, context given once on black (2 lines, 6 s).
6. **Type families.** Blue-chip: warm gold bevel caps ≈6.5 % H + white spaced eyebrow ≈2.8 % H. Auteur: spaced classical serif caps (eyebrow ≈2 %, name ≈4 %, title ≈8 % H). Short film: small geometric sans caps ≈3 % H, dark on snow.
7. **Bugs** top-left (series logo ≈2–3 % H) and streamer logos top-right on trailers.
8. **Loudness** -16.6 to -19.2 LUFS; nature trailers have no drop-outs; the auteur trailer goes from -21 to -11 dBFS and then to silence.

## Recipe (real footage + HTML/GSAP, 1920x1080)
- Series trailer 70 s: 60 hero shots, habitat sequence, logo-in-world, two credit cards, 3D title on a satellite map, sponsor card, fade to silence.
- Auteur doc trailer 130 s: 8 s texture open, logo + laurels on black, archive prints on black, director credits on night sky, press-quote block (real quotes only), accelerate, title on a monochrome plate, 3 s black silence.
- Short film 4 min: 4.6 s black credit, blizzard wides 5–8 s, small title on snow, laurel badge, ASL 4.4 s, one 12 s hero hold, one context card.
