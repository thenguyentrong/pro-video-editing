# Polestar - film style

Chosen as the fourth design-led brand: Swedish minimalism, very strict colour and type discipline, and films that sell design with almost no words. Three official films measured at 480p: cuts2 + eye check of every cut, soft-transition check, EBU loudness, 50 ms RMS, faster-whisper for voices, grade numbers at 2 fps, text measured in % of frame height (H).

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice | Aspect |
|---|---|---|---|---|---|---|---|---|
| [Polestar 4. The performance coupe (2024)](polestar4-performance-coupe/notes.md) | 90.0 s | 41 | 2.20 / 1.88 | 2.25 · 1.61 · 1.88 · 2.81 | 5 % / 17 % | -14.0 | none | 16:9 |
| [Polestar 3 world premiere (2022)](polestar3-world-premiere/notes.md) | 75.0 s (+21 s red) | 20 | 3.75 / 2.06 | 2.68 · 2.68 · 3.12 · 6.25 | 0 % / 40 % | -14.7 | none | 16:9 |
| [Polestar 4 coupe Sightings (2024)](polestar4-sightings/notes.md) | 60.0 s | 30 | 2.00 / 1.78 | 2.50 · 1.88 · 1.36 · 1.88 | 13 % / 13 % | -14.2 | witness voices | 2.35:1 |

## The core idea
Polestar films build a world first and let the car arrive late, as an object in that world: a red flower planet where chrome grows like plants, a white box on a bare rock island, a UFO wrapped in gold foil. There are no claims on screen and almost no text - at most one wordmark, or a neon star. Colour is a strict two-part script: cool grey/blue/white (car, sky, sea, chrome) against one warm accent (Polestar red, flower red, gold foil, the red light bar). The editing is calm and even (ASL 2.0-3.8 s) and always ends on a long, empty, composed frame.

## Sub-styles

**1. Material-rhyme mood film** (Polestar 4 performance coupe)
- 25-30 nature/CG macros and aerials in a red-and-grey palette; liquid chrome forms grow among flowers; shapes and materials rhyme across cuts (chrome drop -> chrome star -> chrome lattice -> silver beetle on car paint -> car).
- Full car at 58.8 s of 90 (65 %), held 4.7 s frontal and symmetric; a neon Polestar star as the only graphic; last shot = empty road to the horizon.

**2. Architecture reveal** (Polestar 3 world premiere)
- A white minimalist box/frame on a rock island in a grey sea; top-down drone open, beat-cut details (63 % of cuts on onsets), frontal symmetric frame-within-frame, a 16 s drone pull-back.
- White flash + light-leak flare into a full-frame Polestar red card (#d12f36 sampled) with a small white "Polestar" wordmark at the left (x 15 %, ~6 % H line box). Music cut to silence for 1.3 s under the flash, hit on the red.

**3. Genre concept** (Polestar 4 Sightings)
- A UFO-sighting story: gold-foil object falls from the sky, the red light bar glows through the foil, wind strips the foil, the car drives off. Witness voices like a documentary.
- 2.35:1 scope frame, desert dusk grade, faster third quarter (ASL 1.36 s), ends on an aerial of a winding road. No text at all.

## Measured ranges (3 films)
- ASL 2.00-3.75 s, median 1.78-2.06 s. Under 1 s: 0-13 %. Over 3 s: 13-40 %.
- Car fully shown at 62-65 % of the runtime in the mood/concept films (Sightings: foil blown off ~37 s of 60; P4: 58.8 s of 90); the premiere shows details from 9 s and the whole car at ~19-23 s, inside the architecture.
- Last shot 3.5-16 s and always a composed wide (road to the horizon, drone pull-back, winding-road aerial).
- Text: 0-1 element per film (neon star logo ~70 % H as an object; "Polestar" wordmark ~4.5 % cap height). Never a claim, spec or URL.
- Loudness -14.0 to -14.7 LUFS integrated (consistent social/web master). Beat sync: 21-22 % of cuts on onsets in the mood films (near chance), 63 % in the premiere's detail section.
- Grade: cool (premiere R-B -24, saturation 25 %), neutral desert (Sightings R-B +1, saturation 17 %), or red-world (P4 saturation 41 %, R-B +13). Median luma 65-108 - moody, never bright.

## Typography
- Almost absent. When used: the "Polestar" wordmark in the brand neo-grotesk (Polestar Unica; free match: Inter Medium), white on red, left-aligned at x 15 %, vertically centred, fade in after the flare, 5 s hold.
- The star logo is shown as light (neon outline with glow and dust) or as an object (on the white box roof, on the glass roof).

## Colour
- Base: cool greys, blue-grey skies and sea, white/silver car, chrome. Accent: one warm red (flowers, light bar, brand red) or gold foil. The brand red is saved for the very end in the premiere.

## Camera
- Drone top-downs and pull-backs, frontal symmetric wides with the car centred, low-angle details, macro nature, long-lens tracking and low skims in drive sections, backlit silhouettes with lens flare. Slow overall; motion comes from the car, wind and light.

## Transitions
- Hard cuts (19-40 per film). The links are made by matching shapes/materials (P4), by physical reveals (foil blown off, box opening), and one white flash + light-leak flare into the brand card. No whips, no graphic wipes.

## Sound
- No narrator. Music-led with long builds; silence used once before the brand hit (premiere: 1.3 s at -60 dBFS). Sightings uses documentary-style witness voices as the "VO". Loud plateaus at the car reveal (P4 -9 to -10 LUFS-M at 55-64 s).

## What makes it premium (across examples)
- The world is built before the car appears; the reveal is earned.
- One warm accent against a cool, grey world - strict colour script.
- Symmetry, negative space and architecture-like framing.
- Zero claims on screen; the brand is a light, a colour or a single word.
- Long, empty final frame instead of a CTA.

## How to recreate with real footage + HTML/GSAP (Hyperframes)
1. Pick a world and one accent colour; grade everything else cool: R-B about -20, saturation ~20-25 %, median luma 70-100; keep the accent saturated (HSL qualifier).
2. Structure: world-building shots 1.5-2.5 s (no product, or only details) for 50-65 % of the runtime -> product reveal held 4-5 s, frontal and centred -> 4-6 drive/detail shots -> final composed wide 4-16 s.
3. Order shots by shape/material so every cut rhymes (round -> round, chrome -> chrome, red -> red).
4. Brand moment options: (a) neon logo: SVG path `stroke:#fff`, `drop-shadow(0 0 6px #fff) drop-shadow(0 0 18px rgba(255,255,255,.6))`, draw 0.8 s with `strokeDashoffset`; (b) flash-to-colour card: 0.6 s white `#f4f8f8` flash, radial flare gradients drifting 3 s, full-frame `#d12f36`, wordmark `font: 500 4.6vh 'Inter'` at `left:15%; top:50%`, fade in 0.8 s, hold 5 s.
5. Scope variant: render the video area at 2.35:1 (`aspect-ratio:2.35/1`) for concept/genre films.
6. Sound: music only (or vox-pop voices for a concept film), one silence of ~1 s before the brand hit, master -14 LUFS.
