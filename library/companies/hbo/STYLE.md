# HBO / Max – video style

Examples studied (Oct 2026):

| Example | Type | Content length | Shots | ASL | Median | Integrated / LRA |
|---|---|---|---|---|---|---|
| [the-last-of-us-titles](the-last-of-us-titles/notes.md) | main title sequence (CG continuous move) | 65.5 s | 2 | 32.75 s | 32.75 s | −22.4 LUFS / 7.5 LU |
| [house-of-the-dragon-s2-titles](house-of-the-dragon-s2-titles/notes.md) | main title sequence (panel chain) | 99.0 s | 24 | 4.12 s | 4.21 s | −15.4 LUFS / 3.2 LU |
| [the-last-of-us-s2-trailer](the-last-of-us-s2-trailer/notes.md) | season trailer | 114.0 s | 63 | 1.81 s | 1.38 s | −18.4 LUFS / 12.7 LU |

## The look in one paragraph
HBO title sequences are built on ONE physical material that stands for the whole show (fungus growing over a miniature world; an embroidered tapestry of the family history). Everything is shot or rendered as macro with very shallow depth of field and one hard light (back-haze for The Last of Us, raking side light for House of the Dragon), so CG looks like a real object on a table. The pace is slow and ceremonial: one 56 s continuous camera move, or a metronomic chain of ~4.2 s panels. Credits are tiny (2.5–3.3 % of frame height), only fade, and sit wherever the frame is empty; the typeface belongs to the show's world (eroded condensed grotesque vs. inscriptional serif). The title arrives at the end as the result of the material (the fungus grows the letters; the title rises over the dark land after the tapestry), holds ~5 s and fades to black. Music is one theme at a flat level, no SFX. HBO trailers are the opposite in pace (ASL 1.8 s) but keep the same restraint: a 24 s quiet cold open, the show's own title face on black cards, black holds with audio drop-outs as "breaths", a split tagline inside the climax, and an end card coloured by the season (red flare). The platform brand stays small: a corner bug (HBO / max) and a 3–5 s platform card after the title.

## Sub-styles
1. **Continuous-metaphor title** (The Last of Us). One unbroken CG macro camera move (56.5 s), the metaphor evolves as the camera travels (tendrils → overgrown city skyline → spore network like city lights → two survivors), one hard cut to black for the title grown from fungus. ~18 credit cards, one every ~3.1 s. Quiet mix (−22 LUFS).
2. **Panel-chronicle title** (House of the Dragon S2). 24 hard-cut panels of embroidery, 15 of them 4.1–4.6 s long, slow glides and focus pulls inside each; 2:1 letterbox; Trajan-like serif credits, staggered; orchestral theme compressed flat (LRA 3.2); title in metallic gold over a dark landscape.
3. **Prestige season trailer** (The Last of Us S2). Three acts: slow cold open (ASL 3.4 s) → "THE ACCLAIMED HBO ORIGINAL SERIES RETURNS" card → world montage (1.3–1.7 s) → two black holds with drop-outs and re-entry hits → accelerating act 3 (~1.1 s) with a two-card tagline (EVERY PATH / HAS A PRICE) → 6 s dialogue face-off with music pulled out → title slam on a red flare card → Max card in the same red.

## Rules (most important first)
1. **One material, one metaphor.** Every shot of a title sequence is the same stuff (fungus, thread). No mixed media, no live-action actors in the titles.
2. **Macro miniature look.** Very shallow depth of field, one dominant light (backlight haze or 15° raking light), heavy vignette or letterbox, floating particles (spores, embers) for life.
3. **Slow, regular time.** Titles: either one continuous move or shots of a fixed length (~4.2 s); no shot under 2 s. Credits change every ~3 s.
4. **Tiny type in negative space.** Credit names at 2.5–3.3 % of frame height, role labels at ~50–60 % of that above the name; plain fades (~0.5 s), position changes per shot to sit in the emptiest area; never over the subject.
5. **The title is the payoff of the metaphor.** It appears in the last 5–8 s, made by or emerging from the material, holds ~3–5 s, then fades to black. Show-specific wordmark, ~10 % (wide serif) to ~75 % (stacked condensed) of frame height.
6. **Restricted palette.** 3–4 colours for the whole piece (near-black + ochre + cordyceps red + haze white; parchment + oxblood + gold + teal). Trailers: one colour world per act, ending in the season colour (red).
7. **Sound: titles flat, trailers breathe.** Titles: one theme, no SFX, LRA 3–7.5 LU, loudest moment on the title. Trailers: LRA ~13 LU, black holds of 1.6–2.5 s with drop-outs, +16 to +24 dB re-entry hits, a 5 s near-silent dialogue beat right before the title slam.
8. **Trailer type = the show's title face.** Black cards, 2–3 words, cap height ~12.5 % of frame height, eroded condensed caps with a white-to-grey gradient; tagline split across two 0.75 s cards between the fastest shots. Brand frame minimal: corner bug + 3–5 s platform card tinted to the show.

## Recipe: an HBO-style title sequence in Hyperframes (real footage + HTML/GSAP)
- Pick the material that is the show's theme (mould, thread, paper, rust, ink in water). Shoot it with a macro lens at f/2.8, one hard light (backlight + haze, or raking side light), 20–24 slow slider moves of 3–5 s, or one long move.
- Grade: blacks #0b0d0e (or warm #1a120c), one mid colour, one accent; radial vignette rgba(0,0,0,0.85) at the edges; grain opacity 0.06–0.08. Optional 2:1 letterbox (bars 5.4 %).
- Timeline (90 s): 0–5 s first texture + two lead names; 5–80 s one panel every 4.2 s (or one continuous wrapper move: scale 1.00 → 1.12, ease "none"); the densest 2.1–3 s shots only in the second quarter; 80–90 s hard cut to dark, title emerges.
- Camera inside each shot: GSAP on the video wrapper scale 1.04 → 1.10 and x 0 → −2 % for the shot length; a CSS blur 2 px → 0 over 0.6 s at the start to fake a focus pull.
- Credits: names at 3 % of frame height (Oswald 600 for modern/grim, Cinzel 400 + letter-spacing 0.28em for historic), labels 50–60 % size at 0.7 opacity; GSAP opacity 0 → 1 (0.5 s, power1.out), hold 2–2.5 s, out 0.5 s; one card every 3 s; anchor list [bottom-left, top-right, bottom-right, bottom-centre] chosen per shot by where the frame is empty.
- Title: SVG mask fed by an animated feTurbulence/feDisplacementMap (or a real growth/ink time-lapse as a luma matte) 2.5 s; hold 3 s; fade 2.5 s to black.
- Sound: one theme, level flat (−15 to −22 LUFS integrated), no SFX, title = loudest moment.
- For a trailer in the same family: 24 s quiet open → card on black (condensed eroded caps, 12.5 % cap height) → montage 1.3–1.7 s → black hold 2.5 s with −25 dB duck → re-entry hit → montage ~1.1 s with a two-card tagline → 5 s dialogue beat → title slam on a coloured glow card → platform card in the same colour.
