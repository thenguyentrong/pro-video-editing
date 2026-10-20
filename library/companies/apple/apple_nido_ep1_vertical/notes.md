# Nido de Villanas: Ep. 1 Don Cristóbal's inheritance  (Apple, 2026-07-22, 1:44 file / 1:39.7 content, 9:16, YouTube Shorts)
URL: https://www.youtube.com/watch?v=wG_LaKvlcqM
Purpose: social reel — vertical "telenovela" series episode, Shot on iPhone 17 Pro (14 episodes on Apple's Shorts tab)
One-sentence point: A soap-opera funeral where every heir is a villain — a serialized vertical drama that proves iPhone can shoot a show.

## Structure
- 0-14.9 s **Cast intro**: four villainesses, one per shot (~3.9 s each), posed on black with a thorny-branch frame, name in yellow serif caps (GABRIELA SPANIC, MARIANA TORRES, ELA VELDEN, ITATÍ CANTORAL).
- 14.9-19.7 s **Title card**: drone over a cemetery; an art-nouveau yellow frame draws on; "CAPÍTULO 1 / NIDO de VILLANAS / SHOT ON iPHONE 17 PRO / ".
- 19.7-30.7 s **Funeral**: priest line "Death is but another journey…", triptych (3 stacked panels build one by one, 26-29 s: mourners, priest + portrait, two young men), "Amen."
- 30.7-61 s **Grave POV**: portrait → camera inside the grave looking up (32-34 s) → each heir throws a blue rose and says a nasty line (low-angle from the grave, 6-8 s shots).
- 61-91 s **The family**: handheld at grave level with the gold picture frame in foreground; a woman films a selfie at the grave with an orange iPhone; heirs walk away in a wide ("We will miss Dad very much").
- 91-99.7 s **Cliffhanger**: a mysterious figure watches; BTS — iPhone on a mount recording ("A true villain… keeps her distance… until the right moment").

## Cut rhythm
- 22 shots in 99.7 s → **ASL 4.53 s**, median 4.25 s; quarters 4.15 / 2.77 / 4.15 / 6.23.
- 0 % < 1 s, 73 % > 3 s; longest 11.9 s (walk-away wide, 79.6 s), 7.9 s (grave POV monologue).
- Slow for a vertical clip — paced like TV drama: one line of dialogue per shot.
- Cuts on onsets 14 % vs chance 26 % → cut to dialogue.

## Typography
- Cast names: 2 lines caps, flared high-contrast display serif (closest free: "Gloock" or "DM Serif Display" — guess), pale yellow ≈ #f2eb9a, cap ≈ 5 % of frame height, centred at y 60-69 %.
- Title card: ornamental art-nouveau frame (drawn-on lines, 15.0-15.5 s), "NIDO de VILLANAS" cap ≈ 7 % H with italic "de", small caps lines for "CAPÍTULO 1" and "SHOT ON iPHONE 17 PRO" + Apple logo, all in the same yellow.
- Burned-in subtitles: SF Pro semibold, pale yellow, 2 lines centred at y 69-73 %, cap ≈ 1.8 % of frame height, soft dark shadow. Legal small white (66-70 s): "Additional hardware and software used. Some audio was recorded in a studio."

## Colour / grade
- Telenovela-noir: deep greens (cemetery), teal-grey overcast sky, crushed blacks, warm skin; black wardrobe with blue roses and gold frame as accents; yellow typography as brand colour.
- Black studio backdrop for the cast cards.

## Camera / shots
Vertical portrait framing; posed cast portraits; drone; extreme low angle from inside the grave; handheld at ground level with foreground objects; selfie-in-scene with an iPhone; BTS phone-on-mount. Triptych split-screen (3 horizontal panels) for the ensemble.

## Transitions
Hard cuts; drawn-on frame for the title; panels building in one by one.

## Sound
- Dialogue-led (lines are subtitled in English; spoken language not verified — no captions downloaded), dramatic telenovela score.
- Integrated **−16.3 LUFS**; no drop-outs; hits at 35.5 s (grave reveal, −8.8 dBFS), 43.6 s, 49.6 s, 54.5 s (each rose throw / line), 98.6 s (cliffhanger).

## What makes it premium
- A real series format (cast cards, chapter title, cliffhanger) instead of an ad; the product only appears as a prop and in the title card.
- Strong, consistent art direction: one yellow, one serif, one ornamental frame.
- Memorable signature shot (POV from the grave) that sells the camera.

## Recipe (real footage + HTML/GSAP)
- 1080×1920. Cast cards: subject on black, name in a display serif, `font-size: 7vh` caps (cap ≈ 5 % H), `color:#f2eb9a`, centred at 62 %; 3.5-4 s per card; `gsap.from(name,{opacity:0,letterSpacing:"0.2em",duration:.8})`.
- Title frame: inline SVG ornament, animate `stroke-dashoffset` 0.5 s, then fade the title in.
- Subtitles: Inter 600, `font-size: 2.5vh`, `#f3eea0`, `text-shadow: 0 1px 3px rgba(0,0,0,.6)`, centred at y 71 %, max 2 lines, 2-3 s each.
- Triptych: three 1080×640 panels stacked, reveal with `stagger: 1.4` (s).
- Grade: `saturate(.9) contrast(1.15) brightness(.92)` + green-teal overlay 12 %.
