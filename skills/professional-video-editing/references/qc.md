# QC before anyone sees the film

Check the rendered file, not the composition.

## 1. Ten-frame test
Grab 10 frames at random times (`ffmpeg -ss T -i film.mp4 -frames:v 1 qc_T.jpg`) and judge each as a still.
- Would it pass as a frame from a real trailer, an Apple film, a documentary, a broadcast promo (whichever style you chose)?
- Does any frame look like a slide, a web page, a template, a dashboard? Fix that shot.
- Is the text composed into the image (negative space, thirds, safe zones) or stamped on top?

Then check the selects: is the opener the sharpest, cleanest image you have of its subject (`scripts/select_media.py` on the final crop)? A soft or cluttered first frame sinks the whole film.

## 2. Story test
Read only the voice and on-screen text, top to bottom. Does each line follow from the last ("so", "but", "that's why")? Can a stranger repeat the one-sentence point after one viewing?

## 3. Restraint count
- On-screen words at any moment ≤ ~6 (title cards excepted).
- One accent colour, used ≤ 2–3 times.
- Heavy display type ≤ 2 times (title, end card) unless the style is built on it (social meme, sports package).
- Every effect other than a hard cut has a reason you can say out loud.
- One big hit. At most one or two drop-outs.

## 4. Numbers vs the style file
Run `python scripts/analyze_video.py film.mp4 --out qc/` and compare ASL, % shots < 1 s, where the cut density peaks, silences and LUFS with the style's Numbers table. A trailer whose densest part sits in the last 10 % or an Apple-style film with a 3 s drop-out in the middle is off-style (a silent logo hold at the end is fine).

## 5. Sound
- Voice clear at arm's length on a phone speaker; music 10–15 dB under the voice.
- No clicks at edits; room tone under every scene.
- Integrated loudness at the style file's target (default −14 LUFS for web/social), true peak ≤ −1 dBTP (`ffmpeg -i film.mp4 -af ebur128=peak=true -f null -`). Broadcast deliveries follow the broadcaster's spec (EBU R128 = −23 LUFS).
- Check in mono.

## 6. Picture and delivery
- Muted test: does the film still make sense with sound off (captions)?
- Safe zones: titles inside 90 %, important text inside 80 %; for 9:16 see `styles/social-vertical.md` (strict zone for must-read text: nothing in the top 14 %, the bottom 35 % or 6 % at each side; it also shows where brands actually place captions).
- No black frames or flashes you did not plan; first frame = poster.
- One grade: shots from different cameras match in exposure, white balance and contrast.
- End card holds ≥ 2–3 s.
- File named `<Project>_<Title>_<ratio>_v<NN>.mp4`; H.264 High, 1080p or 4K, AAC 48 kHz.

## 7. Honesty
Every claim on screen matches its source on screen. Speed changes and edits in demos are labelled. Licences logged. Internal-only material flagged. A synthetic voice is labelled as a guide until the client approves it.
