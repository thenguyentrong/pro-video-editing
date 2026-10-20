# Siemens - style

Examples (official @Siemens uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [transform-the-everyday](transform-the-everyday/notes.md) | 2023-10 | 1:31 | 40 | 2.27 s | 1.78 s | cinematic brand film, dialogue device, wireframe twins |
| [simatic-pick-ai-demo](simatic-pick-ai-demo/notes.md) | 2026-03 | 2:04 | 29 | 4.28 s | 3.96 s | product demo dialogue in a real plant + UI proof |
| [audi-software-defined-factory](audi-software-defined-factory/notes.md) | 2026-05 | 2:55 | 82 | 2.13 s | 1.48 s | customer testimonial at a trade show + plant b-roll |

## Sub-styles
1. **Brand film:** actors, a recurring question ("Can we do something about this?"), ~2.9:1 letterbox, each chapter real -> neon wireframe twin -> real result; mint gradient type for one big number gag; tagline + wordmark on navy.
2. **Demo dialogue:** visitor + engineer in the real plant, an "unknown object" test (her phone), product UI shown on a monitor and full-screen before the robot moves, locked-off real-speed robot shots, navy lower third.
3. **Customer testimonial:** handheld at the booth, trading-card name intro (cut-out B&W + mint caps), b-roll from the customer's plant every 10-20 s.

## Brand system
- Colours: navy #000028 backgrounds, mint/cyan gradient (#00ffb9 -> #00e6dc) for numbers, names and the digital layer, white text.
- Type: Siemens Sans (closest free: Inter) - Black caps for names/numbers, Bold/Regular for roles and taglines.
- End: white SIEMENS wordmark on navy, 3-9 s, sting after a 0.2-0.65 s silence.

## How Siemens shows a machine working credibly
- Real factory, real speed, full cell in frame, 3-8 s per robot shot; the software decision is shown on screen before the action ("Pick point calculation is successful").
- The digital twin is always shown as a stylised wireframe (clearly not real), then a cut to the real object.
- Claims are made by named people (engineer, customer VP) with full titles.

## Recipe for a construction-robot startup
1. Demo: site manager asks "can it handle this?" with an object chosen on camera -> your UI decides -> the machine does it in one locked-off shot.
2. Twin: draw your BIM/CAD as cyan SVG lines, `stroke-dashoffset` over 1.2 s, then cross-fade to the real site from the same angle.
3. Testimonial: customer on site, trading-card name intro, b-roll of your machine every 10-20 s.
4. Navy lower thirds that wipe in (`clip-path` inset 0.4 s) and hold 4-6 s.
