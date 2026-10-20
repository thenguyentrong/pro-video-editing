# Oura - film style

Three official films (ŌURA channel) measured at 480p with `analyze_video.py` (scene detector, cuts added from the adaptive cross-check after a sheet check), EBU loudness, grade numbers at 2 fps, text in % of frame height (H), faster-whisper only to find where the VO is.

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice |
|---|---|---|---|---|---|---|---|
| [Introducing Oura Ring 4 (2024)](ring4-introducing/notes.md) | 30.1 s | 15 | 2.00 / 2.00 | 1.50 · 1.50 · 1.88 · 1.88 | 0 % / 7 % | -23.8 | none |
| [Oura Ring 4: Smart Sensing (2024)](ring4-smart-sensing/notes.md) | 45.4 s | 22 | 2.06 / 1.90 | 3.78 · 0.87 · 2.27 · 2.84 | 41 % / 27 % | -17.8 | female VO 0-45 s |
| [Introducing Oura Ring 5 (2026)](ring5-smallest/notes.md) | 30.0 s | 22 | 1.36 / 1.12 | 1.50 · 1.07 · 1.25 · 1.07 | 36 % / 5 % | -13.2 | none |

## The core idea
Oura takes Apple's product-spot grammar (one claim per shot, white sans on a calm frame, product macro, name card at the end) and makes it warmer and more human: beige linen, oak, satin and olive green instead of white sweeps; the key word in an italic serif; body close-ups (lips, hands, chest) as the "proof". Ring 5 moves closer to Apple again (grey seamless, bigger type, metaphor inserts).

## Sub-styles
**1. Warm word-build spot** (Ring 4 intro). One line per 2.0 s shot, built in two steps, keyword in italic serif; home textures; olive accent; end card on beige satin; music only, mixed very quietly (−23.8 LUFS).

**2. Inside explainer** (Smart Sensing). VO wall-to-wall; x-ray ring; thin call-out lines with tiny labels; a 9-portrait montage (0.25-0.4 s each) for "every skin tone"; glass UI cards over real footage; same end card.

**3. Claim-pair spot** (Ring 5). Light-grey seamless; 7-9 claims, each split over two shots (product shot + metaphor insert) with the line completing on the cut; big white sans at ≈ 7 % H; huge wordmark open.

## Measured ranges (3 films)
- ASL 1.36-2.06 s, median 1.12-2.00 s; 27-44 shots/min. Each shot carries one line or one claim half.
- Shots under 1 s only in bursts (portrait montage) or claim pairs (36-41 %); the launch spot has none.
- Cuts on onsets 5-52 % vs 6-43 % chance: cuts follow the text/VO, only the explainer leans on the beat.
- Loudness: −13.2 (Ring 5), −17.8 (VO explainer), −23.8 LUFS (Ring 4 spot, too quiet). No drop-outs in any film.
- Grade: warm home films R-B +34 to +40, luma 98-132, soft contrast; Ring 5 neutral grey (R-B +3, luma 170, saturation 8 %).

## Typography
- Neo-grotesk sans (closest free: Inter / Inter Display), white, sentence case, centred at y ≈ 48-50 %, one line.
- Ring 4: cap ≈ 3.8 % H, keyword in a light italic serif (closest free: Instrument Serif Italic), built word by word (sans first, keyword ≈ 0.5-0.8 s later).
- Ring 5: cap ≈ 7 % H, tracking ≈ −0.02 em, two-step line that completes on the next shot.
- Call-out labels ≈ 1.5 % H on 1 px lines. Product name with the model number in a small circle (≈ 5-6 % H). Wordmark ŌURA ≈ 13 % H as an opener (Ring 5), small at the top of the end card otherwise.

## Colour
- Ring 4 family: oatmeal, oak, beige satin, olive green as the one accent; silver ring. Ring 5: light grey seamless, desaturated metaphor inserts so the gold/rose finishes and green/red sensor LEDs are the colour.

## Camera
- Product macros, rolling/spinning ring, x-ray morph, turntable call-outs; extreme body close-ups; real portraits; metaphor stock (iceberg, splash, desert night, forest, butterfly).

## Transitions
- Hard cuts; a motion-blur spin past the lens into the end card; text lines that continue across a cut act as match cuts.

## Sound
- Launch spots: music only, sparse; explainer: calm female VO + light bed; small SFX on ring actions and UI events.

## What makes it premium (across examples)
- Apple-like discipline (one idea per shot, centred white type, no boxes) with a warmer, editorial voice (italic serif keyword).
- Home materials and one accent colour make a tech product feel like jewellery.
- Human proof shots: breath, hands, faces of every skin tone.
- A consistent end card across the campaign.

## How to recreate with real footage + HTML/GSAP (Hyperframes)
1. Write 6-9 lines of 2-4 words; mark one keyword per line.
2. One shot per line, 1.7-2.3 s (spot) or one claim over two shots of 1.0-1.6 s (claim pairs).
3. Line: `font: 400 5.2vh 'Inter'` with `<em>` in `'Instrument Serif'` italic; sans `opacity 0→1` 0.4 s, keyword 0.5 s later. Pre-layout the full line so nothing re-centres.
4. Big claim style: `font: 400 9.6vh 'Inter Display'; letter-spacing:-.02em`.
5. End card on a soft fabric plate, name + tagline + small wordmark + CTA, 4 s.
6. Master −14 to −16 LUFS (not −24).
