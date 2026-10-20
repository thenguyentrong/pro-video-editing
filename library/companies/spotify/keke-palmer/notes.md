# Take it from Keke Palmer: never lose who you are in a romantic relationship  (Spotify, 2026-07-23, 61.2 s, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/ea6QABMqCBg
Purpose: podcast clip (video podcast promo, "On Purpose with Jay Shetty")
One-sentence point: A one-minute answer from a celebrity guest about independence in relationships, cut from the video podcast, ending on a "watch on Spotify" card.

Structure: beats with timestamps
- 0.0-1.8 hook: close-up of the guest already mid-answer with a funny comparison; title sticker builds in at 0.1 s.
- 0.1-≈4.5 title sticker (topic) + show tag on screen together with the subtitles.
- 1.8-8.8 wide of guest in the chair, then a 0.75 s cutaway of the host laughing (4.8-5.5 s) as social proof that the line is funny.
- 8.8-59.6 the answer: two long takes on the close-up (16.0 s, then 32.5 s), one 2.3 s wide in between.
- 59.6-61.2 end card: Spotify green, podcast cover tilts in, caps CTA below. Audio is silent under it (1.45 s).

Cut rhythm
- 7 shots, ASL 8.75 s, median 2.96 s, 14 % < 1 s, ≈7 shots/min. Quarters 3.06 / 5.10 / 15.31 / 15.31 s: all the editing is in the first 9 s, then one long take.
- 83 % of cuts on audio onsets (59 % chance): cuts on the start of a sentence.

Typography
- Title sticker: black bold sans on white strip boxes (one box per line, text tight to the box), 2 lines, cap ≈1.9 % H, centred at 53.5-58 % H; show tag white on black with a mic icon at ≈64 % H. Builds in with a horizontal stretch (frame 0.1 s squeezed). Closest free: Inter 800 (title) + Inter Tight 600 (tag).
- Subtitles: white sentence-case sans, cap ≈1.8 % H, 2 lines max, on a dark translucent rounded box (≈rgba(0,0,0,.45)), centred at 68-74 % H; 3-7 words per chunk, switched per phrase. Closest free: Figtree 600.
- End card: cover art ≈34 % W at 24-62 % H, CTA heavy caps black on green, cap ≈2.6 % H, at ≈67 % H.

Colour/grade
- Warm, dim studio with practical lamps and a mustard armchair; teal top; podcast mic branded in shot. End card flat Spotify green (#1ED760).

Camera/shots
- Three-camera podcast: tight single (face + mic), wide single, host reaction. No B-roll.

Transitions
- Hard cuts; the end card cover arrives with a 3D tilt-in (≈0.3 s).

Sound
- Dialogue only, no music; -19.0 LUFS, peak -7.5 dBTP (quiet master). Silence 59.75-61.2 s under the end card.

What makes it premium
- The clip starts mid-sentence on the funniest line; the edit trusts one long answer.
- One reaction cutaway early proves the moment.
- Branded design system: title sticker, show tag, subtitle box and green card are the same on every clip.

Recipe (real footage + HTML/GSAP, 1080x1920)
- Pick a 45-60 s answer that starts with a quotable line. Open on the close-up; 1 wide + 1 host reaction (0.7-1.0 s) inside the first 9 s; then hold the close-up.
- Title: two `.strip{background:#fff;color:#000;font:800 34px Inter;padding:2px 10px}` lines centred at y ≈1030-1110 px, `from {scaleX:0.2}` 0.25 s `power3.out`, out at 4.5 s.
- Subtitles: `600 34px Figtree; color:#fff; background:rgba(0,0,0,.45); border-radius:10px; padding:6px 14px`, centre y ≈1360 px, max 2 lines.
- End card 1.5 s: green `#1ED760`, cover `from {rotationX:25, scale:.9}` 0.3 s, CTA `900 48px` black caps at y ≈1290 px.
