# Introducing DJI Mavic 4 Pro  (DJI, 13 May 2025, 2:42 (≈146 s film + name, logo, 7 s end screen), 16:9, YouTube @DJI)
URL: https://www.youtube.com/watch?v=BNEmDcQr6hk
Purpose: launch film (flagship product introduction, expedition register)
One-sentence point: a pro drone for the ends of the earth - no narrator, a big score, and an expedition across glaciers, deserts and cities, with spec callouts floating next to the drone.

## Structure (cut times from metrics.json, adaptive detector)
- 0-5 s: misty city aerial at dawn; "INTRODUCING / DJI MAVIC 4 PRO" centred (2-4.5 s).
- 5-19 s (9 %) the owners: a couple in a high-rise apartment plan a trip; hands open the case, macros of the triple camera.
- 19-34 s (9 %) promise montage: snow ridges, a climber, desert at sunset, a 4x4 in dust, a guide with the remote, children under a baobab.
- 34-42 s hero: the drone flies close to camera on blue sky; spec callouts appear next to each camera ("4/3 CMOS HASSELBLAD CAMERA / 100 MP / 6K/60fps HDR Video").
- 42-74 s (20 %) features with labels: infinity gimbal (red canyon roll), obstacle sensing (between ice walls), tele camera (whale), video transmission (city skyscrapers top-down), each 4-8 s.
- 74-97 s (14 %) set piece: a paraglider over Antarctic ice chased by the drone - the longest continuous sequence.
- 97-129 s (20 %) more features: dynamic range (sunset over ice), the new remote (hands in sand), desert caravan, night city, nightscape obstacle sensing (drone lights in the dark).
- 129-146 s (11 %) finale montage: rock arches, baobab at night, whale tail, the couple over the night city.
- 146-149 s: the drone unfolds and spins on black.
- 149-151 s: "DJI MAVIC 4 PRO / SPIN YOUR WORLD" on black; 151-154 s DJI logo; 155-161.5 s end screen (silence from 150.35 s).

## Cut rhythm
- 77 shots in 161.5 s, tool ASL 2.10 s, median 1.76 s, 30 % < 1 s, 29 shots/min. Without the black end (from 146 s): ≈76 shots in 146 s → ASL ≈1.9 s.
- ASL per quarter 1.84 / 1.92 / 2.37 / 2.02 s: steady, slightly longer in the paraglider set piece.
- Cuts per 10 s: 2 / 8 / 6 / 5 / 4 / 4 / 6 / 5 / 3 / 3 / 6 / 4 / 7 / 7 / 6 / 0 / 0. Longest real shots: 8.9 s (hero flight with callouts, 34 s), 5 s; three 0.48 s shots in a row at 12.7-14 s (case macros on the beat).
- Cuts on music onsets 39 % vs 11 % chance: strongly cut on the score's beats (music only).

## Typography
- DJI system (see dji/mini-5-pro-meet). Name card: tracked thin "INTRODUCING" (cap ≈2 % H) + "DJI MAVIC 4" medium + "PRO" light, cap ≈5.5 % H, centred at ≈50 % H over an aerial.
- Spec callouts: stacks of bold caps title (cap ≈2.6 % H) + 1-2 regular lines (≈2.4 % H) in white at ≈75 % opacity, placed next to the part they describe (upper left of the big camera, centre right of the tele camera), fading in one after the other.
- Feature labels bottom-left (x ≈6.5 % W, y ≈75-80 % H), "SHOT ON" watermark top-left; disclaimer line at the bottom of the opening shot (≈1.2 % H).
- End card: product name cap ≈3 % H + tagline ≈1.5 % H, centred on black.

## Colour / grade
- Epic teal-and-orange: icy cyan glaciers and steel-blue cities against orange deserts and sunsets; deep contrast but clean highlights. Mean luma 0.34.
- Interiors: soft neutral daylight, beige and white.

## Camera / shots
- ≈65 % the drone's own aerials (reveals, orbits, chase of a paraglider, top-down city, low passes over water), ≈20 % people with the drone (case, remote, climber, guide), ≈15 % the drone itself flying (shot from another drone) and product macros.

## Transitions
- Hard cuts on the beat; gimbal roll used as a transition (the canyon turns over); light leaks on sunset cuts. No graphic wipes.

## Sound
- Music only, no voice (speech detection: 0 words). Big orchestral-hybrid score with risers and drums.
- Integrated −12.7 LUFS (the loudest DJI film here), LRA 12.4 LU (wide: calm interior, huge set pieces), true peak +1.4 dBTP (clips).
- Hits: +18.3 dB at 12.85 s (case opens), +15.6 dB at 34.05 s (hero flight), +17.3 dB at 115.95 s; loudest 115.8 s (desert caravan). No drop-outs; silence under the end cards.

## What makes it premium
- Expedition scale: four continents of locations, people tiny in huge landscapes.
- Specs live next to the object they describe, never on a separate card.
- No narrator - the score and the pictures carry everything; cuts land on the beat.
- One long chase set piece (paraglider) as the emotional peak.

## Recipe (real footage + HTML/GSAP)
- Footage: "antarctica paraglider aerial", "glacier ice walls drone", "red canyon desert aerial", "camel caravan desert aerial", "baobab sunset", "whale tail aerial", "city skyscrapers top down night", "couple apartment window city view"; drone-in-flight shots on blue sky.
- Pace: ≈1.9 s per shot on the beat; one 20 s chase sequence at ≈60 % of runtime; 0.5 s macro shots on beats in the unboxing.
- Callout: `.t{font:700 2.6vh 'Open Sans'; text-transform:uppercase} .l{font:400 2.4vh 'Open Sans'; opacity:.75}` positioned next to the subject, stagger 0.3 s, fade 0.4 s; hold 3-6 s.
- Mix: music only, master ≈ −13 LUFS but keep true peak ≤ −1 dBTP (the original clips); end in silence.
