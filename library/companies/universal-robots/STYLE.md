# Universal Robots - style

Examples (official @UniversalRobotsVideo uploads):
| Example | Date | Length | Shots | ASL | Median | % < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [gen7-physical-ai](gen7-physical-ai/notes.md) | 2026-09 | 1:32 | 37 (adaptive) | 2.49 s | 1.72 s | 38 % | -19.6 | CGI launch teaser, kinetic type, music only |
| [ur15-launch](ur15-launch/notes.md) | 2025-05 | 2:58 | 41 | 4.34 s | 2.48 s | 10 % | -13.4 | launch film: real people + CGI spec chapters, VO |
| [injection-molding-roi](injection-molding-roi/notes.md) | 2025-10 | 3:10 | 68 | 2.80 s | 2.49 s | 0 % | -20.3 | customer case: interviews + subtitles only |

## Sub-styles
1. **Kinetic-type teaser (Gen 7):** deep-blue field, dark product renders, huge condensed statements (≈14 % H per line) built word by word in two colours (light blue + white), thin leader-line callouts on ports and buttons; 5-13 s product orbits alternate with 0.3-1 s type beats.
2. **Launch film (UR15):** heritage open in a desaturated teal grade with years in square tiles; three chapter words ("Optimized", "Personized", "Futurized"); CGI spec shots on light grey with moving blue squares and quarter circles (one spec per shot, metric / imperial); real factory footage for people and hand-guiding; slow female VO (≈1.6 words/s).
3. **Customer case:** real shop, interview-led, b-roll on a 2.0-3.0 s grid, burned-in subtitles as the only text (no name supers, no number card).

## House rules
- **Blues only:** navy, UR blue, light blue; grey product with light-blue joint caps.
- **Graphic system = squares + quarter circles** (2025) or **"+" grid marks on deep blue** (2026); both also act as transitions.
- **Type:** geometric sans for specs and chapters (closest free: Montserrat); heavy condensed for statements (closest free: Anton / Oswald 700); thin leader lines + dark pills for callouts.
- **Product shots are CGI; people shots are real.** They alternate by chapter and rarely share a frame.

## How UR proves things
- Specs as text (5 m/s, 15 kg / 33 lbs, Ø 204 mm) on CGI; payback as a spoken customer claim (title: "ROI in 1,500 hours").
- Gaps: no long real take of a cobot cycle in any of the three (longest real b-roll ≈5 s in the case film); the speed claim is never shown on real footage; no names on screen in the case film.

## Recipe
- Teaser: background `linear-gradient(#00122e,#00297a)`; statements `Anton 14vh`, first words `#5FA8D8`, last words white, word stagger 0.2 s; callouts line + pill `1.8vh`.
- Launch: chapters on dark teal (`600 6vh Montserrat`), spec `700 6vh` label + `400 6vh` value, shape wipes 0.6 s `power3.inOut`.
- Case: subtitles `400 4vh 'Open Sans'` bottom centre; b-roll at 2.0/3.0 s; add name supers, one ROI number card and one 10-15 s cycle take.
