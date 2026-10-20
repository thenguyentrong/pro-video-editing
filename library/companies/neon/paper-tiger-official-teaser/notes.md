# Paper Tiger | Official Teaser Trailer  (NEON, 10 Aug 2026, 61.3 s, 16:9 file / 2.39:1 picture, YouTube)
URL: https://www.youtube.com/watch?v=ldCb77jXIsM
Purpose: teaser for an auteur crime drama after its festival premieres (about 3 months before release); sells festivals, critics and stars
One-sentence point: a period New York crime story about family and power, praised as a modern classic, with three big names.

## Structure (beats with timestamps; % of 61.3 s)
- 0.0–2.0 **NEON logo** in silver caps on black, fading (2 s).
- 2.0–8.7 **night waterfront**, one 8.7 s span with slow dissolves: a man looks at the lights across the water; the first **festival laurel** fades in over the picture and settles on black (6–8.7 s). Voice-over starts at 2.2 s.
- 8.7–15.8 period streets: a man walks under an elevated train (2.3 + 2.1 s), a hit at 13.15 (+22.3 dB, loudest moment −6.7 dBFS); the **second laurel** is composited into a restaurant scene (13.1–15.8).
- 15.8–22.1 diner conversation, a police ceremony with flags (period wide).
- 22.1–25.6 **quote 1 over a blurred night street** (3.5 s, at 36 %), hit +21.3 dB at 22.15.
- 25.6–28.7 faces in the dark, a car interior. 28.7–32.1 **quote 2** over out-of-focus amber light (3.5 s, 47 %).
- 32.1–39.8 shots of 0.6–1.7 s: a car at night, the leads in suits, a woman at a kitchen window.
- 39.8–41.5 **quote 3** "A NEW AMERICAN CLASSIC." (1.75 s, 65 %).
- 41.5–52.9 **cast run**: shots of 0.5–1.0 s alternating with three name cards on blurred light plates (Academy Award nominee + name; 44.96, 46.0, 48.1; 1.0–2.2 s each); densest 30–50 s, 8 cuts per 10 s.
- 52.9–61.3 **final held image 8.4 s**: a green field with a far skyline; the title "PAPER TIGER" fades up over it (54–56, at 88 %), then "WRITTEN & DIRECTED BY" + name (57–58.5), then "IN THEATERS ONLY / NOVEMBER" (59–60.5); sound fades to silence.

## Cut rhythm
- 34 shots (adaptive detector; dissolves and text changes over the last image not counted). **ASL 1.80 s**, median 1.19 s.
- ASL per quarter 3.83 · 1.53 · 1.02 · 1.92 s: slow open, speed-up, a held ending.
- 32 % under 1 s, 12 % over 3 s; 33.3 shots per minute. Longest 8.7 s (open) and 8.4 s (title image).
- Cuts per 10 s: 1 5 6 8 8 5. Cuts on audio onsets 27 % vs 18 % chance.
- Speech in ≈37 s of 61 s: voice-over and dialogue lines carry the first half.

## Typography
- One condensed caps face for everything (closest free: Oswald 500), warm off-white (#fffffa to cream #e1dbc1).
- **Quotes**: two lines at ≈3 % H each with the critic and outlet in a tiny line below, centred, laid **over blurred footage or out-of-focus practical light**, never on flat black. Hold 1.75–3.5 s; they fade in and out (≈0.5 s).
- **Cast cards**: "ACADEMY AWARD NOMINEE" ≈2 % H over the name ≈5 % H, on a soft yellow-white light blur, 1.0–2.2 s each.
- **Laurels** inside shots (composited onto a wall or over the night water) rather than as a separate slide.
- Title ≈13 % H over the final landscape, credit and date ≈2.5–5 % H, each fading in and out on the same picture.

## Colour / grade
2.39:1 (62 px bars at 480p). Period film look: warm amber interiors, sodium-orange nights, desaturated daylight streets, a green open field at the end. Grain visible.

## Camera / shots
Long-lens close-ups, period street wides with an elevated train, ceremony wides with flags, car interiors; few action images.

## Transitions
Dissolves in the open and on every card; hard cuts in the body; text changes over one held image at the end.

## Sound
- Integrated **−16.2 LUFS**, LRA 8.7 LU, true peak −1.0 dBTP.
- Voice-led bed at −20…−28 dBFS with two big hits (+21…+22 dB) at 13.15 and 22.15; music fuller in the cast run (−13…−17); fades out under the final image. No drop-outs.

## What makes it premium
- Praise and prestige (two festivals, three quotes, three nominees) shown inside the film's own light and grain, not as slides.
- One held landscape carries title, credit and date for 8.4 s.
- Quiet master (−16 LUFS) and soft fades: it feels like a drama, not an action trailer.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Bars 138 px (2.39:1).
2. 0–2 s distributor logo; 2–9 s one held night image with voice-over; laurel `opacity 0→1` 1 s over the picture.
3. Quote card: blur a shot (`filter: blur(18px) brightness(.6)`) as the plate; `font:500 34px Oswald; letter-spacing:.04em; color:#f6f1e1; text-transform:uppercase`, outlet line 14 px; fade in 0.5 s, hold 2.5–3 s, fade out 0.5 s.
4. Cast run at the end: 0.5–1.0 s shots alternating with name cards on a soft light blur (1.0–2.0 s).
5. Final 8 s on one wide image: title (`font-size:140px`) fades in 1 s, holds 2 s, out; credit 1.5 s; date 1.5 s; fade the music to silence.
6. Master −16 LUFS, true peak −1 dBTP.
