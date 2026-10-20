# From 1886 to 2026 - 140 years of innovation  (Mercedes-Benz, 2026-01-30, 1:50, 16:9, YouTube @MercedesBenz)
URL: https://www.youtube.com/watch?v=3WnnlvogOUE
Purpose: heritage/anniversary brand film (140 years since the first patent car)
One-sentence point: Every Mercedes since 1886, shown as museum objects on one grey stage, adds up to one idea: pioneering spirit.

## Structure
- 0-5 the 1886 patent motor car alone on a grey studio cyc; vertical chapter label "VISIONARY" on the left edge, a 2-line caps caption bottom right (model + what it did), small "+" registration marks in the four corners. Voice-over starts at 0.9 s and runs to 84 s.
- 5-87 **chapters** (vertical labels): OUR DNA, NEXT LEVEL, QUALITY, SAFETY, DESIGN, EMPOWERING, INVENTING, STATE OF THE ART. Each chapter = 3-6 cars, old and new mixed, always on the same grey cyc. Picture changes by **sliding panels**: the frame splits 1/3 + 2/3 or into 2-4 panels, panels slide in and push each other out; details (steering wheel, grille, crash-test dummy, wheel) sit next to the full car.
- 80-84 a dark beat: one car under a top light on black, then the newest S-Class front-on (≈3 s hold).
- 84-87 back to the 1886 car: the circle closes.
- 87-97 **collage**: the frame becomes a grid of tiles (9, then ≈30, then several hundred tiny tiles of every car and detail from the film); "Welcome home." in serif in the centre (89-92 s), then "140 YEARS OF INNOVATION" (93-97 s).
- 98-100 star logo on black. 100-110 silent web end slate ("Visit us" + the 1886 car), 10 s.

## Cut rhythm
- Hard cuts are rare: 12 detected (ASL 8.5 s is meaningless here). The edit is done with panel slides and wipes: the soft-transition detector finds 63 more picture changes in 0-100 s. Together ≈74 changes in 100 s, **one new image every ≈1.35 s** (≈, cuts + panel moves).
- Hard cuts per 10 s: 0-3; panel moves 5-9 per 10 s, densest 71-78 s (one every ≈0.6-0.8 s).
- Collage section 87-97 s is one continuous zoom-out of a growing grid.

## Typography
- Vertical chapter labels: light grotesque caps (Mercedes corporate sans; closest free: Inter Light / Manrope Light), rotated 90°, reading bottom-to-top on the left edge, cap height ≈4.8 % of frame height, label length ≈29 % of height, x ≈2-4 % from the left.
- Caption: 2 lines, caps, ≈2 % H, right-aligned at x ≈98 %, y ≈82-86 %.
- Corner marks: thin "+" crosses, ≈3 % of height, inset ≈3 % W / 10 % H.
- "Welcome home.": serif (Mercedes corporate serif; closest free: Cormorant Garamond / Libre Caslon Text), sentence case, ≈3.5 % H, centre.
- "140 / YEARS OF / INNOVATION": "140" in light serif ≈8 % H next to a 2-line caps sans block ≈2.7 % H, centred.
- Small legal/consumption line along the bottom on modern cars.

## Colour/grade
- One stage for everything: cool grey seamless cyc, soft top light, gradient from light grey (top) to darker floor; black only for the night/dark beat and the logo. Car colours (lime, orange, red) are the only saturation.

## Camera/shots
- All cars as museum objects: side profile, front three-quarter, top-down, and macro details. Slow dolly moves and turntable-like rotation. Probably a mix of real studio shots and CGI.

## Transitions
- Split-screen panels that slide horizontally/vertically (the signature), hard cuts between chapters, a growing grid for the finale, fade to the logo.

## Sound
- Continuous narrator with orchestral/electronic score. No drop-outs. Integrated -13.1 LUFS, LRA 3.9 LU, true peak -1.6 dBTP. Hits +15 to +18.5 dB at 16.2 and 58.25 s (chapter starts). 10 s digital silence on the end slate.

## What makes it premium
- One neutral stage makes 140 years of very different cars into one catalogue.
- Chapter words instead of dates: the film argues values, not history.
- Speed comes from panel motion, not from cutting: calm and fast at the same time.
- The finale grid shows the scale of the archive in 10 s.

## Recipe (HTML/GSAP + studio shots)
- Stage: `background: linear-gradient(#b9bec4 0%, #9aa0a6 60%, #7d8389 100%)`; every object cut out or shot on the same grey.
- Panels: `.panel{position:absolute; top:0; height:100%; overflow:hidden}`; `gsap.fromTo(newPanel, {xPercent: 100}, {xPercent: 0, duration: .6, ease: 'power3.inOut'})` while the old panel moves to `xPercent: -33`; one change every 1.0-1.5 s, 0.6-0.8 s in the densest chapter.
- Chapter label: `writing-mode: vertical-rl; transform: rotate(180deg); font: 300 4.8vh Inter; letter-spacing: .04em; left: 2vw`.
- Finale grid: CSS grid 3x3 → 6x6 → 24x24 with `gsap.to(grid, {scale: .25, duration: 8, ease: 'power2.inOut'})`, centred serif line on a dark scrim, then logo on black.
