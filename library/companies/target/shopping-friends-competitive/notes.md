# Shopping With Friends Gets Competitive at Target Circle Deal Days  (Target, 2026-06-25, 59.5 s, 9:16, YouTube Shorts / TikTok / Reels)
URL: https://www.youtube.com/shorts/rtmqgLeQbUs
Purpose: social reel / promo (creator duo, reality-TV style, for a sales event)
One-sentence point: Two friends shopping for a Euro trip both want the same 40 %-off top, told like a reality show with confessionals.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-2.7 hook: walk-and-talk toward camera down the aisle ("I made the reservation." "Totally." "Wait."), "circle deal days is here!" disc sticker pops in at 0.25 s and pulses with teal rings; 2.7 s she spots the top on a mannequin ("This top!").
- 2.7-8.7: she grabs it ("Should I get it for Portugal?"), "40% off deals" sticker top-right.
- 8.7-17.6 confessional 1 (fake camcorder REC frame): "We are taking a little Euro trip... 40% off for Target Circle Deal Days" + 40 % sticker.
- 17.6-38.8 conflict: sunglasses, a Target team member suggests "Why don't you both just buy one?" (27.5 s), confessional "I am a Virgo sun with a Capricorn rising and a severe individuality complex" (32.6 s).
- 38.8-49.4 turn: second friend grabs a striped top ("Yes, it's perfect."), confessional 2.
- 49.4-55.6 payoff: "She said that?"
- 55.6-59.5 end card: white dot grows into a "circle deal days is here!" disc with teal rings filling the frame (iris wipe), coin-flip at 57.4 s to red "members save big june 23-26".

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 14 shots (cuts2 11 + 2 added by eye: 49.38 confessional cut, 55.6 iris wipe), ASL 4.25 s, median 3.57 s, longest 8.9 s handheld takes. Quarters 7.44 / 2.98 / 2.48 / 3.72.
- Slow by TikTok standards: the comedy lives in long handheld takes and talking heads; energy comes from stickers and subtitle changes inside the shots.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Subtitles: Helvetica/Arial medium white with thin dark outline, cap ~2.0 % H, 1-2 lines at 83-87 % H, speaker colour-coded (pink for the second friend), one phrase per card.
- Stickers: white discs (diameter ~25 % H) with Target-red bold lowercase ("deal days", "40% off deals for members"), teal or red concentric rings, pop in with overshoot, 1-2 s on screen.
- Confessional UI: red dot + "REC" at ~9.5 % H top-left and a battery icon top-right (fake camcorder).

Colour/grade: palette, contrast, grain, letterbox
- Bright store lighting, natural; outfits (yellow, white, navy polka dots) pop against white aisles; confessionals on a warm grey wall. End cards: teal #5BC2B8-like and Target red #CC0000.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Handheld walk-and-talks, locked talking-head confessionals, one store team member cameo. Creator-made look, produced audio.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts; one bullseye iris wipe into the end card; one coin-flip graphic swap.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Dialogue + confessional VO, gasps and laughter kept, light bed. Integrated -23.9 LUFS (quiet dialogue mix). Original.

What makes it premium (3-5 bullets)
- Borrowed TV format (reality confessional) gives structure without a script feel.
- Sales message spoken by the creator in her own words, backed by a sticker at the same moment.
- Speaker-coloured subtitles make the two-person banter readable on mute.
- The bullseye rings are a reusable brand transition.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 60 s, 12-15 shots: handheld scenes 5-9 s, confessionals 3-9 s.
- Confessional overlay: `● REC` 44 px white at x 90 px / y 180 px with red dot `#E00`, battery SVG at x 920 px.
- Stickers: 480 px white circle, text `700 120px "Helvetica Neue"` #CC0000 lowercase, 3 teal rings behind; `from {scale:0} to {scale:1, ease:"back.out(2.2)", duration:0.25}` then ring pulse `scale 1 -> 1.08 yoyo`.
- Subtitles 40 px white, `-webkit-text-stroke:1.5px rgba(0,0,0,.7)`, bottom at 1670 px; second speaker #FF6FA0.
- End: white dot -> disc + rings `scale 0 -> 6` 0.5 s (iris wipe), coin flip `rotationY: 0 -> 90` swap content `-> 0` 0.25 s.
