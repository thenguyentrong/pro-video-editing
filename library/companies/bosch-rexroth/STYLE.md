# Bosch Rexroth - style

Examples (official @BoschRexroth uploads, [EN] versions):
| Example | Date | Length | Shots | ASL | Median | % < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [electromechanical-actuators](electromechanical-actuators/notes.md) | 2026-10 | 2:21 | ≈8 blocks (adaptive 7) | ≈10-12 s per block | - | 0 % | silent | CGI application catalogue, split screen, no sound |
| [battery-manufacturing](battery-manufacturing/notes.md) | 2026-08 | 2:15 | 0 hard cuts (≈4 pieces by eye) | - | - | 0 % | -14.8 | trade-fair walk-through + one 81 s expert talk |
| [fiori-construction-dumpers](fiori-construction-dumpers/notes.md) | 2026-06 | 4:00 | 67 | 3.58 s | 1.96 s | 22 % | -22.5 | customer case: question cards + interviews + x-ray CGI |

## Sub-styles
1. **Application catalogue (silent CGI):** split screen - dark teal text panel left (category bar + three stepped sub-use tags), white clay render right with the product glowing cyan; 8 applications × 10-12 s; then an advantages grid and a key-data card (axial force up to 250 kN, speed up to 2.5 m/s, stroke up to 1,500 mm). The audio track is silent: built for stand screens.
2. **Trade-fair walk-through:** phone/gimbal walk through the stand with label boxes per exhibit, then one long piece to camera by a named expert in front of a moving demonstrator; numbers printed on the hardware.
3. **Customer case with question cards:** navy full-frame cards show the interviewer's questions (bold ≈7 % H, key words on cyan highlight boxes, typed word by word); customer CTO and driver answer in Italian with subtitles; benefit tags in cyan; a 52 s dark-blue x-ray animation explains the hidden transmission.

## House rules
- **Stripe system:** offset bars in navy, cyan, light grey and Rexroth red build name supers, labels, wipes and the logo animation (the logo assembles from stripes on white at start and/or end).
- **Colours:** navy #0b2a45, cyan #3fc1e6, grey, one red accent bar.
- **Type:** Bosch Sans-like grotesk (closest free: Inter), bold for titles, caps for categories and tags.
- **CGI for the hidden, real footage for the customer:** renders explain inside parts and applications; the customer film uses real machines on real sites.

## How Rexroth proves things
- Data cards with real limits and units ("up to 250 kN").
- Real machines moving behind a real expert in one take.
- Customer CTO and operator speak; the machine works on real ground.
- Gaps: benefit tags without numbers; the catalogue has no sound and no real footage.

## Recipe
- Catalogue: split layout 45/55, category bar `700 3.5vh Inter` caps on navy, tags stepped diagonally, stagger 0.5 s; one data card at the end.
- Labels and supers: two navy boxes + three offset stripe bars (`#3fc1e6 #d0d6db #e20015`), slide in 0.35 s, stagger 0.06 s.
- Question cards: navy, `700 7vh`, `<mark>` highlights `#3fc1e6` that grow behind key words.
- Stand film: 40 s walk (3 s pause per exhibit) + 60-90 s expert talk; add 2-3 cut-aways.
