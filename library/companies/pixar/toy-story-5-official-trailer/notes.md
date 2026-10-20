# Toy Story 5 | Official Trailer  (Pixar, 19 Feb 2026, 144.4 s, 1.86:1 file (854×460 at 480p, no bars), YouTube)
URL: https://www.youtube.com/watch?v=c51ND9Hdbw0
Purpose: main trailer for an animated sequel (4 months before release)
One-sentence point: the toys meet a new rival, a talking tablet, and learn that times change but friends stay.

## Structure (beats with timestamps; % of 144.4 s)
- 0.0–17.9 **comic cold open (12 %)**: a pastel fantasy wedding for a minor character (one 6.5 s shot, soft-focus pastel world), broken by a hard cut to the real bedroom. A gag open, not a story open.
- 17.9–26.5 **the rival arrives**: a child unboxes a frog-shaped tablet that says "Hi!" (2.8 s), the toys watch from under the bed (2.8 s).
- 26.5–28.3 **studio logos** (castle 1.0 s, lamp 0.8 s, at 18–19 %), hit +46 dB rise out of a quiet beat at 26.3.
- 28.3–51.1 **Act 1, comedy**: toys vs the tablet, the cowgirl and the horse argue with the screen, kids with screens (ASL ≈1.5 s; 2–3 s comic holds).
- 51.1–76.5 **night section**: the room in red standby light, the tablet glowing, the cowboy in a held close-up (5.3 s at 63.8), level drops to −22…−36 dBFS, three shots of 2.2–2.9 s.
- 76.5–77.2 **card "ON / JUNE 19"** (0.7 s only, at 53 %).
- 77.2–103.9 **Act 2**: the cowboy alone at a sunlit window, all the toys in a meeting, a chase on the bed, the tablet takes over (ASL ≈1.2 s).
- 103.9–105.4 **card "FROM / DISNEY AND PIXAR"** (1.5 s, at 72 %).
- 105.4–128.9 **action and tagline**: a dark mission, a flame, four cards split over footage: "TIMES MAY / CHANGE" (1.1 s, 78 %), "BUT / FRIENDS" (1.0 s, 81 %), "ARE / FOREVER" (2.0 s, 83 %; the word fades from grey to white), then a sunset ride. Densest 110–120 s, 12 cuts per 10 s (76–83 %); loudest 0.5 s at 111.15 (−10.9 dBFS).
- 129.0–135.6 **button**: a comic exchange between the two heroes (2.1 + 1.3 + 1.5 + 1.0 + 0.8 s).
- 135.6–138.7 one bright, overexposed shot (3.1 s), then the **title** "TOY STORY 5" (2.9 s, at 96 %), then "ONLY IN THEATERS / JUNE 19" (2.8 s), fade out.

## Cut rhythm
- 97 shots (adaptive detector + the end-card change by eye). **ASL 1.49 s**, median 1.08 s.
- ASL per quarter 1.72 · 1.64 · 1.24 · 1.29 s. 34 % under 1 s, 5 % over 3 s. 40.3 shots per minute. Shortest 0.21 s (two whip gags), longest 6.5 s (open).
- Cuts per 10 s: 2 9 5 7 6 7 4 6 7 7 9 12 8 6.
- Cuts on audio onsets 36 % vs 39 % chance: cut to dialogue and gags, not to the beat.
- Speech in ≈117 s of 144 s (81 %, 60 separate lines): a dialogue-led comedy trailer.

## Typography
- One face for all cards: a humanist bold sans in caps (closest free: Fira Sans 800), white on pure black, centred.
- **Two-size stack**: small lead line ≈7–8 % H ("ON", "FROM", "TIMES MAY", "BUT", "ARE") over a big line ≈13.5 % H, both centred at ≈39 % and ≈53 % H.
- Holds are short: 0.7–1.5 s for most cards; the last tagline word holds 2.0 s and fades from grey to white.
- Title: the franchise logo (≈35 % H tall, centred), date card in the same face as the taglines.
- In: hard cut. Out: hard cut.

## Colour / grade
Saturated animated palette (green bedspread, red-blue costumes), a pastel dream open, a red-and-teal night section, golden sunsets. No letterbox: the full 1.86:1 frame is used.

## Camera / shots
Toy-height low angles, under-the-bed wides, two-shot comic dialogue, a few big "camera" moves in action; held reaction close-ups for the jokes.

## Transitions
Hard cuts; short black dips (0.1–0.4 s) at 31.7, 51.1 and 58.5; black cards; a soft fade on the last word.

## Sound
- Integrated **−14.1 LUFS**, LRA 6.9 LU, true peak −0.9 dBTP.
- Flat, dialogue-led mix (most of the trailer at −15…−22 dBFS RMS), quieter night section (to −36), music up in the action (−11…−14).
- **No silence and no drop-out** in the body; the only silence is the last 0.8 s.

## What makes it premium
- It opens on a joke, not on a logo or a threat.
- One clear conflict (old toys vs a screen) carried by dialogue.
- A tagline split into three cards across the action, with the last word given more time.
- The emotional low point (a 5.3 s held face in the dark) sits in the middle, the title arrives late (96 %).

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Full frame, no bars (or 2.00:1 at most for a premium feel).
2. 0–18 s: one funny scene with one 5–7 s shot, then a hard cut to the real world.
3. Logos at ≈18 % after the conflict is set up.
4. Body ASL 1.2–1.6 s; comic holds of 2–3 s; one quiet section with a 4–5 s close-up at ≈45 %.
5. Cards: `.sm{font:800 64px "Fira Sans"}` `.lg{font:800 140px "Fira Sans"}`, white on `#000`, `text-transform:uppercase; line-height:1.05`, hard cuts, 0.7–1.5 s; the last word `color:#777→#fff` over 0.8 s and held 2 s.
6. 6–7 s comic button after the action, one bright shot, title 3 s, date 2.8 s.
7. Master −14 LUFS, true peak −1 dBTP.
