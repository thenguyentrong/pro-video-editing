# Introducing Meta VR Glasses | Spring 2027  (Meta VR, 23 Sep 2026, 1:26, 16:9, YouTube @metavr)
URL: https://www.youtube.com/watch?v=xyD_bmMy5nQ
Purpose: announcement film (product reveal before launch)
One-sentence point: light VR glasses for everyday places - one man watches a giant screen on his sofa, works in a cafe, watches basketball at the airport and a film on a plane, while the product is shown in warm, dark macros.

## Structure (cut times from metrics.json)
- 0-20.6 s (24 %) product tease: black, a warm light line grows along the frame edge (0-6.4 s, one shot), fabric strap macro, a lens catching rainbow light (8.1-11.8 s), then one 8.8 s front shot of the glasses rising in warm light; "INTRODUCING / Meta VR Glasses" fades in on it (15-20 s).
- 20.6-35 s (17 %) use 1, sofa cinema: glasses on a coffee table, a hand picks them up, the man puts them on; the wall of his loft becomes a curved cinema screen (film clip composited into the room), close-ups of his face.
- 35-43 s: product details (hinge macro, the battery puck on a cable), a virtual keyboard projected on a wooden table.
- 43-50 s use 2, cafe: browser windows float in the cafe; an extreme close-up of his eye with the app grid reflected in the iris, "LOOK TO NAVIGATE".
- 50-63 s use 3, travel: airport gate; the players of a basketball game appear life-size on the airport floor ("IMMERSIVE SPORTS").
- 63-72.6 s use 4, sound + plane: speaker macro with sound waves ("Dolby Atmos"), dark plane cabin, the film plays on a huge screen in front of the seats ("IMAX ENHANCED").
- 72.6-86 s (16 %) end: puck and glasses macros, the glasses rise, "Meta VR Glasses" above them (80-82.5 s); "SEE HOW IT FEELS / SPRING 2027" on a warm brown gradient (83-86 s, one 13.5 s shot with the product end).

## Cut rhythm
- 27 shots in 86.1 s, ASL 3.19 s, median 2.46 s, 0 % < 1 s, 30 % > 3 s, 19 shots/min.
- ASL per quarter 4.30 / 2.39 / 1.96 / 4.30 s: slow product open, faster uses, slow product close (a symmetric "bookend" curve).
- Cuts per 10 s: 2 / 1 / 3 / 5 / 5 / 4 / 4 / 2 / 0. Shortest shot 1.2 s - no fast cuts at all.
- Longest: end 13.5 s (72.6 s), glasses front 8.8 s (11.8 s), light-line opener 6.4 s.
- The adaptive detector found 17 cuts, the scene detector 26; the extra ones are real cuts in dark footage (checked on the cut sheet).
- Cuts on music onsets 31 % vs 26 % chance.

## Typography
- Meta's own sans (Optimistic, proprietary). Closest free: **Inter** or **Figtree**.
- Name card: "INTRODUCING" small caps, cap ≈1.9 % H, tracking ≈ +0.25 em, above the logo lockup "∞ Meta VR Glasses" (cap ≈3.4 % H), white, centred at 12-18 % H above the product. Fade in 0.8-1 s, held ≈5 s.
- Feature labels: tracked caps (≈ +0.15 em), cap ≈2.1 % H, white, placed beside the subject (right of the eye, top centre over the court): "LOOK TO NAVIGATE", "IMMERSIVE SPORTS", partner logos (Dolby Atmos, IMAX ENHANCED) at the same size. Held 2-4 s, simple fade.
- End card: "SEE HOW IT FEELS" cap ≈4.6 % H, tracking ≈ +0.12 em, warm white; "SPRING 2027" cap ≈2.7 % H, grey-beige; centred at ≈47 % H.
- Legal micro-text on content shots (≈1.2 % H).

## Colour / grade
- One colour world: warm bronze-brown light on black (gradient ≈#6B5440 → #1A140F), dark product, mean luma 0.18 - the darkest film in this set.
- Lifestyle in the same warm low-key: amber lofts, tungsten cafe, a dim plane cabin; the virtual screens are the brightest things in each scene.
- Soft contrast, filmic; no grain, no letterbox.

## Camera / shots
- ≈40 % product macros (slow slides, rises, rim light), ≈45 % one actor using the product in real places, ≈15 % composited "what he sees" (screens in the room, players on the floor, the iris reflection).
- The POV world is shown from behind or beside the wearer, life-size in the real room, never as a separate UI screen.
- Slow dolly and push-ins only.

## Transitions
- Hard cuts and slow fades; light sweeps over the product act as soft wipes. No flashes, no whips.

## Sound
- Music only (speech detection found no clear spoken lines; a short voice command may be in the mix, not verified). Slow electronic score that builds into the uses section.
- Integrated −16.7 LUFS, LRA 6.8 LU, true peak −0.2 dBTP. No drop-outs; hits +16-23 dB clustered 31-40 s (the cinema scene; biggest +23.1 dB at 39.9 s) and 55-57 s (sports). 1.25 s silence at the end.

## What makes it premium
- Apple-like restraint (dark warm macros, tiny tracked type) married to a people-first story: four everyday places, one person.
- The "magic" is composited life-size into the real room, so the viewer sees what he feels.
- A symmetric pace: slow product, calm uses, slow product.
- One warm colour world from the first frame to the end card.

## Recipe (real footage + HTML/GSAP)
- Shoot (or source) one actor in 3-4 everyday places in warm low-key light ("man sofa loft evening warm light", "cafe laptop tungsten", "airport gate waiting traveller", "airplane cabin night passenger").
- Composite the virtual content: a curved screen = the clip inside a div with `border-radius: 2% / 6%; transform: perspective(1400px) rotateY(0deg)`, `box-shadow: 0 0 120px rgba(255,200,150,.25)`, drawn behind the actor's shoulder mask.
- Product: macros on black with one warm rim light; light-line opener = a 2 px gradient line `scaleX 0 → 1` over 5 s.
- Type: `INTRODUCING` `font:500 1.9vh Inter; letter-spacing:.25em` + name `font:500 3.4vh Inter`; labels `font:500 2.1vh Inter; letter-spacing:.15em; text-transform:uppercase`; fade 0.8 s, hold 2-5 s.
- End card: `background: radial-gradient(circle at 50% 40%, #6B5440, #1A140F)`; line 1 `4.6vh`, line 2 `2.7vh #B8A894`.
- Pace: ASL ≈3 s, no shot under 1.2 s; 4 s product shots at the start and end.
- Mix: music only at ≈ −16.5 LUFS, hits on the reveal of each virtual screen.
