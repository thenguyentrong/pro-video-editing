# Zipline safely flies 100 million autonomous miles  (Zipline, 2025-03-10, 1:06, 16:9, YouTube @FlyZipline, best available 360p)
URL: https://www.youtube.com/watch?v=Ukj4Sdd8TMQ
Purpose: mission / milestone film (one number made tangible)
One-sentence point: one safety milestone (a distance flown autonomously) is translated into comparisons a viewer can feel, then into the real deliveries behind it.

## Structure (narrated)
- 0.0-5.6 hook: runway POV at speed; the number counts in as a giant white super with a small question line above and the unit below.
- 5.6-18.5 comparison 1 (CGI): earth and moon with a measuring line (12.9 s shot), then a dark globe with the country highlighted in brand green and its road network, with a condensed super.
- 18.5-25.3 comparison 2: through clouds into a night-traffic timelapse (the cost of doing it by car).
- 25.3-37.4 what it meant: the drone over water at speed, health workers handling medicine, a man shading his eyes looking up, the drone in sky, a hospital ward, a drip.
- 37.4-54.7 at scale: the home-delivery droid in yards, firefighters opening a package, rolling hills, a family with a delivery, a child carrying the box with its paper parachute, the order app on a phone.
- 54.7-66.3 end: real photos fly in as rounded cards on white and collapse into the logo (11.6 s), logo turns from colour to black.

## Cut rhythm
- 22 shots in 66.3 s (scene detector + 4 cuts added by eye; the cloud-to-traffic change is a dissolve). ASL 3.02 s, median 1.25 s. ASL per quarter 8.29 / 2.07 / 1.38 / 5.53 s.
- 23 % under 1 s, 32 % over 3 s. Cuts per 10 s: 1, 2, 2, 9, 5, 2. Long graphic shots first, fast real montage in the middle (densest 30-40 s), long collage at the end.

## Typography
- Big number: grotesk 700, ≈20 % H, white, left of centre, with a ≈3.5 % question line above and a ≈3 % unit word right-aligned below; digits roll in. Closest free: Inter 700.
- Comparison supers: condensed bold sentence case ≈5 % H, centred over the globe. Closest free: Barlow Condensed 600.
- Real footage carries no text.

## Colour/grade
- Bright, warm, saturated daylight for real footage; CGI in dark navy with brand green; end on clean white.

## Camera/shots
- Real: FPV-style low flights, ground long lens on the drone, handheld documentary at clinics and homes. CGI only for the abstract comparisons (globe, moon, map).

## Transitions
- Hard cuts; a cloud fly-through as transition (14.7-18.5); photo cards fly in and assemble into the logo.

## Sound
- Narrator ≈111 words in 58 s (≈1.9 words/s): question -> two comparisons -> impact numbers -> benefits -> claim.
- Integrated -19.0 LUFS, LRA 4.6 LU, true peak -2.6 dBTP. Hits at 1.05 (+31 dB), 10.35, 14.7, 6.05. Silence under the end.

## What makes it premium
- One number, translated twice (space, roads), before any product appears.
- The real deliveries follow the abstract numbers, so the claim lands on people.
- CGI is used only for the abstract, real footage for the real.

## Recipe (real footage + HTML/GSAP)
- Giant number: Inter 700 20vh, digits roll (`gsap.to(obj,{v:1e8, duration:1.6, ease:'power3.out'})` with `toLocaleString`), question line 3.5vh above, unit 3vh right-aligned below.
- Two comparison cards (globe/map in navy + one brand colour), 5-6 s each, condensed 5vh centred super.
- 12-15 real shots of 1-2 s for the impact list, no text.
- End: 20-30 real photos as rounded cards (`border-radius:2vh`) flying in, then `scale(0)` stagger into the logo position.
