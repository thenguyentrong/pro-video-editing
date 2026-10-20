# Oura Ring 4: Smart Sensing  (ŌURA, 2024-10-03, 0:45, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=SoeMkKJSaaE
Purpose: feature explainer (narrated)
One-sentence point: The ring's sensors adapt to your finger and skin tone, so the data has fewer gaps and the battery lasts.

Structure:
- 0.0-3.0 macro of the inside of the ring with sensor windows, then the ring on beige with "Oura Ring 4"; VO starts at once.
- 3.0-5.4 the ring turns into an x-ray (translucent shell showing the electronics); title "Smart Sensing" (t004.5s).
- 5.4-12.3 the ring on a turning oak disc; thin call-out lines and tiny labels appear one by one for each sensor (t009.5s): 7 s on one shot.
- 12.3-14.5 warm particles (dust/skin texture) fill the frame.
- 14.5-16.2 the ring on a finger, hand turning.
- 16.2-19.1 face montage: 9 portraits of different skin tones at 0.25-0.4 s each (t017.5s).
- 19.1-22.9 the inner sensor macro with blinking green and red LEDs.
- 22.9-27.1 a hand on a bike, glass UI cards with health scores floating over blurred footage (t024.5s), a night scene with a sleep card.
- 27.1-31.5 the ring on beige with a white signal waveform drawn around it (t030.0s).
- 31.5-37.9 the ring in a soft room with floating glass data cards; the charger (t034.5s).
- 37.9-41.8 the ring on the oak disc again, sensor macro.
- 41.8-45.4 end card: "Oura Ring 4 / Sleeker. Smarter. Made for you." on beige satin, ŌURA wordmark (t043.5s).

Cut rhythm: 22 shots, ASL 2.06 s, median 1.9 s, 41 % under 1 s (the face montage), 27 % over 3 s, 29 shots/min. Quarters 3.78 / 0.87 / 2.27 / 2.84 s: slow open with the labelled hero shot, a burst of portraits in Q2, then calm. Longest 7.0 s (call-out shot), 6.4 s (data cards). Cuts on onsets 52 % vs 43 % chance.

Typography: title "Smart Sensing" in the same sans + light weight, cap ≈ 4 % H, centred over the x-ray ring. Call-out labels: tiny (cap ≈ 1.5 % H), grey-white, at the end of 1 px lines from each sensor, in the empty space left and right. UI cards: real app layout, glassy translucent panels (blurred background, white numbers). End card as in the launch spot.

Colour/grade: warm beige and oak (R-B +34), median luma 98, saturation 34 %, soft contrast (p95-p5 101); sensor LEDs green/red are the "tech" colour; data cards white glass.

Camera/shots: CG macro and turntable of the ring; x-ray morph; real portraits (frontal, natural light, city backgrounds); hands; real lifestyle footage behind glass UI.

Transitions: hard cuts; one x-ray morph (solid → translucent) inside a shot; UI cards fade and slide in over footage.

Sound: female VO from 0.0 to 45 s, wall-to-wall, calm explainer tone; light music bed; −17.8 LUFS, LRA 3.0 LU, true peak −3.8 dBTP. Small hits on UI and LED events (+20-22 dB at 23.2, 27.1, 28.6 s).

What makes it premium:
- Hardware explained like Apple's "inside" shots: x-ray shell, thin call-out lines, tiny labels, no boxes.
- A 9-portrait montage makes "adapts to every skin tone" visible in 3 s.
- Glass UI cards over real life = the data belongs to a person, not a dashboard.
- The same beige/oak world as the launch spot: the campaign looks like one family.

Recipe (real footage + HTML/GSAP):
1. Call-out shot (6-8 s, locked or slow turntable): for each part a 1 px SVG line (`strokeDashoffset`, 0.4 s) then a label `font: 400 2.1vh 'Inter'; color:rgba(255,255,255,.85)`, staggered 0.6 s.
2. X-ray morph: stack the product photo and a "translucent" render; cross-fade 0.8 s with `filter: brightness(1.3)` on the top layer.
3. Diversity montage: 8-10 portraits, 6-10 frames each, same framing (eyes at 40 % H), cut on a rhythmic pattern.
4. Glass card: `backdrop-filter: blur(16px); background: rgba(255,255,255,.14); border-radius:18px; border:1px solid rgba(255,255,255,.35)`, enter `y:20, opacity:0`, 0.5 s `power2.out`.
5. VO wall-to-wall, one idea per 4-6 s; master −16 LUFS.
