# NBA – league promo style

Examples studied (Oct 2026, all 16:9, YouTube / NBA channel):

| Example | Type | Length | Shots | ASL | Median | <1 s | Integrated / LRA | Cuts on onsets (chance) |
|---|---|---|---|---|---|---|---|---|
| [finals-2026-history-is-calling](finals-2026-history-is-calling/notes.md) | :30 tune-in promo, game 1 | 30.5 s | 26 | 1.17 s | 0.88 s | 65 % | −16.9 LUFS / 3.3 LU | 16 % (13 %) |
| [playoffs-2026-where-legacies-are-built](playoffs-2026-where-legacies-are-built/notes.md) | :90 tournament promo, archive + current | 90.1 s | 70 | 1.29 s | 1.03 s | 43 % | −18.9 LUFS / 4.5 LU | 4 % (10 %) |
| [tipoff-2025-start-to-finish](tipoff-2025-start-to-finish/notes.md) | season-launch campaign spot | 56.8 s | 45 | 1.26 s | 1.00 s | 49 % | −12.2 LUFS / 9.9 LU | 18 % (20 %) |

## The look in one paragraph
The league's own promos are short-shot (ASL 1.2–1.3 s, median ≈1 s) and almost text-free: no names, no stats, no supers over action. Each film has one visual treatment that unifies very different footage: a "memory" grade with vignette and light leaks that makes 1980s tape and 2026 HD one story, a teal-and-warm commercial grade with shallow focus for a lifestyle campaign, or a CG brand world (team crests rising into the trophy) before real action. All text lives on one end card, or as giant word cards on faces in the last seconds. The music is a steady bed (LRA 3–5 LU) on the event promos and a dynamic build on the campaign spot. Cuts are not placed on beats (near or under chance).

## Sub-styles
1. **Tune-in promo (:30).** Two identical CG shots (one per team) → atmosphere → alternating action (team A / team B) → end card with brand → game → teams → time → network. Black + gold only.
2. **Tournament promo (:90).** Ritual montage first (tunnels, hands, faces) at ≈1.0 s, archive mixed with current, then longer "big moments" (1.5–2.5 s); a 5 s arena wide as a breath at ≈72 %; the edit slows down toward the end (cuts per 10 s 11 → 4). Sponsor + broadcaster row on the end card.
3. **Campaign spot.** Commercial cinematography (players training, fans in every city), quiet hook, music dip before the peak shot, three huge one-word cards (cap ≈50 % of frame height) on faces, sponsor-titled lockup over the last shot with a red light bloom.

## Rules (most important first)
1. **One treatment for all footage.** Vignette + light leaks, or teal/warm grade, or one CG world. Archive is never shown as a separate "old" section.
2. **No text over action.** Recognition is assumed; text appears only on the end card or as 1-word cards in the last 10 %.
3. **Symmetry for match-ups.** Equal shots for both teams, alternating, same CG treatment.
4. **Slow down to land the climax.** Bigger moments get longer shots (1.5–3 s) instead of more cuts.
5. **Strict end-card hierarchy.** Wordmark (12–25 % H) → event/game (≈3 %) → teams (cap ≈9 %) or sponsor (≈3–5 %) → time / "tap to watch" (≈2.5–3 %) → partner logos (≈4 %).
6. **Loudest moment = end card arrival** (tune-in) or the hero shot before the cards (campaign); fade 2–3 s.

## Recipe (real or licensed footage + HTML/GSAP, Hyperframes)
- Tune-in :30: 2 × 2.8 s CG crest moves (SVG crest on a wood plate, `perspective` 1200 px, `rotateX 55deg`), 4 atmosphere shots of ≈1.1 s in one colour each, 18–20 action shots at 0.6–1.0 s, 4 s end card (black, 1.5 px gold court lines, Oswald 700 team line with a gold gradient, trophy right at 60 % H).
- Tournament :90: one layer stack on every clip (`contrast(1.15) sepia(.12)`, oval vignette to 75 % black, light leak flash on 1 cut in 4); 1.0 s shots for 20 s, 1–1.5 s for 45 s, a 5 s wide at 72 %, 1.5–2.5 s for the last 15 s; end card with Barlow Condensed 800 Italic wordmark at 25 % cap height on hazy steel blue.
- Campaign :60: teal shadows / warm skin; 3.5 s quiet hook; montage 0.8–1.0 s; a 2 s breath with a music dip; START / TO / FINISH style word cards in Bebas Neue 300 px skewed −8°, 0.85 s each; lockup over the final face with a radial red bloom.
- Mix: −16 to −19 LUFS for event promos, −12 to −14 for campaign spots; true peak ≤ −1 dBTP (the campaign upload measured +1.3 dBTP, avoid that).
- League marks, team crests, archive and player likeness need licences; use your own crests and footage.
