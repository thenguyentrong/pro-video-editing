# teenage engineering - film style

Three official "introducing" films measured at 480p/360p: cuts2 + eye check of every cut, soft-transition check, EBU loudness, 50 ms RMS, faster-whisper (no speech in any of them), grade numbers at 2 fps, text measured in % of frame height (H).

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice |
|---|---|---|---|---|---|---|---|
| [introducing OP-1 field (2022)](op1-field-introducing/notes.md) | 28.0 s | 9 (~14 beats incl. word swaps) | 3.12 / 2.20 | 1.75 · 1.75 · 3.51 · 3.50 | 0 % / 22 % | -10.7 | none |
| [introducing OP-XY (2024)](op-xy-introducing/notes.md) | 33.5 s | 9 | 3.72 / 3.16 | 2.79 · 2.09 · 2.79 · 4.18 | 0 % / 56 % | -18.0 | none |
| [introducing EP-1320 medieval (2024)](ep1320-medieval-introducing/notes.md) | 64.9 s | 26 | 2.50 / 2.14 | 1.80 · 2.03 · 2.03 · 4.05 | 4 % / 23 % | -21.1 | none |

## The core idea
TE films treat the instrument like an object in a museum or a prop in a strange world. Nothing is explained: no voice, no feature list, no hands playing it. Short lowercase copy (or none), slow macros, a long final hold, the product name as a small logo and the nut-and-bolt pictogram with two tiny legal lines. Each film commits to ONE mood (white museum, black-on-black, medieval art film) and keeps it for every frame. The brand mark often appears as a physical thing first (the "OP-1 field" print on the metal, the chrome bolt-and-nut badge) before it appears as a logo.

## Sub-styles

**1. Museum-white type teaser** (OP-1 field)
- Off-white seamless with a soft grey vignette (median luma 218, saturation 1 %), product macros framed diagonally, one frontal hero held 6.6 s.
- Copy as design: "the beauty of evolution." / "a decade of ideas -> improvements -> refinements." / "thinner, louder, better." - the last word swaps in place on a fixed left anchor (~35 % from the left), no cut.
- Loud, punchy track (-10.7 LUFS) with 0.2 s stutter gaps.

**2. Black-on-black light reveal** (OP-XY)
- Black product, black set (median luma 6/255, 88 % of frames < 40), raking strip light finds edges, keys, LEDs; one green LED is the only colour.
- Full product seen only at 21 s of 34 (63 %), light rising on the floor. No words until the logo.
- One ambient swell (-26 -> -12.7 -> silence), integrated -18 LUFS.

**3. Art-house world film** (EP-1320 medieval)
- 20+ frontal tableaux of a medieval ritual (fire ring, horse, geometric masks, banners), faded teal-grey grade with fire-orange/red accents.
- Product only at 47.2 s of 65 (73 %), on a red altar; then a top-down formation shot (6.6 s).
- Cut on the music (40 % of cuts on onsets vs 18 % chance); end title in huge decorated blackletter (~37 % H) - TE's type follows the theme here.

## Measured ranges (3 films)
- ASL 2.50-3.72 s, median 2.14-3.16 s. Under 1 s: 0-4 %. Over 3 s: 22-56 %.
- The last quarter is always the slowest (ASL 3.5-4.2 s) and holds the longest shot (hero 6.6-6.8 s or the formation 6.6 s).
- Product fully visible late: 15 s / 28 (54 %), 21 s / 34 (63 %), 47 s / 65 (73 %). Macros come before the whole object.
- Text: 0 words in the body (OP-XY, EP-1320) or 5 short lowercase lines (OP-1 field). Line box ~3.5 % H (x-height ~1.7 %); product logo 8-9 % H; pictogram 16-20 % H; legal 2 lines at ~90 % H, 1.5-1.7 % H.
- Loudness varies with the mood: -10.7 (pop teaser), -18.0 (ambient), -21.1 (art film). TE does not master everything loud.
- No people in the product-only films; people only in the concept film, never touching the product.

## Typography
- TE neo-grotesk (free match: Inter Regular/Light, Helvetica Now), lowercase sentences with real punctuation, dark grey #222-#333 on off-white or mid-grey on black, small. Left-aligned at a fixed anchor so word swaps do not shift the line.
- Product logos: "OP-1" + a word in a thin rounded box ("field"); "[OP] XY" with OP in a square outline. Thin, centred, static, short fades.
- Brand end: nut-and-bolt pictogram + 2 legal lines ("teenage engineering and the nut and bolt pictogram are registered trademarks. (c)20xx ...").
- Themed exception: the EP-1320 film uses a decorated blackletter title with a red Lombardic initial and a wide sans caps subtitle.

## Colour
- One base per film (white / black / faded teal-grey), almost no saturation (1.3-1.6 % median in the product films), one accent from the object (screen colours, one green LED, red cloth and fire).

## Camera
- Slow macro drifts and push-ins with very shallow focus, diagonal compositions, a single frontal hero. In the art film: locked-off symmetric tableaux and one top-down. Product shots may be CG or very clean tabletop photography (I cannot tell at 480p/360p).

## Transitions
- Hard cuts only; in-shot text swaps instead of new cards; fade to black or grey for the logo exit.

## Sound
- No voice in any film. Music is the product's world: a punchy electronic track (likely made on the device; a guess), an ambient swell, sampled medieval instruments (per the product description). Long tails; silence at the very end.

## What makes it premium (across examples)
- Restraint and humour in the copy: five lowercase lines, or none.
- Product withheld and shown as an object (macros first, whole thing late, held long).
- Each film is one mood, executed fully (set, light, sound, even type in the art film).
- Brand shown as a physical detail before the logo.
- Quiet masters when the mood asks for it.

## How to recreate with real footage + HTML/GSAP (Hyperframes)
1. Choose the mood: white (`#f2f2f0` + `radial-gradient(ellipse at center,#f4f4f2 55%,#d9d9d6 100%)` vignette), black (`#000` + strip-light sweep), or a themed world.
2. Shoot/collect 5-8 macros (2-3.5 s each, slow push `scale 1 -> 1.04`), one frontal hero (6-7 s), all on the same surface.
3. Copy: 3-5 lowercase lines, Inter 400, `font-size:2.6vh`, `color:#2a2a2a`, `position:absolute; left:35%; top:48%`. Swap only the last word: `tl.set(oldWord,{autoAlpha:0},t).set(newWord,{autoAlpha:1},t)` every 0.8 s.
4. Light-reveal variant: masked sweep `linear-gradient(100deg,transparent 40%,rgba(255,255,255,.18) 50%,transparent 60%)`, `mix-blend-mode:screen`, `backgroundPosition` -100% -> 200% over 3 s.
5. End: product logo (thin sans 8 vh, word tag in `border:1px solid; border-radius:4px`) 1.5-2 s -> pictogram + 2 legal lines (1.4 vh) 2 s -> fade to black 1-1.5 s.
6. Sound: no VO; pick one musical gesture (stutter track, single swell, or a themed score) and master to the mood (-11 to -21 LUFS).
