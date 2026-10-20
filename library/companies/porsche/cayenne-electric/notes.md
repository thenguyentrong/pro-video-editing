# The new Cayenne Electric | Climbing to new heights  (Porsche, 2025-12-09, 2:07, 16:9, YouTube @Porsche)
URL: https://www.youtube.com/watch?v=2yrlNznB2lE
Purpose: launch film (product reveal with feature callouts)
One-sentence point: The electric Cayenne is a real Porsche - fast, comfortable, able to tow - shown through 6 feature callouts on cinematic driving footage.

## Structure (cut list; no voice-over)
- 0.0-14 tease in the dark: car head-on in a concrete studio with a ring light behind it (0-3.4 s), a man in shadow, red rear light bar spelling P O R S C H E (7 s), blue night road with headlights, man lit red (11 s). Teal/black palette.
- 14.2 reveal: a 0.12 s flash cut, then daylight - car on a mountain track (14.4 s).
- 15-30 callout 1+2: "Active aeroblades" (17-19 s), then "Sports car performance with up to 850 kW (1,156 PS) / Overboost Power with Launch Control" with a WLTP legal line (26-30 s).
- 30-41 interior: red-lit cockpit, "Cockpit experience with Flow Display" (32.7-36.5 s), steering wheel push-out to hands (37.4-40.9 s).
- 41-60 off-road: car on a gravel slope by a lake, "Porsche Active Ride" (51-55 s), lone man at the lake at dusk (56-59 s).
- 60-75 rain detail: crest with raindrops (61-62 s), wet body, light bar macro (68 s). 1.75 s silence at 73.05 s, then a +31 dB hit at 75.15 s into the interior/screen section.
- 75-90 utility: touch screen, camera view, "Towing capacity of up to 3.5 t" with a boat trailer, from a drone (81-84 s), mirror shot.
- 90-108 night/tunnel drive (fastest part, 8 cuts per 10 s), "Porsche Wireless Charging" pad (105-107.5 s).
- 108.5-113 name card: car in the ring-light studio again, "Cayenne electric" script logo fades in above it.
- 113.2-127.4 end: black, PORSCHE wordmark blurs in (113.9-117 s), fades, a dark teaser shot of a side profile (119-121 s), legal WLTP text in German + English (123-127 s).

## Cut rhythm
- 70 shots in 127 s (66 from cuts2 + 4 dark cuts at 31.1 / 31.5 / 32.7 / 37.4 s added by eye). ASL 1.82 s, median 1.44 s. ASL per quarter 1.38 / 1.87 / 1.68 / 2.27 s.
- Longest 14.24 s (logo + teaser + legal), 4.70 s (red cockpit with the callout), 4.64 s (name card). Shortest 0.12 s (14.24, the flash into daylight), 0.36 s.
- 27 % under 1 s, 14 % over 3 s. Feature callout shots are the long ones (3-4.7 s).

## Typography (data/specs on screen)
- Feature callouts: Porsche Next (closest free: Inter SemiBold), white, sentence case, no box, no line, no icon.
  - Headline cap+descender ~4.2 % of frame height, 1-2 lines, left-aligned; optional sub-line in Regular at ~3.3 %.
  - Placed in the negative space next to the feature (x 6-30 %, y 27-73 %), not in a fixed safe-area slot.
  - The label stays on screen across 2-4 cuts (e.g. 850 kW label 26-30 s over 4 shots), ~3-4 s total. In/out: soft fade ~0.3 s (the label is dim on its first frame at 26 s and fades at 36.5 s).
  - Numbers are written in full with units and conversions: "850 kW (1,156 PS)", "3.5 t".
- Legal line: centred, bottom (y ~90-94 %), ~2.7 % height, regular weight, shown only with the performance claim.
- Name card: "Cayenne" script logotype ~13 % height + small "electric" script, white, top-right of the car, fade in ~0.5 s.
- Wordmark end card: like the-promise (blur-in, 42 % width, 5 % height).

## Colour/grade
- Cool teal/steel base with deep blacks; two accent lights: red (interior, light bar, man at 11 s) and warm sunset. Daylight scenes are desaturated and slightly hazy.
- Night/tunnel shots crushed to near black (22 % of samples are mostly-empty dark frames).

## Camera/shots
- Tracking car-to-car shots, low wheel-level angles, Russian-arm style moves, FPV/drone top shots (81-84 s, 91-92 s), extreme macro on materials (crest, raindrops, light bar).
- Strong dutch angles (roll 20-40 degrees) on speed shots (40 s, 44 s, 96 s).
- A human "driver" character appears in silhouettes only - mood, not story.
- All footage looks real (practical car, real locations); some backgrounds may be enhanced (a guess - not visible at 480p).

## Transitions
- Hard cuts + light-based transitions inside a shot (the red cockpit light sweeps off at ~36.5 s). One 0.12 s flash frame at 14.24 s. Logo blur-in.

## Sound
- No VO. Electronic/orchestral score + car and whoosh SFX. Integrated -11.8 LUFS. Loudest 0.5 s at 47.8 s (-5.6 dBFS).
- Silences: 73.05 s (1.75 s) and 112.95 s (0.5 s) - each before a new section; hits right after (+31 dB at 75.15 s, +17 dB at 114.75 s on the logo).

## What makes it premium
- Specs are short facts, white, no boxes - they sit in the picture like a magazine caption.
- Callouts hold over several cuts, so the reader can read while the edit keeps moving.
- Dark tease -> 0.12 s flash -> daylight reveal.
- The studio ring-light set opens and closes the film (bookend).

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Callout component: `<div class="callout"><b>Towing capacity<br>of up to 3.5 t</b><span>sub-line</span></div>`; `font-family: Inter; font-weight: 600; font-size: 4.2vh; line-height: 1.12; color: #fff; text-shadow: 0 0 20px rgba(0,0,0,.35)`; sub-line `font-weight: 400; font-size: 3.3vh`.
- Position it per shot in the empty area near the feature (store x/y per callout), NOT tied to one clip: start it on clip 1 and end it on clip 3 of a 3-4 shot run. `tl.fromTo(c, {autoAlpha:0}, {autoAlpha:1, duration:.3}, t0).to(c, {autoAlpha:0, duration:.3}, t0+3.5)`.
- Legal line (if you state a performance number): `font-size: 1.9vh; bottom: 6vh; text-align: center; opacity: .9`.
- For a construction robot: "Lays 300 bricks per hour", "Payload up to 25 kg" - one fact per 3-4 s run, units always written.
- Open dark (teal grade `filter: saturate(.8) hue-rotate(-8deg) brightness(.8)`), flash 3 frames of white, cut to daylight hero.
