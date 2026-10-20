# No one upstages the Grand Tour of Switzerland  (Switzerland Tourism, 12 Apr 2022, 2:10 / 130.0 s, 16:9 frame with ≈2.35:1 picture, YouTube)
URL: https://www.youtube.com/watch?v=IyhpSZBuYoE
Purpose: tourism campaign film with two stars (the ambassador and a Hollywood actress), second film of the "No Drama" series
One-sentence point: in a screening of the road-trip film, the actress fights to be the star, but the Swiss scenery upstages her every time.

Structure (cut times from metrics.json, text times from the sheet):
- 0–2.12 cold open on an aerial of a castle in green mountains (it is the film-in-the-film).
- 2.12–12.4 the screening room: the two stars in cinema seats, the film on a big screen (green valley, lake, mountain pass), the road-trip badge appears over a serpentine road at ≈12.2.
- 12.4–22.3 one 9.8 s continuous dolly past the director and producer to the two stars.
- 22.3–75 argument intercut with the "film": a director's monitor, a glacier aerial, a mountain hotel, a lake village. ASL ≈1.7 s in the second quarter (the densest: 6 cuts / 10 s at 40–60 s).
- 75–101 the actress pitches her own ideas (lake, fjord-like valley); the editor and the director react.
- 101.16–116.56 one 15.4 s walk-and-talk oner down a white corridor; screens on the wall show more scenery (lake, waterfall).
- 116.56–118.44 the punchline shot.
- 118.44–130.0 end block on aerials joined by dissolves (falls, mountain road, badge, a lake city): tagline card 1 ≈123.6–125.0 "When you need an ...", card 2 ≈125.6–127.9 "You need Switzerland.", logo + hashtag + URL ≈128–130.

Cut rhythm: 42 shots, ASL 3.10 s, median 1.92 s, 9.5 % under 1 s, 33 % over 3 s, 19.4 shots/min. ASL per quarter 3.25 · 1.71 · 2.71 · 8.13: fast middle, two long oners and a dissolve montage at the end. Longest: 15.4 s corridor oner, 11.6 s end block (dissolves counted as one shot), 9.8 s dolly. Shortest 0.84–0.96 s. The scene detector found only 18 cuts in this dark footage vs 41 with the adaptive one; I checked the two long shots with a low threshold (0.08) and they contain no hidden cuts. Cuts on onsets 49 % vs 47 % chance.

Typography:
- Same end system as "No Drama": soft bold serif, sentence case, white, two centred lines (cap ≈6 % of the 16:9 frame), then one-line promise, then the red flower logo centred with hashtag and URL.
- Road-trip badge: red shield with a white road "S", ≈12 % H, centred over a serpentine road aerial (2 s).
- No subtitles, no name supers.

Colour/grade: cinematic letterbox ≈2.35:1 (bars 58 px of 480 = 12 % each). Screening room: dark wood, warm practicals, faces lit low-key; the film-in-the-film: bright, saturated summer greens and turquoise lakes; corridor: high-key white. The contrast dark room / bright screen is the device.

Camera/shots: slow dolly and steadicam in the screening room, a walk-and-talk oner, reaction close-ups, drone aerials as "the film". The scenery is shown full-frame when it is "on the screen".

Transitions: hard cuts in the story; dissolves (≈1–2 s) only in the end montage (soft candidates at 120.6, 122.8, 124.7).

Sound: dialogue comedy with score. Integrated −14.6 LUFS, LRA 8.2 LU, true peak +0.1 dBTP. One 0.85 s drop-out at 14.85 (in the room, before a line). Biggest rises +29 to +33 dB at 48.4 and 88.3 (scenery music entering).

What makes it premium:
- Scenery framed as "the film" inside a cinema: big screen, audience, director. The place is literally the star.
- Long, confident takes (9.8 s dolly, 15.4 s oner) inside a 2-minute ad.
- Letterbox and low-key room light read as cinema, not tourism.
- Same tagline system across the campaign.

Recipe (Hyperframes + real footage):
- Letterbox 2.35:1: bars 131 px on 1080p.
- Two layers of picture: "room" shots (dark, warm, 2–4 s) and "screen" shots (bright aerials, 1.5–3 s); 1 in 3 room shots shows the screen in frame.
- Allow 1–2 oners of 10–15 s for the comedy beats.
- End: 11 s aerial montage with 1.2 s cross-dissolves (`tl.to(next,{opacity:1,duration:1.2,ease:"sine.inOut"})`), tagline cards as in no-drama.
