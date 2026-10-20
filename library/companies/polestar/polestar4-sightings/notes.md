# Polestar 4 coupe Sightings  (Polestar, 2024-08-22, 1:00, 2.35:1 scope (1080x460 file), YouTube)
URL: https://www.youtube.com/watch?v=0n8W-GtfHYw
Purpose: launch ad / concept film (sci-fi "UFO sighting" story)
One-sentence point: An "Identified Futuristic Object" falls from the sky wrapped in gold foil, unwraps in the desert into a Polestar 4, and witnesses say they have never seen anything move like it.

Structure:
- 0.0-6.3 hook: a gold foil sphere falls through dark smoke-clouds (frames/t000.5s.jpg), lands as a small glowing point in the night.
- 6.3-17.6 arrival: low skim over a road, the gold-wrapped object on a ridge at dusk, the tail-light bar glowing through the foil (t009.5s), the wrapped shape on the horizon (t012.0s); 11.9 s witness voices start ("So tell us what you saw...").
- 17.6-29.2 unwrapping: silhouette of the wrapped car with the red light bar against the sunset (t017.5s), foil rippling, headlight through foil, interior shots through the glass roof (t023.0s), macro of foil over the headlight, the foil-covered front at dusk (t029.5s).
- 29.2-49.0 drive: the foil blows off and floats away like a jellyfish next to the car (t037.5s), wing-mirror and rear-view mirror details, the car comes out of dust towards camera, rear view, tracking shots on desert roads, interior.
- 49.0-60.0 payoff: front shots in backlight, high-speed tracking shots on straight and winding desert roads (t053.5s), last shot an aerial of the car on a curved mountain road (3.5 s). No end card.

Cut rhythm: 30 shots, ASL 2.00 s, median 1.78 s, quarters 2.50 / 1.88 / 1.36 / 1.88 - speeds up in the third quarter (drive). Shortest 0.44 s (31.6), longest 4.44 s (wrapped object on the horizon) and 4.24 s. 13 % under 1 s, 13 % over 3 s. Densest 40-50 s (7 cuts). Cuts on onset 21 % vs 12 % chance (some cuts on hits).

Typography: none seen (1 fps sheet + key frames). The concept line lives in the YouTube description ("IFO, noun: Identified Futuristic Object...").

Colour/grade: desert dusk: warm-grey sand and mountains, steel-blue skies, gold foil and the red light bar as accents, white car. Median saturation 17 % (p90 29 %), neutral R-B (+1), median luma 78, soft contrast (p95-p5 112). Scope 2.35:1 frame = "movie" signal.

Camera/shots: real live action plus VFX (the falling sphere is CG; the foil on the car looks practical - real fabric blown by wind, my judgement). Low skimming tracking shots, long-lens tracking from a camera car, backlit silhouettes, macro of foil and lights, interior POV, one aerial at the end. Handheld-like energy in the drive section.

Transitions: 29 hard cuts; reveal is done by the object (foil coming off), not by an edit effect.

Sound: witness-interview voices from 11.9 to 58.4 s (whisper: "it went by so fast. I didn't know what it was. I'd never seen anything like it... I've never seen anything move like it. It's amazing... like out of this world"), like a documentary about a UFO; music + SFX under it, level -9 to -15 LUFS-M, loudest hit 13.75 s. Integrated -14.2 LUFS.

What makes it premium:
- A genre frame (UFO sighting documentary) makes the design claim ("futuristic") without saying it.
- Hide-and-reveal with a physical material (gold foil) - tactile, not CG-only.
- Scope 2.35:1, dusk light, desert = feature-film language.
- The car's signature light bar is the first thing you see, through the foil.

Recipe (real footage + HTML/GSAP):
1. Story: "witnesses describe something they saw" - record 4-6 short real-sounding lines (vox-pop style), lay them over picture from ~20 % of the runtime.
2. Shoot the product covered (foil/emergency blanket, fabric), reveal its light signature through the cover, then let wind remove it. Dusk light, long lenses, low tracking.
3. Frame in HTML at 2.35:1: a 1920x817 video area centred, or crop a 16:9 source with `object-fit:cover` inside a `div` with `aspect-ratio:2.35/1` on black.
4. Edit: 2.5 s per shot in the build, 1.3-1.9 s in the drive, one 3.5-4.5 s horizon hold; end on an aerial, no text.
5. Optional sky object: a 3D sphere (Three.js `MeshStandardMaterial` metalness 1, roughness .3, gold `#c9a24a`) falling with motion blur over cloud footage.
