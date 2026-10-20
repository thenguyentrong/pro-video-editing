# The First of a New Era | Introducing the New BMW iX3  (BMW, 2025-09-05, 1:54, ≈2.2:1 letterbox in 16:9, YouTube @BMW)
URL: https://www.youtube.com/watch?v=qxPFC4OkeHw
Purpose: car launch film (first Neue Klasse model) told as a heritage journey
One-sentence point: BMW did not invent the car, it invented a feeling; the iX3 starts the next era of that feeling.

## Structure
- 0-28 **1960s-70s**: a sunlit pool (5.1-s opening shot), a man in a hat walks to a white BMW saloon, coastal road; then a 1970s driver in a red shirt on a desert road, a tachometer, a tractor in a field. Film look with grain and warm cast.
- 28-39 **1980s**: hotel driveway, valet boy in a cap, a boxy saloon, the valet drives off.
- 40-47 **2000s**: desert track, an SUV through dust, a woman with a film camera, horse riders.
- 48-56 **2010s**: neon Asian street at night in rain, an electric sports car with red light blades.
- 57-65 the BMW four-cylinder headquarters at night, lights turning on (the "home" beat).
- 65.24-68.8 **black hold 3.56 s**.
- 68.8-81 **reveal in the dark**: the new illuminated grille appears from black, light sweeps across the body, interior with "WELCOME" on the screen, two people in the car.
- 82-104 **daylight drive**: the new iX3 on mountain and lake roads; the drivers from the old eras appear in the new car (92 s, 100 s): the past rides in the future.
- 104.9-107 light-speed tunnel with "THE FIRST OF A NEW ERA." (2.2 s), logo close-up on the tail.
- 108-111 "BMW iX3" over the car driving away; 111-112.5 roundel + "Freude am Fahren" over the same shot; 112.5-114.3 black, silent.

## Cut rhythm
- 78 shots in 114 s. ASL 1.46 s, median 1.16 s, 33 % under 1 s, 41 shots per minute.
- ASL per quarter 1.43 / 1.14 / 1.68 / 1.50 s: the pace is even; the drama comes from the black hold and the light change, not from speed.
- Cuts per 10 s: 3, 8, 10, 9, 6, 8, 3, 7, 8, 9, 5, 1.
- Longest 5.52 s (106.96, logo into end), 5.12 s (opening pool), 3.88 s (103.08). Shortest 0.36 s.
- Cuts on onsets 8 % vs 13 % chance: the editor avoids cutting on the beat.

## Typography
- BMW corporate sans (closest free: Inter SemiBold / Manrope SemiBold).
- "THE FIRST OF A NEW ERA.": caps, ≈2.9 % H, centre, white on the dark tunnel.
- "BMW iX3": mixed case, ≈6.3 % H, placed right of centre (x ≈60-80 %, y ≈28 %) in the sky.
- Roundel + small claim, centre, ≈8 % H, on the final shot.

## Colour/grade
- Each era has its own look: warm faded film (60s-70s), saturated warm interiors (80s), dusty orange (2000s), teal-and-red neon (2010s), then a clean neutral daylight for the new car. Letterbox ≈2.2:1 (bars ≈10 % top and bottom).

## Camera/shots
- Period recreations with costumes and original cars; car-to-car tracking, inside-the-car profiles, inserts of gauges and hands on wheels; aerials over lake roads at the end. Reveal shot: light-painting on a black body.

## Transitions
- Hard cuts; a black hold of 3.56 s between past and future; one light-tunnel effect for the line.

## Sound
- Slow narrator, only 7 lines in 100 s; a period-pop-to-orchestral score. Integrated -16.6 LUFS, LRA 10.8 LU. **Section loudness rises: 0-65 s -19.9 LUFS, 69-112 s -14.1 LUFS** (+5.8 LU after the black hold). Biggest rise +20.5 dB at 19.8 s. 1.8 s silence at the end.

## What makes it premium
- History as staged cinema, not archive: every era is rebuilt with the same care.
- A long black hold separates "then" from "now".
- Characters from the past re-appear in the new car: one simple idea that ties the film.
- Few words, and the loudest part is the future.

## Recipe
- 4-5 eras of 8-15 s each, shots 0.8-2 s, each era with its own CSS grade class (e.g. `.era60{filter: sepia(.3) contrast(.9) saturate(.8)}`, `.neon{filter: saturate(1.3) hue-rotate(-10deg) brightness(.8)}`).
- At ≈57 % runtime: black hold 3-3.5 s, then the product appears from black with a light sweep (`mask-image: linear-gradient(...)` animated from -100 % to 100 % over 2 s).
- Raise the mix by ≈+6 LU for the future part.
- Close: line on an abstract light tunnel (2 s), product name in the sky, logo on the last shot, 1.8 s black.
