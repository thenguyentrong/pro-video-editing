# Dyson - product film style

Three official product films measured at 480p: cuts2 + eye check of every cut, 1-2 fps strips for in-shot transitions, EBU loudness, 50 ms RMS, faster-whisper for the VO, grade numbers at 2 fps (end screens excluded), text measured in % of frame height (H). All three end with a 5-10 s black YouTube end screen ("dyson / Subscribe"), excluded from the stats.

| Example | Length (film) | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice |
|---|---|---|---|---|---|---|---|
| [V15 Detect laser - TV commercial (2021)](v15-detect-laser/notes.md) | 56.0 s | 10 | 5.60 / 3.92 | 14.0 · 3.5 · 3.5 · 3.5 | 0 % / 70 % | -23.1 | male VO, wall-to-wall |
| [Airstrait - A new way to straighten (2023)](airstrait-new-way-to-straighten/notes.md) | 30.0 s | 10 | 3.00 / 2.60 | 2.5 · 3.75 · 1.5 · 2.5 | 0 % / 30 % | -22.8 | female VO 0-23 s |
| [PencilWash - our slimmest design (2026)](pencilwash-slimmest-design/notes.md) | 42.8 s | 6 | 7.13 / 5.94 | 5.35 · 5.35 · 3.57 · 5.35 | 0 % / 100 % | -15.8 | none (HUD labels) |

## The core idea
Dyson sells engineering, so the film opens the machine. Photoreal CG shows what you cannot see - dust lit by a laser, allergens at microscopic scale, airflow in cyan and magenta, the inside of a cleaner head through an x-ray shell - and a calm narrator (or HUD labels) names the parts with numbers. The camera moves slowly and continuously; cuts are few; nothing is under 1 s. The product's own colourway (purple/nickel/gold, Prussian blue/copper, copper/red/blue) is the palette; everything else is neutral studio grey or black-and-white.

## Sub-styles

**1. VO-led engineering spot** (V15 Detect, Airstrait)
- A narrator talks from the first to the last second (V15 0.3-59 s; Airstrait 0.1-23 s, two long sentences), factual and number-heavy ("14 redesigned cyclones", "99.99% of dust").
- CG one-takes of 8-16 s: floor skim -> laser on -> zoom through the dust into a microscopic world -> whoosh out (V15); x-ray airflow -> pull back as hair passes through (Airstrait).
- Airstrait variant: live action graded black-and-white with the product left in colour (selective colour, median saturation 3 %).
- End card: light (or black) background, product vertical in the right third, 2-3 line claim left-aligned at x 13-15 %, wordmark + model name under it. Broadcast master -23 LUFS (TV file uploaded as is).

**2. Silent HUD explainer** (PencilWash)
- No voice; spec callouts as a technical HUD: ring-dot anchor on the product, 1-2 px white line to a bracket, wide-tracked caps header (~3 % H) + 1-4 sub-lines (~2 % H), typed on with a blinking underscore cursor.
- Six long CG camera moves (3.7-12.9 s) on a light grey floor; x-ray shells show the two water tanks; ends on the product alone, small, centred. Social master -15.8 LUFS.

## Measured ranges (3 films)
- ASL 3.0-7.1 s (median 2.6-5.9 s). 0 % of shots under 1 s in all three; 30-100 % over 3 s.
- Longest shot: the opening or the main mechanism shot, 8-16 s, done as a continuous CG move. The opening of V15 is a 16.2 s one-take (quarter 1 ASL 14.0 s).
- In-shot changes (x-ray fades, zoom-throughs, label build-ups) add a new visual idea every ~2-3 s even when cuts are 5-7 s apart.
- Cuts follow the VO sentences, not the beat (0-30 % of cuts on onsets vs 10-33 % chance); the silent HUD film cuts on music hits (40 % vs 26 %).
- End card 2-3 s per card (1-2 cards), then the platform end screen.
- Loudness: -23 LUFS for TV spots with VO, -15.8 for the social film.
- Grade: neutral (R-B -1 to +2), median luma 86-163, crisp contrast (p95-p5 146-160), median saturation 3-14 % - colour comes only from the product and the effect (laser green, airflow cyan/magenta).

