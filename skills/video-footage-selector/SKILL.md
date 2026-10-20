---
name: video-footage-selector
description: Finds and selects moving footage (stock video, own rushes, archive clips) for each shot of a video — searches free and paid libraries for real, non-AI, at least 1080p (prefer 4K) clips, runs an automatic quality gate (resolution, bitrate, interlacing, sharpness, shake, watermark), checks meaning by eye, sets in/out points and logs licences. Use it whenever a video needs B-roll, stock footage, "a clip of X", or someone complains footage looks cheap, soft, AI-made or off-topic.
---

# Video footage selector

Load the `professional-video-editing` skill: read `references/stock-sourcing.md` and `references/selecting-images-and-sound.md`; tools `scripts/stock_find.mjs`, `scripts/stock_qc.py`, `scripts/select_media.py`.

## Steps per moving shot (from `script.md`)
1. **Shot spec:** purpose, length, framing, camera move, light, frame rate of the project.
2. **Queries:** 3–5 per shot, literal (subject + action + framing + move + light), plus synonyms. Search what is *in* the picture.
3. **Search + gate:** `node stock_find.mjs "<query>" --n 8 --out <dir>` (Pexels, Pixabay, Mixkit, Commons, keyless; drops < 1080p, vertical, AI-labelled, restricted; runs `stock_qc.py`; ranked MANIFEST with licence lines). Paid libraries by hand, then `stock_qc.py` on the file.
4. **Compare at the real use:** `select_media.py clip1.mp4 clip2.mp4 --at <sec> --frame 1920x1080 --sheet footage_<shot>.jpg` (add `@x,y,w,h` when you reframe, e.g. for 9:16).
5. **Watch every pick** full length at 100 %: meaning, AI artefacts, watermarks, logos, faces, the exact usable seconds (stock often starts or ends on a bump).
6. **Choose + runner-up**, set in/out.

## Output (`selects/footage.md`)
`| shot | file | in | out | verdict | why | runner-up | source page | author | licence | AI checked | logos/people checked |`

## Rules
- Real footage for real claims; a technically perfect clip of the wrong thing is a REJECT (a gamepad is not an e-stop).
- One frame rate for the film; no interlaced clips; prefer 4K for reframing.
- Proof shots of a product are never stock: say "needs filming" and give a 3–5 shot list (wide, medium, detail, action, reaction).
