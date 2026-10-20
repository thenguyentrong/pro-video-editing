# Scrub Daddy – social style (YouTube Shorts / TikTok, 2025-2026)

Examples: `listen-up` (15.1 s stitch reply), `morning-routine` (22.5 s mascot vlog), `flow-state` (5.1 s one-shot meme), `texas-hold-em` (24.2 s product drop). All 9:16, analysed Oct 2026 from the brand's YouTube Shorts (TikTok cross-posts). Three of the four are 540-720 px uploads: phone-native on purpose.

## The style in one line
The sponge with a face is a chronically online creator: it replies to complaints, films its own routines, posts one-shot memes in first person, and announces drops with meme-argument VO. Phone footage, TikTok Classic text, no logo moments.

## Overview (measured)
| film | length | shots | ASL | text | end | LUFS |
|---|---|---|---|---|---|---|
| listen-up | 15.1 s | 2 | 7.53 s | 3 captions at 10-21 / 32-37 / 43 % H | "Buy Now" card, hard end | -18.7 |
| morning-routine | 22.5 s | 21 | 1.07 s | clock time at 50 % H | 0.4 s inverted glitch → loop | -12.0 |
| flow-state | 5.1 s | 1 | 5.12 s | 4-line caption at 66-80 % H | seamless loop | -14.0 |
| texas-hold-em | 24.2 s | 5 | 4.84 s | none (package + map labels) | retailer hold-up, hard end | -13.2 |

## Hook (first second)
- Someone else's complaint (stitch, 0-5 s), or the mascot already in the absurd situation with the caption on at 0.0 s, or a 0.3 s whip-in + heckle line.

## Rules (with numbers)
1. The product is the character: shoot at its eye level, give it a routine, a voice, a caption in first person.
2. Text is TikTok Classic: white, thin outline, sentence or lowercase, cap 1.6-3.0 % H (CTA 4.5 %); one caption per job.
3. Length decides the cut: memes are one shot (5 s); vlogs are 1 s cuts (ASL ≈1.1 s); replies and drops are 2-5 long shots with in-shot moves.
4. Endings: memes and vlogs loop (no card; glitch or continuous action); sales posts end on "Buy Now" or the store, never on a logo.
5. Meme inserts (map + orange circle + arrow, letterboxed) are allowed and look cheap on purpose.
6. Mixes -12 to -14 LUFS for music-led posts; replies quieter (-18.7 LUFS).

## Recipe (real phone footage + HTML/GSAP, 1080x1920)
- Caption: `500 40-56px "TikTok Sans"; color:#fff; -webkit-text-stroke:1.5-2px #000; paint-order:stroke fill`; top captions at y ≥270 px (strict safe zone), meme blocks at y 1270-1540 px, clock caption centred at y 960 px.
- Vlog: 15-20 shots of 0.5-2.3 s under purple/blue LED light, one 3.4 s comfort shot, 4-frame invert glitch outro.
- Reply: stitched clip 4-5 s untouched, then one product shot with a push-in (`scale 1→1.8`, 3 s) and three caption switches.
