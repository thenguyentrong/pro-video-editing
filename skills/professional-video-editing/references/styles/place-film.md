# Place film
**Use it for:** films that sell or celebrate a place or a building: a city reel, a campus or event-location film, a tourism campaign, a "why live here" recruiting film, an architecture or construction project film, a competition or pitch film for a design. **Not for:** product launches (use apple-precision or design-tech), fast trailers (use movie-trailer), explainers with charts and narration (use editorial-explainer), robot or machine demos (use industrial-robotics).
**Reference films:**
Independent creator — Brand New Day, Aachen city film (2026, 110.4 s) — aachen-city-film/brand-new-day
Visit OSLO — Is it even a city? (2024, 105.9 s) — visit-oslo/is-it-even-a-city
Visit OSLO — It's totally even a city! (2026, 203.1 s) — visit-oslo/totally-even-a-city
Visit OSLO — This is Oslo (2023, 123.3 s) — visit-oslo/this-is-oslo
Switzerland Tourism — No Drama (2021, 90.5 s) — switzerland-tourism/no-drama
Switzerland Tourism — No one upstages the Grand Tour of Switzerland (2022, 130.0 s) — switzerland-tourism/grand-tour-hathaway
Switzerland Tourism — Beautiful Autumn (2025, 128.0 s) — switzerland-tourism/beautiful-autumn
VisitDenmark — The Danish Zen (2024, 109.0 s) — visit-denmark/danish-zen
VisitDenmark — Greetings from The Land of Everyday Wonder (2021, 132.5 s) — visit-denmark/land-of-everyday-wonder
VisitDenmark — Holiday homes, German cut (2024, 45.0 s) — visit-denmark/holiday-home
BIG – Bjarke Ingels Group — 2 World Trade Center (2015, 180.2 s) — big-architects/2-world-trade-center
BIG – Bjarke Ingels Group — New Tamayo Museum (2010, 117.1 s) — big-architects/tamayo-museum
BIG – Bjarke Ingels Group — Danish Pavilion bike ride (2010, 132.5 s) — big-architects/danish-pavilion-bike

## Signature
The place is the star, but it is never sold with a plain list of sights. The best films we measured put the place inside a frame that gives it meaning: a movie's opening credits (places credited as cast), a local who complains about things that are really benefits, two celebrities arguing while the landscape wins, or one architectural idea drawn on black and then proven in slow camera moves. Shots are real, composed and often still; text is rare and small; one song or one voice carries the film. The plain drone montage with captions (This is Oslo) was measured as the baseline: clean, but it could sell any city.

## Numbers
All values are measured in the reference films (analyze_video.py at 480p or 360p; text in % of frame height H on 16:9 frames). "≈" marks values judged by eye from frames.

| Measure | City film, composed tableaux (credits or deadpan local) | Tourism campaign with a star or presenter | Destination montage (baseline) | Architecture project film |
|---|---|---|---|---|
| ASL | 2.67–3.31 s | 1.42–3.10 s (dialogue 1.42–1.68) | 1.16–1.93 s | 4.1 s (live + CG); 6–16 s per render move; takes up to 57 s |
| Median shot | 2.06–3.32 s | 1.16–1.92 s | 1.04–1.60 s | 3.7–16 s |
| Shots under 1 s | 0–9 % | 10–35 % | 5–37 % | ≈0–5 % (excluding sped-up frames) |
| Shots per minute | 18–22 | 19–42 | 31–52 | 3.6–14.6 |
| Cut curve | flat grid: credits film exactly 3 cuts per 10 s (3.24–3.44 s shots); deadpan 1–5 cuts per 10 s | densest 10 s at 55–75 % of runtime (9–10 cuts); 1–2 long takes of 9.8–15.4 s allowed | even (6–11 cuts per 10 s) or slowing every quarter (1.54 → 2.37 s) | long opening on black, slow middle, coda on black |
| Cuts on music onsets | at chance (9 % vs 8 %; 29 % vs 33 %) | at chance (38–49 %) | at or below chance (8–27 %) | at or below chance (0–26 %) |
| Main text size | credit role 1.9 % H, name 3.1 % H; subtitles ≈2.7 % H; handwritten super name ≈6 %, role ≈3.8 % | taglines ≈3–6 % H; lower third name ≈3.8 %, role ≈2.5 %; pun supers ≈7 % | captions ≈4.5 % H; titles 8.5–9 % H | credits role ≈3 % H over a ≈6 % logo; title cap ≈5.4 % |
| Text moments | one per shot (credits, 32 in 110 s) or one subtitle per line | 3–8 (supers + 2-step tagline + logo) | 1 title + 0–8 captions + URL | 4–6 credits/logos, 0 captions |
| Text animation | none: on with the cut, off with the cut | hard switch (serif taglines) or ≈0.5 s fades (sans system) | ≈0.4 s fades | ≈0.6–1 s fades; letters build in random order (title) |
| End block | last card 3 s + 2.1 s black; or logo over an 8.5 s last shot | 7.4–11.6 s plate: tagline 1 (≈3 s) → tagline 2 (≈2–3 s) → logo (≈2.5 s); optional 2.6 s button after the logo | 2.5–5.3 s aerial with URL or logo | 12.1 s diagram on black, or 15 s credits on black |
| LUFS (integrated) | −18.4 (song only), −16.5 and −13.7 (voice) | −17.4 to −9.0 (use −14 to −16) | −14.0 to −12.2 | −17.4 to −11.1 |
| LRA | 1.8 LU (song only); 7.5–10.5 (voice) | 5.0–9.5 LU | 2.8–11.4 LU | 4.5–18.4 LU |
| Voice | none (credits) or one local's monologue with subtitles | dialogue between stars, or presenter to camera | none | architect on camera, or none |
| Aspect | 2.39:1 (credits film) or 16:9 | 16:9, or ≈2.35:1 letterbox inside 16:9 | 16:9 | 16:9 |

