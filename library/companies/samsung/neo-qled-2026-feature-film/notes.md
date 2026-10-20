# 2026 Neo QLED : Feature Film  (Samsung, 15 Aug 2026 upload, 2:38 (158.3 s), 16:9, YouTube @Samsung Philippines - official regional channel)
URL: https://www.youtube.com/watch?v=LAlECVkOvE8
Purpose: TV feature film / product explainer (brand-level spec film, no narrator)
One-sentence point: Neo QLED is "the answer to true immersion" - colour, contrast, AI football mode, AI sound, Vision AI and 144 Hz motion, each shown as an abstract CGI spectacle and then on the TV in a room.
Note: only a 360p stream at 640 px wide was offered for this upload (the analysis copy is 640x360); measurements are in % of frame, so this does not change them.

## Structure
- 0-12.6 s colour: thousands of coloured balls fly at the camera, "Breathtaking colors" (1.4 s) + second line "Real QLED with 100% Color Volume" fades in 2.6 s later (4.0 s); colour streak tunnel (7-10 s).
- 12.6-23.4 s proof: top-down donut table, "100% Color Volume" VDE badge, camera pulls out to a TV in a dark living room (19.7 s), "A billion shades of color with Quantum Dot".
- 23.4-50 s contrast: night desert, "Ultra-fine Contrast" (24.5 s) + "with Quantum Mini LED" 2.9 s later; landscape dissolves into a field of LED points, aurora; CGI light cones; split "Conventional | Real QLED" city (42.6-50 s).
- 50-93 s AI Soccer Mode: ball in a CGI stadium net, "Immersive stadium experience" + "with AI Soccer Mode"; NQ4 AI Gen2 processor chip; stadium rises from the chip (60 s); TV in a warm room shows a match; a blue scan dome sweeps over the pitch (65-67 s, after a 0.7 s silence); "AI Soccer Mode Off | On" split (81-84 s).
- 88-109 s AI Sound: chip with purple/cyan sound ribbons "AI Sound Controller", "Commentator's voice / Crowd cheers" rings around the TV, "Split the audio and focus on what matters".
- 109-126 s Vision AI Companion: voice request on screen ("Tell me red team stats this season"), big kinetic text of the answer (123 s), "Find everything on the big screen".
- 126-149 s gaming: blue light-speed tunnel with a sports car, "Buttery smooth motion" + "with Motion Xcelerator 144Hz"; walls of TVs; "60Hz | 144Hz" splits; fastest part (9 cuts in 140-150 s).
- 149-157.3 s end: real-looking room, TV with green liquid art, "The answer to true immersion" -> "Neo QLED".
- 157.3 s SAMSUNG on black ~1 s.

## Cut rhythm (cuts2 + 19 soft transitions added after checking by eye)
- 48 shots, ASL 3.30 s, median 2.63 s. Quarters 4.40 / 3.30 / 3.30 / 2.20 - accelerates into the gaming part.
- 4% < 1 s, 44% > 3 s. Longest 11.5 s (23.4 s, desert -> LED field -> aurora, one continuous CGI move), 8.8 s (97.6 s sound rings), 7.9 s, 7.5 s (end room).
- Densest 140-150 s (9 cuts / 10 s). Cuts on onsets 13% vs 11% chance: not cut to music at all - the CGI moves set the timing.

## Typography
- Samsung Sharp Sans, white, centred. Headline line ~9% H incl. descenders (cap ~6% H, "Buttery smooth motion"), weight Bold/Semibold.
- Two-step claim: line 1 = benefit ("Ultra-fine Contrast"), line 2 = "with <technology name>" appears under it 1-3 s later (measured gaps 2.6 s, 2.9 s, ~0.6 s, 2.1 s). Both hold 3-7 s.
- Split labels "Conventional" / "Real QLED", "60Hz" / "144Hz", "AI Soccer Mode Off / On": ~4% H line, bottom of each half.
- Kinetic text once: huge cropped words of the AI answer slide past (123 s).
- Disclaimer micro-text bottom-right on almost every shot.

## Colour / grade
- Hyper-saturated: rainbow balls, magenta-blue speed tunnels, cyan chips on black, purple sound ribbons. Rooms are warm brown-beige so the TV image pops.
- Only 4% of samples are >= 70% empty: the frame is always full.

## Camera / shots
- ~70% CGI (particles, tunnels, chips, stadium), ~30% "TV in a room" composites. Every shot moves: push-ins, fly-throughs, pull-backs from screen content to the room.

## Transitions
- ~40% of boundaries soft: dissolves of landscape into LED grid, chip-to-stadium transforms, pull-out from full-frame content to the TV in the room (19.7 s), camera flying through rows of TVs.

## Sound
- No narrator. Music + diegetic football commentary + a voice command to the TV. Integrated -10.3 LUFS, median momentary loud and steady.
- One real silence: 66.05 s, 0.7 s at -59 dBFS, then +48 dB hit at 66.75 s on the AI scan dome - the single "breath" in the film.

## What makes it premium
- Each abstract tech claim is turned into a big visual metaphor (balls = colour, aurora = contrast, light-speed = 144 Hz).
- The "benefit then technology" two-line super is a strict, repeatable system.
- Before/after splits make invisible picture tech visible.

## Recipe (real footage + HTML/GSAP)
- Use stock CGI loops (particles, speed tunnels) for 3-6 s per chapter opener, then real TV-in-room footage (screen replaced) for proof.
- Super line 1: cap 6% H weight 700, `opacity 0 -> 1, y 20 -> 0` 0.6 s `power2.out`; line 2 (cap 4.5% H, weight 500) 2-3 s later, same move.
- Split compare: two `<video>` in a 50/50 flex with a 2 px white divider; labels at 85% H; optional divider slide `x: 0% -> 50%` 1.2 s.
- Pull-out: full-frame content `scale: 1 -> 0.42` 2 s `power2.inOut` into a TV frame in a room plate.
- Keep the mix at -10/-12 LUFS; one 0.7 s silence before the biggest AI moment.
