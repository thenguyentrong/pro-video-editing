# Ryanair – social style (TikTok, cross-posted to YouTube Shorts, 2026)

Examples: `buy-your-own-plane-stitch` (6.4 s, 596 k on YT), `dont-worry-guys` (6.0 s, 205 k), `act-your-fare` (7.5 s, 82 k YT / 119 k TikTok). All 9:16, analysed Oct 2026. (TikTok itself could not be downloaded without browser impersonation, so the identical YouTube cross-posts were measured.)

## The style in one line
A rude, self-aware low-cost airline that talks like a teenager: 6-8 s memes, phone footage, TikTok's own text tool, and a plane with a pasted human face as the mascot.

## Sub-styles
| sub-style | example | length | ASL | text |
|---|---|---|---|---|
| Stitch reply to a complaint | buy your own plane | 6.4 s | 1.07 s | customer's caption kept + white bold caps word captions (5.3 % H) at 78 % H |
| Topical banter over plain footage | don't worry guys | 6.0 s | one shot | TikTok Classic text, 2-step reveal, 18-33 % H |
| Meme template (expectation vs reality) | act your fare | 7.5 s | 1.26 s | 2 TikTok Classic labels, 14-22 % H |

## Hook (first 1-2 s)
- The set-up is on screen at 0.0 s: either the complaint itself (stitched UGC) or a label naming the target ("don't worry City fans,", "passenger expectations for €19.99:").
- No logo intro; the logo is on the plane.

## Cut rhythm
- 6-8 s total, ASL 1.1-1.3 s, or one single shot when the text is the joke.
- Cuts sit on audio onsets (100 % in two of three examples) and the punch line arrives at 50-65 % of the runtime (3.0 s of 6.0, 4.2 s of 7.5, 4.7 s of 6.4).

## Captions and text
- Default: TikTok's in-app "Classic" text (white, thin black outline, lowercase), cap 3.0-3.3 % H, in the top third (14-33 % H).
- For voiced replies: CapCut-style one-to-two-word white bold caps with drop shadow, cap ~5.3 % H at ~78 % H.
- 1-15 words in the whole video.

## Audio
- Trend-style music or the stitched creator's audio; deadpan VO for the plane; one hit or 0.15 s silence before the punch line. -10 to -14 LUFS.

## Visual signature
- The plane face (human eyes + lips cut out and pasted on a 737 nose), used as reaction shot or 0.4 s end sting.
- Phone footage, no grade, stock clips when contrast is needed (expectation), meme red arrows and digital punch-ins.

## Rules to copy
1. Answer the audience, do not broadcast: stitch the complaint and reply in under 7 s.
2. One joke per video, punch line at 50-65 % of the runtime, then end.
3. Use the platform's own text tool look; never brand fonts.
4. A recurring absurd mascot beats a logo; keep it ugly-funny on purpose.
5. React to news (sport, travel chaos) within 24 h.

## Recipe (real footage + HTML/GSAP, 1080x1920)
- 6-7 s; 1 locked/handheld clip or 5-6 clips of 0.5-1.7 s.
- Label text: `500 56-60px "TikTok Sans"/"Proxima Nova"; color:#fff; -webkit-text-stroke:2px #000; paint-order:stroke fill`, top at y 270-340 px; block reveals with `tl.set` at the punch line time.
- Word captions for VO: `800 100px Montserrat uppercase, text-shadow 0 4px 0 rgba(0,0,0,.6)` at y 1500 px, 1-2 words per card.
- Mascot face PNG layered on product photo; 0.4 s face sting as the last shot; music hit or 0.15 s silence on the punch line.
