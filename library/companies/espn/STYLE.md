# ESPN – broadcast packaging style

Examples studied (Oct 2026, all 16:9):

| Example | Type | Content length | Shots | ASL | Median | <1 s | Integrated / LRA | Cuts on onsets (chance) |
|---|---|---|---|---|---|---|---|---|
| [cfb-2025-season-anthem](cfb-2025-season-anthem/notes.md) | season anthem / title package (licensed single as a music video) | 95.3 s | 117 | 0.81 s | 0.67 s | 86 % | −12.4 LUFS / 3.6 LU | 12 % (8 %) |
| [nba-finals-2026-g5-intro](nba-finals-2026-g5-intro/notes.md) | game-broadcast open (gold CG + archive) | 82.4 s (+10 s end screen) | 53 | 1.55 s | 1.08 s | 45 % | −24.3 LUFS / 6.0 LU | 25 % (9 %) |
| [nba-finals-2026-tonight-promo](nba-finals-2026-tonight-promo/notes.md) | event promo, base version of the same package | 80.7 s | 34 | 2.37 s | 1.15 s | 47 % | −23.8 LUFS / 4.1 LU | 6 % (8 %) |

Loudness is measured on the whole upload (the G5 intro includes a louder YouTube end screen).

## The look in one paragraph
ESPN packages a sport as a world with one rule. For a league it owns as an event (the NBA Finals), the rule is one material: everything, even 1980s tape, is pushed into gold, framed by gold CG objects and finished on a gold 3D wordmark with the trophy. For a season it sells as culture (college football), the rule is a licensed song: the open is cut like a music video with an on-screen song credit, 117 shots in 95 s, and the title arrives at the loudest point over live footage. Supers are almost absent; the brand speaks through the wordmark, the shield logo and one date line. TV versions are mixed to the US broadcast target (≈−24 LUFS), online music-led versions are mastered loud (−12 LUFS).

## Sub-styles
1. **Package open (one material).** Gold CG macro hook (7 s) → archive inside gold frames, portholes and screens → 2–3 long CG fly-throughs (5–11 s each) → full-frame archive with gold bloom and particles → wordmark + trophy lockup (4–5 s) → network sting. Versions per game reuse hook and lockup and change only the middle.
2. **Season anthem (music video).** A real single; artist cutaways every 10–20 s; 0.6–0.8 s shots for 90 s; a cut-out sticker collage as the only designed break; two-line condensed title + shield over a drone shot; shield + date end card on darkened footage.

## Rules (most important first)
1. **One unifying rule per package.** One material (gold) or one song; never both a new look and a new sound.
2. **History goes inside the brand object.** Archive is composited onto CG surfaces of the trophy world or graded to match it, never shown as raw tape.
3. **Two speeds.** CG moves 5–11 s; archive and action 0.4–1.2 s. Nothing in between.
4. **Type only for the brand.** Script wordmark (≈20–25 % of frame height) or condensed caps title (cap ≈14 % H) + logo; date line ≈3.5 % H. No names, no stats.
5. **Cut to the music when the music is the idea.** The G5 open lands 25 % of cuts on onsets (chance 9 %); the event promo and the anthem stay near chance.
6. **Deliver two mixes.** TV: −24 LUFS integrated, momentary within ≈10 dB. Online music cut: −12 to −14 LUFS, flat wall (LRA ≈3.6).
7. **Credit the song like a music video.** Three lines, small grotesk, bottom-left, first 3 s.

## Recipe (real or licensed footage + HTML/GSAP, Hyperframes)
- Package open (80 s): 7 s macro hook in one material (licensed CG or real brass/gold macro) → 23 s archive in frames (`border-image` gold gradient, `perspective` 1400 px, panel flies past in 3 s) → 25 s of three long CG moves → 20 s full-frame archive (`sepia(.35) saturate(1.2)`, bloom, gold particles) → 5 s wordmark + trophy lockup. Mix −24 LUFS.
- Season anthem (95 s): licensed track; 115–120 shots at 0.6–0.8 s; credit in Inter 500 26 px at left 10 % / top 73 % for 3 s; 5 s cut-out collage break (white 6 px outlines, `back.out` pops every 0.7 s); Anton title 150 px two lines + logo at the music peak; logo + date card 4 s on footage at `brightness(.4)`. Master −12 to −14 LUFS.
- Never use ESPN's or the league's real marks, typefaces or music without a licence; the free stand-ins are Anton/Bebas Neue (condensed caps), Montserrat 800 (date line), Yellowtail (script mock-ups).
