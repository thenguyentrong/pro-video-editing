# Canva – social style (YouTube Shorts, 2026)

Examples: `world-tour` (30.0 s creator-style promo), `linkedin-ads` (42.7 s B2B feature explainer), `font-personality` (102.5 s educational explainer with a partner). All 9:16, analysed Oct 2026 from the brand's YouTube Shorts (Canva Design School content).

## The style in one line
A B2B tool that sells through people: creators and designers talk to camera, the product UI does the proving (as background, zoomed recording or split screen), and Canva purple pills or highlights hold the brand.

## Overview (measured)
| film | length | shots | ASL | text | end | LUFS |
|---|---|---|---|---|---|---|
| world-tour | 30.0 s | 23 (background swaps) | 1.31 s | meme pill 15-21 % H, subtitles 80.5-84 % H | question to viewer, no card | -16.4 |
| linkedin-ads | 42.7 s | 14 | 3.05 s | purple subtitle pills 80-85 % H, name tag 65-71 % H | 4 s logo animation | -10.9 |
| font-personality | 102.5 s | 14 | 7.32 s | subtitles 74.5-78 % H (seam 48-51 % H in split), word cards 14-25 % H, CTA 13-19 % H | CTA to description, no card | -20.6 |

## Hook
- A question or a meme line in frame 1: a what-if question, a "pick one" font test, or a self-aware joke about the video's length.

## Rules (with numbers)
1. One person on camera all the way through (a creator with a credential tag, or a designer); the UI is shown behind, beside or after them.
2. Structure the explainer in the product's own words: 3 steps of 8-12 s (create / launch / learn) or 3 examples.
3. Subtitles always on, 1-2 lines, cap ≈1.5-1.6 % H; brand version = white on a purple pill (#7D2AE8).
4. Canva places subtitles low (74-85 % H). Under the platform UI that is risky: for new work move them to 60-70 % H.
5. Endings are soft: a question or a pointer to the description; a logo only on the formal explainer (4 s).
6. Loudness varies widely (-10.9 to -20.6 LUFS); master new work at -14 LUFS.

## Recipe (real footage + HTML/GSAP, 1080x1920)
- Pill subtitle: `background:#7D2AE8; color:#fff; font:500 34px Figtree; border-radius:18px; padding:10px 22px`, 3-7 words, y 1250-1400 px.
- Phone-frame device: selfie masked into a 490x1000 px phone mockup at y 480-1480 px; swap backgrounds per spoken list word (0.5-1.3 s).
- Split demo: screen recording 1080x960 on top, presenter below, subtitles on the seam (y 960 px).
