# Nike – social / short ad style (YouTube Shorts / Reels / TikTok, 2026)

Examples: `caitlin-normal-day` (30.0 s, deadpan type story), `kobe10-protro` (27.8 s, product hero montage), `sabrina-vs-rider` (27.5 s, 2:3, CCTV comedy sketch). Analysed Oct 2026. (Long-form Nike films are covered elsewhere; this folder is only the social cut.)

## The style in one line
Nike's social shorts are small, smart ideas with print-grade restraint: one device per video (a growing paragraph, a material montage, a fake CCTV match), very little text, and a quiet logo end card.

## Sub-styles
| sub-style | example | ASL | text | audio |
|---|---|---|---|---|
| Deadpan type story (athlete) | caitlin-normal-day | 10.0 s (1 locked 26.7 s shot) | serif paragraph typed word-by-word with VO, ends on giant condensed caps | VO, -24 LUFS |
| Product hero / material montage | kobe10-protro | 0.87 s (72 % < 1 s) | none | sound design, -10.4 LUFS |
| Athlete comedy sketch | sabrina-vs-rider | 2.5 s | 2 title cards + 3 end cards on black | room tone + stings, -19.7 LUFS |

## Hook (first 1-2 s)
- Curiosity, not shouting: a tiny athlete in an empty frame with one typed word; a drill carving clay; "NIKE BASKETBALL PRESENTS: Sabrina vs. The Rider".
- No captions-as-hook, no faces talking to camera.

## Cut rhythm
- Either extreme: one locked shot for the whole story (Caitlin) or a sub-second material montage (Kobe, Q3 at 0.54 s).
- Speed curve in montages: fast middle, 2.5 s holds for the hero and the logo.

## Text
- Editorial type: condensed serif body (cap 2.7 % H, line height 4.3 % H, left-aligned) vs Nike Futura Condensed ExtraBold caps (cap ~6 % H) for the payoff; gradient title cards on black (line box ~3.5 % H) for sketches.
- Text either IS the subtitle (synced to VO) or is absent.

## Audio
- VO-led stories mixed low (-24 LUFS); product films are sound-design driven; no trending audio in these three.

## End
- Small logo card 1-4 s (CC monogram + swoosh; Kobe logo embossed in clay; "ANYTIME ANYWHERE" + SABRINA 4 + swoosh). Dates and prices stay in the post caption.

## Rules to copy
1. One idea, one device per short.
2. Use negative space and small elements; the feed is loud, be quiet.
3. Text must be designed type (serif or condensed caps), never default captions.
4. Montage = shape rhymes (same object, many materials); hold the hero.
5. Sketches: frame a tiny moment like a big sporting contest.
6. Logo last, small, no CTA.

## Recipe (real footage + HTML/GSAP, 1080x1920)
- Type story: #F2F2F0 background, keyed figure 360 px tall at the bottom, serif 52 px / 82 px line height, per-word `tl.set` from VO timings; payoff in 120 px condensed caps, word every 0.25 s.
- Montage: 30 shots, ASL 0.85 s, grayscale 85 % + 3 false-colour gradient-map shots; SVG outline draws; logo relief with light sweep.
- Sketch: black gradient title cards 1 s each, CCTV filter + VHS band glitches on 2-3 beats, 1 s product insert, 3 black end cards.
