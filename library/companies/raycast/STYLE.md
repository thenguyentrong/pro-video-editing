# Raycast — launch style

Three official films measured at 480p (analyze_video.py, cuts checked by eye on cut sheets and 4-8 fps strips, EBU loudness, speech spans from a speech detector; nothing transcribed). Sizes are % of frame height (H).

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice |
|---|---|---|---|---|---|---|---|
| [New Raycast. Coming 2026 (2025)](new-raycast-coming-2026/notes.md) | 38.6 s | 12 | 3.21 / 2.22 | 2.41 · 3.21 · 1.61 · 4.82 | 0 % / 33 % | −13.2 | none |
| [Raycast, on the go. (iOS, 2025)](raycast-on-the-go-ios/notes.md) | 101.1 s | 21 | 4.80 / 3.68 | 5.04 · 4.20 · 2.80 · 6.31 | 0 % / 86 % | −13.8 | none |
| [It's out (2026)](its-out/notes.md) | 160.6 s | 31 | 5.18 / 4.38 | 3.65 · 4.46 · 5.02 · 6.69 | 0 % / 81 % | −14.2 | presenter to camera, 0-160 s |

## The core idea
Raycast is calm and exact. No film has a shot under 1 s; ASL is 3.2-5.2 s. Each film picks one device and does nothing else: rendered UI floating over dark chrome folds (teaser), a deadpan live-action object story in a white void (iOS), or a person from the company talking plainly to camera with screen inserts (launch day). Colour lives only in the product (the coral brand red #ff6363, emoji, app icons); everything around it is black, graphite or warm off-white. Type is small and technical: monospaced caps for lists, wide caps with full stops for end lines, Inter for cards.

## Rules with numbers
1. **No rush.** 0 % of shots under 1 s in all three films; 33-86 % over 3 s. Hold the opening shot 3.7-9.2 s.
2. **One feature per set-up** in UI films: 2.0-3.3 s per set-up, cut on the downbeat (27 % of cuts on onsets vs 7 % chance in the teaser).
3. **Speed lives in the text, not the picture.** The teaser's "NEW ___" list swaps a word every 0.25-0.5 s (≈10 swaps in 5 s) while the shot stays put.
4. **UI as a product shot:** UI panels rendered huge (search text ≈9 % H), tilted 10-20°, slow dolly, shallow depth of field, on a dark material background; never a flat desktop capture in the teaser.
5. **Show the product late in the story film:** in the iOS film the phone lights up at 89 % of the runtime; the first 89 % only removes the desk.
6. **Founder/team video = creator grammar:** two locked cameras (A/B cuts every 3-15 s on sentence ends), warm home-studio light, screen inserts ≈27 % of the runtime in 8 blocks of 2-8 s, two designed graphics in 160 s, no end card.
7. **End small:** two columns of tiny type on the centre line (≈2.7-2.9 % H), or a lone logo mark 1.9 s. No URL shouting, no CTA button.
8. **Mix:** −13.2 to −14.2 LUFS integrated (web level). Music-only teasers rise to the loudest point on the final text (loudest 0.5 s at 28.1 s and 95.8 s).

## Type
- Lists and feature names: monospaced caps (free: JetBrains Mono 400 / IBM Plex Mono), cap ≈2.9 % H, fixed two columns on the centre line ("NEW" at x ≈33 %, name at x ≈51 %), hard swaps.
- End lines: wide geometric caps with full stops (free: Lexend Exa 400 / Archivo SemiExpanded), cap ≈2.7 % H, left column at x 15 %, italic right column at x 73 %.
- Cards and overlays: Inter 400-500, white; "Public Beta" cap ≈9 % H beside a glowing app icon; side lists cap ≈5.5 % H at x 66 %, lines built 0.5 s apart.

## Recipe (teaser, 30-40 s)
1. Background: dark abstract fold loop (#000-#2b2b2b with soft grey highlights).
2. 8-9 UI set-ups of 2-3.3 s: HTML panels (`#1c1c1c`, radius 16 px, 1 px rgba(255,255,255,.08) border) in a 3D stage (`perspective 1400px; rotateY(-14deg) rotateX(6deg) scale(1.8)`), drifting `x -6% → +4%`, cut on the downbeat; one morph between two set-ups.
3. Hard cut to black; mono "NEW ___" list swapping every 0.3-0.5 s for ≈5 s; join to the product name, add "COMING <year>" under it; logo mark 1.9 s.
4. Music only, rising to the list; master ≈−13 LUFS.

## Recipe (live-action product story, 90-100 s)
Two locked-off set-ups on a warm white cyc (wide + top-down close), one deadpan action loop that removes everything the product replaces, shots 2-11 s, lights dim for the last 10 %, the product appears once at ≈89 %, one two-column end line for 5.5 s. Music + Foley, no voice, ≈−14 LUFS.

## Recipe (launch-day presenter video, 2-3 min)
A team member to camera with two cameras, warm practical light; inserts of the website, download page and screen recordings every 15-25 s; one "Public Beta" style title card with the app icon; one side list over the presenter; no end card; voice at ≈−14 LUFS with a very even level (LRA ≈2 LU).
