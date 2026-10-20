# buy your own plane (#stitch w/ @niamhdoherty3)  (Ryanair, 2026-09-17, 6.4 s, 9:16, TikTok stitch cross-posted to YouTube Shorts)
URL: https://www.youtube.com/shorts/zsNb49CFVO0
Purpose: social reel (brand replies to a customer complaint with a stitch)
One-sentence point: A passenger complains there is no cup holder; the Ryanair plane, with a human face, tells her to put it in the holder and, if she does not like it, to buy her own plane.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-1.3 hook: the customer's own clip, untouched: phone video in the cabin, a Smirnoff Ice can on the tray, her caption "Thanks Ryanair 😋✈️". The complaint is the hook; the viewer waits for the brand's answer.
- 1.3-2.0: cut to the Ryanair 737 nose with pasted human eyes and lips (the account's signature "plane face"), staring.
- 2.0-3.0: back to her clip; then the plane face grins: "WELL MAYBE".
- 3.0-4.6: "PUT (IT IN THE) HOLDER" over a 250 % punch-in on her clip with two red meme arrows on the cup holder.
- 4.5 0.15 s of full silence, 4.7-6.4 payoff: wide of a Ryanair 737 taking off with the face, words "LIKE / YOUR / PLANE" one per beat. Hard end.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 6 shots, ASL 1.07 s, median 1.08 s, shortest 0.53 s, longest 1.70 s (the takeoff). Quarters 0.80 / 0.54 / 0.54 / 1.61: fastest in the middle (the comeback), slower on the payoff.
- All 5 cuts land on audio onsets (100 % vs 40 % chance): cut on the plane's words.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Brand captions: CapCut "auto caption" look, white bold caps (Montserrat ExtraBold / The Bold Font), dark soft drop shadow, no box, 1-2 words per card, cap ~5.3 % H, centred at ~78 % H, hard on/off per word (no animation).
- The customer's caption stays as found (TikTok classic white, ~1.5 % H cap) and is even magnified in the punch-in: proof, not decoration.

Colour/grade: palette, contrast, grain, letterbox
- No grade: phone footage as shot + bright airport daylight. Brand colours (Ryanair blue #073590, yellow #F1C933) come from the plane and seats.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- UGC phone clip (stitch), photo-cut-out face composite on stock/plane photos, one planespotter long-lens takeoff. Digital punch-in (about 2.5x) instead of new footage.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 5 hard cuts, no transitions. One digital punch-in.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Customer audio, then a deadpan plane "voice" ("Well, maybe put it in the holder..."). 0.15 s hard silence at 4.5 s before the payoff line, hit at 4.9 s. Integrated -12.1 LUFS.

What makes it premium (3-5 bullets)
- The brand punches back at the customer (self-aware villain persona) in 6 s: rude, fast, funny.
- Uses the complainer's own footage as the set-up (stitch = free hook + social proof).
- One recurring absurd mascot (the plane face) instead of a logo.
- Meme grammar (red arrows, zoom, word captions) on purpose: looks native, not "brand".

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 6-7 s, 5-6 clips of 0.5-1.7 s. Start with the "problem" clip unedited for 1.0-1.3 s.
- Mascot face: PNG eyes + mouth layered on the product photo, `mix-blend-mode: normal`, slight 2 % scale wobble.
- Word captions: `font: 800 100px Montserrat; text-transform: uppercase; color:#fff; text-shadow: 0 4px 0 rgba(0,0,0,.6), 0 0 18px rgba(0,0,0,.5)`, centre at y 1500 px, one or two words per card switched with `tl.set` on each spoken word.
- Punch-in: `gsap.to(clip,{scale:2.5, transformOrigin:"62% 58%", duration:0.12})`; red arrow PNGs `from {scale:0, rotation:-20}` 0.1 s.
- Audio: cut the music to silence for 0.15 s before the payoff word.
