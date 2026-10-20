# INTRODUCING Hilti Jaibot - semi-autonomous drilling robot for overhead drilling  (Hilti North America, 2020-10-28, 1:09 incl. 11 s YouTube end screen, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=ytpzbOtNo3w
Purpose: product launch film (first construction robot of a tool brand)
One-sentence point: Hilti turns the BIM data that already plans a building into a robot that drills ceiling holes for MEP installers.

## Structure (content 0-57.4 s; 57.4-68.7 s is a white "like / comment / subscribe" end screen, excluded from the numbers)
- 0.0-9.5 (0-17 %) hook: brand-voice line about striving for change. Low-angle staircase in a raw building, a site manager in hi-vis and red helmet looking out of a window, a worker's boots and a red Hilti case walking past studs, gloved hands on a red tool, a top-down drone shot of a concrete deck with red formwork (two flash shots of 0.42 s and 0.29 s inside it).
- 9.5-16.8 (17-29 %) people: a worker with an exoskeleton walking away into an empty floor, a crew of five in PPE walking towards camera, a manager talking with two workers.
- 16.8-26.7 (29-47 %) the BIM idea: tablet showing a site photo, an engineer at a two-screen BIM workstation, a close-up of the 3D model on screen, a surveyor on a dirt site, a tower under construction (city skyline), an empty MEP ceiling corridor, the robot's red controller tablet with the floor plan and a total station blurred behind it.
- 26.7-36.0 (47-63 %) the problem: Hilti rep and site worker reading a tablet; a long handheld close-up of a worker drilling overhead with dust and debris (the pain shot); macro glides along the red robot body, tracks and an orange status light.
- 36.0-38.5 (63-67 %) black pause, 2.46 s, sound drops out for 1.1 s.
- 38.5-54.3 (67-95 %) reveal: wide of the robot in a corridor with its arm raised (on the music hit), arm close-ups on a white wall, a worker watching it drill, the drill bit entering concrete with red dust, finished channel hangers in the ceiling, then the robot wide again for 3.0 s, then a macro of the "JAIBOT" lettering on the red body.
- 54.3-57.4 (95-100 %) logo: red Hilti box on a light grey gradient, 3.1 s.

## Cut rhythm
- 34 shots in 57.4 s (end screen excluded). ASL 1.69 s, median 1.71 s, 9 % under 1 s, 6 % over 3 s, 35.5 shots/min.
- ASL per quarter 1.44 / 1.30 / 1.59 / 2.05 s: a flat, steady pulse; 6-7 cuts per 10 s until the logo.
- Longest: logo 3.14 s, robot wide 3.0 s, tower 2.6 s. Shortest: 0.29 s and 0.42 s flashes in the drone shot.
- 64 % of cuts sit on an audio onset (chance 38 %): cut to the music.

## Typography
- No supers, no captions, no spec cards at all. The only words are the product name printed on the machine (shot as a tilted macro, letters ≈45 % of frame height, Hilti's own condensed bold grotesk; closest free font: Barlow Condensed ExtraBold) and the Hilti logo end card (red box, ≈9 % of frame width, centred, on light grey).
- The voice-over carries every claim.

## Colour/grade
- Clean, bright commercial grade. Neutral concrete greys and white, the brand red appears in almost every shot (case, tool, helmet, robot, tablet frame). Mild contrast, no grain, no letterbox.

## Camera/shots
- Polished commercial production: gimbal moves, slider macros of the product, shallow depth of field with the red product sharp and the site blurred behind.
- One top-down drone shot of the site deck; one skyline shot of a tower (likely stock).
- Real site people with full PPE (hi-vis, helmets, gloves, glasses), crews walking towards camera.
- BIM shown as: a monitor close-up of the 3D model and the real robot tablet with a floor plan; no full-screen UI recording.
- The robot works at real speed in 2-3 s shots; the film never shows a complete drilling cycle.

## Transitions
- Hard cuts only. One hard cut to black for 2.46 s before the reveal; a short dip at ≈51 s (weak soft candidate) on the robot wide.

## Sound
- Male brand voice-over, calm, over a building corporate-electronic track. Integrated -19.8 LUFS, range 5.2 LU, true peak -1.8 dBTP.
- Drop-out 37.3-38.4 s (1.1 s, floor -55 dB) during the black, then the biggest hit at 38.6 s (+48.8 dB rise from near-silence, so the rise figure is inflated) as the robot appears.
- Hits on cuts in the hook (1.3 s, 5.15 s, 6.5 s).

## What makes it premium
- One brand colour in every frame ties tools, people and robot together.
- Problem shot before the product: a real worker drilling overhead in dust, then the robot doing the same task.
- The black + silence + hit before the reveal: a trailer device in an industrial film.
- Macro glides on the product body (tracks, status light, printed name) instead of graphics.
- People in correct PPE everywhere: the film looks like a real, safe site.

## Weak points
- No proof of autonomy or speed: no full cycle, no numbers, no speed label, no customer name. It sells a vision, not a measured result.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- 30-35 shots of 1.3-2.5 s, cut on music onsets; hold the hero wide 3 s and the logo 3 s.
- Beat order: brand line (0-17 %) -> crew in PPE (17-29 %) -> BIM screen + plan on the machine's tablet (29-47 %) -> the pain shot, worker drilling overhead (47-63 %) -> 2.5 s black with 1 s silence -> reveal on the hit -> 4-6 work close-ups -> name macro -> logo.
- Black pause: `<div class="clip" data-start="36" data-duration="2.5" style="background:#000">`; duck the music to silence for the last 1.1 s; place the hit exactly on the first frame of the reveal.
- Product name: film the real lettering on the machine with a slow slider move (no added text); if you must add it, Barlow Condensed 800, 40vh, white on brand red, `gsap.fromTo(el,{x:'6vw'},{x:0,duration:2.8,ease:'none'})`.
- Logo: brand box 9vw wide on `radial-gradient(#f4f4f4,#dcdcdc)`, cut in, hold 3 s.
