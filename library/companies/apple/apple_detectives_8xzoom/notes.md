# iPhone 17 Pro: Detectives Solve the Mystery with 8x Zoom  (Apple, 2025-12-31, 1:05 file / 1:00 content, 16:9 with 2.39:1 letterbox, YouTube)
URL: https://www.youtube.com/watch?v=leYJBhat7zw
Purpose: narrative comedy ad ("Shot on iPhone 17 Pro")
One-sentence point: Two noir detectives argue about the "crash zoom" while the 8× zoom keeps crash-zooming on clues — the feature is the joke.

## Structure
- 0-7.8 s **Set-up**: establishing wide of a brick factory, car pulls in (car SFX), low-angle tyre on gravel, foot steps out (door slam), detective low angle.
- 7.8-20.5 s **Build**: dark warehouse, slow walk-in wides, door screech, footsteps; very little cutting (3-4 s shots).
- 20.5-27.6 s **Dialogue starts**: two-shot (7.1 s hold): "You feel that?" "Feel what?" "The crash zoom." — punch-in close-up.
- 27.6-41 s **Gag run**: each line ("It heightens tension. Builds suspense… Uncovers evidence…") triggers an in-camera crash zoom onto a clue: rat, light bulb, pipes, radio, red gas can, foil.
- 41-54.7 s **Turn + payoff**: "Yeah, I don't know…" (balloon-deflate SFX), "Foreshadows danger", the floor gives way [CRASH] 48.8 s, "Do you feel it now?" "Oh yeah!", deadpan tag "I guess I'll go and try and find a ladder…"
- 54.7-58.35 s **Product**: orange iPhone 17 Pro macro, the detectives reflected in the lenses; "8x zoom" → "Shot on iPhone 17 Pro".
- 58.35-60 s **End**: Apple logo on black.

## Cut rhythm
- 27 shots in 60 s → **ASL 2.22 s**, median 1.75 s; quarters 2.14 / 2.14 / 1.67 / 2.14.
- 4 % < 1 s, 19 % > 3 s. Longest 7.1 s (two-shot set-up of the joke, 20.5 s), 4.2 s (50.5 s), 3.6 s (product).
- The crash zooms happen inside shots (35-41 s: 4-5 zoom-ins inside 2 shots), so the comic rhythm is faster than the ASL.
- Cuts on onsets 38 % vs chance 13 % → cuts land on SFX hits (door slam, crash).

## Typography
- Only at the end: "8x zoom" cap ≈ 7.5 % H and "Shot on iPhone 17 Pro" cap ≈ 6.3 % H, white SF Pro Display medium, centred over the product macro; legal "Additional software used" grey ≈ 2 % H at the bottom of the picture.
- Text cross-fades in place (one card replaces the other, same centre).

## Colour / grade
- 2.39:1 letterbox (active rows 61-418 of 480). Desaturated cool noir: grey-teal shadows, dirty greens, cold daylight outside.
- Warm accents: the glowing bulb, the red gas can; final product is saturated orange — the only strong colour in the film.

## Camera / shots
Classic film language parody: low angles, slow push-ins, wides of the warehouse, extreme close-ups of eyes, insert shots of clues via crash zooms (8× optical zoom shown in action), POV down through the broken floor.

## Transitions
Hard cuts only; whip/crash zooms do the "transition" work inside shots.

## Sound
- Score "throughout spot" (captions) — suspense music; dense diegetic SFX: car, door slam, door screech, footsteps, balloon deflating, floorboard creak, crash.
- Integrated **−16.0 LUFS**; loudest hit 25.9 s (−8.9 dBFS, +22.8 dB) on the first crash zoom; 0.25 s silence at 43.55 s before the next gag hit (43.9 s).
- Dialogue is dry and deadpan; music stops for the punchlines.

## What makes it premium
- The feature is demonstrated *as* the film technique, so the demo is the joke.
- Real cinema craft (2.39:1, noir lighting, actors) for a 60 s phone ad.
- No supers until the very end; product shot reflects the story in the lenses.

## Recipe (real footage + HTML/GSAP)
- Letterbox: two black bars `height: 12.7vh` top and bottom (2.39:1 inside 16:9).
- Crash zoom in HTML on real footage: `gsap.to(video,{scale:3,transformOrigin:"62% 40%",duration:.18,ease:"power4.in"})` + 2-3 frames of `filter: blur(4px)` + a whoosh/hit SFX; hold 0.8-1.2 s.
- Grade: `saturate(.6) contrast(1.1)` + teal overlay 18 % soft-light; keep one prop warm.
- End cards: white Inter/SF Pro 500 centred, "8x zoom" `font-size: 10vh` then crossfade (0.3 s) to "Shot on iPhone 17 Pro" `font-size: 8.5vh`; legal 12 px grey above the lower bar; Apple logo on black 1.6 s.
