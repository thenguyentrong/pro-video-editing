# Duolingo – social style (TikTok / YouTube Shorts / Reels, 2026)

Examples: `tremendous-spike` (8.8 s, 4.2 M views), `streakity` (7.5 s, 3.3 M), `duotv-ep1` (84.7 s, 0.7 M), `spanish-test-street` (68.4 s, 80 k). All 9:16 1080x1920, analysed Oct 2026.

## The style in one line
The mascot behaves like a chronically-online creator: short audio memes in which the app itself (word tiles, lesson screens) is the caption, plus longer series formats (animated sitcom, real-people challenge) that end with "to be continued" / "check our channel".

## Three sub-styles
| sub-style | length | ASL | captions | audio | loop / end |
|---|---|---|---|---|---|
| Audio meme (tremendous, streakity) | 7-9 s | 2.2 s or one shot | app word-bank tiles, word by word | sung track, trending or meme song, -7 to -11.5 LUFS | no logo, no CTA; streakity loops perfectly |
| Animated micro-series (DuoTV) | 85 s | 3.0 s (median 1.8) | dark-box subtitles, speaker colour-coded | voice cast + sitcom bed, -13 LUFS | title card at 29 s, "To Be Continued" card |
| Real-people challenge (spanish test) | 68 s | 1.75 s | typewriter hook text + game UI (timer, score) | dialogue + bed, -25.6 LUFS | CTA "check our channel" + Duo face end card |

## Hook (first 1-2 s)
- No intro, no logo. Frame 1 is already the joke or the stake.
- Meme: the mascot in an absurd situation + the first lyric word as a tile at 0.0 s.
- Series: a native-UI first frame (phone chat with "Why is he green tho?").
- Challenge: human stake typed on screen in 2.3 s ("This guy said he'd learn Spanish for his fiancée... ...did he!?").

## Cut rhythm
- Memes: one shot per lyric line (about 2 s) or a single locked shot; cuts follow the lyric, not the drum.
- Longer formats: ASL 1.7-3 s, dialogue holds up to 12 s, reaction inserts 0.5-1 s, jump cuts compress game time (60 s timer in 45 s).

## Captions and text
- Signature: Duolingo word-bank tiles (white rounded rectangle, grey bottom edge, dark grey #3C3C3C text, rounded sans), one word per tile, pop-on per sung word. Tile height 6-13 % H, cap 2.3-4.4 % H, in the upper third (14-31 % H) or as one big "shout" tile at 71-84 % H.
- Translation stack: source-language lyric (coloured Feather Bold-like, no box) over the English tiles.
- Subtitles in series: rounded dark box at 73-80 % H, cap ~2 % H, speaker colours (white / Duo green).
- Text density low: 1-8 words on screen; after the hook the visuals carry the joke.

## Audio
- Memes: one song does everything (no VO, no SFX), mastered loud (-7 to -11.5 LUFS).
- Series: original voice and location sound; much quieter mixes (-13 to -26 LUFS).

## Brand presence
- Mascot + app UI + brand green (#58CC02) instead of logos. Brand colour end card only on series content.

## Rules to copy
1. First frame = joke or stake; never a logo.
2. Put the caption in the product's own UI language (tiles, chat bubbles, timers).
3. One idea per shot, one shot per lyric line.
4. Short memes end without CTA and should loop; series end with a cliffhanger or "check our channel".
5. Keep all text in the top third or at 70-80 % H, never under 80 % H on TikTok.
6. Episode numbering + title cards make a feed into a show.

## Recipe (real footage + HTML/GSAP, 1080x1920)
- Meme (8 s): 4 clips x 2 s or 1 locked shot; word tiles `background:#fff; border:2px solid #E5E5E5; border-bottom-width:5px; border-radius:24px; font:600 84px Nunito; color:#3C3C3C`, pop `back.out(3)` 0.08 s per sung word; song at -9 LUFS; no end card; last frame = first frame.
- Series (60-90 s): open on an HTML phone UI for 4-5 s; subtitles in a `rgba(42,32,51,.85)` pill, 40 px Inter, bottom at 1540 px; title card at ~30 s; end on a 2 s brand-colour card.
- Challenge (60-70 s): typewriter hook 64 px IBM Plex Sans with bold punch line; timer box with 10 px #FFC800 border at y 1250-1400 px; ASL 1.7 s; CTA line + 3 s mascot end card.
