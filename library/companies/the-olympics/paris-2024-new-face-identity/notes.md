# Here is the new face of the Olympic and Paralympic Games of #Paris2024  (Paris 2024 organising committee, uploaded 2019-10-21, 73.0 s incl. 5.8 s of partner cards, 16:9, YouTube / Paris 2024 channel)
URL: https://www.youtube.com/watch?v=ccrHmiad6XA
Purpose: identity launch film (emblem reveal + kinetic-type explainer of what the emblem means); the visual system later carried the Games' broadcast look
One-sentence point: the emblem is a face built from three symbols (medal, flame, national figure), and it stands for people at the heart of the Games.

Structure (content 0–67.2 s; times from metrics.json):
- 0.0–6.2 HOOK: the emblem lockup (gold emblem, wordmark, rings) on white, one 6.2 s still shot; music in at 0.7 s; the emblem "speaks" in first person through subtitles.
- 6.2–11.4 THESIS: the emblem grows full-frame, then type cards ("MY FACE", "UNION OF THREE SYMBOLS") on a background of repeated words.
- 11.4–19.4 SYMBOL 1 (medal): a circle on gold with the word in a type ring, then athletes' faces in triumph (0.3–1.2 s).
- 19.4–32.4 SYMBOL 2 (flame): coral card with ring text, flame graphic in pop red/yellow, archive Olympians, swimming baby, a high-jumper in a circle cut-out; densest part (17 cuts in 20–30 s).
- 32.4–48.0 SYMBOL 3 (national figure): coral bust with two concentric type rings, a famous painting, giant outline words ("EGALITARIAN", "SHARING", "GENEROUS") tiled over celebration footage.
- 48.0–57.4 PEOPLE: a young man in a crowd with photos flipping over him (0.25–0.8 s), then the three symbols as circles (gold disc, flame circle, bust circle).
- 57.4–67.2 LOCKUP 9.8 s (one shot): the event name tiled as a pattern, then circular word spirals (OLYMPIC / PARALYMPIC), collapsing into the emblem lockup (Olympic, then Paralympic version). Music ends at 65.5 s.
- 67.2–73.0 partner logo cards in silence (not studied).

Cut rhythm (0–67.2 s): 64 shots, ASL 1.05 s, median 0.58 s, 67 % under 1 s. ASL per quarter 1.40 / 0.70 / 0.99 / 1.20; cuts per 10 s 3, 12, 17, 8, 9, 14, 0. Long still lockups at both ends (6.2 s and 9.8 s) frame a fast middle. Cuts land on onsets 44 % vs 38 % chance (busy music, weak sync). Union of adaptive + 10 scene-detector cuts; 6 of those (48–52.5 s) are photo flips over one plate, counted as cuts.

Typography:
- The custom display face (Art Deco-inspired, rounded, high contrast between thick and hairline strokes) is the star. Closest free: "Poiret One" for the thin style, "Righteous" or "Monoton"-like outlines for display, "Bungee" for heavy cards; none matches well.
- Four type behaviours: (1) stacked heavy word cards (≈12 % H cap) on a background of the same words repeated at 15 % opacity; (2) circular text rings, two concentric (outer ≈10 % H outline caps, inner ≈3 % H solid caps) around an object; (3) giant outline words (white 2 px stroke, ≈30 % H) tiled and cropped over footage; (4) spirals of words collapsing into the emblem.
- Subtitles: plain white sans, sentence case, ≈3.5 % H, centred at ≈92 % height, on every line of the French voice. Closest free: Source Sans 3 600.
- Emblem lockup: wordmark caps with wide tracking ≈3 % H.

Colour/grade: a fixed brand palette as flat card colours: gold (#d5c46b family), coral/pink (#f07a73), cream (#f3eee6), off-white; footage stays natural or is duotoned (red-coral halftone on a portrait), with one pop red/yellow flame. Archive in B&W.

Camera/shots: mostly graphics; sport footage (current and archive), art (a painting, a bust), street crowd shot; circle cut-outs (footage inside a disc).

Transitions: hard cuts on type changes; circle masks; tile/pattern wipes; photo flips; the final spiral collapse is one continuous motion graphic.

Sound: a French voice-over (the emblem speaking; inferred from the subtitles) on a rhythmic bed. Measured: integrated −19.9 LUFS, LRA 6.1 LU, true peak −3.7 dBTP; momentary −15 to −20 through the body, dips at 41, 43, 45 s (−25/−28); 0.7 s silence at the start, music ends at 65.5 s, 7.4 s of silence over the partner cards.

What makes it premium:
- The typeface carries the film: one face used four ways (stack, ring, tile, spiral).
- A three-part structure that mirrors the emblem (medal, flame, figure), each with its own card colour.
- Still lockup at the start and the end, fast montage between.

Recipe (HTML/GSAP in Hyperframes, licensed footage):
- Cards: full-frame flat colours from a 4-colour palette; word stack 130 px caps; background word tile at 15 % opacity, `x` drift −3 % over the card.
- Ring text: SVG `<textPath>` on two circles (r 420 px and 300 px), outer outline caps 110 px `fill:none; stroke:#fff8; stroke-width:2`, inner 32 px solid; rotate rings in opposite directions 12°/s; object image centred.
- Giant tiled word over footage: 3 rows of outline caps 320 px, cropped, `x` scroll ±4 % per row.
- Spiral end: 8 rings of words with `scale 1.6→0`, `rotate 0→180deg`, stagger 0.08 s, then emblem `scale 0.8→1` 0.5 s `back.out(1.5)`; hold 4 s.
- Subtitles at 92 % height, 38 px, max 45 characters per line.
