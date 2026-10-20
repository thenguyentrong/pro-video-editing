# FANUC - style

Examples (official @FANUCEurope uploads):
| Example | Date | Length | Shots | ASL | Median | % < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [m2000ia-strongest-robot](m2000ia-strongest-robot/notes.md) | 2016-06 | 1:36 | 19 | 5.07 s | 4.24 s | 5 % | -17.0 | product launch filmed at a trade-fair stand |
| [loop-technology-case-study](loop-technology-case-study/notes.md) | 2026-09 | 4:25 | 48 | 5.53 s | 4.72 s | 0 % | -19.4 | customer case study (template series) |
| [mattress-assembling-auping](mattress-assembling-auping/notes.md) | 2026-05 | 3:16 | 19 | 10.34 s | 5.17 s | 0 % | -10.9 | integrator application demo ("GET IT DONE. TOGETHER!") |

## Sub-styles
1. **Product launch at the stand:** a real robot doing the impossible (holding a car), dark hall, yellow robot as the only colour; one spec per shot with a physical reference (floor ruler "3.7 m", yellow target circle under the wheel); two-line statement cards (white line + yellow line) over darkened macros; VO slow (≈1.6 words/s); silent logo open and a 4.55 s drop-out before the end title.
2. **Case-study template:** five-line ExtraBold caps title + a four-icon fact bar (company, industry, country, employees); yellow "The Challenge:" box with a cut corner; yellow caps key-message tags; burned-in subtitles of all speech; three named speakers; one long process take (23.8 s) near the end.
3. **Integrator application demo:** a yellow word sting ("GET IT DONE" / "WITH" / "FANUC"), then 3-4 locked real-time takes of 20-30 s of a real cell with no text at all, music only and loud (-10.9 LUFS); slows down towards the end (ASL per quarter 7.0 / 6.1 / 16.4 / 12.3 s).

## House rules
- **FANUC yellow (#FFD800) is the whole brand:** robots, cards, boxes, rulers, target circles; red only in the wordmark.
- **DIN-style bold sans** (closest free: Barlow / D-DIN), black on yellow or white on dark.
- **Real machines, real time.** No CGI in any of the three; motion comes from slow slider moves and low angles.
- **Flat rhythm:** 0-3 cuts per 10 s in all three films.

## How FANUC proves things
- The stunt is the proof (2.3 t car held in the air) - one spec per shot, with a ruler or target in the frame.
- Long real-time takes: 23.8 s (case study), 24.5-27.4 s (integrator demo).
- Gaps: no cycle time or rate on screen anywhere; the integrator series has no labels at all.

## Recipe
- Launch: yellow card 5-9 s (silence under the logo) → macro reveal → 4-6 spec shots of 4-9 s with a yellow box `600 4.5vh Barlow` top-left and a floor ruler → statement card (white + yellow line, 5vh) → end title after a 3-4 s music drop-out → yellow end card.
- Case: caps title `800 10.5vh` + fact bar; yellow challenge box with `clip-path` corner cut; subtitles `700 3.5vh` white; one 20 s+ process take; add one number card.
- Application demo: sting + 3-4 uncut cycles; add a corner line per take (robot, task, cycle time) and "Real time".