Per film (shots, ASL / median, % under 1 s, LUFS):

| Film | Shots | ASL / median | <1 s | LUFS |
|---|---|---|---|---|
| aachen-city-film/brand-new-day | 34 | 3.25 / 3.32 | 0 % | −18.4 |
| visit-oslo/is-it-even-a-city | 32 | 3.31 / 3.00 | 0 % | −16.5 |
| visit-oslo/totally-even-a-city | 76 | 2.67 / 2.06 | 9 % | −13.7 |
| visit-oslo/this-is-oslo | 64 | 1.93 / 1.60 | 5 % | −12.2 |
| switzerland-tourism/no-drama | 54 | 1.68 / 1.32 | 24 % | −17.4 |
| switzerland-tourism/grand-tour-hathaway | 42 | 3.10 / 1.92 | 10 % | −14.6 |
| switzerland-tourism/beautiful-autumn | 90 | 1.42 / 1.22 | 23 % | −9.0 |
| visit-denmark/danish-zen | 71 | 1.54 / 1.16 | 35 % | −16.3 |
| visit-denmark/land-of-everyday-wonder | 114 | 1.16 / 1.04 | 37 % | −14.0 |
| visit-denmark/holiday-home | 27 | 1.67 / 1.52 | 7 % | −12.2 |
| big-architects/2-world-trade-center | 44 | 4.10 / 3.72 | 5 % | −17.4 |
| big-architects/tamayo-museum | 7 | 16.7 / 16.0 | (title and credits on black inside the first and last shot) | −13.4 |
| big-architects/danish-pavilion-bike | ≈20 real | two takes of 57.0 s and 39.5 s | (detector inflated by sped-up frames) | −11.1 |

## Structure
**City film as opening credits** (110 s): 0–2 % black with the song already playing (1.9 s) → 2–5 % hook shot + title → 5–23 % "production" credits (studio line, writer, editor, featuring) → 23–90 % cast: one place per shot → 90–95 % the authors (camera, lens, creator) → 95–98 % last card, music drops out 0.8 s under it, one final note on the cut → 98–100 % black (2.1 s).

**Deadpan local** (106 s): 0–6 % cold open on the character with the city active behind him → ≈20 % handwritten name super → 6–92 % one complaint per shot, the city proves him wrong in the background → last 8 % one long dusk shot with the logo.

**Tourism campaign with a star** (90–130 s): 0–3 % cold open (star alone, or the place as "a film") → 3–15 % setup (call, screening, shoot) → 15–55 % argument; every 3rd–4th shot shows scenery inside the story (on a screen, behind a window) → 55–75 % gag or scenery montage at ≈1 s per shot → 75–90 % turn, one long take → last 7–12 s end plate with the two-step tagline and logo; optional button.

**Architecture project film** (120–180 s): 0–10 % logos or film-style credits (on black or over context footage) → 10–20 % the concept in its simplest form (a 7 s line diagram on black, or CG boxes composited into the real street behind the architect) → 20–85 % slow moves outside → inside → roof, day → dusk → night, people in every frame → 85–100 % the building in its city, then a diagram or credits coda on black, ending in silence.

