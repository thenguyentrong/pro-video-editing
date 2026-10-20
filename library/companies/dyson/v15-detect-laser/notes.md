# Discover Dyson V15 Detect laser technology - TV commercial  (Dyson, 2021-06-02, 0:56 film + 10 s end screen, 16:9, YouTube / TV)
URL: https://www.youtube.com/watch?v=Yh_jmGso64E
Purpose: TV commercial / product explainer
One-sentence point: A laser shows you dust you could not see, a sensor counts it, and the machine's engineering (cyclones, motor, filtration) removes it - explained by a calm voice over CG.

Structure (VO lines from whisper in quotes):
- 0.0-16.2 one continuous CG camera move: the vacuum swings down on a dark wood floor, the cleaner head lands, the green laser fan switches on and lights thousands of dust particles (frames/t007.0s.jpg), camera skims the floor, zooms THROUGH the dust into a macro world of green spiky allergen particles (11-15 s, t013.0s), then whooshes out. "Dyson's latest vacuum is the only one to use a laser. It's precisely angled to reveal invisible dust..."
- 16.2-23.1 the wand: dust travels up the tube into a cut-away bin with the particle sensor (t020.5s). "...this special sensor, which counts each size..."
- 23.1-25.8 the LCD: bar chart of particle counts by size (t024.0s). "...and gives you scientific proof."
- 25.8-35.2 the cleaner head on a dirty floor, shell turns transparent (x-ray) to show the brush bar (t032.0s).
- 35.2-46.7 cyclones (t036.0s), motor and filter revealed by cutaways, the LCD again. "Fourteen redesigned cyclones... the power of this [Hyperdymium] motor, and five-stage filtration capturing 99.99% of dust" (whisper wrote "hypodinium"; Dyson's motor name is Hyperdymium)
- 46.7-54.0 product on a dirty floor, mini motorised tool on a sofa.
- 54.0-56.0 end card: white wall with window-light stripes, product standing right, text left "Buy direct from the people who made it." + "dyson v15 detect" (t054.8s).
- 56-66 black YouTube end screen (excluded from the stats).

Cut rhythm (0-56 s): 10 shots, ASL 5.60 s, median 3.92 s, quarters 14.0 / 3.5 / 3.5 / 3.5. Longest 16.2 s (the one-take opening), 7.5 s, 6.9 s. Shortest 2.0 s (end card), 2.6 s. 0 % under 1 s, 70 % over 3 s. Many more "beats" happen inside shots (camera moves, x-ray reveals, zoom-throughs): about 17 soft changes. Cuts on onset 0 % = cuts follow the voice, not music.

Typography: almost none in the body (only the device's own LCD numbers). End card: Dyson's sans (clean geometric-humanist, sentence case; free match: Lexend / Outfit with a two-storey a), dark grey #333 on light, 3 lines left-aligned at x 13 %, line box ~7 % of frame height (cap height ~4.5 %), then the wordmark "dyson" + model name in the product accent colours ("v15" blue, "detect" grey), ~6 % high. Product on the right third. Static, no animation visible.

Colour/grade: neutral CG studio, R-B +2. Product colours do all the work: purple, nickel, yellow-gold cyclones, red trigger; one effect colour = laser green (#39ff6a-ish) that turns the dust and the macro world green. Median luma 99, contrast p95-p5 160 (crisp). No people, no skin.

Camera/shots: 100 % CG product animation (photoreal). Long motion-controlled-looking camera paths: low floor skims, orbits, macro push-ins, zoom-throughs into microscopic scale, x-ray cutaways where the shell fades to glass. Diagonal "hero angle" product compositions.

Transitions: 9 hard cuts; most changes are continuous moves: zoom-through into the particles (10.5-11) and back out with a motion-blur whoosh (15-16), x-ray dissolves of the shell (30-33, 39-43).

Sound: British-accent male VO from 0.3 to 59 s, every second covered; soft music bed + SFX (onsets 0.53/s, flat level -20 to -24 LUFS-M). Integrated -23.1 LUFS = EBU R128 broadcast level (TV master uploaded as is). No hits, no drop-outs.

What makes it premium:
- Shows the invisible: laser + microscopic CG make an abstract benefit (clean) visible and countable.
- Engineering as spectacle: x-ray cutaways of real internal parts (cyclones, motor, sensor) = credibility.
- One-take CG opening (16 s) without a cut feels expensive and controlled.
- Calm, factual VO with numbers ("14 cyclones", "99.99%") - no hype adjectives.

Recipe (real footage + HTML/GSAP):
1. If no CG: shoot real macros with a green line laser grazing a floor at 1-2 deg (dust lights up), plus a clear acrylic/cut-away prop or exploded flat-lay of parts.
2. HTML x-ray: stack two aligned images (shell + internals), GSAP `clipPath: "inset(0 100% 0 0)" -> "inset(0 0 0 0)"` on the internals over 1.2 s `power2.inOut`, plus `opacity .4` on the shell = cutaway reveal.
3. Zoom-through: scale the macro layer 1 -> 6 over 0.6 s `power3.in` with a 6 px CSS blur at the end, cut to the next layer at scale 0.6 -> 1 `power3.out`.
4. Write the VO first (one fact per 3-4 s), cut picture to the sentence ends, not to music.
5. End card: light wall with diagonal window-light stripes (`repeating-linear-gradient(120deg, ...)` at 6 % opacity), product right third, 3-line claim left at 13 % x, 4.5 % cap height, wordmark under it. Hold 2 s.
6. Mix for the platform: -23 LUFS for broadcast, -14 for social.
