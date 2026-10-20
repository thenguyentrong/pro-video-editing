# New Raycast. Coming 2026  (Raycast, 2025-12-18, 38.6 s, 16:9, YouTube / social)
URL: https://www.youtube.com/watch?v=Mi173xGb0ZA
Purpose: teaser (announces a rebuilt version of the app months before release)
One-sentence point: Every part of the launcher has been rebuilt, and it is coming in 2026.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-3.7 (0-10 %) hook: fade up from black; a huge macro of the empty search bar with a blinking cursor, sliding in over dark chrome folds.
- 3.7-28.3 (10-73 %) feature tour, all rendered UI, one feature per set-up: typing a query, action menu and hotkey, clipboard history, emoji grid (one emoji glows when selected), dictation (a mic tile shrinks into a waveform pill), AI chat presets, an agent running steps, "checking for updates" spinner.
- 28.3-33.4 (73-87 %) the list: a black card with "NEW" in a fixed left column and the feature name in a right column, swapping every 0.25-0.5 s (about 10 names).
- 33.4-36.7 (87-95 %) "NEW RAYCAST", then "COMING 2026" added below.
- 36.7-38.6 (95-100 %) the small logo mark alone on black.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 12 shots (scene detector found 5 cuts; the adaptive detector's 4 extra set-up changes were confirmed by eye on a 4 fps strip, plus 2 more added at 11.1 and 36.7). Inside each set-up the camera keeps moving and the UI animates; those changes are not counted.
- ASL 3.21 s, median 2.22 s, 0 % under 1 s, 33 % over 3 s. Quarters 2.41 / 3.21 / 1.61 / 4.82 s.
- Shortest set-ups 1.7-2.0 s (agent steps, logo); longest: the text-card block 8.4 s, emoji + dictation 6.2 s.
- The text cards carry the fast rhythm instead of the picture: ≈10 word swaps in 5 s.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- End cards: monospaced caps, white on pure black. Closest free: JetBrains Mono 400 or IBM Plex Mono 400. Cap ≈2.9 % H. Two fixed columns on the centre line: "NEW" at x ≈32-36 %, the feature name left-aligned at x ≈51 %. 1-3 words per card, swap every 0.25-0.5 s by hard replace; the two words then join in the centre ("NEW RAYCAST"), second line added below.
- The UI type is the product's own (system sans, closest free: Inter), shown very large: the search field text is ≈9 % H in the opening macro.
- No headline over the UI, no captions.

Colour/grade: palette, contrast, grain, letterbox
- Monochrome: black and graphite (#020202-#2b2b2b) with soft grey chrome highlights (#878685). Colour appears only inside the UI: emoji, the red/blue swatches in the clipboard (#ff6363 is the brand red, #56c2ff), a gold glow on a selected emoji tile (#6c5938).
- No grain, no letterbox.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Rendered UI only: crisp UI panels composited in 3D space over a dark, softly lit wave/fold background; continuous slow dolly, push-ins and lateral slides, shallow depth of field on the panel edges, tilted angles (10-20°).
- No people, no hardware, no desktop around the UI.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts between set-ups, each landing on a music accent (cuts on onsets 27 % vs 7 % chance).
- One morph: the selected mic tile shrinks and becomes the dictation pill (16.7-17.5 s).
- Fade up from black at the start; the text block is a hard cut from the last UI shot.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Music only, no voice (speech detector found none). UI ticks and whooshes on the moves.
- Biggest rise +25.5 dB at 3.6 s (first cut). Loudest 0.5 s at 28.1 s, right on the cut into the text list. No drop-outs; 0.3 s silence at the end.
- Integrated −13.2 LUFS, wide range (LRA 13.5 LU) from a quiet open to a loud list, true peak +0.4 dBTP.

What makes it premium (3-5 bullets)
- The UI is treated like a product shot: huge, tilted, lit, on a material background instead of a desktop.
- One feature per set-up, 2-3 s each, cut on the beat.
- A monospaced "NEW ___" list says "everything changed" in 5 seconds without a single sentence.
- Monochrome world; the only colour is in the product.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920x1080, 38 s, 120-ish bpm bed. Background: looped dark abstract fold footage or a CSS layer `radial-gradient(ellipse at 70% 30%, #4a4a4a 0%, #0d0d0d 45%, #000 80%)` with a slow `backgroundPosition` drift.
- Each UI set-up: an HTML panel (`#1c1c1c`, `border-radius 16px`, `1px solid rgba(255,255,255,.08)`) inside a 3D stage: `perspective: 1400px; transform: rotateY(-14deg) rotateX(6deg) scale(1.8)`; tween `x -6% → +4%` and `scale 1.8 → 1.95` over the shot, `ease: none`. Edge blur with a mask layer `filter: blur(6px)` on a copy outside the focus band.
- Shot lengths 2.0-3.3 s, 8-9 set-ups, cut on the downbeat; one morph (`width`, `height`, `borderRadius` tween 0.6 s `power3.inOut`).
- List cards: `400 32px "JetBrains Mono"` caps, white on #000; "NEW" fixed at left 33 %, feature name at left 51 %, swap text with `tl.call` every 0.3-0.5 s; then tween both to the centre (0.4 s `power2.out`), add a second line 1 s later; logo mark 1.9 s; fade audio 0.3 s.
