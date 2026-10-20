# UEFA Champions League – broadcast package style

Examples studied (all 16:9):
| Example | What | Content length | Shots | ASL | Loudness (integrated) |
|---|---|---|---|---|---|
| ucl-2024-25-intro | broadcast opening titles, first season of the 2024 rebrand (fan upload of the feed) | 43.8 s | 20 | 2.19 s | −23.2 LUFS |
| ucl-2026-27-anthem-intro | official "Anthem" promo: 28 clubs lining up during the anthem | 61.5 s | 30 | 2.05 s | −17.5 LUFS |
| ucl-md2-every-goal-highlights | official goals compilation, first 125 s studied for the score bar | 125 s | 23 | 5.43 s | −33.2 LUFS |

## The system in one paragraph
Everything is built from two brand assets: the starball (shape) and the anthem (sound). The 2024 identity adds one motif, thin iridescent "light lines" (cyan → blue → magenta, a little yellow-green) on deep navy and royal blue. Real football is shown almost raw; the brand sits around it (CG worlds, lines, a single blue bar), never on top of it. Typography is minimal: no credits, no taglines, one centred logo lockup, one centred score bar.

## Sub-styles
1. **Opening titles (CG world → real action → logo)**, ucl-2024-25-intro: 0–17 s slow CG (starball facets, a stadium shaped like the starball), 17–30 s fast real action (shots 0.5–1.9 s, 25 % under 1 s) with light ribbons painted on the grass, one hero moment (trophy lift) as the loudest point, CG aerial pull-out, then a ~9 s logo hold on navy. ASL per quarter 2.2 / 1.4 / 1.2 / 11.0 s.
2. **Ritual montage (anthem line-ups)**, ucl-2026-27-anthem-intro: one club per shot, metronomic 2.0 s shots for 60 s (5 cuts in every 10 s), hard cuts only, no graphics, no end card; the anthem and a repeated colour motif (orange-black mascot kits) carry it.
3. **In-match graphics (score bar)**, ucl-md2-every-goal-highlights: one centred bottom bar (60 % width, 75–85 % height): royal-blue score box + gradient wings + crests + scorer strap + "FINAL SCORE" tab. Static during play, content swaps on the cut, full rebuild centre-out in 0.8 s when the match changes. Natural sound only.

## Rules (most important first)
1. **Two brand assets do all the work: starball shape + anthem.** Wipes, buildings, banners and end cards are all made from the starball; the anthem (or an arrangement) is the sound. Nothing else is invented.
2. **One motif travels through every section.** The iridescent light lines appear on the CG facets, then on the CG grass, then on the real grass, then around the logo: they connect CG and live action.
3. **Colour discipline: navy (#101030 / #000035) + royal blue (#1010b0–#0726f2); accent colours only inside thin lines.** Real footage keeps its natural colour; the blue bar works because blue is complementary to the pitch green.
4. **Real football is short and fast; brand moments are slow.** Action shots 0.5–1.9 s; CG and logo shots 3–12 s. The contrast is the energy.
5. **Rhythm is even, not beat-chopped.** Cuts land on phrases, not on audio onsets (7–11 % on onsets vs 10–17 % by chance). The anthem montage holds 2.0 s ± 0.3 s for a whole minute.
6. **Symmetry and centre.** Logo lockup 31 % of frame height tall (34–65 %, centred ≈ 49.5 %); score bar centred; bar animations build from the centre outward. This mirrors the round, symmetric starball.
7. **Graphics are stable; change happens on the cut.** Score/scorer/tab swap on the cut frame with no animation; only a change of match earns the 0.8 s rebuild.
8. **Typography is minimal and functional.** White condensed bold caps for data (team names cap height 4.2 % of frame height, digits ~7 %), small regular caps for secondary data (scorer); the wordmark is a fixed logo, never set as live text.
9. **Let the ritual be the content.** Line-ups, mascots, centre-circle banners and trophy arches are real-world brand graphics; film them instead of adding overlays.

## Recipe (real footage + HTML/GSAP, Hyperframes)
**A. 40–45 s opening titles**
- 0–5 s: brand mark as SVG, scaled to ~600 %, slow rotation 8° over 5 s, navy background, facet edges with a 2 px gradient stroke (#48d8d8 → #1878d8 → #d848d8).
- 5–6 s: shape-edge wipe: clip-path polygon moves across the frame in 0.9 s, ease "power3.inOut".
- 6–17 s: "brand world": real footage of your venue/building graded navy (lift blacks to #101030, cool highlights), slow push 1.0 → 1.15; enter the space at ~12 s (move through a doorway/over a rim).
- 17–30 s: 10–12 real action clips, 0.6–1.8 s, getting shorter; SVG light-line bundles (5–6 parallel paths, 3 px strokes, 9 px gaps, rounded corners, drop-shadow glow 6 px) drawn on with stroke-dashoffset in 0.8 s, staggered 0.06 s, placed in perspective on the floor.
- 30–32 s: one hero moment held 2.2 s, loudest music point.
- 32–35 s: wide pull-out, fade through #000035 over 1.5 s.
- 35–44 s: logo lockup 31 % of frame height tall, centred ≈ 49.5 %, fade + scale 0.96 → 1.0 over 1.0 s (power2.out); two line bundles sweep in from opposite corners 0.3 s later; music ends ~3 s before the hold ends.

**B. 60 s ritual montage**
- 28–30 shots of people in a line (eye level, 85–135 mm, slow slider or 3 % push), 2.0 s each, final wide shot 3.5 s; hard cuts; one repeated colour element in every frame; anthem-like choral cue at −15 LUFS momentary plateau; no text except a small bug.

**C. Score / data bar**
- 1920×1080: bar 1152 px wide centred, top 814 px; score box 190×102 px #0726f2; wings 481×65 px gradient #2c39e7 → #29336e; Barlow Condensed 700 (names 62 px, digits 104 px); scorer strap 200×45 px #1e3cbe with Barlow 500 26 px; optional top tab of the same size for a state ("FINAL SCORE").
- Build centre-out in 0.8 s: vertical line → box → digits → horizontal lines to full width → wings thicken → names unmask from centre → crests → strap drops down. Within the same item swap text on the cut; between items remove on the cut and rebuild.

## Sound branding
- The anthem is the sonic logo (Tony Britten, 1992, after Handel's "Zadok the Priest"): choral, legato, ceremonial. It is used as a flat, full plateau (−15 LUFS momentary) rather than with drops or hits.
- Opening titles: one dip before entering the "world" (−31 at 10.5 s), loudest on the trophy (−17 at 30.5 s), silence under the end of the logo hold.
- Highlights: no music; crowd swells of +8–10 LU on goals.
- I did not listen to the audio; all statements about instruments are from known facts or guesses, the levels are measured.
