# UEFA Champions League 2024/25 – broadcast intro / opening titles  (UEFA, aired from 2024/25 season, 43.9 s, 16:9, fan upload of the broadcast feed on YouTube)
URL: https://www.youtube.com/watch?v=HiZHwiW3zcA
Source honesty: uploaded 2024-08-19 by a fan channel ("No UEFA presents"), description "(c) UEFA 2024 – Full, upscaled to 4K". Not an official UEFA upload; the content is UEFA's intro, the file is 30 fps (likely converted). The last 5 s (38.5–43.9) are a silent logo hold that may be the uploader's tail.
Purpose: broadcast opening titles (played before match coverage), first season of the 2024 rebrand (new league format)
One-sentence point: the starball becomes a place (a stadium shaped like the starball), and one iridescent light-line motif carries you from that CG world into real football and back to the logo.

Structure:
- 0.0–5.0 HOOK: extreme close-up of CG starball facets (royal-blue panels, thin iridescent edges cyan → green → yellow → magenta) slowly rotating.
- 5.0–5.9 TRANSITION: a facet edge sweeps across the frame as a wipe line and reveals the next shot.
- 5.6–12.0 WORLD: a fictional night stadium by the water whose roof is shaped like starball star points; slow push and orbit.
- 12.0–16.9 ENTRY: camera rises over the roof rim into a CG bowl full of crowd (12–14.9), then the CG pitch with a starball centre-circle banner and the first light ribbons entering bottom-left (15–16.9).
- 16.9–29.8 BUILD: real match action: 12 shots, 0.53–1.9 s each (dribbles, shots, saves, goal net). Iridescent light ribbons are drawn on the grass around the players' feet (22.5 s) and trail the ball.
- 29.8–32.0 PAYOFF: Real Madrid trophy lift under the "WINNERS – UEFA CHAMPIONS LEAGUE FINAL 2024" arch, light rays behind (loudest moment, 30.5 s).
- 32.0–35.0 RETURN: top-down CG aerial of the starball stadium (the roof reads as the starball), slow pull-out, fade through dark navy.
- 35.0–43.8 LOGO: starball + UEFA badge + CHAMPIONS LEAGUE wordmark centred on deep navy; bundles of 5–6 parallel rounded neon lines sweep in from the corners. Music ends at 38.5 s.

Cut rhythm: 20 shots in 43.8 s, ASL 2.19 s, median 1.79 s. ASL per quarter 2.19 / 1.37 / 1.22 / 10.95 s: slow CG opening → fast real action → one long logo hold (11.8 s). 25 % of shots are under 1 s, all inside 17–30 s. Cuts per 10 s: 3, 6, 9, 1, 0. Cuts do not sit on audio onsets (11 % vs 17 % chance). Verified by eye: the facet wipe at 5.6 s and a missed cut at 27.75 s were added; 0.4 s and 1.5 s are motion inside one CG shot.

Typography: no credits, no supers. Only two type moments:
- In-footage: "WINNERS / UEFA CHAMPIONS LEAGUE FINAL 2024" arch (white wide bold caps on blue).
- End card lockup, centred, white: starball 15 % of frame height, UEFA badge 5 %, "CHAMPIONS" and "LEAGUE" each 3.5 % (cap height), whole lockup 31 % of frame height (34–65 % y). Wordmark = UEFA's custom bold flared caps; no good free match (closest feel: Montserrat ExtraBold with wider tracking); use the official logo file. Logo fades in over ~1 s (34.7–35.6 s).

Colour/grade: deep navy base (~#101030, end-card background measured #000035), royal blue facets (~#1010b0 → #1048d0), accents only in the light lines: cyan (~#48d8d8), magenta (~#d848d8), blue (~#1878d8), a little yellow-green. Real footage keeps natural colour; the pitch green looks pushed (saturated). The celebration shot at ~29.5 s has a blue-magenta background (graded or lit; can't tell). 21 % of frames are "mostly empty" (the navy end card).

Camera/shots: CG fly-throughs (orbit, crane over the roof edge, top-down aerial) for 16 s; real broadcast footage (tight tele shots, reverse-angle goal-net shots, celebration close-ups) for 13 s; logo 9 s.

Transitions: 1 graphic wipe made from the brand shape (facet edge, ~0.9 s); hard cuts in the action; the light ribbons appear on the CG pitch first and then on the real grass, so the motif bridges CG and live action; fade through dark navy into the logo (33.4–35.0 s).

Sound: probably an arrangement of the UCL anthem / new brand music (guess; I did not listen). Measured: opening −19 LUFS momentary, a dip to −31 at 10.5 s just before the camera enters the bowl, back up at 12 s; a second dip (−27/−28) at 18–21 s; loudest −17.3 at 30.5 s on the trophy lift; ends at 38.5 s. Integrated −23.2 LUFS, LRA 8.3 LU, true peak −7.8 dBFS. No voice.

What makes it premium:
- The logo is turned into architecture: the starball is a stadium, so the brand is a world, not a sticker.
- One motif (iridescent light lines) travels through every section: facet edges → ribbons on CG grass → ribbons on real grass → neon bundles around the end logo.
- Hard colour discipline: navy + royal blue; all colour accents only in thin lines.
- Real football is short (13 s) and fast; CG is slow; the contrast makes both feel bigger.
- Long, calm logo hold (≈9 s) with the lockup at only 31 % of frame height.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Sections: 0–5 s brand-shape macro (SVG of your mark, scaled 600 %, slow rotate 8° over 5 s); 5–6 s wipe with the shape's own edge; 6–16 s "brand world" (real footage of a building/venue graded navy, or a still with a slow 1.0 → 1.15 push); 17–30 s real action, shots 0.6–1.8 s, cut faster toward the end; 30–32 s one hero moment held 2.2 s; 32–35 s pull-out + fade through #000035; 35–44 s logo hold.
- Light lines: 5–6 parallel SVG paths with rounded corners, stroke 3 px on 1080p, gap 9 px, stroke = linearGradient #48d8d8 → #1878d8 → #d848d8, `filter: drop-shadow(0 0 6px currentColor)`; animate with stroke-dasharray/dashoffset draw-on, 0.8 s, ease "power2.inOut", staggered 0.06 s; over footage, place them on the ground plane (skew/perspective transform) so they read as painted on the grass.
- Wipe: an SVG polygon edge (the brand shape) translated across the frame in 0.9 s, ease "power3.inOut", used as a clip-path between shot A and B, with a 2 px iridescent stroke on the edge.
- Logo: centre, lockup 31 % of frame height, fade + scale 0.96 → 1.0 over 1.0 s, ease "power2.out"; line bundles enter from two opposite corners 0.3 s later.
- Grade: navy blacks (#101030), push greens +10 % saturation on action shots; keep accent colours only in the lines.
- Audio: orchestral/choral cue, one dip before entering the "world", loudest on the hero moment, cut music before the logo hold ends.