## Picture
- **Real places, real people, small in frame.** The city or building does something behind the subject (divers, trams, crowds on a ramp).
- **Composition first:** locked-off wides with a large calm area (sky, wall, lawn, water). Low angles against sky give clean space for text and make ordinary buildings heroic.
- **Two lighting worlds** for contrast stories: dark, cool interior vs golden landscape; dark cinema room vs bright screen; teal studio vs sunny memory.
- **Screens inside the frame** (laptop, phone, cinema screen, wall screens) let scenery appear inside a story without becoming an ad.
- **Architecture:** symmetric interiors, top-down drone views of plazas and roofs, slow push/orbit/rise moves of 6–16 s, people for scale in every render.
- **Grade:** one look per film. City credits film: warm, soft film simulation (start with `contrast(.95) saturate(.92) sepia(.06)` and grain 0.05–0.07, ≈ tune by eye). Tourism: warm golden hour and haze; Nordic films: clean natural daylight and pastel dusk.
- **Aspect:** 2.39:1 for the credits film (bars 138 px on 1080p), ≈2.35:1 for a cinema-themed campaign (131 px), otherwise 16:9.

## Type
- **Credits (city film):** role over name, caps, light geometric sans with wide tracking. Free font: Montserrat 300–400. Role 1.9 % H (21 px on 1080p, tracking .22 em), name 3.1 % H (34 px, tracking .16 em), gap ≈0.7 × name height. Placed in the calm area of each shot, so the position moves (centre, right third at x 70–94 %, bottom centre at y 82–92 %, upper sky). No box, no shadow, no fade.
- **Subtitles (deadpan local):** white sans (Inter 500), cap ≈2.7 % H, on `rgba(0,0,0,.55)`, bottom centre, one per spoken line.
- **Handwritten super:** name ≈6 % H, role ≈3.8 % H, next to the subject. Free fonts: Patrick Hand or Gaegu.
- **Campaign tagline, serif version:** soft bold serif, sentence case, white, centred, 2 lines then 1 line, cap ≈6 % H. Free font: Fraunces 700 (soft) or Young Serif. Hard switch between cards.
- **Campaign system, sans version:** wordmark bug top-right ≈3 % H; lower thirds bottom-left (x ≈4.5 %, y 60–70 %), name 3.8 % H / role 2.5 % H (Plus Jakarta Sans 600/500); one-line tagline ≈3 % H, ≈0.5 s fades.
- **Destination brand block:** heavy geometric caps (Montserrat 800–900), stacked 3 lines, leading ≈0.9, titles 5.5–8.5 % H, one red accent word.
- **Architecture:** neo-grotesque (Inter/Arimo) light + bold in one line, cap ≈5.4 % H; credits as role ≈3 % H over a logo.

## Transitions
- Hard cuts in almost every film. Text cuts with the picture in the credits film.
- Dissolves only in end montages (≈1.2 s) and in architecture films, where the project's own pattern makes the wipe (halftone dot dissolve, façade-pattern wipe).
- Composited idea → building: CG lines or boxes appear inside a live shot, box by box every 0.5–0.8 s.
- Jump cuts along one path compress a ride or walk between two long takes.
- Finale oner (25–30 s): push in on the last line, crane up to the skyline, logo fades in.

## Sound
- **One song or one voice.** Song-only films are flat (LRA 1.8–3.5 LU); voice films swing more (7.5–10.5 LU).
- **Cuts follow bars, lines or movement, not hits** (onset sync at chance in every film).
- **Silence as punctuation:** 1.3 s drop-out before a key word card; 2.8 s silence before a chorus; 0.8 s drop-out under the last card; end cards in silence; 0.8–1.5 s of silence at the start of architecture and montage films.
- **Start over black with the music already playing** (1.4 s in the credits film).
- **Masters vary from −18.4 to −9.0 LUFS.** For online delivery use −14 to −16 LUFS, true peak −1 dBTP.

## Do / Don't
**Do**
- Find a frame for the place (credits, a complaining local, a celebrity conflict, one diagram) before you pick shots.
- Turn every complaint or joke into a benefit of the place.
- Hold composed shots ≈3.3 s; keep a steady grid when the film has no story beats.
- Show scenery inside the story (screens, windows, backgrounds).
- Put people in every architecture shot.
- End with a calm plate: a 2-step tagline and a logo, or a diagram on black.

