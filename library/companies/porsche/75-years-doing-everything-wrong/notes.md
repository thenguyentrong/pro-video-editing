# Porsche | 75 Years of Doing Everything Wrong  (Porsche, 2026-03-24, 2:26, 16:9, YouTube @Porsche)
URL: https://www.youtube.com/watch?v=yXND4eExf-w
Purpose: brand film (heritage anthem, made mostly from archive and earlier campaign footage)
One-sentence point: Every time the world said "that's how it's done", Porsche did the opposite - and that is the right thing to do.

## Structure (cut list + English captions)
- 0.0-15.2 hook: ONE shot, 15.2 s. Black, a red tail-light bar fades up (1 s), then a GT3 RS silhouette against a red sunset (3-15 s). Text left "FOR OVER 75 YEARS" (fades in ~7 s), right "WE'VE DONE EVERYTHING WRONG." (~12 s). VO: "For over 75 years, we've done everything wrong."
- 15.2-32: archive on black - small photo/film windows (each ~11 % of frame width) float on a black field, 1-3 side by side like a contact strip (16-28 s): early 911, crest, 356 with engine in the back, Le Mans. VO "When they said engines go in the front, we put them in the back... ignition on the left..." Then full-frame B&W race film (30-31 s).
- 32-60: product chapters as the VO argues: Cayenne ("A real sports car can't have four doors", 2002 archive at 38 s), off-road in dust and snow (Dakar/rally footage 43-55 s), Taycan/Mission E ("You can't build fully electric sports cars - we built the Taycan", 50 s), CGI/sim cockpit with a G-FORCE HUD (59 s).
- 60-90 "Luxury is for the few, they said - until we built the biggest car community": Porsche design house on a lake, fans, festival from a drone (70 s), triptych windows again (72-73 s), aerial road from drone (74-78 s), a lightning storm, a speedo at 157 (87 s).
- 90-131 build: "Times are tough... we pushed the pedal instead. Never stopping." Track, 911 Turbo badge, eye macro (105 s), old and new 911s side by side, Le Mans, podium champagne (127-128 s). 10-16 cuts per 10 s here (densest 100-110 s, 16 cuts).
- 131.9-142.8: black (10.9 s held): "IT IS JUST THE RIGHT THING TO DO." (132.5-135.5 s, fades), then PORSCHE wordmark (137-140 s). VO 126.5-137.9: "So, if being us means being wrong, it is just the right thing to do. Porsche. There is no substitute."
- 142.8-145.8: legal WLTP text (3 s).

## Cut rhythm
- 92 shots in 146 s. ASL 1.59 s, median 0.78 s. ASL per quarter 6.08 / 1.52 / 0.96 / 1.35 s (slow 15 s open, then very fast).
- Longest 15.16 s (the opening silhouette), 11.36 s (15.16 - the archive-windows sequence, counted as one "shot" because the black field stays), 10.92 s (end text on black), 9.36 s. Shortest 0.12 s, 0.24 s (flash cuts in the 100-130 s build).
- 60 % under 1 s, 13 % over 3 s. One black flash (<0.5 s) at 38.2 s.
- Beat sync near chance (26 % vs 22 %): cut to the VO argument, with flash cuts on accents.

## Typography
- Porsche Next Semibold (closest free: Inter SemiBold), ALL CAPS, white, small: cap height ~2.3 % of frame height.
- Opening: two lines flank the car at the height of the light bar (y 50 %), left block x 9-24 %, right block x 71-97 %. The text uses the light bar as its baseline - layout tied to the product.
- End: "IT IS JUST THE RIGHT THING TO DO." centred, 2.3 % height, 26 % frame width, fade in ~0.5 s, hold ~2.5 s, fade out. Then the wordmark (42 % width, 5 % height, centred) ~3 s.
- 4-6 words per card; long holds (3-7 s).

## Colour/grade
- Mixed sources on purpose: B&W archive with scratches, faded 2000s video, glossy modern campaign footage, CGI. The black frame and the VO hold it together.
- Opening and end are the "designed" parts: red/black silhouette, then pure black.

## Camera/shots
- Re-used footage from 75 years: archive film, rally, studio, drone aerials, cockpit inserts, macro eye. Probably several shots are CGI renders (Mission concept at 56-57 s, G-FORCE HUD at 59 s) - a guess from the look.
- New footage seems limited to the opening silhouette.

## Transitions
- Hard cuts. The "windows on black" device is the main transition into the archive section: frames appear one after the other inside the black field, slide/grow, and the last one fills the frame (29-30 s).
- Fades only on the end text.

## Sound
- Male VO with a confident, slightly ironic tone; music builds steadily. Integrated -14.1 LUFS, loudest 0.5 s at 131.35 s (-11.0 dBFS) = the last montage shot before the black.
- Hit at 134.6 s (+29 dB rise) on "the right thing to do" card; 138.05 s on the wordmark.

## What makes it premium
- A long, still, perfectly designed first shot (15 s) earns the fast archive montage after it.
- The argument structure "When they said X, we did Y" turns heritage footage into a story.
- Text uses the product's own lines (tail-light bar) as layout grid.
- Ends on 11 s of black with only two cards - confidence.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Opening: one slow 12-15 s hero shot (silhouette against a gradient sky). Two caps labels `font: 600 2.3vh Inter; letter-spacing: .02em; color:#fff` placed at the y of a strong product line; `tl.fromTo(left,{autoAlpha:0},{autoAlpha:1,duration:.8},6).fromTo(right,{autoAlpha:0},{autoAlpha:1,duration:.8},11)`.
- Archive windows: black stage; `<div class="win">` 11vw x 6.2vw each, `top: 50%`, appear with `gsap.from(win, {autoAlpha:0, scale:.96, duration:.25})` one per VO phrase; 1-3 visible; the last one `gsap.to(win, {width:'100vw', height:'100vh', left:0, top:0, duration:.6, ease:'expo.inOut'})` to go full frame.
- Build: 0.3-0.8 s shots, a few 0.12 s flash frames on accents.
- End: 10 s of black: caps line (fade .5 s, hold 2.5 s), 1.5 s empty, logo (hold 3 s), legal 3 s.
- For a startup: "When they said robots can't work on a real site, we ..." - the device works for any category disruptor.
