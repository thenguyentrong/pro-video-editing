# Quantum Systems Image Film: Aerial intelligence when it matters  (Quantum Systems, 2025-07-07, 1:30, 16:9, YouTube @QuantumSystems)
URL: https://www.youtube.com/watch?v=r-M8k0smtII
Purpose: brand / mission film (company image film)
One-sentence point: the whole product family and its software are framed as one system that helps soldiers decide calmly and fast.

## Structure
- 0.0-8.4 hook: a soldier from behind in a forest; the tagline super top-left; aerial of the forest; the view through a hatch. 0.5 s drop-out at 7.2, then +30.4 dB hit at 8.25.
- 8.4-24.9 first product: a case opened, the drone assembled in the field, the product name super top-left with a 3-row spec table (span, take-off weight, endurance) lower-left; a soldier looks up; the drone flies; a one-line value super about confident decisions in the centre.
- 24.9-34.8 software: a soldier at map screens, drone view inset over the real road, a ground station screen, a controller in hands.
- 34.8-52.8 second and third products: split-screen layouts on black with cut-out product pictures, monospaced telemetry columns and a running timecode; hand-held ground controller; fleet-management screen with drone list.
- 52.8-66 portfolio: a portfolio super, a multi-drone mission map, launch from a vehicle, a desert with three drones, an urban tower block with drones composited, an alpine forest.
- 66-78 operations: mission map screens, a helicopter team, a ship deck launch, an operator at dusk, a fleet UI with an execute button.
- 78.2-83.2 people: a 6-face grid of employees in the factory looking into the lens.
- 83.2-89.9 logo + tagline on black (6.6 s).

## Cut rhythm
- 49 shots in 89.9 s (scene detector + 2 cuts added by eye; UI changes inside a shot not counted). ASL 1.83 s, median 1.68 s. ASL per quarter 1.40 / 1.87 / 1.50 / 2.50 s.
- 25 % under 1 s, 10 % over 3 s. Cuts per 10 s: 5, 8, 6, 5, 4, 8, 5, 6, 1. Even, music-driven pulse.

## Typography
- Supers: geometric sans light/regular, sentence case, ≈5 % H, top-left (x ≈5 %, y ≈12 %) or centred; the product name ≈4.5 % with a 1.8 % descriptor under it. Closest free: Montserrat 300/400.
- Spec table: two columns (label / value with unit), ≈2.8 % H, lower-left, white, no box.
- Data overlays: tiny monospaced telemetry columns (≈1.2 %) and a running timecode (≈2.5 %, lower-right). Closest free: JetBrains Mono.
- Animation: soft fades and slides; text rarely held more than 3 s.

## Colour/grade
- Natural greens and greys, slightly desaturated, soft contrast; product shots on black with cold white light; UI in green/teal.

## Camera/shots
- Mix of real field footage (forest, soldiers, vehicles, helicopter, ship) and studio product shots; several composited layouts (split screens, cut-outs, drones placed over city plates). Close-ups of hands on controllers.

## Transitions
- Hard cuts, slides of split-screen panels, soft fades into the layouts.

## Sound
- Voice-over: one calm narrator, ≈140 words over 86 s (≈1.6 words/s): questions, then contrasts, then claims, ending on the tagline.
- Integrated -8.9 LUFS (very loud), LRA 5.9 LU, true peak -0.1 dBTP. Drop-out 7.2-7.7 then +30.4 dB hit; dense hits 8-20 s (+25 to +30 dB). Ending: fade.

## What makes it premium
- Every product appears with its numbers (span, weight, endurance) as a clean table, not as adjectives.
- The software is shown as real screens next to real soldiers.
- Real employees close the film (the makers stand behind the claim).

## Recipe (real footage + HTML/GSAP)
- Tagline super in Montserrat 300 5vh top-left; product name 4.5vh + descriptor 1.8vh; spec table as a 2-column grid 2.8vh lower-left; fade 0.4 s in, 0.3 s out, hold 2-3 s.
- Telemetry: 6-10 lines of mono text 1.2vh, a timecode counter `00:0m:ss:ff` updated per frame.
- End: 3x2 grid of employee portraits (each `<video>` 4-5 s), then logo + tagline 6 s.