**Don't**
- Don't make a sights list with captions as the main idea; it is the generic baseline.
- Don't add fades, slides or boxes to the credits film.
- Don't use more than one grade, one song or one type system.
- Don't name facts and numbers on screen in architecture films; show them.
- Don't master as hot as −9 LUFS / +1.4 dBTP.

## Recipe
Target: 1920×1080 (or 2.39:1 inside it), 24/25 fps, real or licensed footage plus HTML/GSAP compositions (Hyperframes).
1. **Pick the variant** (below) and write the frame in one sentence: "the city as a superhero opening", "a local who finds the city too easy", "a star who refuses the ad".
2. **City credits film:** choose a 70–75 BPM song; bar = 240/BPM s (≈3.3 s); N shots = runtime / bar. Write N credits in film order with real places and 3–5 self-aware jokes. Cuts at `t_i = t0 + i * bar`. Credit on/off with `tl.set(credit,{opacity:1},t_i); tl.set(credit,{opacity:0},t_i+bar)`.
3. **Deadpan local:** 30–35 locked-off shots for 105 s, one line each; subtitles on every line; one handwritten super at ≈20 %; an 8 s dusk shot with the logo (fade in 0.5 s at +1 s).
4. **Star campaign:** cold open 2–4 s; dialogue at ASL ≈1.5 s; a 10 s montage at ≈1 s per shot at 55–75 %; one long take for the turn; 9 s end plate: tagline 1 at +0.7 s, tagline 2 at +3.7 s, logo at +6.7 s.
5. **Architecture film:** logos 3 s on black; 7 s line diagram (white 2 px strokes, `power2.inOut`); 6–10 slow moves of 8–16 s with people; a pattern mask wipe in the middle (`mask-image` of the façade pattern, scale 0→1.5 in 0.8 s); 10–12 s diagram coda on black in silence.
6. **Grade and frame** as in Picture; add the bars on top of everything.
7. **Sound:** song or voice only; place 1–2 real silences; master `loudnorm=I=-16:TP=-1`.
8. **QC:** on a phone, every credit or subtitle is readable and never on a face; no two shots of the same size in a row in the tableau films; the logo plate is calm.
9. **Stock queries (licensed, no AI people):** "old town street wide static morning", "facade low angle blue sky", "university canteen wide", "harbour swimming jump slow motion", "aerial peaks sea of fog sunrise", "lake steamer aerial autumn", "cable car over lake aerial", "top down plaza drone people", "modern museum interior symmetric", "bike ride follow shot ramp", "city skyline dusk bridge".

## Variants
- **City opening-credits film** (aachen-city-film/brand-new-day): 2.39:1, 32 shots of 3.24–3.44 s, one two-tier credit per shot (1.9 % / 3.1 % H) that cuts in and out with the picture, places credited as cast, one flat song (−18.4 LUFS, LRA 1.8), 1.9 s black open and 2.1 s black tail. Pair it with opening-credits.md.
- **Deadpan local** (visit-oslo/is-it-even-a-city): ASL 3.31 s, 0 % under 1 s, still centred character, subtitles on every line, handwritten super, 8.5 s logo plate. Sequel form: switch to a musical at ≈50 %, 2.8 s silence before the chorus, 28.7 s finale oner.
- **Tourism campaign with a star** (switzerland-tourism/*, visit-denmark/danish-zen): ASL 1.42–1.68 s on dialogue, scenery inside the story, densest montage at 55–75 %, 7–12 s end plate with "When you need ... / You need [place]" and logo. Presenter form: direct address with jump cuts every 1–1.5 s and one verbal pun turned into type.
- **Architecture project film** (big-architects/*): concept diagram on black, architect on site with composited massing, slow render moves of 6–16 s with people, pattern wipes, diagram coda; or the building as one continuous ride (takes of 57 s and 39.5 s around a jump-cut middle).
- **Destination montage** (visit-denmark/land-of-everyday-wonder, visit-oslo/this-is-oslo): ASL 1.16–1.93 s, even density or slowing quarters, matched shapes, a 2 % H location bug or 8 captions; use only when there is no story frame.
- **Face–memory film** (visit-denmark/holiday-home): faces in a teal studio cut against bright memory shots (1.5–2 s / 1.0–1.3 s), one tagline at the end.
- **Vertical (9:16):** keep the 2.39:1 band (452 px tall on 1080×1920) for the credits film and size text as % of the band; for the deadpan form keep the subtitles inside the lower safe zone (above 20 % from the bottom).
