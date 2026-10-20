# Polestar 4. The performance coupe  (Polestar, 2024-04-15, 1:30, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=RIBszBOGPf4
Purpose: brand / launch film (mood film, no claims)
One-sentence point: "The beauty of the natural world meets the beauty of the Polestar world" (description): red flower landscapes, macro petals and liquid-chrome forms slowly turn into the car.

Structure:
- 0.0-11.4 opening: dark aerial of jagged rock with red vegetation (frames/t000.5s.jpg), then a CG field of white liquid-chrome "roots" flowing (t003.5s), mountains with a red valley floor at dusk.
- 11.4-37.7 nature build: endless red flower field, macro of a yellow cosmos flower (t013.5s), a dew drop on petals, a chrome drop sliding on forest ground, a chrome liquid star forming among red flowers, puddle with a chrome reflection, an aerial of red-tinted karst, a chrome organic lattice sculpture (t032.6s), chrome tendrils next to a flower, a backlit petal. The car appears only as a 1.7 s glimpse of a door edge (20.1).
- 37.7-58.8 bridge: a chrome jellyfish-like form floating above the red field; a silver beetle walking on the car's paint (t041.0s); chrome lattice; a car side in motion (44.9); a tall chrome monolith in the field; a starry night sky; a figure on a green ridge; a chrome water-drop shape on grey paint; white coral-like growth; the monolith turns out to be the car's rear seen tall (55-57).
- 58.8-70.9 reveal: the full white car parked in the red field, front view (4.7 s) (t059.0s), headlight macro, top-down on the flowers, 3/4 view.
- 70.9-73.1 brand: a glowing white neon outline of the Polestar star on grey (t071.0s), sparks/dust around it.
- 73.1-90.0 drive-off: rear view in the field, a fast skim over the flowers, the car on a road at sunset, rear-glass macro, aerial of the car on a winding road through red fields, front 3/4 at sunset, final 4.7 s: a straight road through the red field to the horizon, no car (t086.0s). No text, no URL.

Cut rhythm: 41 shots, ASL 2.20 s, median 1.88 s, quarters 2.25 / 1.61 / 1.88 / 2.81. Shortest 0.52 s (37.2), longest 4.72 s (car reveal) and 4.68 s (last shot). 5 % under 1 s, 17 % over 3 s. Very even pace (3-6 cuts every 10 s). Cuts on onset 22 % vs 28 % chance = edited to the music's phrasing, not its beats.

Typography: none. The only graphic is the neon star logo (70.9-73.1, ~70 % of frame height, white glow line on a grey car surface). No wordmark, no claim, no URL - the YouTube title carries the name.

Colour/grade: one controlled palette: deep red/orange-red (flowers, vegetation) against desaturated blue-grey (sky, mountains, the car's white/silver and chrome). Median saturation 41 % (p90 71 %), R-B +13 (warm because of the reds), median luma 65 (moody, low-key), contrast p95-p5 133. Soft overcast/dusk light, no hard sun except the sunset end. Chrome forms reflect the red world.

Camera/shots: mix of real aerials, macro nature photography and CG (liquid chrome, sculptures, beetle - likely CG; the red landscapes may be colour-shifted real locations or generated, I cannot tell). Very slow drifts and push-ins on macros, slow aerial moves; the car shots are locked or slow tracking. Symmetry: the car is centred and frontal in the reveal; the end road is a one-point perspective.

Transitions: 40 hard cuts, no effects. The "morph" between nature and car is done by MATCHING shapes and materials across cuts (chrome drop -> chrome star -> chrome lattice -> beetle on paint -> car paint), not by VFX transitions.

Sound: no voice (whisper returned only a music caption tag "Pomp and Circumstance" - unverified, could be a hallucinated label; treat as orchestral/cinematic music, a guess). Dynamics: quiet open (-30 to -22 LUFS-M), building to a long loud plateau at the car reveal (55-64 s, -9 to -10), a dip under the neon star (71-73 s, down to -31) and a final loud section (74-87 s) with a fade at 88-90. Integrated -14.0 LUFS.

What makes it premium:
- The car is withheld for 65 % of the film; the world is built first.
- Strict two-colour script (red vs chrome/grey) gives every frame the same "look".
- Material rhymes (liquid chrome in nature -> car paint) make the link without words.
- Brand mark as a physical light object, not a graphic end card.
- Ends on an empty road: confidence, no CTA.

Recipe (real footage + HTML/GSAP):
1. Pick ONE accent colour for the world (e.g. #b4281e red) and keep everything else blue-grey; grade: push the red hue into all foliage (HSL qualifier), desaturate skies to 15-20 %, median luma ~65.
2. Gather 25-30 nature macros/aerials + 6-8 chrome/metal macros (spoon, mercury-like liquid, polished metal objects) + 8-10 car shots. Cut 1.5-2.5 s per shot; reveal the full product at ~65 % of runtime and hold 4-5 s.
3. Order the shots by material: organic -> wet -> chrome -> paint -> car (each cut shares a shape or texture with the next).
4. Neon logo in HTML: SVG path of the logo, `stroke:#fff; stroke-width:3; filter: drop-shadow(0 0 6px #fff) drop-shadow(0 0 18px rgba(255,255,255,.6))`, draw with `strokeDashoffset` 0.8 s, then flicker `opacity` 1/0.6/1 in 3 steps; background `#5b6166` with a soft radial light.
5. Final shot: a one-point perspective road/horizon held 4-5 s, music fades; no text.
