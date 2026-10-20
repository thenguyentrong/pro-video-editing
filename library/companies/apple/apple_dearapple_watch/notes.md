# Dear Apple: How Apple Watch Is Changing People's Lives  (Apple, 2025-09-09, 3:19 file / 3:11.7 content, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=HKphYoxGeRE
Purpose: testimonial / narrative ad (event film, "Dear Apple" series)
One-sentence point: Real people read their letters to Apple — Apple Watch helped them get healthy or saved their life.

## Structure
- 0-21 s **Letters**: a blue cursor types "Dear Apple," then many letter openings in different fonts and languages ("Hola Tim…", "I'm a college student", "firefighter.", "…do, Ohio", Japanese "東京出身です" + small "Tokyo, Japan"), camera very close to a real screen.
- 21-47 s **Story 1-2 (health)**: video calls framed as windows on an off-white canvas; mental health, weight loss, marathon; phone footage and news clips appear as small windows that slide and stack.
- 47-70 s **Story 3**: "It was about five in the morning…" typed, watch alert on wrist, X-ray flicker (0.1 s), hospital, "That Apple Watch just saved your life."
- 70-90 s **Story 4**: "I got home" typed big → doorbell-camera footage of a man collapsing (9.4 s hold), interview, medical micro-imagery.
- 90-147 s **Stories 5-6 (SOS)**: typed paragraphs, Japan snowstorm phone footage, a car crash into a pool (news clips + 9.0 s hold), thermal helicopter footage, rescue; **1.8 s of near-silence at 115.8 s** after the blizzard line.
- 147-186 s **Finale montage**: "I've always read those stories about how Apple Watch saved someone's life" typed; fast montage of all people (9 cuts / 10 s at 160-180 s), ending on laughter: "it had my back, my front, my sides…"
- 186-191.7 s **End**: " WATCH" wordmark, black on off-white; legal on black.

## Cut rhythm
- 95 shots in 191.7 s → **ASL 2.02 s**, median 1.67 s; quarters 1.65 / 1.92 / 3.42 / 1.60 (slow third quarter = SOS stories, long holds on found footage).
- 22 % < 1 s, 12 % > 3 s; shortest 0.10 s (X-ray flicker 59.0 s); longest 9.4 s (doorbell fall), 9.0 s (car in pool), 8.8 s (thermal).
- Cuts on onsets 23 % vs chance 33 % → cut to speech, not to music.

## Typography
- "Typed letter" device: dark grey text with a blinking blue cursor (≈ #5b6fd6), typed character by character, filmed off a real monitor (pixel grid and slight colour fringing visible), shallow focus.
- Many typefaces, one per writer: SF Pro, a serif (Times/New York-like), italic serif, monospace, condensed italic, Japanese.
- Size varies with the camera: cap ≈ 3 % H for full sentences up to ≈ 14 % H ("Dear Apple,") and larger when the camera pushes into a word ("I got home", "firefighter.").
- Backgrounds of typed shots: pale grey (#d2d1d4-#dfddd9) or mint (#e1f0f0), soft vignette.
- End wordmark " WATCH": black on off-white, cap ≈ 6.7 % H, centred.

## Colour / grade
- Very light, clean canvas (off-white #ebe9e7) for collage sections; found footage left in its own colours (phone, doorbell cam, news, thermal).
- 23 % of frames mostly empty, all on light.

## Camera / shots
Self-recorded video calls, phone videos (vertical and horizontal), doorbell/security cam, local-news clips with their tickers, helicopter thermal, X-rays, macro of a cracked Apple Watch, macro of typing on a screen. Media sits as floating rectangles (no shadow, no frame) on the canvas; windows slide in and overlap.

## Transitions
Hard cuts; windows slide/stack on the canvas; push-ins on typed words; X-ray flicker cut (0.1 s).

## Sound
- Music: "The Adam Project" by Rob Simonsen, emotional score under real testimonial audio; keystroke SFX on the typing; diegetic sounds from found footage (glass shattering, wind, whirring helicopter).
- Integrated **−16.0 LUFS**. 1.8 s near-silence at 115.8 s, then hit 118.1 s; biggest hit 133.5 s (car-in-pool news, +28.5 dB).
- Ends on a laugh, not on music.

## What makes it premium
- Real people, real footage, real letters — the brand stays almost invisible until the last 5 s.
- One strong graphic device (typing cursor) ties 10+ stories together.
- Raw footage is "framed" on a clean canvas, so it looks curated, not cheap.
- Pacing follows emotion: fast set-up, long holds on the most dramatic footage, fast happy finale.

## Recipe (real footage + HTML/GSAP)
- Canvas `#ece9e6`; place each clip as a rectangle 40-60 % W, no border, no shadow; `gsap.from(win,{x:120,opacity:0,duration:.5,ease:"power3.out"})`, stack 2-3 windows with 3-6 % offset.
- Typing card: pale mint/grey bg with radial vignette; text `#2b2b2b`, font per speaker (Inter, Newsreader italic, JetBrains Mono, Noto Sans JP); type with a GSAP `TextPlugin` or a stagger of chars (`stagger: 0.045`); cursor `2px × 1.1em` in `#5b6fd6`, blink 0.53 s steps(1); slowly scale the card 1 → 1.25 over the line.
- For the screen-filmed look: overlay a 3 px dot-grid pattern at 6 % opacity + `filter: blur(.3px)` and a tiny RGB offset on edges.
- Hold dramatic found footage 6-9 s; cut finale at 1.0-1.2 s.
- End: wordmark centred, cap ≈ 6.7 % H, 4-5 s; legal on black.
