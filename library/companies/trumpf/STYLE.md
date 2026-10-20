# TRUMPF - style

Examples (official @TRUMPFtube uploads):
| Example | Date | Length | Shots | ASL | Median | % < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [blechexpo-2025](blechexpo-2025/notes.md) | 2025-09 | 0:31 | 8 (adaptive) | 3.93 s | 3.24 s | 0 % | -19.2 | trade-fair invitation ad, outline verbs on blue |
| [trubend-center-7020](trubend-center-7020/notes.md) | 2026-01 | 3:14 (9:16) | 3 + logo | ≈163 s main take | - | 0 % | -11.3 | vertical one-take application demo |
| [hago-laser-welding-case](hago-laser-welding-case/notes.md) | 2025-09 | 3:40 | 67 | 3.28 s | 2.04 s | 0 % | -19.1 | customer success story, strict 2 s b-roll grid |

## Sub-styles
1. **Trade-fair teaser:** four verbs in huge outline caps (≈18 % H: DISCOVER / PRODUCE / MEET / EXPERIENCE), each followed by a short lowercase phrase (≈8 % H); all footage tinted TRUMPF blue with diagonal blue wipes; date, city and ticket CTA on blue cards; "you win" mark; 31 s, music only.
2. **Vertical one-take demo:** 9:16, tripod, panel bender + robot + pallet in one frame, one ≈163 s uncut cycle, two tiny captions, loud music (-11.3 LUFS), no machine sound.
3. **Customer success story:** blue gradient title panel with a 5-line summary over a drone shot; white name boxes and a white fact box (location, employees, products); German interviews; b-roll on an exact 2.0 s grid (43 of 65 gaps); a flat explainer of the optics; "you win" blue card + white logo.

## House rules
- **Electric TRUMPF blue** (#0028FF-ish) for panels, tints, wipes and end cards; white for name and fact boxes.
- **Light humanist sans** (closest free: Noto Sans / Open Sans), light weight for titles, regular for body; outline caps only in ads.
- **Brand line "you win"** as a bold lowercase mark on blue, at the start and end.
- **Clean, high-key factories;** macro of sparks and seams as the visual hero.

## How TRUMPF proves things
- The success story names the customer, place and head-count and shows seams and a cross-section.
- The vertical demo keeps the whole cycle in one take.
- Gaps: no process numbers (cycle time, leak rate) on screen; the English-titled case has no subtitles for the German speech; music replaces machine sound in the demo.

## Recipe
- Ad: tint overlay `rgba(0,40,255,.75→.3)`, verb `700 18vh` outline (`-webkit-text-stroke:1.5px #fff`), phrase `700 8vh`, diagonal wipe 0.6 s, end cards 3 s each.
- Case: panel slides in 0.8 s over the drone shot, title `300 9vh`, summary `400 3.5vh`; b-roll exactly 2.0 s; 0.3-0.5 s music gap before each interview bite.
- Demo: 9:16 tripod one-take; add a cycle timer and "Real time".
