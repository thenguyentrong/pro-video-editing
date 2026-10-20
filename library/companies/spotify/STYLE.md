# Spotify – social style (YouTube Shorts / Reels / TikTok, 2026)

Examples: `keke-palmer` (61.2 s podcast clip), `eleven-shaved-head` (49.0 s podcast clip), `talk-to-spotify` (33.2 s feature launch in motion graphics). All 9:16, analysed Oct 2026 from the brand's YouTube Shorts.

## The style in one line
Two modes: (1) celebrity video-podcast clips that start mid-sentence on the best line and then just hold the face, with a fixed sticker + subtitle system; (2) product features as a colour-coded call-and-response between big quote cards and the real app UI.

## Overview (measured)
| film | length | shots | ASL | median | text | audio |
|---|---|---|---|---|---|---|
| keke-palmer | 61.2 s | 7 | 8.75 s | 2.96 s | title sticker 53-58 % H, subtitles 68-74 % H, green end card | dialogue, -19.0 LUFS |
| eleven-shaved-head | 49.0 s | 7 | 7.01 s | 5.09 s | name sticker 52-58 % H, 1-4-word subtitles ≈70 % H, no end card | dialogue, -20.3 LUFS |
| talk-to-spotify | 33.2 s | 10 (adaptive; ≈13 by eye) | 3.32 s | 2.55 s | quote cards 25-80 % H, no subtitles | music, -12.3 LUFS |

## Hook
- Podcast clips: the first frame is the guest mid-answer on a quotable line; the title sticker names the guest and the topic within 0.1 s.
- Feature films: the real app opens at 0.0 s and the prompt bar types the claim by 2-4 s.

## Rules (with numbers)
1. Podcast clip editing is front-loaded: 4-6 cuts in the first 9-22 s (wide, reaction 0.75 s, close), then takes of 16-34 s.
2. Subtitles below centre (68-74 % H) on a dark translucent box, cap ≈1.8 % H, max 2 lines; stickers in the centre band (52-58 % H) for the first ≈4.5 s only.
3. End: either a 1.5 s green card (cover + caps CTA, silence underneath) or no card at all (ends on the last word).
4. Feature films: one request per colour, ≈2.3 s card + ≈2.7 s answer; morph transitions; finish by repeating the opening shot, then a 1.6 s logo.
5. Dialogue clips are mastered quiet (-19 to -20 LUFS, peaks -7.5 to -9.5 dBTP); the music-led film is -12.3 LUFS.

## Recipe (HTML/GSAP, 1080x1920)
- Clip system: title strips `800 34px Inter` black on white boxes at y 1000-1110 px (`scaleX 0.2→1`, 0.25 s), show tag white-on-black below, subtitles `600 34px Figtree` in `rgba(0,0,0,.45)` boxes at y ≈1340 px; green `#1ED760` end card 1.5 s.
- Feature system: flat colour quote cards in `700 74px Unbounded` with 260 px quote marks; answer = real UI capture with a neon outline in the card colour; blob morph 0.4 s between them; typing bar at start and end.
