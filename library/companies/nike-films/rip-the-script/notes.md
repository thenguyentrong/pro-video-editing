# Rip The Script  (Nike Football, 2026-06-04, 6:00, 16:9 with 2.39:1 letterbox in the "ad" scenes, YouTube @nikefootball)
URL: https://www.youtube.com/watch?v=IyZ1WIua_1s
Purpose: long-form ad / comedy short film (World Cup 2026 campaign)
One-sentence point: The players refuse to follow the director's script - football is better unscripted.

## Structure (cut list + English captions)
- 0.0-17 fake ad: a glossy stadium "commercial" in 2.39:1 letterbox - smoke, flares, Mbappe dribbling, slow-motion ball into the net (13-15 s). Director yells "No!" (17.7 s).
- 18-60 reveal + setup: hard cut to the real set (no letterbox, handheld, test-pattern backdrop, green-screen pitch, crew). Director: "No improv, no theatrics. Just head the ball." Players walk off ("What are you doing? Where are you going?").
- 60-130 chase: players escape through the studio lot - handheld chase shots, CCTV/security-camera views with "NORTH" label and time code (71 s, 76 s, 130 s), corridors, a western set, a fan meet (Lisa signing at 122 s).
- 132-146 TV-studio parody: a football talk show desk; players run through the background.
- 146-160 B&W flashback "Croydon 1995" (small serif caption, pillarboxed 4:3, fishing boat, seagulls) - a joke cutaway.
- 160-235 escalation: more chases, Haaland + lookalike, CCTV with a tracking box around a player (193 s), then one 17.3 s locked-off wide shot of an office meeting ("The GOATs' Goodbye" script, 194.7-212 s) - a comedy hold.
- 236-259 action-movie parody: explosions, a silhouette walking out of fire with a ball (253-257 s), "NO LINK" monitor glitch (259.8 s, 0.9 s black).
- 260-300 music-video parody: rapper in an ice cave, scribbled handwritten titles "ICEMAN FREESTYLE", "COLD VILLAIN" (261 s, 264 s).
- 300.4-302.7: 2.3 s black.
- 302.7-355 payoff: "Roll the film. And go." - the real unscripted match on the studio pitch, back in 2.39:1, celebrities in the crowd (331-335 s), young player scores.
- 355-360 end card: "RIP THE SCRIPT" + swoosh emblem.

## Cut rhythm
- 286 shots in 360 s. ASL 1.26 s, median 0.96 s. ASL per quarter 1.04 / 1.23 / 1.45 / 1.34 s.
- Longest 17.31 s (194.74, office meeting), 6.17 s (0.88, opening), 5.92 s, 5.84 s. Shortest 0.21-0.25 s (flash frames in the opening and in the chases).
- 50 % under 1 s, 5 % over 3 s. Densest 10-20 s (13 cuts); quietest 200-210 s (0 cuts, the static comedy hold).
- Cuts on dialogue and gags, not on music (24 % on onset vs 23 % chance).

## Typography
- In-story labels only: CCTV overlay ("NORTH", time code, small mono, top corners), "Croydon 1995" (small serif, bottom centre, ~2 % height), handwritten scribble titles in the music-video part.
- End card: heavy wide grotesque display caps (closest free: Dela Gothic One or Archivo Black Expanded), white on black. "RIP" ~25 % frame height, small "THE" tucked right of the P (~6 %), "SCRIPT" ~45 % height; block spans x 12-89 %.
- Texture: LED/scanline pattern inside the letters, a diagonal paper-tear crack across the card with RGB-split edges. Holds ~2 s, cut to a fast close-up, then the swoosh+ball emblem on black with the same crack.

## Colour/grade
- Two grades on purpose: (1) "the ad" = teal/orange, smoke, flares, deep blacks, 2.39:1 bars (~12.5 % top and bottom); (2) "real life" = flat, neutral, daylight-white studio light, full 16:9.
- Each parody has its own look: CCTV (desaturated, high angle, wide), TV studio (blue/LED), flashback (B&W, 4:3, grain), action (orange fire), music video (cyan ice).

## Camera/shots
- Handheld documentary camera in the BTS scenes, long lenses for reactions; wide-angle locked-off for the office gag.
- Slow motion for hero ball moments (13-15 s, 320 s ball under the lights).
- Many "found" formats: CCTV, monitor feed, TV broadcast.

## Transitions
- Hard cuts, plus format switches as the transition (letterbox on/off is itself the "cut" between fiction and reality). Black holds at 259.8 s (0.88 s) and 300.4 s (2.34 s).

## Sound
- Dialogue-driven comedy, music only in the action, music-video and final-match parts. Integrated -24.2 LUFS (broadcast-level, quiet).
- Drop-outs before gags: 21.3 s (0.7 s), 82.55 s (0.95 s silence -> "Stop!"), 174.7 s (0.6 s).
- Loudest at 262.5 s (freestyle track). Biggest rise 302.8 s (+34.7 dB) - the match kicks off after the 2.3 s black.

## What makes it premium
- Real stars + real comedy acting; the film laughs at the polished-ad style while also delivering it.
- Clear "fiction vs. reality" code: letterbox = scripted, no letterbox = real.
- Big set-piece variety (8 parody formats) inside one story.
- Long comedy holds (17 s) next to 0.25 s action cuts.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Use letterbox as meaning: `.bars { position:absolute; left:0; right:0; height:12.5%; background:#000 }`, top and bottom. Animate them in/out with a hard `gsap.set` at the cut between "staged" and "real" footage (for a startup: polished render/ad vs. raw site footage).
- CCTV overlay layer: `font-family: 'JetBrains Mono'; font-size: 1.6vh; color:#fff; opacity:.85`, top-left label + top-right running clock (update `textContent` from the timeline time), add a 1 px white tracking box around the subject with `gsap.to(box, {x, y})` keyframes.
- End card: `font-family: 'Archivo Black'; transform: scaleX(1.25)`; white; "RIP" 25vh, "SCRIPT" 45vh; scanline overlay `repeating-linear-gradient(0deg, rgba(0,0,0,.35) 0 2px, transparent 2px 4px)`; a crack SVG path drawn with `stroke-dashoffset` in 0.2 s, plus 2 px red/cyan offset copies for RGB split.
- Pacing: 2.3 s black before the final act, then a loud hit.
