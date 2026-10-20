# KUKA - style

Examples (official @KUKARobotGroup uploads):
| Example | Date | Length | Shots | ASL | Median | % < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [kmf-1500p-autonomous-forklift](kmf-1500p-autonomous-forklift/notes.md) | 2026-10 | 1:59 | 17 | 6.97 s | 6.40 s | 0 % | -14.8 | CGI product launch with VO + caption = VO |
| [iiqka-ai-vision](iiqka-ai-vision/notes.md) | 2026-10 | 1:27 | 13 | 6.68 s | 5.72 s | 15 % | -21.9 | CGI software launch, dark studio, music only |
| [touchless-car-wash](touchless-car-wash/notes.md) | 2026-10 | 4:09 | 94 | 2.65 s | 2.35 s | 0 % | -16.5 | customer case: interviews + even 2-3 s b-roll |

All three end on the same pair: KUKA logo on white with "making automation easier." (≈4 s), then a 20 s animated brand ident (orange particles, ring logo). Counting the ident inflates ASL; without it the two launch films are 6.2 s (16 shots in 98.6 s) and 5.6 s (12 shots in 66.9 s).

## Sub-styles
1. **CGI launch (hardware):** 100 % render, white warehouse, low fly-throughs at fork height; one feature per camera journey; data shown as orange light in space (scan ring, sensor rays, laser grid, safety field); VO wall to wall and a caption that repeats each VO phrase; product name as a big title over the moving shot.
2. **CGI launch (software):** one orange robot in a dark studio, light trails and sparks as energy, the real UI as floating cards in 3D space, small feature labels; music only, quiet (-21.9 LUFS).
3. **Customer case:** translucent white title panel with logo + title + 2-line summary over the real site; white name box with orange name; a spec list card (one white bar per spec, metric units); founders and integrator talk wall to wall; b-roll cut on an even 2-3 s pulse (3-5 cuts in every 10 s).

## House rules
- **Orange is data and brand.** KUKA orange appears only on robots, data light and the logo; everything else is white, grey or charcoal.
- **Humanist sans** (closest free: Source Sans 3 / Fira Sans), regular weight, sentence case, small (≈4-4.5 % H), never shouted.
- **Long camera journeys:** in renders, feature changes happen inside 10-20 s continuous moves, so the scene detector under-counts edits.
- **Same ending everywhere:** white logo card + 20 s ident.

## How KUKA proves things
- Launches prove nothing on real footage: all render, no numbers beyond the model name.
- The customer case adds the proof: named customer and integrator, the real vision UI, a spec list (payload 35 kg, reach 2,013 mm, repeatability ±0.03 mm).
- Gap: no long real take of one work cycle in any of the three.

## Recipe
- Launch: 6-10 render journeys of 6-20 s, caption = VO phrase (`400 4vh 'Source Sans 3'`, centred, bottom 12vh), one orange light effect per feature, product title `400 7vh` held 3 s, white logo card 4 s.
- Case: title panel `rgba(255,255,255,.85)` 4 s; name box white with orange name `600 4.5vh` + grey role `400 3vh`; spec list rows stagger 0.3 s; b-roll 2-3 s; add one 10-15 s real cycle take.
- Drop the 20 s ident for social cuts; it doubles the ASL and adds nothing.