## Typography
- End cards: Dyson's sans (clean geometric-humanist; free match: Lexend or Outfit with a two-storey a), sentence case, dark grey on light or white on black, left-aligned at x 13-15 %, cap height ~4.5 % H, line pitch ~8-9 %. A second line can be a heavier weight ("Only at / **Dyson.com**"). Wordmark "dyson" ~6 % H, model name next to it in a lighter weight and sometimes in the product accent colour ("v15" in blue).
- HUD labels: white caps, wide tracking, technical sans (free match: Michroma for headers, Barlow Semi Condensed for sub-lines), 3 % / 2 % H, typewriter type-on with "_" cursor.
- No titles over the action in the VO spots - the narrator carries the words.

## Colour
- Neutral studio (grey/white walls, dark wood or concrete floors, window-light stripes on the end card wall) + the product colourway + one effect colour per film (laser green; airflow cyan with heat magenta; the brown "dirty water").
- Selective colour (b/w world, colour product) for beauty products.

## Camera
- Photoreal CG with motion-control-like paths: low floor skims, macro push-ins, orbits, zoom-throughs to microscopic scale, x-ray shells that fade to glass. Live action (beauty) is slow push-ins and locked portraits on grey seamless.

## Transitions
- Few hard cuts (5-10 per film). The real transitions are camera moves: zoom-through into a particle and whoosh back out, shell-to-glass x-ray dissolves, pull-backs from inside the machine.

## Sound
- Narrator + quiet music bed + small SFX, flat level (V15 -20 to -24 LUFS-M the whole film); no drop-outs or big hits in the VO spots. The silent film opens with one big splash hit (+36 dB) and runs a music bed with a mid-film dip.

## What makes it premium (across examples)
- The invisible made visible (laser dust, particle counts, airflow), which turns a claim into proof.
- Real internal engineering shown by x-ray cutaways = credibility.
- Long, controlled, uncut camera moves.
- Factual numbers instead of adjectives; calm VO.
- Product colourway as the only colour (or selective colour).

## How to recreate with real footage + HTML/GSAP (Hyperframes)
1. Script one fact per 3-4 s of VO; cut picture to sentence ends. For social, replace the VO with HUD labels.
2. X-ray reveal: align a "shell" plate and an "internals" plate (photo of the opened product or exploded flat-lay); `tl.to(internals,{clipPath:"inset(0 0% 0 0)",duration:1.2,ease:"power2.inOut"})` from `inset(0 100% 0 0)` while `shell` goes to `opacity:.35`.
3. Make-the-invisible: overlay particles (canvas, 2-3 px dots, `#39ff6a` with `shadowBlur:6`) or SVG airflow paths (`stroke:#3fd8ff`, animated `strokeDashoffset`, `mix-blend-mode:screen`).
4. Zoom-through: scale the macro layer 1 -> 6 in 0.6 s `power3.in` with blur 0 -> 8 px, cut to the next layer at 0.6 -> 1 `power3.out`.
5. HUD callout component: ring dot (scale 0->1, 0.2 s) -> 1.5 px polyline (`strokeDashoffset`, 0.5 s) -> header type-on (0.04 s/char + blinking `_`) -> sub-lines stagger 0.15 s; header `font: 3vh 'Michroma'; letter-spacing:.08em; text-transform:uppercase; color:#fff`.
6. End card: product cut-out at x 70-78 %, claim at `left:13%`, `font: 400 4.6vh 'Lexend'`, 2-3 lines, `line-height:1.25`, wordmark below at ~67 % H; hold 2-3 s; light card then optional dark "Only at ..." card.
7. Master -23 LUFS for TV, -14 to -16 for social.
