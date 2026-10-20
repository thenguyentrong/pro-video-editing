# The Olympics – Games packaging style

Examples studied (Oct 2026):

| Example | Type | Format | Content length | Shots | ASL | Median | <1 s | Integrated / LRA |
|---|---|---|---|---|---|---|---|---|
| [grazie-mille-2026-cinematic-highlights](grazie-mille-2026-cinematic-highlights/notes.md) | closing highlight film cut like a fashion film | 16:9 | 180 s | 291 | 0.62 s | 0.57 s | 91 % | −26.4 LUFS / 9.4 LU |
| [mc2026-opening-ceremony-60](mc2026-opening-ceremony-60/notes.md) | social highlights of the live ceremony | 9:16 | 59.9 s | 28 | 2.14 s | 1.82 s | 18 % | −23.2 LUFS / 4.7 LU |
| [paris-2024-new-face-identity](paris-2024-new-face-identity/notes.md) | identity launch film (kinetic type) | 16:9 | 67.2 s (+5.8 s partner cards) | 64 | 1.05 s | 0.58 s | 67 % | −19.9 LUFS / 6.1 LU |

The first two are from the Olympics channel; the identity film is from the Paris 2024 organising committee's channel. Loudness is for the whole upload.

## The look in one paragraph
Olympic packaging is restrained around the footage and rich in culture. The rings are a small white corner bug on every shot and otherwise appear inside the event (in pyro, on boards, on kits). Each Games brings its own culture layer: Milano Cortina is told through Italian craft (a B&W fashion-film prologue, team kits shown like art in a painting gallery, "GRAZIE" printed on a garment), Paris through a custom Art Deco typeface used as stacks, rings, tiles and spirals in a gold/coral palette. Highlight films either cut very fast for minutes (ASL 0.62 s over 180 s, kept alive by a silent open and a quiet valley) or simply follow the live event in order (ASL 2.1 s, no text). Mixes are quiet: −20 to −26 LUFS.

## Sub-styles
1. **Culture highlight film.** Silent 3 s establishing aerial → B&W craft prologue → colour returns on an object → minutes at 0.5–0.7 s with a recurring "object" chapter shot every 20–30 s → a 10–15 s quiet valley at ≈55–60 % → end word on a real object.
2. **Live-event social cut.** Host feed reframed to 9:16, running order, 1–2.5 s shots, opening and peak held 5–6 s, original sound, corner bug only.
3. **Identity film.** Still lockup (6 s) → three chapters, one per symbol, each with its own card colour → fast mixed-media montage under giant outline words and ring text → word spirals collapsing into the lockup (10 s). Voice-over in the host language with on-screen subtitles.

## Rules (most important first)
1. **The mark is small; the event is big.** Rings bug ≈6–10 % of frame width top-right; the real brand moments happen in the footage.
2. **Culture before sport.** Craft, art, fashion and the host city frame the athletes.
3. **No supers in highlights.** No names, scores or captions; the identity film uses subtitles only.
4. **Give long fast cuts a breath.** Silence at the start (3 s), a quiet valley (−12 dB) in the middle, 0.3–0.4 s silences at section turns.
5. **Chronology for live events.** Keep the running order; select, don't rearrange.
6. **One typeface, many behaviours** (identity work): stack, ring, tile, spiral.

## Recipe (real or licensed footage + HTML/GSAP, Hyperframes)
- Highlight film: 3 s silent aerial; 20 s B&W prologue (`grayscale(1) contrast(1.1)`); 0.5–0.7 s shots; a recurring location shot every 20–30 s; music down 12 dB for 12 s at 55–60 %; end on an object with the message; mix ≈−23 LUFS (measured −26).
- Ceremony social cut: 25–30 moments, keyframed 9:16 crop, original audio at −23 LUFS, bug 108 px wide at `top:2%; right:3%`.
- Identity film: 4 flat brand colours; SVG `textPath` rings (outer outline 110 px, inner 32 px, counter-rotating 12°/s); tiled outline words over footage; spiral collapse `scale 1.6→0`, `rotate 0→180deg`, stagger 0.08 s; subtitles at 92 % height.
- The Olympic rings, Games emblems and footage are strictly protected marks; use your own mark and licensed footage.
