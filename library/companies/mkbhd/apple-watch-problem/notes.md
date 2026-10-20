# The Apple Watch Has a Problem  (MKBHD / Marques Brownlee, 2026-09-22, 15:06 full / first 300 s analysed, 2:1 frame inside 16:9 player, YouTube)
URL: https://www.youtube.com/watch?v=pOX1l1edBME
Purpose: tech commentary / analysis (product line + market, not a single-unit review)
One-sentence point: the new watch updates look minor, but read together they are aimed at two specific rival companies, and the second target is the surprising one.

Data note: first 300 s analysed (trimmed with ffmpeg after download). Frame 854x428 = 2:1. The scene detector missed 10 cuts (talking-head wide↔tight switches, screen changes, keynote clips); all 10 were checked on before/after frames and added with `--add-cuts` (16.98, 29.83, 47.78, 122.96, 132.13, 188.19, 264.30, 267.27, 270.24, 289.39 s), plus 2.4 s (end of the sting).

## First 30 s (hook)
- 0.0–2.4 channel logo sting (2.4 s, dip to black 1.5–2.4 s), loudest 0.5 s of the film at 0.85 s.
- 2.4–13.2 iris reveal onto overhead hands-on of the new watches on grey felt (2 shots, cut at 8.0 s). Voice-over starts at 2.44 s and names both products in the first sentence.
- 13.2 host on camera (bright office, glass wall, big plant, centred); cut to a tighter angle at 17.0 s.
- ≈12–27 s the promise: the updates target two companies, the first obvious, the second surprising (curiosity gap, then the first one is answered at once).
- 26.5–30.9 chapter title card: white condensed caps over purple-tinted b-roll, held 4.4 s across 2 shots.
- 30.9–34.1 the real news-article headline, full frame (black page, red top bar), as proof of the first claim.
- Cuts in 0–30 s: 6 (2.4, 8.0, 13.2, 17.0, 26.5, 29.8). No sponsor.

## Structure (first 300 s)
- 0–34 sting, products named, two-target promise, chapter 1 title, headline proof.
- 34–44 overhead hands-on with the rival band and the watch on a wrist; 44–54 talking head.
- 54–74 macro of the watch back and band; 74–94 talking head.
- 94–104 phone in hand showing the health app; 104–115 talking head.
- 115–172 long stretch of phone app comparisons held in hand overhead (8–12 s shots): rival app vs the new built-in features.
- 172–193 talking head; 193–196 borrowed keynote feature title with a source tag; 196–214 the maker's own newsroom page/slides scrolled.
- 214–231 talking head 16.7 s; 231–289 chapter 2: keynote clips (feature titles, UI on black, lifestyle scenes) intercut with talking-head reactions; densest part (4 cuts per 10 s, ASL 3.57 s in the last quarter).
- 289–300 talking head.

## Cut rhythm
52 shots in 300 s, ASL 5.77 s, median 4.91 s. 3.8 % under 1 s, 71.2 % over 3 s, 10.4 shots/min. ASL by quarter 4.69 / 8.33 / 8.33 / 3.57 s. Longest 16.7 s (talking head, 214.3 s), 15.9 s (172.3 s), 12.3 s (142.0 s, app demo). Shortest 0.63 s (271.8 s) and 0.9 s (284.5 s), both borrowed keynote clips. Cuts per 10 s 0–4. Cuts on onsets 65 % vs 61 % chance (near chance).

## Typography
- Chapter title: white condensed grotesque caps, medium weight, cap height ≈10 % H, ≈50 % W wide, centred at ≈50 % / 49 % H, on footage washed with a magenta→violet gradient (≈#B23AA6 → #3B2C9C) and darkened. Hold 4.4 s. Closest free: Oswald 500 or Barlow Condensed 500.
- Source tag on borrowed keynote footage: "APPLE" white bold caps in a small black slanted tag bottom right, ≈3.5 % H, x ≈92 % W, y ≈91 % H.
- Borrowed type kept as is: the article headline (white bold sans on black), the maker's own feature titles and newsroom pages.
- No lower thirds, no captions.

## Colour / grade
Clean, bright, natural. Office set: white/grey with a green plant and cool daylight. Product shots on neutral grey felt with small colourful desk toys as accents. The one stylised look is the chapter card colour wash.

## Camera / shots
Two-angle talking head (wide + tight, cut between on sentence ends). Overhead hands-on, macro, phone screens filmed in hand (not screen recordings), the maker's keynote and newsroom material as evidence.

## Transitions
Hard cuts; iris from the sting; chapter title cut in over b-roll (no wipe).

## Sound
Integrated −20.0 LUFS, LRA 4.2 LU, true peak −1.0 dBTP. Voice median −27.1 dBFS (50 ms RMS), p10 −53.6 dBFS → pauses ≈27 dB under the voice, no bed under talking; 15.0 % of 50 ms windows below −45 dBFS. Drop-outs ≥0.8 s at 191.8, 197.1, 228.2, 285.9 s (around borrowed clips). Borrowed keynote clips keep their own music/sound and enter hard (rises of 50–53 dB in 50 ms at 192.7, 211.6, 229.2, 233.0 s).

## What makes it premium
- A news-analysis promise in the first 25 s: two targets, one obvious, one surprising.
- A chapter card gives the argument a shape; each claim then gets a primary source (article, app, keynote).
- Product demos are real use in hand, long enough to read (8–12 s).
- Borrowed footage is credited with a small tag, not re-styled.

## Recipe (real footage + HTML/GSAP)
- Sting 2.4 s → iris → overhead product b-roll with voice from the first frame; name the products in sentence one, state the promise by ≈25 s.
- Chapter card: footage `filter:brightness(.55) saturate(.6)` + overlay `linear-gradient(90deg,rgba(178,58,166,.75),rgba(59,44,156,.75))`; title `font:500 13.5vh/1 Oswald;text-transform:uppercase;color:#fff;letter-spacing:.01em`, hard on, hold 4–4.5 s, hard off.
- Source tag: `.src{position:absolute;right:3%;bottom:4%;background:#000;color:#fff;font:800 2.6vh Inter;text-transform:uppercase;padding:.3em .8em;transform:skewX(-12deg)}`.
- Pace: talking head 6–17 s, demos 8–12 s, borrowed clips 0.6–3 s in the payoff chapter.
