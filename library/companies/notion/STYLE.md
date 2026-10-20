# Notion – social style (YouTube Shorts / TikTok / Reels, 2025-2026)

Examples: `prehistoric-tools` (13.4 s visual-metaphor sketch), `how-well-did-they-do` (23.5 s event interview game). Both 9:16, analysed Oct 2026.

## The style in one line
A productivity app that almost never shows its product: short office sketches and people-on-the-street games, one plain white line of text, and the mascot/logo used as the game piece.

## Sub-styles
| sub-style | ASL | text | audio |
|---|---|---|---|
| Visual metaphor sketch | 1.91 s (six cuts on a 1.4 s grid + 4.8 s wide) | one static centred line, cap ~2 % H at 53 % H | music, -12.4 LUFS, silence at the end |
| Interview game (draw the logo) | 1.31 s (61 % < 1 s) | question 3.6 % H at 10-13 % H + logo disc 21 % H, red X / green check | dialogue + bed, -18.9 LUFS, music cuts on verdicts |

## Hook
- An absurd image with an aphorism (T-rex at a desk, "You are what you use."), or a clear challenge with the answer key on screen ("Can you draw Nosy?").

## Rules to copy
1. One metaphor or one game per video; no product UI needed.
2. Text: one plain line, white, centred; no captions for dialogue.
3. Repetition on a strict grid (1.4 s) is a gag; end on a long "find it" wide.
4. Turn the logo into the challenge; show the answer key first so viewers judge along.
5. Verdict beats: freeze, black and white, red X / green check, music off.

## Recipe (real footage + HTML/GSAP, 1080x1920)
- Sketch: 6 clips x 1.4 s + 4.8 s wide; `500 46px Inter` white, thin shadow, centre y 1130 px, off after the montage.
- Game: 5-6 s set-up with question (52 px at y 190-260) and 400 px logo disc (y 330-730); per guest 1.2 s wide / 0.9 s CU / 0.5 s B&W verdict with SVG X (`#E53935`, 18 px stroke) or green check pop.
