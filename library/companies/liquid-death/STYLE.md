# Liquid Death – social style (YouTube Shorts / Reels / TikTok, 2025-2026)

Examples: `nothing-extreme` (30.1 s product launch parody), `size-matters` (47.0 s innuendo testimonials), `spinal-tap` (92.1 s talent collab mockumentary). All 9:16 vertical originals (not crops), analysed Oct 2026 from the brand's YouTube Shorts.

## The style in one line
A water brand that edits like a comedy studio: TV-commercial production value, a deadpan script that says the opposite of the picture, and the product only as the punch line or the straight man.

## Overview (measured)
| film | length | shots | ASL | median | % < 1 s | text | LUFS |
|---|---|---|---|---|---|---|---|
| nothing-extreme | 30.1 s | 11 | 2.73 s | 2.67 s | 0 % | phrase captions cap 1.6 % H at 67 % H; end card | -15.2 |
| size-matters | 47.0 s | 8 | 5.88 s | 5.30 s | 0 % | none until the end card (28-32 % H) | -17.6 |
| spinal-tap | 92.1 s | 30 | 3.07 s | 2.65 s | 3 % | logo 46-54 % H, cue card, product line 24 % H, black tagline 48-51 % H | -16.2 |

## Core idea
Contradiction. A sober claim + an extreme speaker (metal, gimp suit, sword swallower), or an innocent product + an innuendo script, or a famous band that cannot read the brief. The joke repeats on a grid; the product arrives last.

## Hook (first 1-2 s)
- Product-first when the product is new (can racks into focus at 0.4 s with a word caption already on).
- Line-first when the joke is the hook (a person saying the double-meaning line at 0.0 s, no text).
- Talent-first for a collab (band on screen + "Liquid Death presents" lockup at 0.0-4.0 s).

## Rules (with numbers)
1. One set-up per speaker or per claim; 2.5-6.5 s each; ASL 2.7-5.9 s. No fast montage.
2. The longest shot carries the biggest joke (11.3 s take in size-matters; 4 s gag in nothing-extreme).
3. Captions only when the visual is busy: 2-4 words per card, heavy italic caps in cream with a black outline, at ≈67 % H. Otherwise no captions at all.
4. End card: plain statement of the product truth in heavy caps, 2-3 lines, upper third (12-32 % H), 4-7.5 s, then hard end. No logo animation.
5. Loudness -15 to -18 LUFS: dialogue-led mixes, music only as a bed and on the card.
6. Cuts follow dialogue, not beats (cut-to-onset 43-52 % vs 43-50 % chance).

## Recipe (real footage + HTML/GSAP, 1080x1920)
- Script: write the claim list straight, then cast the opposite person for each line.
- Shoot locked mediums, centred, eye level, full art direction per set; product in hand.
- Caption CSS: `italic 900 46px "Archivo Black"; skewX(-10deg); color:#F3E3B5; -webkit-text-stroke:3px #000; paint-order:stroke fill; uppercase`, centre y ≈1290 px.
- End card: `900 40-56px "Archivo Black"` white caps on a brand gradient or the product table, y 230-620 px; second line replaces the first with `tl.set`.
