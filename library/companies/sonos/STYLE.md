# Sonos - film style

Four official films measured at 480p with `analyze_video.py` (adaptive detector for the dark Amp Multi and for Roam 2, both checked on frame strips; Amp Multi +2 dissolves added), EBU loudness, grade numbers at 2 fps, text in % of frame height (H), faster-whisper only to check for voice.

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice |
|---|---|---|---|---|---|---|---|
| [Roam 2 - Size-defying sound (2024)](roam2-size-defying/notes.md) | 40.8 s | 38 | 1.07 / 0.83 | 1.13 · 0.78 · 0.85 · 1.46 | 61 % / 3 % | -13.9 | none |
| [Sound for how you live (2025)](sound-for-how-you-live/notes.md) | 70.0 s | 2 (one CG take) | 35 (meaningless) | camera: 5 room visits of 5-14 s | - | -16.5 | male VO 0.2-67 s |
| [Amp Multi - World-class audio, amplified (2026)](amp-multi-amplified/notes.md) | 130.0 s | 26 | 5.00 / 4.50 | 4.06 · 3.25 · 4.64 · 8.12 | 0 % / 81 % | -15.1 | none (labels) |
| [Feel the system (2026)](feel-the-system/notes.md) | 30.0 s | 33 | 0.91 / 0.33 | 0.68 · 1.25 · 0.68 · 0.94 | 67 % / 6 % | -15.1 | female VO 0.5-27.5 s |

## The core idea
Sonos sells a system for the home. Its product films show where each product lives and how they work together: a cut-away house the camera flies through, colourways matched to their worlds, a dark studio with one label per feature. The newest brand campaign (Feel the system) deliberately breaks with this precision look and goes paper collage. Across all four, products are matte black/white objects that are never re-coloured; colour comes from the world around them.

## Sub-styles
**1. One-take system tour** (Sound for how you live). Photoreal CG cut-away house; the camera pushes into a room, skims the product, pulls back to the overview; VO one sentence per room; no supers; logo on black in silence.

**2. Colour-world spot** (Roam 2). Each colourway in a world of its own colour (olive garden, blue pool, red clay court); hands on the product in every world; triptych opener; no text; cuts at ≈ 0.8 s median.

**3. Dark spec film** (Amp Multi). Near-black CG studio, light finds the product; one label per shot at the bottom (cap ≈ 4.6 % H + ≈ 3.5 % sub-line); UI on phone/laptop; 4-6 s shots with fades through black; the music stops for 0.3-0.45 s at each new section; logo held 5.9 s in silence.

**4. Collage campaign** (Feel the system). Paper collage, condensed caps labels, marker highlights, handwritten end lines, playful VO. The counter-example: emotion over precision.

## Measured ranges
- Precision films: ASL 1.07 s (lifestyle spot) to 5.0 s (spec film); the one-take tour has no cuts for 67 s. The collage ad is the fastest (median 0.33 s pop-ins inside 2-5 s layouts).
- Loudness −13.9 to −16.5 LUFS; LRA 1.9-3.0 LU (tight, compressed mixes).
- Silence: logo endings in 2.2-5.9 s of silence (tour, spec film), a 2.6 s black silent tail (Roam 2). Section stops of 0.3-0.45 s in the spec film (8 drop-outs).
- Cuts on onsets 16-48 % vs 22-44 % chance: Sonos cuts to action or VO, not to the beat.
- Grade: tour and Roam warm-natural (R-B +4 to +11, luma 64-66); spec film black (luma 16, saturation 0 %); collage bright paper (luma 201).

## Typography
- Precision films: neo-grotesk sans (closest free: Inter), sentence case, white, no box. Labels low (y ≈ 85 %), titles and end lines in the upper third (y ≈ 27-37 %), payoff word in grey (#9a9a9a) on a second line.
- Supers are rare: the tour and Roam 2 have none at all.
- Wordmark SONOS in its own wide caps, ≈ 4 % H, on black.
- Collage: heavy condensed caps (closest free: Barlow Condensed ExtraBold / Anton), purple and orange highlight boxes, scanned handwriting.

## Camera
- Photoreal CG with a single continuous camera path (tour), slow light sweeps on dark products (spec film), live-action hands on the product (Roam 2). No presenters.

## Transitions
- The camera move as transition (in through the wall, out to the overview); fades through black between sections; hard cuts in the lifestyle spot; pop-ins in the collage.

## Sound
- VO only where the system needs explaining (tour, collage); music-only for single-product films. Logos land in silence.

## What makes it premium (across examples)
- Products shown in context, small, matte, never re-coloured; colour comes from the world.
- Clean frames: few or no supers; one label per shot when needed.
- Engineered continuity (one-take camera path, one colour per world).
- Silence used as punctuation (section stops, logo holds).

## How to recreate with real footage + HTML/GSAP (Hyperframes)
1. Tour: one large cut-away still; GSAP push-ins `scale 1→3.2`, 2.2 s `power2.inOut`, cross-fade into a real room clip, hold 4-8 s, reverse out; VO one sentence per room.
2. Colour worlds: 3 worlds × 6-9 s; wardrobe/props match the colourway; triptych opener with a 3-column CSS grid of videos.
3. Spec film: black stage, radial light mask that travels, label component at `bottom:12%`, `font: 500 6.3vh 'Inter'` + sub-line 4.8vh; 4-6 s per shot; 0.35 s music stop per section.
4. End: SONOS-style wordmark on black, 2-6 s, in silence. Master −15 to −16 LUFS.
