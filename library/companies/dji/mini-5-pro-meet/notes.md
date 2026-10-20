# Meet DJI Mini 5 Pro - All-In-One 1-Inch Large CMOS Mini Camera Drone  (DJI, 17 Sep 2025, 2:00 (≈106 s film + logo + 7 s end screen), 16:9, YouTube @DJI)
URL: https://www.youtube.com/watch?v=jRzpagPx6uY
Purpose: launch film (product introduction)
One-sentence point: a tiny drone with a big camera - one narrator walks through nine features, each proven with a gorgeous travel shot that was "shot on" the drone.

Analysed at 360p (YouTube only served format 18 that day); cuts and loudness are reliable, text sizes ±0.5 % H.

## Structure (cut times from metrics.json, adaptive detector)
- 0-9 s (8 %) promise: drone-shot travel wides (bay, kayak at sunset), a couple in the Alps, hands take the drone out of a bag and unfold it; VO starts at 1.2 s.
- 9-10.5 s name card: "INTRODUCING / DJI MINI 5 PRO" over the drone held in a hand.
- 10.5-20.6 s tech beat: ONE continuous 10 s CGI move - fly into the gimbal camera, it opens, the sensor grows from 1/1.3" to 1", an image appears inside the sensor and the camera pulls out to the full-frame mountain lake ("4K/60FPS HDR VIDEO").
- 20.6-100 s feature chapters (≈66 %), 6-12 s each: 48 mm mid-tele (split screen wide | tele), portrait, forward LiDAR (a translucent sphere around the drone in a forest; night castle), 10-bit D-Log M (split lavender field), 225° gimbal rotation (the image rolls), true vertical shooting (a 9:16 frame inset on its own blur), ActiveTrack (cyclists on a coast road), low light (city at dusk -> night), O4+ transmission + battery. Each chapter = people using the drone (remote in hands, pointing at the sky) + the drone's own footage with a feature label.
- 90-100 s summary montage: kayak, lavender, drone hovering in shallow focus, turquoise water; the claim line in VO.
- 100-106 s: drone hover against mountains, then the drone spins on black (render).
- 107-112 s: "DJI MINI 5 PRO" small on black, then the DJI logo on black.
- 113-120 s: YouTube end screen (silence from 106.8 s).

## Cut rhythm
- 86 shots in 120.1 s. Without the end (last shot from 102.3 s = drone on black + logo + end screen) ≈85 shots in 102 s → editorial ASL ≈1.2 s. Tool ASL 1.40 s, median 0.92 s, 52 % < 1 s, 2 % > 3 s, 43 shots/min.
- ASL per quarter 1.43 / 1.25 / 0.97 / 2.31 s (last quarter includes the end cards). Cuts per 10 s: 11 / 1 (the 10 s sensor move) / 8 / 10 / 6 / 7 / 10 / 9 / 10 / 12 / 1.
- Longest real shot: the 10.1 s CGI sensor move at 10.5 s, then a 6.3 s night-city timelapse. Shortest 0.4 s.
- Cuts on music onsets 45 % vs 33 % chance: cut to the beat under the VO.
- The scene detector missed 12-14 low-contrast cuts in landscapes; the adaptive detector found them (all checked against the sheet).

## Typography
- Name card: "INTRODUCING" thin caps, tracking ≈ +0.3 em, cap ≈2 % H; under it "DJI MINI 5 PRO" with "DJI MINI 5" in medium and "PRO" in light, cap ≈5.5 % H; white, centred at ≈25 % H over the product. Closest free: **Montserrat** Medium + Light.
- Feature labels: bold caps, white, cap ≈2.5 % H, left-aligned at x ≈6.5 % W, y ≈78 % H (bottom-left), 1-2 lines ("4K/60FPS HDR VIDEO", "TRUE VERTICAL SHOOTING"). Held for the whole chapter (3-8 s), cut in and out with the shot, no animation. Closest free: **Open Sans Bold** / **Inter Bold**.
- "SHOT ON / DJI MINI 5 PRO" watermark top-left (x 6.5 % W, y ≈12 % H): "SHOT ON" ≈1 % H, product name ≈3 % H line, on every drone shot.
- Legal micro-text (≈1.2 % H, centred, 2-3 lines) at the top or bottom edge of most feature shots.
- End: product name small (cap ≈2.5 % H) centred on black, then the logo.

## Colour / grade
- Travel-postcard grade: golden hour and blue hour, saturated but natural (alpenglow on the Matterhorn, lavender, turquoise water). Mean luma 0.36. No grain, no letterbox.
- Tech scenes: dark graphite CGI with a magenta-to-blue sensor gradient.
- Close on pure black.

## Camera / shots
- ≈60 % the drone's own aerial footage (orbits, reveals, top-downs, low fast passes), ≈30 % people with the drone (hands, remote screen, launching from the palm, couple/friends looking up), ≈10 % CGI (sensor, LiDAR sphere, spinning product on black).
- Split screens (wide | tele, normal | D-Log), 9:16 inset on a blurred copy, image roll for gimbal rotation.

## Transitions
- Hard cuts on the beat; one long in-camera CGI push into the lens that ends in full-frame footage (10 s); split-screen wipes; the image roll as a transition. No flashes.

## Sound
- One calm male narrator from 1.2 s to 100.5 s, ≈165 words (≈100 words/min), one sentence per 3-4 s, every feature named with its spec.
- Music: upbeat cinematic pop bed, steady; cuts on its beat.
- Integrated −17.0 LUFS, LRA 3.0 LU (very flat), true peak −1.3 dBTP. No drop-outs; hits only +15-19 dB (chapter starts at 1.65, 4.2, 7.3, 11.4, 17.6, 74.7, 79.7 s).
- Silence from 106.8 s (logo + end screen).

## What makes it premium
- Every feature claim is proven with the product's own beautiful footage, labelled "shot on".
- One long CGI push into the sensor explains the main upgrade without a chart.
- People are small and happy in big landscapes: the drone is a travel companion.
- A very consistent, quiet type system: one label bottom-left, one watermark top-left.

## Recipe (real footage + HTML/GSAP)
- Footage: drone/aerial stock at golden hour ("matterhorn lake reflection sunrise aerial", "lavender field aerial sunset", "coastal road cyclists aerial", "city skyline dusk timelapse", "kayak turquoise water aerial") + people with a drone ("hiker launching drone from hand", "remote controller screen hands").
- Pace: ≈1.2 s per shot on the beat, one 8-10 s continuous tech move after the name card.
- Feature label: `font: 700 2.5vh/1.2 'Inter'; text-transform: uppercase; left: 6.5%; top: 78%`, hard in/out with the shot.
- Watermark: `SHOT ON` 1vh over the product name 3vh, `left: 6.5%; top: 9%`.
- Name card: eyebrow `font: 300 2vh Montserrat; letter-spacing: .3em`, name `font: 500 5.5vh Montserrat` with the last word in weight 300, centred at 25 % H, fade 0.5 s.
- Split screen: two clips 50/50, 2 px dark divider, labels under each.
- VO ≈100 words/min, one sentence per feature; mix VO-led at ≈ −17 LUFS, music bed flat, no drops.
