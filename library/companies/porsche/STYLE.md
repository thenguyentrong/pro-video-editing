# Porsche - style

Examples (official @Porsche uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [the-promise](the-promise/notes.md) | 2025-07 | 1:34 | 117 | 0.80 s | 0.68 s | community anthem, warm film look |
| [cayenne-electric](cayenne-electric/notes.md) | 2025-12 | 2:07 | 70 | 1.82 s | 1.44 s | product launch with feature callouts, no VO |
| [75-years-doing-everything-wrong](75-years-doing-everything-wrong/notes.md) | 2026-03 | 2:26 | 92 | 1.59 s | 0.78 s | heritage argument, archive montage |

## Sub-styles
1. **Anthem montage** (Promise, 75 Years): VO with one rhetorical device, 60-75 % of shots under 1 s, real people/archive, one designed hero shot, end on black with wordmark.
2. **Launch film** (Cayenne Electric): no VO, music + car SFX, dark tease -> daylight reveal, 6 feature callouts as white sentence-case captions, name card in the studio set, wordmark.

## Rules that repeat
- **End sequence is fixed:** cut to black -> PORSCHE wordmark (wide extended caps, 42 % frame width, 5 % height, centre) with blur-in ~0.9 s -> hold 3-4 s -> fade -> WLTP legal text 3 s. Sting hit on the logo (+15-29 dB rise).
- **Small white type, no boxes.** Caps labels at 2.3 % height (75 Years) or sentence-case callouts at ~4.2 % (Cayenne). Never a lower-third bar, never an icon.
- **Specs = one fact + unit**, e.g. "850 kW (1,156 PS)", "Towing capacity of up to 3.5 t". The callout survives 2-4 cuts (3-4 s) and sits in the empty part of the image near the feature. A legal line appears only when a performance number is claimed.
- **Silence before a new section** (Promise 0.65 s, Cayenne 1.75 s and 0.5 s), then a hard hit.
- **Dutch angles + low speed angles** on road plates; macro on crest/light bar/raindrops; drone tops.
- **One long, still shot** somewhere (75 Years opens with 15.2 s; Cayenne bookends with the ring-light studio).

## Recipe (real footage + HTML/GSAP)
1. Shoot or select: 1 hero silhouette (backlit, gradient sky or studio ring light), 20-60 detail and action clips, 2-3 drone tops.
2. Grade: launch = cool teal, crushed blacks, red accent light; anthem = warm golden hour, soft contrast, grain.
3. Callouts: Inter 600, 4.2vh, white, left-aligned, 1-2 lines, fade .3 s, hold 3.5 s across cuts. Caps labels: Inter 600, 2.3vh, letter-spacing .02em.
4. Rhythm: tease 10-15 s slow -> body 1.4-1.9 s median (launch) or 0.7-0.8 s (anthem) -> 0.5-1.75 s silence -> hit.
5. End: black, wordmark `filter: blur(18px) -> 0` over .9 s, hold 4 s, legal 3 s.
