# Introducing Linear Agent  (Linear, 2026-03-24, 54.9 s, 2:1 wide upload, YouTube / web)
URL: https://www.youtube.com/watch?v=mRql2VJ99gM
Purpose: launch film (software feature, polished rendered-UI product film)
One-sentence point: You type one request and the agent finds the issues, writes the plan and builds the spec inside Linear.

Structure: beats with timestamps
- 0.0-3.1 hook: the Linear app, tilted ≈25-30° in perspective on pure black, a "Project spec" page; slow push.
- 3.1-17.1 ask: macro on the empty prompt box; the request is typed letter by letter (≈10 chars/s), sent, and a result list of issues with coloured status icons builds line by line.
- 17.1-22.0 second request typed into the same thread ("make a plan").
- 22.0-35.1 payoff: the plan document writes itself (title → overview → table), then a node diagram draws its boxes and lines on black.
- 35.1-45.1 context: full app, wide, the doc and the agent side panel together; back to a tilted close-up of the agent's answer.
- 45.1-54.9 end: wordmark on black, the tagline extends from the wordmark, then a hard cut to the logo mark alone; 2.2 s silent tail.

Cut rhythm (verified)
- Scene detection found 0 cuts (footage is near-black, mean luma 0.05). The adaptive detector found 8; all 8 checked on before/after pairs: each is a hard cut to a new camera angle on the rendered UI. One cut added by eye at 50.4 s (tagline card → logo mark; luma step).
- 10 shots, ASL 5.49 s, median 5.32 s, 0 % under 1 s, 100 % over 3 s, 10.9 shots/min. Per quarter 4.57 / 4.57 / 3.43 / 4.57. Range 3.07-8.2 s: a very even pulse.
- Inside each shot the camera never stops: slow dolly/drift across the tilted UI and rack focus (front of the UI sharp, the back soft).

Typography
- Inside the UI: the product's own type (Inter-like), small; it is read through the camera, never enlarged as a title.
- End card: "Linear." in white semibold + tagline in regular weight, one line, centred at ≈50 % H; line box ≈8.9 % H incl. descender (cap ≈6 % H), 53 % of the width. Wordmark alone first (≈2.2 s), the tagline extends to the right of it (≈0.5 s ease), hold ≈3 s; then the logo mark alone ≈4.5 s.
- Closest free font: Inter Display / Inter (600 + 400).
- No other text: no feature labels, no captions, no voice.

Colour/grade
- Pure black #000 world; UI in dark greys (#16171a-#26282c), white text, small colour only in status icons (orange, yellow, green, red dots) and a soft blue accent. Very dark overall (mean luma 0.05). No grain, no letterbox inside the 2:1 frame.

Camera/shots
- 100 % rendered UI (a 3-D card of the real interface), no people, no device, no desk. Tilted perspective close-ups with shallow depth of field, one flat wide of the full app at 35-40 s.

Transitions
- Hard cuts between angles (8), every 3-8 s. UI changes inside a shot are animated (typing, list builds, document writing), not cut.

Sound
- No voice. A quiet ambient music bed; one swell at ≈4 s (loudest 0.5 s at 4.65 s, −11.4 dBFS) and a second at ≈40 s; the body sits around −33 to −36 dBFS RMS.
- Integrated −28.9 LUFS (very quiet for web; loudness range 11.3 LU). Silence 52.65-54.85 s under the logo mark.

What makes it premium
- One continuous task shown from prompt to result: the story is the workflow, not a feature list.
- The real UI as a sculpted object: tilted, lit from the dark, shallow focus, slow camera.
- Discipline: zero words on screen until the end card, one tagline, mostly silence.
- Even 5 s pulse with no shot under 3 s.

Recipe (Hyperframes, 1920×960 or 1920×1080)
- Background `#000`. Put a real UI screenshot or live HTML of the UI in a 3-D card: `transform: perspective(1600px) rotateX(28deg) rotateZ(-14deg)`; `filter: blur()` mask for depth (sharp band in front, 3-6 px blur behind) or a gradient mask `mask-image: linear-gradient(180deg, transparent, #000 30%, #000 70%, transparent)`.
- 8-10 shots of 3-8 s; each shot = a slow camera move on the card (`translate` 3-6 % + `scale 1.0 → 1.06`, `ease: none` or `sine.inOut`), cut hard between angles.
- Typing: reveal the prompt string with `steps()` at ≈10 chars/s and a blinking caret; result rows stagger in 0.08-0.12 s each (`opacity 0 → 1`, `y 6px → 0`).
- End: wordmark `600 6vh Inter Display` centred 2 s → tagline slides out to the right (0.5 s `power2.out`) and holds 3 s → hard cut to the logo mark 4 s in silence.
- Sound: soft pad at about −30 to −20 LUFS-S, one swell on the first result; no VO, no SFX ticks. Master to −16 LUFS for web unless you want this whisper-quiet look.
