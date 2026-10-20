# Around the world in 24 races with Sky Sports F1  (Sky Sports, uploaded 2024-02-21, 40.0 s, 16:9 with ≈2.4:1 letterbox, YouTube / Sky Sports channel)
URL: https://www.youtube.com/watch?v=HYrH70o8I8U
Purpose: season-launch promo (:40) for the channel's F1 coverage, ending on a start date
One-sentence point: the season is a trip around the world, one city after another, and it starts on the named date on this channel.

Structure (times from metrics.json):
- 0.0–1.6 HOOK: sunrise over a desert city skyline; the channel logo sits small in the sky (≈1.0–1.6 s).
- 1.6–9.4 PADDOCK: celebrities and drivers in the paddock, cockpit details, an exhaust flame; 0.4–0.8 s shots.
- 9.4–32.0 THE TOUR: one city per beat, in season order: aerial of a harbour circuit, tunnel, a neon-lit city, then the race's place name written in giant 3D letters INTO the location (on the tarmac, along the pit wall, on a run-off area: "LAS VEGAS", "SINGAPORE", "BELGIUM", a circuit name on a bridge). Fans, pit stop top-down, flags; 0.5–1.2 s shots, 9–12 cuts per 10 s.
- 32.0–37.4 FINALE: one 5.3 s shot: night-race cars on the grid, fireworks; the title "AROUND THE WORLD IN 24 RACES" appears over it (≈35.5–37.3 s).
- 37.4–39.0 DATE CARD: channel logo + "SEASON STARTS <date>" on a blue haze.
- 39.0–40.0 CORPORATE CARD: white card, parent-brand gradient logo + slogan; 0.7 s silence at the end.

Cut rhythm: 43 shots in 40.0 s, ASL 0.93 s, median 0.80 s, 74 % under 1 s, 65 shots/min. ASL per quarter 0.77 / 0.77 / 0.71 / 1.67 (the finale). Cuts on onsets 33 % vs 19 % chance: cut on the music. Adaptive detector; 2 scene-only candidates (27.72/27.84) were a flash inside one shot.

Typography:
- Place names: giant extruded sans caps rendered into the scene in perspective (ground or wall), white or the surface colour, 25–40 % of frame width; they are part of the shot, not overlays. Closest free: Archivo Black / Montserrat 900 extruded in 3D.
- Title: wide italic sans caps, white with a metallic gradient, cap ≈9 % of frame height, small "THE" and "IN" set between words at ≈35 % size, two lines centred in the upper half. Closest free: Exo 2 700 Italic or Saira Semi Condensed 700 Italic.
- Date card: logo ≈8 % H centred, date line small caps ≈1.5 % H below.
- No driver names, no team names, no race dates beyond the start date.

Colour/grade: cinematic: warm sunrise open, cool steel-blue for the tour, neon at night races; contrast high, blacks deep; letterbox bars ≈12.5 % top and bottom (≈2.4:1) until the date card.

Camera/shots: drone aerials over host cities, onboard and low trackside shots with motion blur, top-down pit stop, paddock celebrity close-ups (handheld), fireworks wide.

Transitions: hard cuts, many with motion blur (speed ramps and whip pans); one flash; the place-name type is revealed by the camera move itself.

Sound: music-driven, broadcast-level: integrated −23.0 LUFS (the EU broadcast target), LRA 2.8 LU, true peak −12.2 dBTP; momentary −20 to −25 throughout, loudest 0.5 s at 34.7 s under the finale/title, one rise at 4.2 s. I did not listen (no claim about voice).

What makes it premium:
- The data (24 races) is the creative idea and the title: the edit IS the calendar, in order.
- Type lives inside the world: place names are built into the locations, not stuck on top.
- Letterbox + cinematic grade make a channel promo feel like a film trailer.
- Three end cards in 2.6 s, each with one job: title, date + channel, parent brand.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- Footage: one aerial or iconic shot per destination (licensed drone/city plates), plus speed shots (onboard, trackside blur) and crowd. 0.5–1.2 s each, cut on onsets; one 5 s hero at ≈80 %.
- Place names in the scene: a CSS 3D plane matched to the ground (`transform: perspective(900px) rotateX(70deg) rotateZ(-12deg)`), text Archivo Black caps 260 px, `color: rgba(255,255,255,.85)`, `mix-blend-mode: overlay`, slow drift matching the camera (`y +4%` over the shot). For real tracking use a corner-pinned plate from your NLE.
- Letterbox: two black bars 135 px tall (1080 frame) on top of everything until the date card.
- Title: Exo 2 700 Italic caps 96 px (cap ≈9 % H), metallic `linear-gradient(180deg,#fff,#b8c0cc)` text fill; "THE"/"IN" 34 px; fade + `y 12px→0` 0.4 s `power2.out` over the fireworks shot.
- End: logo card 1.6 s with date, then a white corporate card 1 s, 0.7 s silence.
- Stock queries: "desert city skyline sunrise drone", "race car onboard motion blur", "city circuit night aerial", "pit stop top down", "fireworks stadium night", "motorsport fans flags".
