# Introducing the Titan Print System  (ICON, 2026-05-14, 1:30, 16:9, YouTube, official ICON channel)
URL: https://www.youtube.com/watch?v=Ebir6dl_cxc
Purpose: product launch film (spec reveal of a new construction 3D-printing system)
One-sentence point: Titan is a truck-delivered, multi-story concrete printing system that sets up in an hour, prints 27 ft high and builds walls for about $20 per square foot.

Real vs CGI: almost certainly a full 3D render (clean surfaces, perfect light, impossible macro camera paths through the gravel/nozzle, a hologram worker). Not labelled as render. No speech (no auto captions exist), music + sound design only.

## Structure (89.8 s)
- 0.0-4.0 (0-4 %) title: ICON logo + "TITAN" + mono subtitle "MK1 / T27 MULTI-STORY CONSTRUCTION SYSTEM" over a soft-focus truck; four mono corner labels (READY TO BUILD / WORLD CLASS DESIGN / 3D PRINTING TECHNOLOGY / ROBOTIC CONSTRUCTION).
- 4.0-8.3 (4-9 %) world + start: desert aerial, then a START/STOP power button lights up cyan (first sound hit 7.25 s).
- 8.3-28.4 (9-32 %) deploy: top-down truck with HUD card "1 HOUR" (setup), arm unfolds, outriggers, card "10' CLEARANCE", side view with card "27' MAX PRINT HEIGHT" plus dimension HUD (MAX LENGTH 100', MAX WIDTH 40', MARGIN 10').
- 28.4-34.7 (32-39 %) software: hologram-style worker holding a tablet, floating web UI choosing house models (Alphabeta, House Zero; bed/bath/floors/sq ft row), then a white wireframe of the house on black.
- 34.7-49.7 (39-55 %) material story: abstract particle macro on black (aggregates float, gravel pile, tunnel through mix), then the nozzle starts the first bead; loudest moment 36.1 s.
- 49.7-77.6 (55-86 %) printing: chrome nozzle macro with sky reflection, walls rising, card "PRINTED-IN REINFORCEMENT", batch-truck card "ON DEMAND", top-down nozzle push, bead macro, card "$20 PER SQ FT" with fine print "40 % less than the national average".
- 77.6-83.3 (86-93 %) payoff wide: whole house footprint printed, card "7 DAYS".
- 83.3-89.8 (93-100 %) ICON logo white on black, fades out; 1.15 s silence at the end.

## Cut rhythm (after adding 6 cuts verified by eye: 37.71, 39.42, 43.75, 46.9, 47.35, 66.17)
- 26 shots, ASL 3.45 s, median 3.35 s, 7.7 % under 1 s. ASL per quarter 3.21 / 2.49 / 2.81 / 4.49 s.
- Longest: logo 6.46 s, house UI 6.33 s, top-down truck 6.04 s. Shortest 0.45 s and 0.79 s inside the nozzle macro run (43-48 s).
- Calm, even pulse (1-5 cuts per 10 s). Each spec card owns one shot of 3-6 s; the camera moves slowly inside the shot.

## Typography
- Title "TITAN": neo-grotesk (Neue Haas / Inter look) 500, caps, cap height ≈10.6 % H, centred; logo above ≈3 %; subtitle monospaced caps ≈2 % (IBM Plex Mono / Space Mono), 2 lines.
- HUD / spec card system (the signature): frosted translucent rectangle (white ≈25 %, background blur) at x ≈14-36 %, y ≈24-43 %; small outlined tag ("MAX HEIGHT", mono caps ≈1.4 %); value in light grotesk caps ≈3.8 % cap height, 2 lines ("27'MAX / PRINT HEIGHT"); description in mono caps ≈1.5 %, 2 lines. Dotted crosshair guides cross the whole frame (vertical at ≈12 % and ≈88 % x, horizontal at ≈45 % y) with small mono labels at the corners (MAX HEIGHT: 27', MAX WIDTH: 40'...).
- Cards appear with a short type-on of the tag and a fade/slide of the panel (≈0.3-0.5 s), hold 3-5 s, then leave with the cut.
- Closest free fonts: Inter (value), IBM Plex Mono (tags, corners).

## Colour/grade
- Cool, desaturated grey-beige world (concrete, desert, white machine); one cyan accent (power button glow). Clean high-key daylight for site shots; black void for the material macro section. No grain, no letterbox.

## Camera/shots
- Slow CGI camera moves: top-down truck, low-angle orbit of the arm, macro slider along the nozzle, chrome reflection close-ups, final high wide. Scale is shown by HUD dimension lines, not by people.
- One stylised person only (a line-shaded hologram worker with tablet). No real site, no crew, no PPE.

## Transitions
- Hard cuts throughout; the material section moves "through" particles (cut-on-motion). Fade from logo to black at the end.

## Sound
- Music + sound design, no voice. Integrated -15.4 LUFS, LRA 13.6 LU (wide: quiet intro, loud material section). True peak +0.7 dBTP (clips).
- Hits: power button 7.25 s (+20.8 dB), material section 36.1 s (+18.2 dB, loudest). No drop-outs inside the film; 1.15 s silence after the logo.
- Cut-to-onset sync 5 % (chance 7 %): cuts are not on beats, they follow the camera.

## What makes it premium
- One graphic system for every number (frosted card + mono tag + dotted HUD guides) = "engineering drawing" feel.
- Exactly one spec per shot: 1 HOUR, 10' CLEARANCE, 27' MAX PRINT HEIGHT, PRINTED-IN REINFORCEMENT, ON DEMAND, $20 PER SQ FT, 7 DAYS.
- Restraint: no voice, no people, grey palette, slow moves, long logo.
- Weak spot for credibility: nothing is real; a startup copying this must label renders or pair them with a real site film.

## Recipe (HTML/GSAP, Hyperframes)
- Background: real or rendered shot, `filter: saturate(.6) contrast(1.05)`.
- HUD guides: `<div class="guide v" style="left:12vw">` with `border-left:1px dashed rgba(255,255,255,.6)`; corner labels `font:400 1.5vh 'IBM Plex Mono'; text-transform:uppercase; letter-spacing:.06em`.
- Spec card: `.card{position:absolute;left:14vw;top:24vh;width:22vw;padding:1.6vh 1vw;background:rgba(255,255,255,.22);backdrop-filter:blur(10px)}`; tag `border:1px solid #fff; font:400 1.4vh 'IBM Plex Mono'; padding:.3vh .5vw`; value `font:300 5vh/1 Inter; text-transform:uppercase`; desc mono 1.5vh.
- In: `tl.from(card,{autoAlpha:0,x:-20,duration:.4,ease:'power2.out'})`, tag typewriter 0.03 s/char; hold 3-5 s; leave on the cut.
- Title: logo 3vh, "TITAN" Inter 500 14vh, mono subtitle 2vh, over a blurred hero (`filter: blur(6px)`) for 4 s.
- End: logo 8vh white on black 6 s, fade out last 2 s.
