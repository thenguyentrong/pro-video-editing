# AirPods Pro 3  (Apple, 2025-09-09, 0:48 file / 0:42.9 content, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=EMmKs8vMKhU
Purpose: product launch spot (event film)
One-sentence point: AirPods Pro 3 = best ANC + health (heart rate, hearing aid) + Live Translation, shown as dance and sound-wave rings in a white void.

## Structure
- 0-2.2 s **Title**: "AirPods Pro 3" in black on white with an RGB-split glitch in and out (heartbeat SFX).
- 2.2-6.5 s **Hook**: black silhouette dancer inside clear glass rings → "The world's best in-ear Active Noise Cancellation" inside an iridescent ring (small 3-line text in the centre, legal line under).
- 6.5-11.5 s **Reveal**: black silhouette of the earbuds turns into the white product, earbud turns, pull back through rings into a dancer (zoom-through).
- 11.5-18.6 s **Health**: earbud macro + "Heart rate sensing during workouts" (rainbow rings pulse around the tip), three dancer shots (silhouette, breakdance).
- 18.6-23.3 s **Fit**: ear tips line up while "A more secure fit for more ears" builds word by word; dancer through glass.
- 23.3-28 s **Hearing**: profile silhouette, glowing blue ring around the AirPod, "A clinical-grade Hearing Aid feature" in blue.
- 28-32 s **Translation**: "Live Translation" label, "Hola" left → "Hello" right (gradient), earbud between.
- 32-40.4 s **Finale**: two dancers top-down, earbuds tumble (silhouette→product morph), case on green lightning "Up to 8 hours listening time with ANC", buds drop into the case, lid closes (clicks).
- 40.4-42.9 s **End**: Apple logo with RGB smear → clean black logo + legal; last heartbeat at 42.1 s, cut to black.

## Cut rhythm
- 19 shots in 42.9 s → **ASL 2.26 s**, median 2.30 s (15 hard cuts + 4 morph/zoom-through changes added by eye). Quarters 2.14 / 1.53 / 2.14 / 2.14.
- No shot < 1 s; 16 % > 3 s. Longest 4.6 s (hearing-aid profile), 3.8 s (translation), 3.4 s (ear tips).
- 50 % of cuts on an audio onset (chance 34 %) → cut to the beat.

## Typography
- SF Pro Display medium, black on white (blue for "Hearing Aid"), sentence case, 2 lines centre-aligned, placed in the empty half next to the product. Cap ≈ 3.5-4 % H.
- Translation words bigger: cap ≈ 9 % H ("Hola" black, "Hello" blue→magenta gradient).
- Title "AirPods Pro 3" ≈ 37-45 % of W wide (cap estimated ≈ 7 % H; every sampled frame was mid-glitch).
- Animations: RGB-split glitch (title, logo), word-by-word build, fade.

## Colour / grade
- Pure white void (#f3f3f5), black silhouettes, white product. 65 % of frames mostly empty, all on light.
- Colour only as iridescent rainbow edges on glass rings, the blue hearing ring and the green battery lightning.

## Camera / shots
Studio silhouettes of dancers against white (black shapes, no detail), 3D product renders and macros, CG glass torus rings that the camera flies through, top-down dancers. Smooth moves, no handheld.

## Transitions
Hard cuts on beat; zoom-through rings (product → dancer), silhouette → product morph (black shape becomes the white earbud), RGB glitch on title/logo.

## Sound
- Music: "BLUH BLUH BLUH" by _BY.ALEXANDER; opens and closes with heartbeats (0-3.4 s, 40.8-42.8 s) = the heart-rate feature as sound motif. SFX: charging tone 36.4 s, case clicks 39.4 s. No VO.
- Integrated **−15.6 LUFS** (loudest of the set). 0.2 s silence at 41.8 s, then the final heartbeat at 42.1 s (−8.0 dBFS, +31.7 dB) → black.

## What makes it premium
- Graphic purity: only black, white and thin iridescent colour.
- Callback to the iconic silhouette iPod ads, but with a new 3D twist (glass rings).
- Feature = sound motif (heartbeat) = visual motif (pulsing rings).
- Short labels set in the empty half of the frame, never over the product.

## Recipe (real footage + HTML/GSAP)
- Shoot dancers on a white cyc, push curves to pure black silhouette (`filter: brightness(0)` on a keyed layer, or `contrast(3) grayscale(1)`), background #f3f3f5.
- Rings: SVG/Canvas ellipses with 1-2 px strokes, `stroke: url(#rainbow)` (red→yellow→cyan→blue), scale 0.6→1.4 while the camera "flies through" (scale the whole layer 1→4 over 0.8 s, ease "power2.in").
- Labels: Inter/SF Pro 500, `font-size: 4.8vh` (cap ≈ 3.7 % H), 2 lines, centre-aligned, placed at x 65-85 %.
- Glitch: three copies of the text in R, G, B with `mix-blend-mode: multiply`, offset ±6 px for 4-6 frames.
- Cut on downbeats, about every 2.2 s (tempo not measured — "one bar per shot" is a guess); open and close with a heartbeat SFX; 0.2 s silence before the last hit.
