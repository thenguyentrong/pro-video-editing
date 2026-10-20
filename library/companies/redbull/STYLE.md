# Red Bull – social style (YouTube Shorts / TikTok, 2026)

Examples: `waves-intense` (101.6 s, 103 M views), `f1-car-train` (10.6 s, 5.0 M), `she-made-it-look-easy` (29.1 s, 2.9 M). All 9:16, analysed Oct 2026.

## The style in one line
Real athletes and stunts filmed on phones, almost no editing, one small italic caption, and a jaw-drop moment that is either shown in frame 1 (climb, F1 in the metro) or promised in frame 1 and held back to the end (cliff dive).

## Sub-styles
| sub-style | example | ASL | text | audio |
|---|---|---|---|---|
| Athlete POV, real-time suspense | waves-intense | 33.9 s (3 shots, 95.7 s take) | ~12 ritual cards, 1.7 % H cap, centre | ambient + soft music, -18.6 LUFS |
| Stunt reveal + BTS | f1-car-train | 2.13 s | 1 question card at 66 % H | engine/ambient, -13.8 LUFS |
| Athlete UGC one-take | she-made-it-look-easy | 14.6 s | 1 card, first 2.5 s | ambient, -21.6 LUFS |

## Hook (first 1-2 s)
- The extreme is visible immediately: a person upside down, an F1 car in a metro, a diver pointing at deadly waves.
- Caption is a casual phrase or question ("take a look at this...", "fastest commute ever?"), never a title.

## Cut rhythm
- Very few cuts; the one-take is the proof. When there are cuts, the reveal shot is long (4.7 s) and the BTS shots short (1-1.7 s).
- Retention by waiting: in the 103 M-view clip the payoff comes at 95 % of the runtime.

## Captions and text
- Bold italic sans (Poppins / Proxima Nova Bold Italic-like), white, soft shadow, lowercase, no box, small (glyph line 2.1-2.9 % H, cap ~1.7 % H).
- Placed where the frame is empty or on the subject's body: 24-30 % H, 44-53 % H or 66 % H, always inside the safe centre band.
- 1 card in short clips; in long clips one card per action every 3-8 s.

## Audio
- Location sound first (sea, crowd, engine, breathing), music low or absent; -14 to -22 LUFS. No VO.

## Brand presence
- Logos only where they live in the world (dive board, F1 livery, crash pad); no end card, no CTA. Titles with an emoji carry the framing ("Those Waves Are INTENSE 🫣").

## Rules to copy
1. Put the most extreme frame first, or show the danger and delay the payoff.
2. Don't cut what is impressive: one take = credibility.
3. One small casual caption beats a big headline; ask a question.
4. Show the result before the explanation (reveal, then BTS).
5. Let real sound carry it; no logo, no outro, end abruptly so it loops.

## Recipe (real footage + HTML/GSAP, 1080x1920)
- Caption style: `italic 700 40-42px Poppins; color:#fff; text-shadow:0 2px 6px rgba(0,0,0,.55); text-transform:lowercase; text-align:center`, 1-2 lines, placed in empty space (y 460-560, 900-1000 or 1430 px).
- Long POV: 2 short handheld hook shots (3 s each) + one locked long take; ritual captions one per action (hold 3-6 s).
- Stunt: 1 locked reveal shot 4.5-5 s (subject passes the lens), 3-4 BTS shots 1.0-1.7 s, cut out mid-action.
