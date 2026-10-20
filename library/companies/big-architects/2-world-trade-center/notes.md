# 2 World Trade Center in New York City, a BIG design, Squint/Opera production  (BIG – Bjarke Ingels Group, 14 Dec 2015, 3:00 / 180.2 s, 16:9, YouTube; only 360p available)
URL: https://www.youtube.com/watch?v=aR28ZmqumKk
Purpose: architecture project film (design reveal for a tower), architect as on-camera presenter, CG by a visualisation studio
One-sentence point: the tower is a stack of boxes that joins the old low-rise city and the new towers, explained by the architect on the street and then shown finished in photoreal CG.

Structure (cut times from metrics.json, text from the sheet):
- 0–1 black; 1–17.96 film-style opening credits over live-action New York: client logos (≈2–6.5), architect's logo (≈8–9.5), developer (≈12–14), "Directed By" + studio logo (≈15.5–17.9). Each over its own shot (skyline from the river, the memorial pools, crowds).
- 18–43 the context: the architect walks the streets (low wide angles), on a rooftop, under the towers; low-rise brick next to glass. ASL ≈3.4 s.
- 43–66 the idea on location: CG wireframe boxes stack up in the real street behind the talking architect (composited, white line + glow), the massing grows box by box; long takes (10.8 s at 45.9).
- 66–131 the building in photoreal CG: plaza, lobby, big atrium stairs, a TV studio floor, terraces with trees, offices with staff, a cinema logo wall; human scale everywhere. ASL ≈4.5 s.
- 131–168 the city with the tower: aerials, dusk skyline from the bridge, the tower lit at night.
- 168.12–180.2 diagram coda (12.1 s on black): white boxes stack into the tower, then the silhouette alone; sound out from 176.8.

Cut rhythm: 44 shots, ASL 4.10 s, median 3.72 s, 4.5 % under 1 s, 68 % over 3 s, 14.6 shots/min. ASL per quarter 3.75 · 4.51 · 3.75 · 3.47. Longest 12.1 s (diagram coda), 10.8 s (massing on location), 8.2 s. Shortest 0.72–0.76 s (two quick inserts at 136.8). Densest 130–140 s (5 cuts / 10 s). Cuts on onsets 26 % vs 24 % chance.

Typography:
- Credits as in a feature film: small "Directed By" in a clean sans (≈3.3 % H, sentence/title case) above the company logo (≈6 % H), centred, white, over live footage; the client and studio logos are shown as logos, not as typed names.
- No captions, no lower thirds, no project data on screen; the architect is never named in a super.

Colour/grade: soft, slightly desaturated New York daylight with cool shadows and lifted blacks; the CG matches it (overcast blue sky, warm interior wood). Dusk ending warm. 360p source, so grain cannot be judged.

Camera/shots: very wide lenses at low angles on the architect (he gestures into the lens), handheld walk-and-talk, rooftop wides, CG camera moves that behave like steadicam and drone (slow push, rise, orbit), a few top-down CG views of the city.

Transitions: hard cuts; the CG massing grows inside a live shot (compositing as the transition from idea to building); one dip at 77.2.

Sound: the architect's voice to camera and as VO in the CG part, over a building score. Integrated −17.4 LUFS, LRA 18.4 LU (wide: quiet voice passages, loud music swells), true peak +1.1 dBTP. Silences at 0–0.8, 93.1–94.7 (a pause in the CG section) and 176.8–180.2. Biggest rises +17 to +20 dB at 138.4–148.4 (music swell under the city aerials).

What makes it premium:
- The idea is shown where it lives: CG boxes stacked into a real street behind the architect.
- The film opens like a movie (credits over the city) and ends like a diagram (boxes on black): story first, logic last.
- Long CG takes with human life in every frame.

Recipe (Hyperframes + real footage + CG or 3D renders):
- 0–18 s: four 3.5–4.5 s live shots with centred credits (role 30 px ≈3 % H over a 60–70 px logo or name), opacity 0.6 s in / 0.6 s out.
- Presenter shots: 16–20 mm look, low angle, subject on the right third, idea overlay on the left (white 2 px lines, `filter: drop-shadow(0 0 6px #fff)`), boxes appear one by one every 0.5–0.8 s.
- CG section: 4–6 s per move, slow ease (`power1.inOut`), people in every frame.
- Coda: 10–12 s on black, white boxes stack (`stagger 0.25 s`, `y:+40→0`, `opacity 0→1`), end in silence.
