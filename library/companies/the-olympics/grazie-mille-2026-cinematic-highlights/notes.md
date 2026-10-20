# Grazie Mille Milano Cortina 2026 | Cinematic Highlights  (Olympics, uploaded 2026-02-23, 180.0 s, 16:9, YouTube / Olympics channel)
URL: https://www.youtube.com/watch?v=5ffk_5Fbdg4
Purpose: Games-closing highlight package / thank-you film (long-form highlights cut like a fashion film)
One-sentence point: the Games were made by craft, places and people, and the whole event is wrapped into one "thank you".

Structure (times from metrics.json):
- 0.0–3.2 HOOK: one aerial of the host city's cathedral at dusk in total silence (3.15 s digital silence).
- 3.2–23.0 PROLOGUE: black-and-white fashion-film footage: a sewing needle, a pattern on paper, a model's face, a tailor, fabric, an old car in a narrow street; then team kits displayed like art on mannequins in a painting gallery (colour returns at ≈20 s). 0.3 s silence at 22.7 s.
- 23.0–100 GAMES I: re-entry with a +25 dB rise at 23.25 s: athletes in their kits, start gates, skis, bobsleigh, ice, medal moments, mountain aerials as breathers (56–60 s), gallery kits again between sports every ≈20–30 s.
- 100–113 BREATH: quieter (−36 to −42 LUFS momentary), night ski jump, empty stadium, hugs; two short silences at 101.95 and 102.4 s.
- 113–175 GAMES II: the emotional half: celebrations, flags, tears, family, crowd, figure skating, halfpipe; same pace.
- 175–180 END: the gallery again, then the back of a white team hoodie with the word "GRAZIE" and the Games emblem (3.3 s, the longest shot); fade, 0.65 s silence.

Cut rhythm: 291 shots in 180 s, ASL 0.62 s, median 0.57 s, 91 % under 1 s, 97 shots/min, longest shot 3.3 s. ASL per quarter 0.56 / 0.63 / 0.82 / 0.52: three minutes at the same very high speed, only the breath around 100–113 s slows down. Adaptive detector; 10+ extra scene-detector candidates in the B&W prologue were not added (low-contrast B&W, not checked one by one), so the true ASL in the first 20 s may be slightly lower.

Typography: none added in the edit except the Olympic rings as a small corner bug (white outline rings, ≈6 % of frame width, top-right, ≈3 % margin) on every frame. All other type is in the world: country names and flags on kits, Games "look" graphics on boards and ice, the final "GRAZIE" printed on a garment (a soft serif-display in blue, ≈18 % of frame height). Closest free for a similar end word: "Fraunces" 700 or "DM Serif Display".

Colour/grade: two worlds: B&W fashion prologue with soft vignette; then warm, low-key gallery shots (wood, gold frames) alternating with cold bright snow and ice; teal/blue sports venues. Blacks soft, not crushed; filmic.

Camera/shots: fashion-film macro (needles, fabric), handheld close-ups of athletes, broadcast and drone sports shots, mountain aerials, gallery dolly moves around mannequins in kits, slow-motion celebrations.

Transitions: hard cuts only (two black flashes folded: 28.7, 155.3 s); the gallery kits act as recurring "chapter" shots instead of graphics.

Sound: music-led, mixed quietly: integrated −26.4 LUFS, LRA 9.4 LU, true peak −4.6 dBTP. Silent first 3.15 s; momentary −23 to −33 for most of the film, loudest 0.5 s at 42.1 s (−20 momentary); the 100–113 s breath drops to −36…−42; fade from 175 s. Cuts are not on onsets (10 % vs 9 % chance). I did not listen; music style and any voice are not verified.

What makes it premium:
- The highlight reel borrows a fashion-film language (B&W craft prologue, kits as museum pieces), so sport footage reads as culture.
- A recurring "chapter" image (kits in the gallery) instead of title cards.
- Silence at the start and a quiet valley in the middle make a 3-minute fast cut breathe.
- The end word is a real object (printed on a garment), not a graphic.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- 3 s silent establishing aerial → 20 s B&W craft prologue (`filter: grayscale(1) contrast(1.1)`, vignette 0.6) → colour returns on a gallery/object shot → 0.3 s silence → music in.
- Body: 0.5–0.7 s shots for minutes; every 20–30 s insert one recurring "object" shot (the same location, different item) as a chapter marker; one 10–15 s quieter valley at ≈55–60 % of runtime with the music down ≈12 dB.
- Corner bug: event mark as white SVG, 110 px wide at 1920, `top:3%; right:3%`, opacity 0.9, on all shots.
- End: one 3 s hero object with the message on it; fade 1 s; 0.6 s silence.
- Mix ≈−23 LUFS if the platform normalises; the measured −26 is quieter than most online sports films.
- Stock queries: "sewing needle macro black and white", "tailor fabric close up", "museum mannequins gallery", "dolomites aerial winter", "ski jump night floodlight", "athletes celebrating snow".
