# Magic Capture on Google Pixel 11 Pro | Starstruck  (Google, 27 Aug 2026, 0:30, 9:16, YouTube Shorts @madebygoogle)
URL: https://www.youtube.com/watch?v=w5pkWHE4zB0
Purpose: social reel (vertical feature ad, narrative humour)
One-sentence point: at a small concert the singer sings straight to one fan; she keeps eye contact AND gets the video and photos, because Magic Capture shoots both in one tap.
Note: analysed at 480x854; text sizes are % of frame height H (9:16).

## Structure
- 0-2.9 s: wide of a purple-lit theatre stage, singer at the mic, phones up in the crowd. Song starts at 0.4 s ("I'm questioning everything").
- 2.9-5.1 s: the crowd, everyone filming.
- 5.1-8.2 s: the singer, medium close-up, singing to someone.
- 8.2-13 s: the fan (sequin jacket) realises he means her (my reading of the looks); tighter singer close-ups (9.9-11.4 s), back to her.
- 13-14.7 s: her thumb taps the shutter in camera UI (macro).
- 14.7-17.7 s: singer close-ups smiling; her face, starstruck.
- 17.7-21.3 s: phone screen POV - the Magic Capture frame captures a burst while she keeps looking up (frames slide out as thumbnails).
- 21.3-26.1 s: her face, phone lowered in her hand; VO "Capture everything without missing anything."; super "Video and photos" then "in one tap." (line by line, 23.5 / 24.1 s).
- 26.1-27.3 s: black, "Ask more / of your phone." (coral-tinted, 2 lines).
- 27.3-29.6 s: product on black: "Google / Pixel 11 Pro / with ✦ Gemini Intelligence" above the coral phone (stacked for vertical).
- 29.6-30 s: Google "G" on black.

## Cut rhythm (cuts2 + 1 soft transition added after checking by eye)
- 14 shots, ASL 2.15 s, median 1.73 s. Quarters 2.50 / 1.25 / 1.88 / 1.88.
- 7% < 1 s, 21% > 3 s. Longest 4.8 s (21.3 s, her face + super), 3.6 s (17.7 s, UI), shortest 0.46 s (logo).
- 4-5 cuts per 10 s. Cuts on onsets 31% vs 20% chance - cut on sung phrases.

## Typography
- Google Sans, sentence case with full stops, white over footage (lower-middle, ~45-50% H), cap ~2.5% H, building line by line.
- End line "Ask more / of your phone." lines 4.9% / 6.3% H (incl. descenders), coral on black. Name card stacked top: "Google" 6.4% H, "Pixel 11 Pro" 5.2% H, tagline 2.1% H, phone below.

## Colour / grade
- Concert world: violet/magenta stage light, cool blue fill on faces, warm bulb string in the background. Then black + coral product.
- 22% of samples >= 70% empty (black end cards); median empty share 56%.

## Camera / shots
- Real performance staging, longer lenses on faces (shallow focus), POV screen insert, one thumb macro. All framed for 9:16 - faces fill the frame.

## Transitions
- Hard cuts only; the in-UI thumbnail animation is the only "effect".

## Sound
- Licensed song carries the story (lyrics match the plot: "Do I close the door or let you in?"); one VO line. Integrated -15.4 LUFS (not pushed to Shorts loudness). Hits +27 dB at 19.6 s, +33.5 dB at 0.55 s (instant start).

## What makes it premium
- A tiny rom-com in 30 s; the feature solves a real human moment (watching vs filming).
- Same end system as the 16:9 hero ad ("Ask more of your phone." + coral phone on black), re-stacked for vertical.
- Film lighting on a small stage - it looks like a music video, not an ad.

## Recipe (real footage + HTML/GSAP)
- Shoot 9:16 natively: wide, crowd, singer CU, fan CU, thumb macro, screen POV. Coloured stage light (violet key, magenta back).
- Cut on lyric phrases, ASL ~2 s; the reaction close-up is the longest shot (4-5 s) and carries the super.
- Super: DM Sans/Google Sans 400, cap 2.5% H, white, `text-shadow: 0 1px 12px rgba(0,0,0,.4)`; line 1 then line 2 0.6 s later, each `opacity 0 -> 1, y 12 -> 0` 0.4 s.
- End: black 1.2 s line in #E8A496, product card 2.3 s stacked (name top 6% H, phone below), logo 0.5 s.
