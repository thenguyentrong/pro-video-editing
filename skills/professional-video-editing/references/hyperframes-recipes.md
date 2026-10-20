# Code-built film recipes (HTML + GSAP via Hyperframes)

Tested with `hyperframes` 0.8.x. A 16 s demo with every recipe is `assets/recipes-demo.html`; it expects your own images in `assets/img/` (a photo, a cropped headline, a product shot) and fonts in `assets/fonts/`.

Start a project: `npx hyperframes init <name> --example blank --non-interactive`, copy the `<style>` blocks you need, declare every named font with `@font-face` pointing at a local file (lint requires it), then `npx hyperframes check` and `npx hyperframes render`.

Rules that bite:
- One paused timeline on `window.__timelines["<composition-id>"]`.
- A `<video data-start>` must not sit inside another element with `data-start`.
- Every `<audio>` needs an `id`, or the render is silent.
- Never put a CSS `transform` on an element GSAP also transforms; use `fromTo`.
- `fromTo` renders its start state immediately; a second `fromTo` on the same element needs `immediateRender: false`.
- Wrappers that zoom past the frame need `data-layout-allow-overflow`.
- Many blur/radial-gradient layers slow the render and trigger a warning: share one background and one vignette layer for the whole film instead of one per shot.

## R1 One grade for every shot
```css
.shot img, .shot video { object-fit: cover; filter: contrast(1.06) saturate(0.86) sepia(0.08) brightness(0.96); }
.vignette { position:absolute; inset:0; background: radial-gradient(ellipse 75% 70% at 50% 50%, rgba(0,0,0,0) 55%, rgba(0,0,0,.55) 100%); }
```
Stills move by slow drift only: `scale 1.05 → 1.0`, `ease: "none"`, over the whole shot. No zoom punches on stills, no Ken Burns on every still.

## R2 Credit block (opening-credits language)
```css
.credit { position:absolute; text-align:center; color:#f4f3ef; text-shadow: 0 0 28px rgba(0,0,0,.55), 0 1px 3px rgba(0,0,0,.4); }
.credit .role { font-weight:400; font-size:22px; letter-spacing:.32em; opacity:.82; }
.credit .name { margin-top:10px; font-weight:400; font-size:42px; letter-spacing:.2em; }
```
In 0.5 s `power1.out`, hold, out 0.4 s; or, as in the measured city film (`styles/opening-credits.md`), cut the credit in and out with its shot. Place it in the darkest negative space of the shot. Over bright sky a credit failed contrast (1.9:1) until it moved to a darker area with the soft shadow; `hyperframes check` reports contrast.

## R3 Title card (trailer language)
Black frame, condensed caps (Bahnschrift or the free Barlow Condensed / Oswald): `font-weight:600; font-stretch:75%; letter-spacing:.04em; text-transform:uppercase; font-size:120px` at 1080p. In: `{opacity:0, y:12, filter:"blur(6px)"} → {opacity:1, y:0, filter:"blur(0px)"}`, 0.6 s `expo.out`. Out: hard cut on the next hit. 1–4 words.

## R4 Paper in light (documents as evidence)
Tight crop of the key line, not the full page. Two stacked copies: a blurred, darkened base and a sharp copy masked to the key line.
```css
.stage3d { position:absolute; inset:0; perspective:1600px; }
.paper { position:absolute; box-shadow: 0 50px 90px rgba(0,0,0,.55), 0 8px 18px rgba(0,0,0,.35); }
.paper .base  { filter: blur(3px) brightness(.62) sepia(.25); }
.paper .sharp { mask-image: linear-gradient(to bottom, transparent 39%, #000 42%, #000 61%, transparent 64%); filter: sepia(.18) contrast(1.04); }
.paper .tint  { position:absolute; inset:0; background:#f2eee6; mix-blend-mode:multiply; opacity:.9; }
.paper .tex   { position:absolute; inset:0; opacity:.35; mix-blend-mode:multiply; background-image:url("data:image/svg+xml;utf8,<svg ...feTurbulence...>"); }
```
Desk: `radial-gradient(ellipse 60% 55% at 50% 45%, #2a2622, #121110 70%, #0b0b0c)`. Move: `rotationX 12→8, rotationY -9→-6, rotationZ -1.2→-0.6, scale .98→1.06` over the whole shot, `ease:"none"`. Optional thin underline (`height:5px`, one muted accent) drawn `scaleX 0→1` in 0.5 s `power2.inOut`. Source line below in small wide-tracked caps (publication, date). Sharpen small screenshots before use: `ffmpeg -i in.png -vf "scale=iw*2:-1:flags=lanczos,unsharp=5:5:0.8" out.png`.

## R5 Light sweep + pull-back + lockup (Apple language)
```css
.sweep { position:absolute; inset:0; background: linear-gradient(105deg, rgba(255,255,255,0) 38%, rgba(255,240,220,.32) 50%, rgba(255,255,255,0) 62%); mix-blend-mode: screen; }
.lock .eb { font-weight:600; font-size:28px; letter-spacing:.007em; color:#a7a9ad; }
.lock .hd { font-weight:600; font-size:80px; line-height:1.05; letter-spacing:-.015em; }
```
Shot `scale 1.6→1` over 4 s `expo.out`; sweep `xPercent -120→120` over 1.6 s `power2.inOut`; lockup blur-in 0.8 s `expo.out`; hold ≥ 1 s before the end sound.

## R6 Letterbox + grain (top layer, full duration)
2.39:1 inside 1920×1080 = bars of 138 px top and bottom. Captions can sit in the bottom bar. Grain: SVG `feTurbulence` tile as background, `opacity:.13; mix-blend-mode:overlay`, element 2040×1200 at −60 px, moved `x 0→-48, y 0→-40` with `ease:"steps(160)"` over the film so it flickers like film.

## R7 Headline match-cut montage
Crop 8–12 headlines so the key word sits at the same screen spot; durations 8, 8, 6, 6, 5, 4, 4, 3, 3 frames (30 fps), a shutter/click on each, then a hard stop on the main headline (R4). Each is a short `<section data-start data-duration>` with an `<img>`.

## R8 Audio
- Music under voice 10–15 dB lower: a −11 LUFS track needs `volume ≈ 0.08–0.1` under a −21.5 LUFS voice. Use `data-automation` volume lanes for ducking, drop-outs and the end swell.
- Shorten a track's drop-out with ffmpeg (`atrim` pieces + `acrossfade=d=0.03`) so the silence lasts 0.5–2 s; rebuild a track's length by joining sections at bar lines.
- Reverse a whoosh for a suck-back: `ffmpeg -i whoosh.wav -af areverse,volume=4dB suck.wav`.
- Master: `loudnorm=I=-14:TP=-1.5:LRA=11`, AAC 192k, 48 kHz.

## R9 Poster as frame 0
Pick the strongest frame as `poster.jpg`, then bake it into frame 0 so every player shows it as the thumbnail:
`ffmpeg -i film.mp4 -i poster.jpg -filter_complex "[0:v][1:v]overlay=enable='eq(n,0)'" -c:a copy film_final.mp4`

## R10 Speed and proof labels (robotics / demos)
Small label top-right, mono or the body sans at ~2.5 % H, 60–70 % opacity: "Autonomous", "1x", "2X", "Teleoperated". It stays for the whole shot; changing speed without a label reads as a lie.

## Configure, don't hand-write
For films over ~20 shots, generate `index.html` from a config (a shot list array with type, source, start, duration, text, move) in a small Node script. Timing changes then mean editing one number and rebuilding, and the voice, caption and SFX times stay in one place.
