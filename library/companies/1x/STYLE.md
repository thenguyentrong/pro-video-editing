# 1X - style

Examples (official @1X uploads):
| Example | Date | Length | Shots | ASL | Median | % < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [introducing-neo-gamma](introducing-neo-gamma/notes.md) | 2025-02 | 0:37 | 13 | 2.86 s | 2.58 s | 0 % | -20.9 | lifestyle teaser, no text, music only |
| [redwood-ai](redwood-ai/notes.md) | 2025-06 | 1:25 | 10 | 8.55 s | 9.66 s | 0 % | -17.1 | capability demo: one take per skill + engineer |
| [neo-home-robot-order-today](neo-home-robot-order-today/notes.md) | 2025-10 | 9:53 | 141 (162 adaptive) | 4.21 s | 2.79 s | 5 % | -16.4 | keynote launch film with chapters, specs, price |

## Sub-styles
1. **Lifestyle teaser:** the robot as a calm resident: 2-5 s human moments (serving, carrying laundry, sitting with the family), shots through house windows, warm oat palette, no words on screen, soft music at about -21 LUFS.
2. **Capability demo:** one locked take per skill (6-14 s), a lower-case technical word beside the action ("generalization", "retrial"), a deliberate failure and retry, a named engineer between blocks.
3. **Keynote launch film:** Apple-style presenter in a wood studio, frosted spec panels, three numbered chapters (Chores / Companion / Autonomy), price pills on an off-white end card.

## House rules
- **Home, not factory.** Real houses, daylight, plants, wood, linen; people in almost every frame. The beige knit suit sets the palette of the whole film.
- **Frosted pills.** Labels sit in translucent capsules with blur, sentence case, one grotesk (Inter is the closest free match), ≈3.3 % H; small plain words (≈1.7-2.7 % H) for status lines.
- **Small text, big calm.** No kinetic type, no hits on words; text fades in and holds.
- **Named people with titles** carry claims (founder, presenter, VP of AI); name super left, mid-height, no box.

## How they show autonomy vs teleoperation
- The launch film separates the two modes on screen: teleoperated chores get a mode pill ("Expert Mode Enabled") and the head ring turns blue; a remote operator is shown on a phone; the autonomy chapter labels each sub-step with a small "Autonomous" line.
- The cold open also shows a person in a VR headset whose movements NEO mirrors: teleoperation is shown as a feature, not hidden.
- Gaps: no film studied uses a speed label (no "1x", no "real time"); the Gamma teaser and Redwood demo carry no autonomy/teleop label on screen at all (Redwood's description says autonomous). Older EVE-era clips (where 1X is said to have used "autonomous, 1x speed" labels) were not studied; none of these three films carries such a label.
- One-take proof lives in the capability demos (Redwood: 6-14 s takes), not in the launch film, where the autonomy wide is cut into 2-17 s pieces.

## Compared with others
- vs Agility: 1X sells to homes (warm, people, feelings, price per month); Agility sells to warehouses (named customer site, task cycles, totes).
- vs Figure: both use near-monochrome product colour, but 1X adds people and warmth where Figure stays cool and industrial.

## Recipe (real footage + HTML/GSAP)
1. Shoot in a real, lived-in home with daylight; product colour repeated in walls and props.
2. For each skill: one locked take of 6-14 s; top-down for table tasks; include one disturbance and one failed try.
3. Label the mode every time: a frosted pill bottom centre ("Remote assist" / "Autonomous") plus a status-light colour change on the robot; add a speed note if not 1x.
4. Pill CSS: `padding:1.6vh 2.4vw;border-radius:99px;background:rgba(255,255,255,.18);backdrop-filter:blur(12px);font:500 3.3vh Inter;color:#fff`, in 0.35 s `power2.out` from y 8.
5. Launch structure: cold open montage 12 % → founder 7 % → design macros 10 % → presenter + specs 20 % → 3 numbered chapters 50 % → price end card.
6. Music soft (-17 to -21 LUFS integrated for teasers; dialogue films around -16), cut to speech, not to beats.
