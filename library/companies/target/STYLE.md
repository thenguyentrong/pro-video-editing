# Target – social style (YouTube Shorts / TikTok / Reels, 2026)

Examples: `bagspotting-chicago` (77.5 s creator street series), `shopping-friends-competitive` (59.5 s creator duo, reality-TV), `no-tricks-40-off-6s` (6.0 s promo cutdown). All 9:16, analysed Oct 2026. YouTube views are low (1.7-8.9 k); the formats are built for TikTok/Reels paid + organic.

## The style in one line
Creators do the talking in real Target stores and streets; the brand appears as a colour (red), a shape (the bullseye) and a few white disc stickers, never as a long logo moment.

## Sub-styles
| sub-style | ASL | text | audio | end |
|---|---|---|---|---|
| Creator street series (Bagspotting) | 1.49 s | 2 graphics in 77 s (name super, show wordmark over rings), no subtitles | dialogue + bed, -11.7 LUFS | host walks off, no end card |
| Creator duo, reality confessional (Deal Days) | 4.25 s | speaker-coloured subtitles 2 % H at 83-87 % H, disc stickers, fake REC UI | dialogue, -23.9 LUFS | bullseye iris wipe -> 2 offer cards (4 s) |
| Promo cutdown 6 s | 2.0 s (4 beats) | huge lowercase pun 7-15 % H, offer disc 47 % H | music only, -24 LUFS, works muted | ends on offer + date |

## Hook (first 1-2 s)
- Creator content: a person already in motion (sliding on steps toward a red bag; walk-and-talk "Wait."), no title card.
- Cutdown: a 3-word seasonal pun in giant type with the product overlapping it, beat-pulse at 0.4 s.

## Cut rhythm
- Street series: interview grammar (wide approach -> CU answers -> product insert), ASL 1.5 s.
- Reality confessional: long handheld takes (5-9 s) + confessionals; stickers keep the screen moving.
- Cutdown: 3 beats of 1.5-2 s + 1 graphic flip.

## Captions and text
- Brand type: Helvetica Neue Bold-like lowercase, Target red #CC0000 on white discs, or white on red/teal.
- Stickers are circles (bullseye logic), pop in with overshoot, stay 1-2 s, sit in the left or upper half.
- Subtitles only when two people banter: small (2 % H), low (83-87 % H), speaker colours.

## Brand devices
- Red wardrobe and red bags = brand in every frame.
- Concentric rings: title background, iris-wipe transition, end card.
- Coin-flip of a disc to change from event name to offer/date.

## Rules to copy
1. Let a creator's persona carry the video; give them a repeatable game (spot the bag, buy it first).
2. Make the brand a colour + a shape you can see on mute.
3. Use one reusable transition built from the logo (rings).
4. Promos: 3 beats x 1.5-2 s, one message each, end on offer + date.
5. Sales message in the creator's own words, with a sticker on the same line.

## Recipe (real footage + HTML/GSAP, 1080x1920)
- Disc sticker: 480 px white circle, `700 120px "Helvetica Neue"` lowercase #CC0000, teal/red rings; `back.out(2.2)` 0.25 s in, pulse 1 -> 1.08.
- Rings transition: 7 SVG circles, white dot scales into a 900 px disc while rings `scale 0 -> 6` (0.5 s).
- Coin flip: `rotationY 0 -> 90`, swap, `90 -> 0`, 0.12 s each.
- Lower third: 58 px white bold with 3 px red stroke + red pill sub-line, 1.4 s.
- 6 s cutdown: 0-1.5 pun (150/165/330 px type, product in front), 1.5-3.1 product + badge, 3.1-4.75 lockup, 4.75-6.0 offer + date.
