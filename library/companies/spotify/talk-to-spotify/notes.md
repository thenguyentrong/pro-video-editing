# Now you can talk to Spotify  (Spotify, 2026-07-14, 33.2 s, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/Qf-iBP8X7pI
Purpose: feature launch (voice / chat requests in the app), motion-graphics social cut
One-sentence point: Four spoken-style requests (upbeat music for cooking, the meaning of a lyric, slower music for dinner, a play count) each get an instant answer in the app.

Structure: beats with timestamps
- 0.0-1.5 hook: the real app home screen slides up; the prompt bar types "now you can talk to Spotify" (1.5-3.8 s on black).
- 3.8-5.3 kinetic title: the same line as giant mixed-size words that bounce into place.
- 5.3-28.0 four call-and-response pairs, each ≈5-6 s: a full-colour quote card (request, ≈2.3 s) then the answer as glowing app UI with album art (≈2.5-3 s). Colours change per pair: red, violet, magenta, lime.
- 25.0-28.0 montage of many floating request bubbles (the feature is open-ended).
- 28.0-31.6 callback: app home again, prompt bar types the title line (the end repeats the start).
- 31.6-33.2 logo: white Spotify icon on black, ≈1.6 s. Hard end.

Cut rhythm
- Adaptive detector: 10 shots, ASL 3.32 s, median 2.55 s, 0 % < 1 s (scene detector: 8). By eye ≈13 scenes, most joined by liquid morphs that no detector counts as cuts (≈2.5 s each).
- Quarters 2.77 / 2.07 / 2.07 / 4.15 s: steady 2-3 s pulse, slower at the callback and logo.

Typography
- Quote cards: wide, heavy, rounded geometric sans, lowercase sentence case, 4-6 lines, cap ≈3.5-4 % H, centred on 25-80 % H, with giant 3D chrome-ish quote marks above and below. Closest free: Unbounded 700 (or Clash Display-like wides; Unbounded is free).
- Kinetic title: the same face at 4-15 % H per word, letters at different sizes and baselines, bounce in.
- UI text: the app's own UI at native size; answer text white on dark cards.
- No subtitles: the lyrics/VO are music; the cards carry the words.

Colour/grade
- Black base; one saturated flat colour per request card (red #E22134-like, violet #5B2BE0, magenta #A3239C, lime #D7F26B); answer UI glows in the same colour as a neon outline.

Camera/shots
- No live action: screen captures of the product + 2D/3D motion graphics, album art cards in a 3D swirl.

Transitions
- Liquid/blob morph from card to UI (≈0.3-0.5 s), glow outline wraps the next element; one black dip 1.5-3.8 s for the typing bar.

Sound
- One track (rap/club beat with lyric hook) under everything; -12.3 LUFS, peak +1.1 dBTP. Hits +26.6 dB at 22.7 s on the lyric drop.

What makes it premium
- The feature is shown as a rhythm: request card → answer, four times, colour-coded.
- Product UI is the hero and the proof; motion graphics only frame it.
- The ending repeats the opening typing bar, so the loop reads cleanly.

Recipe (HTML/GSAP, 1080x1920)
- 30-34 s: 1.5 s real UI, 2.3 s typed prompt, 1.5 s kinetic title, 4 × (2.3 s quote card + 2.7 s answer UI), 3 s bubble montage, 3.5 s typing-bar callback, 1.6 s logo.
- Quote card: `font: 700 74px Unbounded; color:#E9E3FF; line-height:1.0; text-align:center` on a flat colour; quote marks 260 px, `from {scale:0, rotation:-15}` 0.35 s `back.out(2)`.
- Morph: SVG blob path `morphSVG` from card rect to UI rect in 0.4 s `power3.inOut`; neon outline `filter: drop-shadow(0 0 12px currentColor)`.
- Typing bar: `tl.to(input,{text:"Now you can talk to Spotify", duration:1.6, ease:"none"})` (TextPlugin), ≈17 characters/s.
