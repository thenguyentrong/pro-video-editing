# iiQKA.AI Vision: AI-powered industrial image processing for robotics  (KUKA Group, 2026-10-08, 1:27, 16:9, YouTube @KUKARobotGroup)
URL: https://www.youtube.com/watch?v=pPomgMBx9Jw
Purpose: product launch film for software (vision platform), 100 % CGI, music only
One-sentence point: iiQKA.AI Vision brings 2D/3D image processing straight into KUKA's robot controller, set up by drag and drop.

## Structure
- 0-1 dark studio fade-in; 1-5.9 orange KR robot on a small controller, label "Native AI" (top centre, small).
- 5.9-9.7 two fast inserts (0.92 s each): sparks and light trails flying around the arm (energy beat).
- 9.7-26 one 16.2 s camera move: light trails wrap the robot ("Integrated Control"), a camera beam scans parts ("Connected Workflow"), a floating UI window shows shapes being recognised ("2D und 3D Algorithm Platform", German/English mix on screen).
- 26-35.7 real software UI on a white split panel next to the robot ("Fully integrated in iiQWorks"), then UI cards float next to the robot ("Drag and Drop").
- 35.7-58.7 feature beats: camera head with light beams ("Fast Engineering"), collision ring on the floor ("Collision Detection"), floating setup cards ("Simplified Setup"), controller box hero ("Real Applications"), application vignettes "Pick and Place", "Bin Picking", "Depalletizing".
- 58.7-63.1 title on dark: "KUKA / iiQKA.AI Vision", ≈5 % H, centred.
- 63.1-66.9 robot + KUKA wordmark, then white logo card "making automation easier.".
- 66.9-86.9 20 s KUKA brand ident (particles).

## Cut rhythm
- 13 shots in 86.9 s, ASL 6.68 s, median 5.72 s, 15 % < 1 s, 77 % > 3 s, 9.0 shots/min. ASL per quarter 4.3 / 4.3 / 5.4 / 10.9 s (the last quarter is the ident).
- Longest 20.0 s (ident), 16.2 s (9.7 s, one continuous move through four features), 10.4 s. Shortest 0.92 s (two spark inserts).
- 0-4 cuts per 10 s. Most feature changes happen inside long virtual camera moves, so the film feels like one flowing take with three accents.

## Typography
- Feature labels: humanist sans (closest free: Source Sans 3), regular, title case, white ≈4.5 % H (cap ≈3 %), placed in empty space left of the robot or top centre; fade in 0.3 s, hold 3-5 s, fade out.
- Floating UI cards: real iiQKA UI elements as 3D planes in the scene (light grey cards ≈8 % H with an icon, a label and a play arrow).
- Product title: "KUKA" orange caps ≈3 % over "iiQKA.AI Vision" white ≈3 %, centred on dark.

## Colour/grade
- Dark charcoal studio with a soft floor gradient, KUKA orange robot as the only colour; white/orange light trails and sparks. Second half moves to a light grey studio.

## Camera/shots
- 100 % CGI. Slow orbits and push-ins around one robot, macro of the camera head, overhead of an application cell. Real software UI composited as screen planes.

## Transitions
- Mostly hidden in camera moves; light trails and sparks wipe through frame between features; fade to the white logo card.

## Sound
- Music only, no VO (speech detector finds only the two-word tagline at the logo). Integrated -21.9 LUFS (quiet), LRA 9.6 LU, peak -4.7 dBTP. 1.5 s silence at 65.75 s between film and ident. Rises +15-16 dB at 19.3, 23.2, 27.0, 34.7 s on feature changes. Cuts are not placed on audio onsets (0 % vs 15 % chance).

## What makes it premium / credible
- One hero object, one colour, dark studio: reads like a premium product film for software.
- The real UI appears, both as a flat screen recording and as cards in 3D space.
- Weak as proof: no real cell, no numbers, no speed of the vision step.

## Recipe (HTML/GSAP)
- Dark stage: `background:radial-gradient(ellipse at 50% 85%, #6b6b6b 0%, #2b2b2b 45%, #1c1c1c 100%)`.
- Feature label: `font:400 4.5vh 'Source Sans 3'; color:#fff; left:12vw; top:72vh`; `gsap.fromTo(l,{autoAlpha:0,y:8},{autoAlpha:1,y:0,duration:.4})`, hold 3-5 s.
- UI card in space: a screenshot of your real UI on a `div` with `transform:perspective(900px) rotateY(-18deg)`, `box-shadow:0 20px 40px rgba(0,0,0,.4)`, slide in 0.6 s `power2.out`.
- Light trail: SVG path `stroke:#FF5800`, `stroke-dasharray` draw 1.2 s with a blur glow, under the product layer.
