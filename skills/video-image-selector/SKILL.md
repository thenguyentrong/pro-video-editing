---
name: video-image-selector
description: Finds and selects the still images for a video — photos of real products, people and places, document and headline captures, archive images — and proves each pick is sharp enough at its real on-screen crop, clean in the background, right in meaning and licensed. Use it whenever a video needs photos, screenshots, headlines, documents or "the best image of X", and whenever someone says an image looks low-res, blurry, cheap or has a bad background.
---

# Video image selector

Load the `professional-video-editing` skill: read `references/selecting-images-and-sound.md` and `references/stock-sourcing.md`; the tool is `scripts/select_media.py`.

## Steps per image shot (from `script.md`)
1. **Gather 5–10 candidates.** Own photos first; then Wikimedia Commons (API, check licence per file), Unsplash/Pexels, official press kits (licence!), NASA/EU archives. Download originals, never thumbnails or old exports.
2. **Documents and headlines:** never upscale a screenshot. Re-capture the page with a headless browser at 2–3× device scale, crop to the key line(s); for 9:16 re-wrap the text into a narrow column (narrow viewport) so it stays large. Remove banners and ads. Note publication + date for the on-screen source line.
3. **Decide the real use:** frame size, the crop that will be on screen (subject fills it), the largest push-in.
4. **Gate:** `python select_media.py a.jpg@x,y,w,h b.jpg ... --frame 1920x1080 --zoom 1.08 --look dark --sheet images_<shot>.jpg`. Upscale ≤ 1.0 for heroes (never > 1.15), sharp ≥ 40 at output size, no busy or loud-colour background behind the subject.
5. **Look at the sheet for meaning:** is it the right thing, does it say the line, does it fit the film's world? The script measures technique only.
6. **Pick + runner-up**, with the crop box, and write why.

## Output (`selects/images.md`)
`| shot | file | crop box | verdict | why chosen | runner-up | source URL | author | licence | credit line |`

## Rules
- The opener and end card get the best image. If the only image of a subject is weak, use it small, short or behind type — or ask for a photo to be taken.
- Burst photos of one scene are for choosing the cleanest frame, not for fake motion.
- No AI images for real things; no third-party logos you can't use; CC BY needs an on-screen or end credit.
