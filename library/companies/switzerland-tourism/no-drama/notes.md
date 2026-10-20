# No Drama.  (Switzerland Tourism, 4 May 2021, 1:31 / 90.5 s, 16:9 full frame, YouTube)
URL: https://www.youtube.com/watch?v=wXcBGfXXL4w
Purpose: tourism campaign film with two stars (a tennis legend as brand ambassador and a Hollywood actor)
One-sentence point: the actor refuses the ambassador's Swiss film because it has no drama, which is exactly the selling point: a holiday without drama.

Structure (cut times from metrics.json; text times from the sheet, exact labels):
- 0–4.24 cold open: the actor alone in a dark loft at a laptop (4.2 s hold).
- 4.24–8.0 the "mood film" on the laptop: a kitsch postcard title over a castle on a lake, then snow scenery.
- 8.0–22 the call: phone ringing, the ambassador in a bright chalet with a Matterhorn view, the video call starts.
- 22–60 the pitch and the argument: scenery played on the laptop screen (lake, castle, vineyard, fountain) intercut with the two men on their phones. ASL ≈1.6 s.
- 60–72 the "too perfect" montage: aerials of peaks, snow, a ski hut, paragliders, cows on the laptop.
- 72–81.3 the turn: the actor declines, the ambassador on the balcony accepts with a smile.
- 81.32–90.5 one 9.2 s aerial plate (peaks above a sea of fog at sunrise) carrying the end block: tagline card 1 (≈82.0–84.9), tagline card 2 (≈85.0–87.9), logo + hashtag + URL (≈88.0–90.5).

Cut rhythm: 54 shots, ASL 1.68 s, median 1.32 s, 24 % under 1 s, 5.6 % over 3 s, 35.8 shots/min. ASL per quarter 1.41 · 2.06 · 1.19 · 2.06 (the last quarter is lifted by the 9.2 s end plate). Densest at 60–70 s (9 cuts / 10 s) in the scenery montage. Longest: 9.18 s end plate, 4.44 s (21.96), 4.24 s cold open. Shortest 0.64–0.76 s. Cuts on onsets 38 % vs 37 % chance: cut on dialogue and reactions, not on music.

Typography:
- No text inside the story except the laptop "mood film" title (a parody of postcard script, not the brand type).
- End taglines: soft, bold serif with ball terminals, sentence case, white, centred, two lines; cap height ≈28 px of 480 (≈6 % H); line spacing ≈1.1. Closest free font: Fraunces 700 (soft) or Young Serif. Two-step copy: "When you need ..." then the brand promise "You need Switzerland." (one line). Each card ≈3 s; hard changes between cards over the same moving plate.
- Logo: red square with a white flower mark and wordmark, centred, ≈20 % of frame height, hashtag and URL small below (≈2 % H).

Colour/grade: two worlds. The actor's loft is dark, cool and contrasty (deep shadows, window light); the ambassador's chalet is golden, warm, sunlit with snowy peaks behind. The scenery on the laptop is saturated postcard colour. End plate: warm sunrise on blue-grey peaks. Clean digital, no grain.

Camera/shots: locked-off and slow dolly coverage of two people in two locations; screen inserts (phone, laptop) as the device that brings scenery into the story; drone aerials only inside the "pitch" and the end plate.

Transitions: hard cuts. The only "soft" moments are camera moves inside shots. Text cards change by hard cut over the same plate.

Sound: dialogue-led comedy with score under it. Integrated −17.4 LUFS, LRA 9.5 LU, true peak −2.5 dBTP. No drop-outs; 0.35 s silence at the very end. Biggest rises (+25 to +28 dB) at 14.8, 24.6, 42.0 and 58.9 s: the ring tone, entries of the scenery music.

What makes it premium:
- The joke is the selling point: "no drama" is the product benefit, said by the man who stands for drama.
- Scenery is never shown as a plain ad: it is always inside the story (on a laptop, a phone, behind the star).
- Two clear lighting worlds (dark loft vs golden chalet) make the contrast visible without words.
- A long, calm end plate (9.2 s) after a busy middle, with a two-step tagline.

Recipe (HTML/GSAP Hyperframes + real footage, 1920×1080):
- Story: star A (the critic) vs star B (the host of the place) on a video call; 4 s cold open on A; scenery appears only on screens or behind B.
- Cut dialogue at ASL ≈1.5 s; scenery montage at ≈1.1 s (9 cuts / 10 s) for 10 s at 65–75 % of the runtime.
- End plate 9 s: slow aerial; card 1 at +0.7 s (2 lines, Fraunces 700, 64 px ≈6 % H, white, centred, `text-shadow:0 2px 12px rgba(0,0,0,.25)`), card 2 at +3.7 s (one line), logo at +6.7 s. Cards hard-switch (`tl.set`).
- Mix dialogue on top, music under at −24…−20 LUFS short-term, master −16 LUFS.
