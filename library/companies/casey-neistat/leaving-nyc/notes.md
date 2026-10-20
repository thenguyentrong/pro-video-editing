# i'm leaving New York City  (Casey Neistat, 2026-06-30, 10:25 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=zLganMVbY8g
Purpose: travel / road-trip vlog (day into night)
One-sentence point: Casey picks up his repaired car and drives out of the city with the family dog to join a holiday, through dusk, a ferry and a motel night.

Data note: first 300 s analysed (trimmed with ffmpeg). Cuts from the adaptive detector plus one verified scene-only cut (209.04 s, hand-to-lens). Three dips to black (79.1, 179.9, 230.7 s) are counted as transitions. Speech timings from a local speech-to-text pass (±0.5 s). Family members are not named in these notes.

## First 30 s (hook)
- 0.0–10.9: one locked-off wide on the sidewalk: Casey skates from far away straight into a close-up. He starts talking at ≈2.9 s and lists the repairs on his car; a numbered list types on top-left item by item in sync with his words (≈4.5, 6.5, 8.5, 10, 12.5 s).
- 10.9–14.6: handheld close, the fifth list item lands; loud hit at 13.0 s (+21 dB).
- 14.6–18.1: Dutch-angle wide as he skates down a ramp into a garage.
- 18.1–24.7: POV/handheld inside the garage, a short exchange with a mechanic (≈17.4–23.8 s), the board handed over.
- 24.7–33.9: the mechanic tries the electric board, Casey coaching from behind the camera.
- (after the hook) 33.9–46 the car revealed in the garage, driving out; the reason for the trip is told at ≈52–64 s at home while packing.
- Cuts in 0–30 s: 6. The typed list is the only type in the hook; no title card.

## Structure (first 300 s)
- 0–34 hook (above). 34–47 car pickup, first drive.
- 47–79 home: the dog, packing bags, talk to camera with the dog in frame; dip to black at 79.1 s.
- 79–106 loading the car, studio stop (wide static of his workshop), tyre/plate inserts.
- 106–138 driving out: in-car selfies, then a road-sign montage (115.7–122.4 s, 9 shots at 0.67–0.8 s: highway signs shot telephoto from the car, skyline, bridge), dog in the passenger seat, rest stop with the dog.
- 138–158 one 20.1 s talk-to-camera take in a gas-station shop.
- 158–170 drone aerials of the highway at dusk; 170–180 phone video call on the dash, a highway exit sign; dip to black at 179.9 s.
- 180–197 night: ferry/bridge aerials with lights; 197–215 dog in the car; 215–231 night talk next to the car.
- 231 "welcome to" state sign at night after a dip to black; 236–282 motel room talk (one 33.6 s take at 248.7 s, the longest shot).
- 282–300 morning: motel corridor, sky, a windshield timelapse of the parked car (288–297 s, 6 cuts), hand with keys.

## Cut rhythm
75 shots in 300 s, ASL 4.00 s, median 2.96 s, 21.3 % under 1 s, 49.3 % over 3 s, 15.0 shots/min. ASL by quarter 4.2 / 2.6 / 5.0 / 4.7 s: the drive montage makes the second quarter densest. Longest 33.6 s (248.7 s motel), 20.1 s (138.1 s shop), 11.9 s (197.2 s). Shortest 0.42 s (289.0 s timelapse), 0.54 s, 0.67 s. Cuts per 10 s: 0–6; peaks of 6 at 110–130 s (sign montage) and 290–300 s (timelapse). Cuts on onsets 46 % vs 40 % chance.

## Typography
- Numbered list: Helvetica-style bold grotesque (closest free: TeX Gyre Heros Bold / Inter Bold), sentence case, black with a soft white halo for legibility on any ground, flush left at x ≈3.5 % W, first line top ≈33 % H, cap height ≈6.7 % H, line pitch ≈10.4 % H, one line appears per spoken item (hard on, no animation), whole list stays ≈12 s then cuts off.
- Location "titles" are real road signs and a state welcome sign, filmed telephoto and held 0.7–2 s.

## Colour/grade
Overcast daylight, neutral; dusk aerials blue-hour; night footage left dark with sodium orange highlights and crushed blacks; motel interior warm tungsten. No letterbox, no grain.

## Camera/shots
Locked-off self wide (opening), handheld fisheye selfies, GoPro-style dash and footwell angles in the car, telephoto road signs from the passenger side, drone aerials at dusk and at night, a phone screen shot on the dash, a windshield timelapse, the dog at eye level.

## Transitions
Hard cuts; three dips to black of 0.5–0.8 s as "time passes" markers (79.1, 179.9, 230.7 s); one hand-to-lens cut (209.0 s); a timelapse sequence to compress the night into morning.

## Sound
−14.3 LUFS integrated, LRA 8.4 LU (widest of the three), true peak +2.3 dBTP (480p re-encode). RMS median −19.8 dBFS. Music under montages (driving 110–190 s: p10 within 5–11 dB of the median); dry dialogue at home and at night (p10 −41…−53 dBFS). Night section has short near-silences 0.3–0.75 s (192–195 s, to −57 dBFS) followed by +39…+45 dB rises. Big hits +36…+38 dB at 245.4 and 281.8 s (motel talk punctuation, music re-entry).

## What makes it premium
- The opening list gives a concrete, fast payoff and sets the "practical errand" tone without a title card.
- Real signs and borders tell the geography — no maps, no location graphics.
- Day-to-night arc with clear markers: dusk drone, dips to black, a night aerial, a morning timelapse.
- Intimate one-take talks (20 s, 34 s) are the emotional anchors between fast travel montages.

## Recipe (real footage + HTML/GSAP)
- Opening: one 10–11 s locked-off wide, host travels from far to a close-up while talking; list lines set on as he says them.
- List: `.list{position:absolute;left:3.5%;top:33%;font:700 9.4vh/1.1 "TeX Gyre Heros",Inter,sans-serif;color:#000;text-shadow:0 0 6px #fff,0 0 2px #fff}` (cap ≈6.7 % H); `items.forEach((el,i)=>tl.set(el,{autoAlpha:1},wordTimes[i]))`; clear the whole list 1–2 s after the last item.
- Travel montage: 7–9 telephoto sign/skyline shots at 0.67–0.8 s on the music, then a 10–20 s talk take.
- Time markers: 0.5–0.8 s dip to black between day parts; morning = 6-cut windshield timelapse at 0.4–1.8 s per cut.
</content>
</invoke>
