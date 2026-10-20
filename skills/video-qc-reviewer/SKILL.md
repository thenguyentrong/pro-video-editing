---
name: video-qc-reviewer
description: Reviews a rendered video with fresh eyes before anyone sees it — ten-frame still test, story test, measured rhythm vs the chosen style, image quality of the opener and every hero shot, sound and loudness, safe zones, captions, licences and honesty of every claim — and returns a pass/fail list with the role that must fix each problem. Use it after every render, before publishing, and whenever someone asks "is this good", "review my video" or "why does this look cheap".
---

# Video QC reviewer

Load the `professional-video-editing` skill: `references/qc.md`, the chosen style file; tools `scripts/analyze_video.py`, `scripts/select_media.py`, `scripts/loudness.sh`.

## Steps (on the rendered file, never the project)
1. **Ten-frame test:** grab 10 frames at random times; would each pass as a still from a real film of this style? Any slide, web page or template look fails.
2. **First and last frame:** is the opener the sharpest, cleanest image of its subject (`select_media.py` on a grabbed frame and on the source crop)? End card holds ≥ 2–3 s.
3. **Story test:** read voice + on-screen text only; does each line follow ("so / but / that's why")? Can you say the one sentence?
4. **Numbers:** `python analyze_video.py film.mp4 --out qc/` → ASL, % < 1 s, density curve, silences, LUFS vs the style's Numbers table.
5. **Sound:** voice clear on a phone speaker; music 10–15 dB under; loudness at the style's target (default −14 LUFS), true peak ≤ −1 dBTP (`loudness.sh measure`); no clicks; mono check.
6. **Picture/delivery:** muted test with captions, safe zones (9:16 must-read text: not in the top 14 %, the bottom 35 % or 6 % at each side), no unplanned black frames, one grade, correct file name and specs.
7. **Honesty + licences:** every claim matches its on-screen source; speed changes labelled; promises labelled; every file in the licence log; synthetic voice labelled.

## Output (`qc.md`)
`| check | pass/fail | evidence (time, frame, number) | fix | owner role |` — owners: script writer, image selector, footage selector, music selector, voice producer, sound designer, editor. End with the top 3 fixes in order.
