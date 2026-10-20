# The Fantastic Four: First Steps — Final Trailer  (Marvel Studios, 25 Jun 2025, 2:25 (144.7 s, 143.2 s before the trailing black), 16:9 with 2.40:1 letterbox, YouTube)
URL: https://www.youtube.com/watch?v=18QQWa5MEcs
Purpose: final trailer (one month before release)
One-sentence point: a retro-future family of heroes faces a planet-eating god, and their real strength is each other.

## Structure (beats with timestamps)
- 0–1.4 s **custom studio logo**: a retro "MARVEL · STUDIOS" sign over a diorama of the four (the logo is built in the film's 1960s world).
- 1.4–9.6 s **TV-show frame**: four centred portrait close-ups of the team (0.8–1.0 s each) in front of a big blue "4", a talk-show host, the studio audience, the statue diorama, then an X-shaped four-way split screen of "ALERT!!" gadgets (8.6–9.6 s).
- 9.6–34.8 s **Act 1, heroes + city life**: fire rescue, Sue's force field, cheering crowds, Johnny flying past a "TAN, DON'T BURN — Coppertone" billboard (comic beat), Ben Grimm chatting with neighbours on a retro street (20.7–30.9 s), Johnny writes a fiery "4" in the sky.
- 34.8–69.5 s **Act 2, the threat**: night balcony, the sky lights up (one 5.0 s held shot at 39.8 s), Silver Surfer in an orange cloud, Times Square crowd looking up, Earth from space → dissolve to Galactus's giant foot → dissolve to a dark planet; space suits; Silver Surfer close-up (fades up from black at 60.5 s); Galactus's helmet in fire (63 s).
- 69.5–71.1 s **date card** "JULY 25TH".
- 71.1–113.1 s **Act 3**: press frenzy, Reed in a space suit, white flash (76.8 s), Sue carrying the baby through a crowd, Galactus's shadow over Manhattan (aerial, 84.3 s, 3.3 s), Fantasticar chase, destruction, the family in bed, Paris with giant machines, a kiss, Sue close-up.
- 113.1–121.7 s **tagline in two cards** with warm family moments between: "THEIR / GREATEST STRENGTH" … "IS / EACH OTHER".
- 121.7–129.9 s **one 8.3 s slow-motion hero shot**: Ben flying through clouds with Johnny on his back.
- 129.9–137.5 s finale action, 6 shots of ~1.2 s (Sue's power with RGB split, team running, Ben smashing, Reed stretching, Johnny's flame).
- 137.5–141.5 s **title**, 141.5–143.2 s **tickets/date card**, black. No button after the title.

## Cut rhythm
- 104 shots, **ASL 1.38 s**, median 1.08 s. ASL by quarter 1.33 · 1.43 · 1.12 · 1.56 s (flat, densest in Q3).
- 38% under 1 s, 4% over 3 s. Longest: 8.26 s (121.7, hero slow-mo), 5.0 s (39.8, sky), 4.0 s (title), 3.55 s (30.9). Shortest 0.21–0.33 s (flash frames at 68.1, 71.1, 76.8).
- Cuts per 10 s: 9 · 7 · 7 · 7 · 3 · 7 · 8 · 10 · 9 · 7 · 10 · 8 · 4 · 6 · 1. Densest at 70–80 s and 100–110 s (10 per 10 s); the threat section (40–50 s) and the hero shot (120–130 s) breathe.
- Cuts are not on the beat (23% on onsets vs. 22% chance).

## Typography
- 5 cards, all on a **steel-blue radial gradient** (≈ #1d3247 at the edges, #3b5c7c in the centre), never on black; cream text (≈ #ece6d6); hard cut in, hard cut out.
- Taglines: geometric sans caps with very wide tracking (~0.25–0.3 em), closest free match Josefin Sans SemiBold or Jost Medium (guess). Two-line layout: a small connector word on top ("THEIR", "IS", cap height ~3.5% H) and the main phrase below (~6.7% H), centred, spanning up to 82% of the width.
- Holds: JULY 25TH 1.58 s, THEIR GREATEST STRENGTH 1.84 s, IS EACH OTHER 1.08 s, title 4.05 s, tickets 1.67 s.
- Title: "the Fantastic 4" retro italic logo with the 4 in a ring (~43% H block), "MARVEL · STUDIOS" in retro box letters above, "FIRST STEPS" in spaced italic caps that flicker letter by letter into place over 1.5 s (137.5–139.0 s).
- In-picture graphics replace text: the X split screen, the "4" stage backdrop, the "4" written in fire.

## Colour / grade
Retro-futurist 1960s: teal and steel blue, cream, mustard and burnt orange; warm tungsten interiors; soft contrast with visible grain. Blue-and-white costumes are the anchor colour; space and threat scenes go orange-black. 2.40:1 bars.

## Camera / shots
Symmetrical centred portraits, period street scenes with people (not just heroes), big VFX wides (Galactus, Paris, Manhattan shadow), practical-looking car chase, one long slow-motion hero shot. Many shots are composed like 1960s magazine illustrations.

## Transitions
Mostly hard cuts; 2 dissolves (54.5 s Earth → foot, 55.5 s foot → planet surface); 6 dips to black (48.7, 57.8, 60.5, 80.4, 86.4, 109.5 s) that work as short breaths; a white flash at 76.8 s; one split-screen device.

## Sound
- Integrated −14.1 LUFS; loudness by quarter (median M) −15.5 · −17.4 · −16.1 · **−12.5**: this trailer gets *louder* into the end.
- No long silence. The deepest gap: 0.65 s at −50 dBFS at 61.2 s, right before the Silver Surfer / Galactus reveal (hit at 63.3 s).
- Emotional dip 104–105.5 s (−35 LUFS M) in the family section.
- The title cut (137.47 s) lands on a sustained peak (−8.6 LUFS M), with no pre-title silence; the music rings out under the tickets card.

## What makes it premium
- The whole package lives in the film's world: retro studio logo, TV-show framing, period ads, a split-screen device, cards in the film's blue.
- Character first: humour and family scenes get as much screen time as action.
- The tagline is split across two cards with footage between them, so the sentence lands with the hero shot.
- One 8 s slow-motion shot after 120 s of 1.4 s cutting: the most memorable image is the longest one.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Open with 4 portrait close-ups, 0.8–1.0 s each, subject dead centre, same background — then a split-screen card: four `<video>` clips in a 2×2 grid clipped by `clip-path: polygon()` into an X, 1.0 s.
2. Body at ASL ~1.4 s; insert a 1 s dip to black (`opacity` 1→0→1 over 0.3+0.3 s) every ~25 s as a breath.
3. Cards on a brand gradient, not black: `background: radial-gradient(ellipse 70% 80% at 50% 60%, #3b5c7c, #1d3247 75%)`; `font: 600 52px "Josefin Sans"; letter-spacing:.28em; color:#ece6d6;` small connector word 27px above. Hard cut in/out, hold 1.1–1.8 s.
4. Split the tagline: card 1 ("THEIR / GREATEST STRENGTH"), 5–7 s of family moments, card 2 ("IS / EACH OTHER"), then one 7–8 s slow-motion hero shot.
5. Title on the same gradient, hard cut on a music peak; subtitle letters flicker in (`opacity` random 0/1 steps per letter for 1.5 s, `ease:"steps(12)"`), hold 4 s; tickets card 1.7 s.
6. Let the music build to the end (no drop-out before the title); one 0.6 s gap before the villain reveal instead. Master −14 LUFS, letterbox 2.40:1.
