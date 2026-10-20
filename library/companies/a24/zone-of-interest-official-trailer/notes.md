# The Zone of Interest — Official Trailer  (A24, 17 Oct 2023, 1:01 / 60.9 s, 16:9 full frame, YouTube)
URL: https://www.youtube.com/watch?v=r-vfg3KkV54
Purpose: trailer (awards-season teaser-length trailer built on festival prestige and critics' quotes)
One-sentence point: a calm, pretty family home next to something unspeakable; the trailer never shows it, it makes you feel it.

Structure: (times from cut detection; sheet tiles show the frame ~1 s after their label)
- 0–2.29 distributor logos in one row on black (FILM4 · A24 · ACCESS).
- 2.29–5.21 a red card: Cannes palm laurel + "FESTIVAL DE CANNES / GRAND PRIX / 2023".
- 5.21–10.68 the longest shot (5.46 s): a static wide of a mother carrying a baby through a flower garden by a high wall, with a dog.
- 10.68–48.84 strict alternation: one picture (~2 s) then one black critics' card (~2 s), 10 cards in total. The pictures are the family's garden, a flower close-up (0.38 s), a garden party, the wife trying on a fur coat, a horse rider in tall grass with smoke, a gilded interior, three lit windows at night, a dinner seen through a doorway. One TIME quote is split over four cards (31.7–46.8) with pictures between: "It's about wanting the best for your children… / …following the rules and working hard… / …feeling that you deserve the best in life… / …entwined with the unspeakable".
- 47.76 "Do not look away" — the last card.
- 48.84–55.76 three night pictures with no text (2.0, 2.0, 2.92 s): a bedroom lamp, a girl with a torch, a couple in twin beds.
- 55.76–57.9 title; 57.9–59.48 "Coming soon"; 59.48–60.9 billing block.

Cut rhythm: 33 shots, ASL 1.85 s, median 1.96 s. ASL by quarter 2.54 · 1.52 · 1.38 · 1.69. Only 9 % of shots are under 1 s (flower 0.38 s, gilded interior 0.58 s, garden 0.58 s) and 3 % over 3 s. The middle runs on a near-metronome: most shots and cards are 1.96–2.05 s. 69 % of cuts land on an audio onset vs 18 % by chance: every cut is placed on a thump. 18 of the 33 shots are text, logo or black cards; text is on screen for ~28.5 s (47 % of the runtime). "Mostly empty" frame in 56 % of samples (52 % dark), median empty share 75 %: the most empty frames of the four A24 examples.

Typography:
- Critic cards: white mixed-case condensed sans, centred, with curly quote marks. Quote ink height 5.6–6.0 % H (cap height ≈ 3.8 % H), one line, width 30–60 % of the frame. The attribution sits right-aligned under the end of the quote in small italic (2.9–3.3 % H), with ★★★★★ when there is a star rating. Typeface is a guess: DIN Condensed / DIN Next Condensed look-alike (closest free: Barlow Condensed Medium).
- Holds: 2.04, 2.05, 2.00, 1.96, 1.21, 1.75, 2.04, 2.04, 1.96, 1.08 s. Hard cut in and hard cut out, no fades, no motion.
- Title "The Zone of Interest": the same condensed face, mixed case (not caps), white with a soft glow/bloom around the letters, 9.8 % H, x 22–77 %. 55.76–57.9 (2.14 s), then "Coming soon" (5.6 % H, 1.58 s).
- Festival card: white on Cannes red #A30001, laurel 15.8 % H, three small lines at 2.3–2.9 % H, 2.92 s. Logo row: 18.5 % H, 2.29 s.

Colour/grade: cool, flat, natural digital daylight. No stylised grade, low contrast, deep focus, a clean modern look in period. Night pictures are very dark, with practical lamps only. No grain visible at 480p, no letterbox (full 16:9).

Camera/shots: static, wide, often symmetrical frames (the garden wall, three windows, a doorway framing the dinner table). Observational distance: people are small in the frame. No face close-ups; the closest shots are the flower (20.73) and the torch-lit hands (50.84). I could not see camera moves on the sheet (all shots look locked-off at 1 fps).

Transitions: hard cuts only. Every second shot is a black card, which works as a rhythmic "dip to black" without any fade. The single red card is the only colour flash.

Sound: no speech at all (faster-whisper found none). Integrated −21.1 LUFS, 4–5 LU quieter than the other A24 trailers. A low drone sits at about −24 dBFS (50 ms RMS) with a short thump (+8…10 dB, ~0.15 s) on every cut, every ~2.0 s (10.75, 12.85, 14.85, 16.8, 18.8, 20.85 …), like a slow heartbeat or a door slam far away. From 43 s it gets louder (the loudest moment is −13.5 LUFS momentary at 45 s) and the pulses get heavier, with deeper troughs (−30 dBFS) between them at 47–55 s. It decays to silence under "Coming soon" and the billing block (57–60.9). There are no hits in the trailer sense and no silence before the title; the thump itself is the hit. Source of the track: unknown (it sounds like the film's score, but that is a guess).

What makes it premium:
- Restraint as the hook: it never shows the camp. Only a pretty home, critics' words and a sound that won't stop.
- A metronome edit: picture / card / picture / card at 2.0 s, each cut on a thump. The structure is the tension.
- Prestige up front: the Cannes Grand Prix card in festival red is the second thing you see.
- One sentence from a review is split over four cards with pictures between, so the critic's words become the voice-over.
- Very quiet mastering (−21 LUFS) and empty frames (75 % median empty share): it feels serious because it refuses to shout.

Recipe (real footage + HTML/GSAP Hyperframes, 1920×1080):
- Footage: locked-off wides only, subject small, symmetry. Grade `filter: saturate(.9) contrast(.95) brightness(1.02)`, no vignette, no grain.
- Grid: `const P = 2.0;` lay shots and cards alternately at `t = 10.7 + i*P`; let 2–3 inserts break the grid (0.4–0.6 s) and end the alternation 7 s before the title with 3 untexted shots.
- Cards: black `#000`, Barlow Condensed 500, white, `font-size:56px` (cap height ≈ 40 px ≈ 3.8 % H), `letter-spacing:.03em`, centred at 50 % height. Attribution: Barlow Condensed Italic 400, 30 px, right-aligned to the quote's right edge, 6 px below. `tl.set(card,{opacity:1},t)` / `tl.set(card,{opacity:0},t+P)`: no tweens.
- Title: the same face, mixed case, 106 px, `text-shadow:0 0 18px rgba(255,255,255,.55), 0 0 40px rgba(255,255,255,.25)`, hard cut in, hold 2.1 s, hard cut to "Coming soon" (60 px) for 1.6 s, then the billing block.
- Prestige card: background `#A30001`, white laurel SVG ~170 px tall + 3 lines of 30 px caps, 2.9 s, at 2.3 s.
- Sound: a drone bed at −24 dBFS, one low thump sample (kick + door slam layered, 150 ms) exactly on every cut (`data-start` = cut time); raise the bed 6–8 dB over the last third and widen the gaps between thumps; master to −21 LUFS integrated; let it decay to silence over the last 3 s.
