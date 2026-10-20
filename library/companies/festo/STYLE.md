# Festo - style

Examples (official @festo uploads):
| Example | Date | Length | Shots | ASL | Median | % < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [microfluidics-medtech](microfluidics-medtech/notes.md) | 2026-04 | 2:22 | 40 | 3.56 s | 2.88 s | 5 % | -14.0 | real-footage application demo, macro, music only |
| [car-t-cell-therapy](car-t-cell-therapy/notes.md) | 2026-04 | 3:25 | 112 | 1.83 s | 1.12 s | 43 % | -14.3 | research-partner case, cinematic grade + 3D explainer |

A third film (Festo at CIIF 2025, trade fair) could not be downloaded (YouTube bot check); the company style rests on two films.

## Sub-styles
1. **Application demo (macro):** a white demonstrator in a cool grey studio; each module is spot-lit while the others go dark, then 3-5 macros of 2-4 s with rack focus; coloured liquid (cyan) as the only strong colour; a two-line module label with a Festo-blue line; real device UI filmed in macro; music only, cuts on the beat (54 % on onsets vs 36 % chance).
2. **Partner case (documentary-cinematic):** opening line on near-black, teal-and-orange grade, macro microscopy and ink-in-water shots, named scientists and a Festo manager with big name supers (≈7 % H); an 18 s white/light-blue 3D explainer for the biology; b-roll bursts of 3-10-frame flash cuts on music hits (up to 13 cuts per 10 s) between calm 2-6 s interview pieces.

## House rules
- **The line:** a thin Festo-blue (#0091DC) line runs in from the left frame edge to every title, label and name super, and to the end tagline "Automation for a world in motion." before the blue FESTO logo on white.
- **Type:** Festo face (closest free: Fira Sans), semibold titles, white on footage, dark grey on white animation.
- **Cool and clean:** desaturated grey-white or teal; product white; one saturated accent from the process itself (liquid, cells, light).
- **CGI only as explainer,** in its own flat white/light-blue look; the hardware is real.

## How Festo proves things
- Real fluid in real channels, filmed in macro; the device's own sensor screens.
- Partners (a research institute) explain the problem; Festo appears as the enabler.
- Gaps: no numbers on screen (dosing volume, precision, throughput); the automated cell is shown in macros, never in one long take.

## Recipe
- Labels: `.ln{height:2px;background:#0091DC;transform-origin:left}` drawn 0.4-0.5 s from the frame edge, then text `600 4.5-6vh 'Fira Sans'` fades in 0.3-0.4 s.
- Demo: one lit wide per module (2-3 s) + 3-5 macros (2-4 s) on the beat; 14-15 s final macro into the end card.
- Case: name `600 7vh` + blue line + role `400 3.3vh`; bursts of 4-6 shots of 3-10 frames on one hit, then back to a 3-6 s interview piece.
