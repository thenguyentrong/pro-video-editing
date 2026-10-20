# Dyson's new PencilWash wet cleaner | our slimmest design  (Dyson, 2026-02-20, 0:43 film + 7 s end screen, 16:9, YouTube / social)
URL: https://www.youtube.com/watch?v=xWzhMDiEfpU
Purpose: product film / feature explainer (no voice, HUD labels instead)
One-sentence point: A very thin wet floor cleaner, explained part by part with x-ray CG and futuristic HUD callouts on a clean grey studio floor.

Structure:
- 0.0-5.8 hook: a coffee-like spill splashes onto the cleaner head (top, macro), the camera pulls back and up as the slim stick stands on a white floor (frames/t000.5s.jpg).
- 5.8-11.9 handle: macro of the copper handle with the power button; HUD callouts draw in: "ULTRA-SLIM HANDLE / 38MM DIAMETER / 380G IN HAND / ERGONOMIC / INTUITIVE STEERING" and "LED SCREEN" (t006.0s); the shell turns x-ray to show the internals (t009.5s).
- 11.9-24.8 head (12.9 s, the longest move): red/blue roller head moves into a spill (t012.0s), shell goes transparent, tanks are labelled ("DEDICATED CLEAN WATER / 300ML", "SEPARATE DIRTY WATER TANK") (t019.0s), then a macro of dirty water in the channel with "EASY-EMPTY DESIGN" and "AUTOMATIC DIRT EXTRACTION" (t023.0s).
- 24.8-28.8 top view of the head gliding forward on the floor.
- 28.8-39.1 low profile: the head slides under furniture ("LOW PROFILE"), flex neck, "LIGHTWEIGHT", "GLIDING MOTION" labels (t035.5s).
- 39.1-42.8 end: the product stands alone, small, centred on a white floor (t041.0s). No text card - the black YouTube end screen with the dyson wordmark follows (42.8-50).

Cut rhythm (0-42.8 s): 6 shots, ASL 7.13 s, median 5.94 s, quarters 5.35 / 5.35 / 3.57 / 5.35. Longest 12.9 s, shortest 3.7 s. 100 % of shots over 3 s. Changes happen INSIDE the shots (camera moves, x-ray fades, label build-ups) - roughly one new label or reveal every 2-3 s. Cuts on onset 40 % vs 26 % chance (the few cuts sit on music hits).

Typography: HUD callout system (all caps, white, wide tracking ~0.08 em, geometric/technical sans; free match: Eurostile-like "Michroma" for the headers or "Barlow Semi Condensed" Medium). Header cap height ~3 % of frame height with a small ring-dot bullet on the left; 1-4 sub-lines ~2 % high, each with a dot tick on a vertical bracket line; a thin 1-2 px white line runs from the bracket to a dot ON the product part. A blinking underscore cursor "_" types the lines on (visible in t006.0s and t019.0s). Labels sit in the free space left/right of the product, ~10-15 % from the frame edges.

Colour/grade: light grey/white studio (median frame luma 163, 33 % of frames brighter than 170), neutral (R-B +2), median saturation 5 % - the only colours are the product's copper handle, red and blue roller and the brown "dirty" liquid. Contrast p95-p5 156 (clean, crisp CG).

Camera/shots: 100 % CG, photoreal; long motion-control style paths: macro push along the handle, orbit around the head, x-ray fade of shells, very low floor-level skims, top-down glide. No people, no hands.

Transitions: 5 hard cuts. Everything else is camera movement and shell-to-glass dissolves (x-ray). Callouts draw in with lines + type-on, and leave by fading.

Sound: no voice (whisper found none). Electronic music bed; loudest hit at 1.05 s (-6.5 dBFS, +36 dB rise, the spill splash), then -14 to -18 LUFS-M with a dip at 5-8 s (-21 to -25) and a lift at 28 s (-10). Integrated -15.8 LUFS (social master, not broadcast). Music ends at 48 s under the end screen.

What makes it premium:
- The HUD callouts turn specs into a "technical drawing" - precise, small, never cover the product.
- X-ray CG shows the real internal layout (two tanks, rollers) = engineering proof.
- Very long, slow camera moves (6-13 s) on a clean set = calm confidence.
- No VO: the film works muted on social.

Recipe (real footage + HTML/GSAP):
1. Footage: slow slider/motion-control moves on a white/grey sweep, product macros; optional "x-ray" = second plate of the opened/disassembled product aligned to the same move, crossfaded 1 s.
2. Callout component (HTML/SVG): `<g>` with a 6 px ring dot at the anchor on the product, a 1.5 px white polyline (anchor -> elbow -> bracket), a vertical bracket line with tick dots, header text + sub-lines. GSAP timeline: ring `scale 0->1` 0.2 s, line `strokeDashoffset len->0` 0.5 s `power2.out`, header type-on 0.04 s per character with a blinking `_` cursor (`repeat:-1, yoyo:true, duration:.35`), sub-lines stagger 0.15 s. Hold 2-3 s, fade out 0.3 s.
3. Type: `font-family:'Michroma'` (or Barlow Semi Condensed 600), `text-transform:uppercase; letter-spacing:.08em`, header 3vh, sub-lines 1.9vh, colour #fff with `text-shadow:0 0 6px rgba(0,0,0,.25)` for legibility on light backgrounds.
4. Edit: 5-6 shots of 4-13 s; 2-4 callouts per shot; end on the product alone, small, centred, 3-4 s.
5. Music only, open with one strong SFX hit on the first action (spill/splash), -14 to -16 LUFS for social.
