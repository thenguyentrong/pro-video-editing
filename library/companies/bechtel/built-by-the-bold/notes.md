# Built by the Bold  (Bechtel, 2026-07-02, 4:03, 16:9, YouTube, official Bechtel Corporation channel)
URL: https://www.youtube.com/watch?v=Lr06WP4DRpg
Purpose: brand anthem / heritage-to-today corporate film (company identity, recruiting and client audience)
One-sentence point: The same boldness that built Bechtel's historic megaprojects is building today's energy, chips, minerals, defence and transport projects, and it lives in its people.

## Structure (243.0 s)
- 0-41 (0-17 %) heritage: sepia/B&W archive photos inside a rounded vintage slide frame on black, slow push-ins, one photo every ≈3 s, narrator VO about people who saw possibility in canyons, coasts and deserts.
- 41-57 (17-23 %) bridge: colour portraits of workers in hard hats (still frames with quick push), a 0.17-0.25 s flash run at 53-55 s, then a 1.9 s black hold.
- 57-78 (23-32 %) three firsts: archive film of a desert pipeline + word slam "VISIONARY"; tunnel boring under the sea + "PIONEERING"; waste vitrification + "BOLD". Each word fills the frame width, white on the picture, inside a white border. 1.25 s black hold after.
- 78-99 (32-41 %) the turn to today: four employees (office, glass walls, Bechtel neon logo) speak straight to camera, sharing the narration line by line.
- 99-141 (41-58 %) energy + industry: solar fields, LNG trains, nuclear, chip fab interior, pharma, mines (copper/lithium/aluminium), ships, cranes. Mostly drone; some shown as a smaller window inside black that grows to full frame. 1.9 s black hold at 141.6 s.
- 143-157 (59-65 %) the four employees again, one word each ("Groundbreaking. Critical. Massive.").
- 157-184 (65-76 %) security + connection: missile defence, submarine yard, hazardous-waste crew in yellow suits, rail tunnels, airports, motorways; macro of train wheels. 1.1 s black hold at 184.3 s.
- 185-214 (76-88 %) people: employees again, then hard-hat workers on site in quick portraits, then an accelerating flash montage of archive and people photos (17 + 22 cuts in 200-220 s, shots 0.2 s).
- 214-238.5 (88-98 %) one continuous take (24.1 s): the employees walk towards camera through the office and end side by side, saying the last line together.
- 238.5-243 (98-100 %) Bechtel logo on white with URL.

## Cut rhythm (7 archive-photo cuts added from the adaptive detector)
- 150 shots, ASL 1.62 s, median 1.25 s, 34 % under 1 s, 37 shots/min. ASL per quarter 1.96 / 1.84 / 1.52 / 1.24 s - the film accelerates to the end.
- Longest: 24.1 s final walk-and-talk, 5.4 s first archive photo, 4.8 s archive film. Shortest 0.13-0.17 s (flash runs).
- Archive photos ≈3 s each; today's b-roll 1-2 s; flash montages 0.2 s; final single take 24 s.
- Four black holds of 1.1-1.9 s are the chapter breaks (55.2, 76.6, 141.6, 184.3 s).

## Typography
- Word slams: one word per shot, ultra-bold neo-grotesk caps (Helvetica/Open Sans ExtraBold look; free: Inter 900 or Archivo Black), white, centred, filling ≈90 % of the frame width: VISIONARY cap height ≈15.6 % H, BOLD ≈40 % H. The picture sits inside a white border (≈4 % inset), so the whole frame reads like a print poster.
- No supers, no names, no captions; the employees are unnamed.
- End card: red/white Bechtel ring logo ≈20 % H centred on white, URL small below.

## Colour/grade
- Archive: sepia and B&W with vignette, film dust, rounded slide frame. Today: clean, saturated corporate daylight, teal office with glass, warm sunsets on sites. Black between chapters.

## Camera/shots
- Archive photos with digital push-ins; archive 16 mm film.
- Today: drone wides of plants, solar, ports, motorways; slider inside a chip fab; macro machinery; window-in-black framing for some project shots.
- Employees: medium shots to camera (direct address), shallow depth, glass office, neon logo behind; the finale is a backward-tracking gimbal shot of 3 walking people.
- PPE on all site workers (hard hats, hi-vis, glasses, yellow hazmat suits).

## Transitions
- Hard cuts, dissolves between archive photos, four cuts to black (1.1-1.9 s) as chapter breaks, window-to-full-frame grows, white-border frames on the word slams, flash montages before the finale.

## Sound
- Narrator VO + employee voices + orchestral/cinematic track; integrated -13.9 LUFS, LRA 7.7 LU, true peak +0.5 dBTP.
- Biggest hits on the word slams and section starts (rises +32 dB at 38.5 s, +24 dB at 50.3, 120.4, 164.6 s). Drop-outs 0.3 s at 233.1 s and 0.6 s at 234.0 s right before the last words, then the music button under the logo.

## What makes it premium
- A clear three-act time line: past (archive) - present (projects) - people (faces), with black holds as chapter breaks.
- Heritage proof: each historic first is named with one giant word.
- Real employees as narrators (direct address) instead of a voice from nowhere.
- Pace rises from 2.0 s to 1.2 s ASL, then releases into one 24 s take.

## Recipe (real footage + HTML/GSAP)
- Archive: `<div class="slide">` 44vw × 88vh, `border-radius:2vh; box-shadow:0 0 6vh rgba(0,0,0,.8); filter:sepia(.5) contrast(1.1)` on black; push `scale 1 -> 1.06` over 3 s; cross-fade 0.5 s between photos.
- Word slam: `h1{font:900 22vh/0.9 Inter; text-transform:uppercase; color:#fff; width:90vw; text-align:center}` fitted per word with `font-size` to 90vw; white frame `outline:4vh solid #fff; outline-offset:-4vh`. `tl.from(h1,{scale:1.15,autoAlpha:0,duration:.25,ease:'power3.out'})` on the music hit, hold 1.5-2 s.
- Chapter break: 1.2-1.9 s of pure black with the music tail.
- Window grow: `clip-path: inset(15% 10%)` -> `inset(0%)` over 1.2 s `power2.inOut`.
- Finale: one 20-25 s backward gimbal move of the team walking to camera, last line together; logo on white 4-5 s.
