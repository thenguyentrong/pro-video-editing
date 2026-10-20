# Sonos Roam 2 | Size-defying sound. Everywhere.  (Sonos, 2024-06-25, 0:41, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=iCmorCOT5P4
Purpose: product spot (colourways, lifestyle)
One-sentence point: A small speaker goes everywhere, and each colour belongs to its own world.

Structure:
- 0.0-2.8 triptych: three vertical panels, red / olive / blue speaker, each in its matching world (frames/t001.0s.jpg).
- 2.8-13 olive world: leaves in sun, a hand lifts the olive speaker from a bush, macro of the SONOS logo with an olive-painted nail (t005.5s), a woman in olive clothes stretches on a garden wall, walks through green hills.
- 13-22 blue world: pool water, a blue towel with the blue speaker (t014.5s), infinity pool view, a swimmer, a hand presses the top button at the pool edge (t020.5s).
- 22-29 red world: clay tennis court, a player in coral with a red bag, the red speaker on a bench, the player's shadow serving on red clay (t028.0s).
- 29-33 packaging: hands open the card box, cable, the speaker slides out (t031.0s).
- 33-38.2 home: blue speaker on a table at a window view, a hand puts the red one on a kitchen counter (t036.0s).
- 38.2-40.8 black, 2.6 s of silence.

Cut rhythm: 38 shots (adaptive detector, checked by eye), ASL 1.07 s, median 0.83 s, 60.5 % under 1 s, 56 shots/min. Quarters 1.13 / 0.78 / 0.85 / 1.46 s: fastest in the pool and tennis worlds, slower at home. Longest 3.1 s (red speaker in the kitchen), 2.8 s (triptych). Cuts on onsets 16 % vs 22 % chance: cut on movement, not on the beat.

Typography: none on screen. The name and line live only in the title of the upload; the product logo on the speaker is the only text (macro at 5.5 s).

Colour/grade: product colour = world colour. Olive speaker / olive clothes / olive nails / green leaves; blue speaker / blue towel / blue pool; red speaker / coral shirt / red clay. Natural sunny grade, slightly warm (R-B +4), median saturation 34 %, luma 66.

Camera/shots: live action, handheld-feeling but steady, many inserts of hands on the product (lift, press, place), macros of the logo and texture, one triptych split-screen, one shadow shot. People are mostly cropped (hands, legs, back).

Transitions: hard cuts; the triptych opens the film; a black tail ends it.

Sound: music only, bright pop track; −13.9 LUFS, LRA 3.0 LU, true peak +1.2 dBTP (hot). Silence at start (0.3 s) and on the 2.6 s black tail. No drop-outs inside.

What makes it premium:
- Strict colour matching: every frame shows one colourway inside its own world.
- Hands on the product in almost every world: touch, scale and use without text.
- Triptych opener = the whole range in one frame.
- No supers: the product and its logo carry the message.

Recipe (real footage + HTML/GSAP):
1. Plan 3 worlds, one per colourway; wardrobe, props and nail colour match the product.
2. Per world 6-9 s: 1 wide, 2-3 inserts of hands on the product (0.6-1 s), 1 logo macro, 1 action shot.
3. Triptych opener: CSS grid `grid-template-columns:repeat(3,1fr); gap:0`, each column a `<video>` with `object-fit:cover`, 2.5-3 s.
4. End on the product at home, 3 s, then 2-3 s of black and silence (no logo card needed if the logo is on the product).
5. Music-only master −14 LUFS, true peak ≤ −1 dBTP.
