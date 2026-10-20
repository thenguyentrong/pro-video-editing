# LEGO – social style (YouTube Shorts, 2026)

Examples: `spiderman-stopmotion-bts` (19.6 s split-screen BTS), `glass-blowing` (37.6 s craft challenge), `nascar-prank` (36.7 s prank with a sports guest). All 9:16, analysed Oct 2026 from the LEGO YouTube channel's Shorts.

Download note: the channel's Shorts returned "not available" to anonymous requests (likely the made-for-kids setting); they downloaded with an anonymous browser-session cookie.

## The style in one line
Show the making and the result together: split screens, counters and game graphics turn crafts, builds and pranks into short TV-style formats, always ending on the finished object or a laugh, never on a logo.

## Overview (measured)
| film | length | shots | ASL | text | end | LUFS |
|---|---|---|---|---|---|---|
| spiderman-stopmotion-bts | 19.6 s | 32 (incl. stop-motion steps; ≈14 set-ups by eye) | 0.61 s (≈1.4 s per set-up) | title on the split seam 44-57 % H | light-leak flash → loop | -12.7 |
| glass-blowing | 37.6 s | 20 | 1.88 s | title / counter / labels at 46-55 % H + emoji | result on table, hard end | -9.7 |
| nascar-prank | 36.7 s | 36 | 1.02 s | question 40-45 % H, name tag + timer at 13-21 % H | laughter, no card | -13.3 |

## Hook
- The format in frame 1: "BTS" title over a split of process + result; three finished glass pieces in the fire; the end reaction with the result pixelated and a question caption.

## Rules (with numbers)
1. Split screens (two stacked 1080x960 halves) for process vs result; labels sit on the seam at ≈47-50 % H.
2. Progress devices: "ELEMENT 1/3" counters, a 13 → 00 countdown box, clock-like structure; one round = 8-13 s.
3. Pace: ASL 1.0-1.9 s with no slow-down at the end; reveals get 2-3 s.
4. Text: white with outline or light italic caps; cap 2-6 % H; emoji as reaction labels (1-3 per label).
5. End: on the object or the laugh; the only end text is a small legal line at 85-90 % H in the last 2-3 s.
6. Loud, music-led masters (-9.7 to -13.3 LUFS).

## Recipe (real footage + HTML/GSAP, 1080x1920)
- Split: two `<video>` layers `height:960px` stacked; label `italic 300 52px Montserrat` caps at y ≈900 px + emoji 48 px at y ≈1000 px.
- Game graphics: name tag in black boxes at y 250-400 px, timer box at x 670 / y 230 px (`tl.set` per second, yellow at 00).
- BTS title: `800 76px "TikTok Sans"` white with 3 px black stroke centred on the seam, 0-2.6 s.
