# Premier League – league brand and graphics style

Examples studied (Oct 2026):

| Example | Type | Format | Content length | Shots | ASL | Median | Integrated / LRA |
|---|---|---|---|---|---|---|---|
| [is-back-2024-25](is-back-2024-25/notes.md) | season-launch campaign (comedy + montage + identity card) | 16:9 | 60.0 s (+7.7 s end screen) | 76 | 0.79 s | 0.38 s | −11.0 LUFS / 8.3 LU |
| [38-matches-in-38-seconds](38-matches-in-38-seconds/notes.md) | season data package (animated bump chart) | 9:16 | 38.1 s | 1 (continuous) | — | — | −32.1 LUFS / 1.5 LU |
| [goal-animations-2026-27](goal-animations-2026-27/notes.md) | score-bug goal animations for all 20 clubs | 9:16 | 13.1 s | 1 (continuous) | — | — | −9.0 LUFS / 0.5 LU |

Loudness is for the whole upload.

## The system in one paragraph
The league's brand is a graphic system more than a film language: deep purple, neon green, a lime-to-cyan gradient, diagonal "lion-mane" stripes, the lion and a geometric heavy sans. The same pieces build a season campaign's end card, a data chart's chapter columns and the in-match score bug. Film content around it is fast and human: a scripted local story (a barbershop) with the season's football as the punchline, 76 shots in 60 s, median shot 0.38 s in the montage, two sub-second silences before the biggest moments. The graphics follow one rule: a fixed template with a personal slot (every club gets its own goal animation, every chapter its own gradient), and one transition (a neon gradient wipe) that opens and closes every state.

## Sub-styles
1. **Season campaign.** 6 s slow establishing shot → dialogue scene → a burst of the brand "in the wild" (tattoos, shirts, murals, 0.12–0.3 s each) → 25 s montage at 0.3–0.6 s with cut-out athletes on neon plates → comic pay-off → purple card with campaign wordmark + date pill.
2. **Data package.** One continuous move: a bump chart pans at one matchweek per ≈0.92 s; season chapters are named on a recoloured position column; club colours only on lines; final table holds 2.7 s in silence.
3. **In-match graphics.** Score bug: club-code tab, score + lion disc, gradient wing, clock tab. Goal state ≈3.3 s: neon wipe 0.3 s → club colour + crest + club icon wipe ≈1 s → "GOAL" hold ≈1.7 s → neon wipe 0.3 s → score updated.

## Rules (most important first)
1. **One palette everywhere.** Purple (#37003c family / #3d0a6b), neon green (#00ff85 family), lime→cyan gradient (#d6f23a → #22e3d8); club colours only for club data.
2. **Template + personal slot.** Fixed positions for score, clock and table; the variable part (club colour, crest, icon, chant word, chapter name) changes inside them.
3. **One transition.** The neon gradient wipe (≈0.3 s) for every state change; cut-out pops (≈0.15 s) in films.
4. **The brand in the world first.** Show the logo on real things (tattoos, shirts, a TV in the shop) before the end card.
5. **Short silences before peaks.** 0.35–0.85 s drop-outs before the montage, the reveal and the logo.
6. **Text sits on cards, not on football.** Campaign wordmark cap ≈16 % H, date pill ≈7 % H, chapter labels ≈25–30 % H vertical.

## Recipe (real or licensed footage + HTML/GSAP, Hyperframes)
- Campaign card: purple background with `repeating-linear-gradient(115deg, …)` stripes, logo 18 % H, wordmark Outfit 800 caps with a lime→cyan text gradient, date pill 7 % H; 4 s hold, 0.8 s silence, logo card.
- Cut-out athlete: PNG with an 8 px white outline (SVG `feMorphology dilate`), three duotone echo copies stepping −9 % in x, on a #00ff85 plate; pop 0.15 s `back.out(2)`.
- Score bug and goal state: see goal-animations-2026-27/notes.md (580×64 px at 1080p; wipe `clip-path inset` 0.3 s; GOAL hold 1.7 s).
- Data film: D3/SVG bump chart, 20 rows × 70 px, 150 px per matchweek, linear pan; chapter column recolours with a 0.4 s crossfade.
- Free stand-ins: Outfit 800 or Lexend 800 for the league sans; never use the real lion, club crests or the league typeface without a licence.
