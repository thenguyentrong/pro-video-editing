# Figma — software launch film style

Three official Figma films measured at 480p/360p (scene + adaptive cut detection, cut pairs and 4 fps strips checked by eye, EBU loudness, voice detection). Sizes are % of frame height (H). "≈" = by eye. In rendered-UI films a "shot" is a hard change to another screen or a hard punch-in/out; panel pop-ins and UI animation are not counted, so counts are ±10 %.

| Example | Year | Length | Set-ups | ASL / median | ASL by quarter | <1 s / >3 s | Voice | LUFS (I) |
|---|---|---|---|---|---|---|---|---|
| [Introducing Figma Motion](introducing-figma-motion/notes.md) | 2026 | 68.1 s | 22 | 3.10 / 2.63 | 2.13 · 2.84 · 2.84 · 3.40 | 14 % / 41 % | none | −13.4 |
| [All the launches at Config 2025](config-2025-all-launches/notes.md) | 2025 | 81.1 s | 45 | 1.80 / 1.50 | 1.56 · 1.35 · 1.84 · 2.25 | 18 % / 13 % | none | −15.6 |
| [Introducing the glass effect](glass-effect/notes.md) | 2025 | 29.6 s | 9 | 3.29 / 3.77 | 3.70 · 2.46 · 1.48 · 3.70 | 0 % / 67 % | none | −9.0 |

## The core idea
Figma launches are **the product doing the talking**: 100 % rendered UI, no people, no narrator, one music track. Every film shows real-looking work made in the tool (posters, websites, app screens), zoomed until the UI is readable, with a large cursor acting like a hand. Words are almost absent: the product name, a short end line, and the logo. Structure comes from colour: each feature or product gets its own flat background world, and black chapter cards separate products in the big recap. The last 4-8 % is always coloured shapes that bounce and morph into the logo.

## Sub-styles
**1. Feature film** (Figma Motion, 68 s): hook on the RESULT (a moving graphic in extreme close-up), pull back to reveal the canvas, product name card at 10-14 %, then 7 features × 4-10 s, each on its own colour; the AI/"magic" feature gets the longest shot (10.2 s, the prompt types and the result plays). End line at 92-95 %, logo morph 95-100 %. ASL slows from 2.1 to 3.4 s across the quarters.

**2. Launch recap / keynote sizzle** (Config 2025, 81 s): opener wordmark on a strong colour (maroon), then four chapters, each with a black chapter card (1.2-2.1 s) whose single effect hints at the product (type-on, glitch, hand-drawn underline, outline frames). 7-20 s of UI per product at ASL ≈1.5-2 s; densest stretch is a colour-flip grid at 0.4-0.6 s. End line "brand promise" at 88-95 %, logo, 1.75 s silence.

**3. Single-property reel** (glass effect, 30 s): six test designs, one per shot, on a strict musical grid (four shots of 3.8 s, then 3.1 / 1.9 / 1.8 / 1.7 s), the only words are the property names in the panel, 62 % of cuts on onsets (vs 29 % chance), master −9 LUFS for social.

## Rules with numbers
- **No voice, no people.** Music + UI clicks/pops only. Master −13 to −16 LUFS for YouTube launches, −9 LUFS for the social reel. No drop-outs mid-film; silence only on the last 1-2 s.
- **Type:** brand grotesque (free: Inter / Inter Tight 500), sentence case. Product title cap 11-15 % H; end line cap 11-16 % H; 2-4 words; holds 1.2-2.3 s. Colour: white on black (chapter cards), orange ≈#f2643a on black (Motion), black + red ≈#e5384b on pastel (Config end line).
- **UI scale:** UI is shown at 200-400 % so labels read at ≈3-6 % H; cursor ≈8-10 % H at that zoom, black with a white outline.
- **One colour world per feature:** lime ≈#d9ff82, violet ≈#4b00c9 + lilac, maroon ≈#6b141c, black, pastels; sample designs are art-directed (serif websites, festival posters, sneaker ads).
- **Shot length:** feature films 2.5-3.5 s average with long "result plays" shots up to 10 s; recaps ≈1.5-1.8 s; inside every shot the UI changes every ≈0.5-1 s.
- **Transitions:** ≈half hard cuts on a colour change, half continuous virtual-camera moves (zoom out from a detail, punch in to the timeline) and morphs; logo always arrives by a shape morph.
- **End:** end line (optional) → shapes bounce in (`back.out`) → logo on black or a soft gradient, 3-6 s. No URL.

## Recipe (HTML/GSAP Hyperframes, 1920×1080)
1. Build each feature as a real HTML mock at 2× inside a `#stage`; the camera is a tween on the stage's `scale/x/y` (`power3.inOut` 0.8-1.2 s for moves, `set()` for punches).
2. Open on the result in extreme close-up (3-4 s), pull back to the tool (3 s), name card (1.8 s, `Inter Tight 500 14vh`).
3. One feature per background colour, 4-10 s each; let the "magic" feature run longest; cursor moves `power2.inOut` 0.6 s, click `scale 0.85 → 1` + click SFX.
4. For a multi-product recap insert black chapter cards (`Inter 500 11vh #fff`, 1.2-2 s) with one product-specific effect each.
5. End line 1.5 s, shapes `back.out(2.5)` stagger 0.12 s into the logo, hold 2 s, last 1.5 s silent.
6. Music only, UI pops on actions; cut on the bar for short reels.
