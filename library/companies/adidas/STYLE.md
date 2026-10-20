# adidas - style

Examples (official @adidas / @adidasOriginals uploads):
| Example | Date | Length | Shots | ASL | Median | < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [you-got-this](you-got-this/notes.md) | 2024-02 | 1:28 | 95 | 0.93 s | 0.68 s | 67 % | -13.7 | platform anthem: B&W 4:3 pressure → colour play |
| [football-anthem](football-anthem/notes.md) | 2024-05 | 1:30 | 97 | 0.93 s | 0.68 s | 74 % | -13.8 | same platform, football stars, comedy beat |
| [superstar](superstar/notes.md) | 2026-02 | 1:33 | 79 | 1.17 s | 0.83 s | 58 % | -13.8 | product heritage, celebrity narrator, surreal set |

## Core idea
adidas anthems are built on **two worlds and one switch**. A "pressure" or "memory" world (B&W, pillarbox, alone, quiet) and a "play" world (colour, full frame, crowds, joy). The switch is a hard cut with a short audio drop. Words come as a litany ("It's only ...") or a narrator who talks like a person, never as a sales voice.

## Rules that repeat
- **Format carries meaning.** Pressure = B&W + pillarbox (1.0-1.37:1 inside 16:9); play = colour, full frame. Switch at 20-38 % of runtime.
- **Same fast median in both platform films:** 0.68 s, 67-74 % of shots under 1 s, 65 shots per minute. The first world is slower (ASL 1.7 s in the first quarter of You Got This), the second doubles the speed.
- **Litany voice:** one short line per idea, each line opens a new place or person. Cuts follow the voice (cuts on onsets 18-20 % vs 15-17 % chance).
- **Stars mixed with amateurs**, same framing and same grade.
- **One breath:** a 0.4-0.9 s drop-out before a new world, then a +30 to +45 dB rise.
- **End card = type only:** "YOU GOT THIS" in spaced serif caps on black (cap height ≈10 % H, a letter grid ≈44 % of width), 1.5-1.8 s, then the logo 1.4-2.2 s, last 0.6-1.3 s silent. Originals ends on the trefoil only.
- **Social-level loudness:** -13.7 to -13.8 LUFS, LRA 3.9-6.8 LU; level stays flat across the switch (the change is in the picture).
- **Originals variant:** a long opening hold (12.3 s), a symmetrical set (one-point-perspective corridor) as a memory palace, a strict 5-colour palette.

## Recipe (real footage + HTML/GSAP)
1. Write a litany of 8-12 "It's only X" lines (or a narrator monologue of ≈130 words for 90 s).
2. 0-35 %: B&W pillarbox (`clip-path: inset(0 12.5%)`, `grayscale(1)`), 10-15 shots of 1-4 s, faces into the lens, no voice or a few overheard voices.
3. Switch: 0.4 s audio drop, hard cut to colour full frame on the same person.
4. 35-90 %: 60-70 clips at 0.3-0.8 s, one voice line per scene, densest 55-70 %; a slower 8-10 s scene for humour if the film is > 60 s.
5. End card: serif caps grid (Libre Caslon Text 10vh), hard on, 1.5 s; logo 1.5-2 s; 1 s silence.
