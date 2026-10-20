# Agility Robotics - style

Examples (official @AgilityRobotics uploads):
| Example | Date | Length | Shots | ASL | Median | % < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [first-day-at-gxo](first-day-at-gxo/notes.md) | 2024-10 | 1:53 | 18 | 6.26 s | 4.57 s | 0 % | -21.4 | customer deployment film: site label + long takes + co-founder |
| [five-material-handling-workflows](five-material-handling-workflows/notes.md) | 2024-12 | 1:28 | 22 | 3.98 s | 3.07 s | 4.5 % | -11.6 | skills catalogue: big gradient titles + one take per workflow |
| [introducing-digit-5](introducing-digit-5/notes.md) | 2026-09 | 1:10 | 58 | 1.21 s | 1.15 s | 41 % | -14.4 | brand launch film: people first, fast montage, VO |

## Sub-styles
1. **Deployment film:** customer building → robot in customer livery doing one task → permanent location label ("Customer: Town, State") → co-founder interview under the b-roll → two full-cycle takes of ≈15 s (overhead + medium) → black end card. ASL 6.3 s, slows down towards the end.
2. **Skills catalogue:** one bold title per workflow (≈9 % H caps, mint gradient) over a 7-11 s take; quick 2-3 s tour first; ends on an overhead of the whole cell with every skill pinned to its station.
3. **Brand launch:** people and industry before the robot, a 3 s rack-focus reveal on the biggest hit, CAD and hologram graphics in brand teal, 1.2 s flat rhythm, VO wall to wall, no text until the logo.

## House rules
- **Work is the message:** tagline "Made for work"; totes, conveyors, AMRs, fence lines; real warehouses and Agility's own test cell.
- **Teal is the brand.** Robot, rules on name supers, title gradient, CAD and hologram all in teal/mint; customer colours (GXO red) stay when on site.
- **Geometric bold sans** (Poppins/Montserrat look) for labels and titles; wide caps for names; end card "AGILITY ROBOTICS / MADE FOR WORK" on black.
- **Overheads** to show the whole cell: start, path and target in one frame.
- **Fleet in frame:** several Digits at once in the test cell.

## How they show a real machine working / keep it credible
- Named customer + permanent site label on every on-site shot; customer livery on the robot.
- Long locked takes of whole task cycles (15.8 s, 15.3 s at GXO; 10.6-11.4 s in the catalogue).
- Real lab clutter: fiducial markers on the floor, cables, staff walking through.
- Gaps: none of the three films has a speed label or an autonomy/teleop label on screen; "regular operations" is only in the description. The Digit 5 launch mixes CGI (hologram, CAD, likely some product shots) with real footage without saying which is which, and labels the product a prototype only in the description.

## Compared with others
- vs 1X: warehouse vs home; customer + site name vs family life; bold titles vs frosted pills.
- vs Figure: Agility uses bolder, more "trade-show" type and brighter colour; Figure stays monochrome with typewriter labels.
- vs Chinese makers (Unitree, AgiBot, studied separately): Agility's films are slower and more customer-led; little spectacle, no stunts.

## Recipe (real footage + HTML/GSAP)
1. Deployment film: 4 s customer building → 7-8 s hook task → 3 b-roll shots at exactly 2 beats (≈1.9 s) → 4 s interview → 5 task shots of 4-10 s → two ≈15 s full-cycle takes → 5 s end card. Keep interview audio under the b-roll.
2. Site label: `font:700 4vh Poppins;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.5)`, bottom centre (y ≈82 %), on from the first on-site shot, never animated.
3. Workflow titles: `font:800 9vh Poppins;text-transform:uppercase;background:linear-gradient(#9FF0D5,#fff);-webkit-background-clip:text;color:transparent`, in 0.4 s from y 20, hold over the whole take.
4. Finish with an overhead and pinned dashed callouts per station.
5. Add what Agility leaves out: "Autonomous · 1x" corner label on every proof take, and a "Concept render" note on CGI shots.
