# Those Waves Are INTENSE  (Red Bull, 2026-10-08, 101.6 s, 9:16, YouTube Shorts / TikTok)
URL: https://www.youtube.com/shorts/Jw5TdfVYXwM
Purpose: social reel (Red Bull Cliff Diving, athlete POV; 103 M views, 1.3 M likes in 12 days)
One-sentence point: A cliff diver waits on a 20+ m platform for the right wave while captions list her ritual, then dives.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-3.0 hook: a diver (teal suit) on the platform points over the edge, caption "take a look at this..."; 2-3 s the phone looks straight down at turquoise waves smashing the cliff. Danger first.
- 3.0-5.9: POV down at the sea (another diver swimming), the diver grins into the lens.
- 5.9-96 build: one long, almost locked phone shot of the second diver (neon bikini) on the ledge. Captions name each step: "now it's her turn", "final psych up", "small pat down", "shoes & towel down", "make sure feet are in the right place", "understand the timing of the waves", "visualize the dive", "the timing has to be perfect", "now we're ready", "let's go".
- 96-97.5 payoff: she dives; the camera tilts down to follow her into the water.
- 97.5-101.6: churning water, "and stick the landing". No logo, no end card.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 3 shots (3.0 s, 2.8 s, 95.7 s). ASL 33.9 s. All edits are in the first 6 s; the rest is real-time waiting. The rhythm comes from about 12 caption cards (one every 3-8 s) and her small movements.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Bold italic sans (Poppins / Proxima Nova Bold Italic-like), white, soft dark shadow, lowercase, centred, no box. Glyph line 2.2-2.3 % H (cap ~1.7 % H): small. Placed at 44-53 % H, on her body in the frame centre. 2-7 words per card, 1-2 lines, hard on/off, gaps without text between cards.

Colour/grade: palette, contrast, grain, letterbox
- Natural phone colour: turquoise sea, white limestone houses, blue sky; neon-yellow swimsuit and the Red Bull Cliff Diving board as the only brand marks.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Athlete-perspective phone footage: handheld POV for the hook, then a fixed phone at the platform corner (subject full body, ~45 % of H), one tilt-down follow of the dive.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 2 hard cuts in 101 s.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Location sound (wind, sea, crowd) with soft music; no VO. Integrated -18.6 LUFS; biggest rises at 5.2 s (+26.5 dB) and the splash at 101 s.

What makes it premium (3-5 bullets)
- Shows the danger (waves) in the first 3 s, then withholds the dive until 95 % of the runtime.
- Captions make waiting interesting: a step-by-step ritual is a story with a countdown feel.
- Real athlete POV, no edit tricks: feels like a friend's phone.
- Brand only on the board; the sport is the brand.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920. Shot 1 (3 s): handheld "look at this" + point; shot 2 (3 s): POV of the danger; shot 3: one long locked phone take of the preparation, payoff at the end.
- Captions: `font: italic 700 40px Poppins; color:#fff; text-shadow: 0 2px 6px rgba(0,0,0,.55); text-transform: lowercase; text-align:center`, centre at y 920 px (48 % H). One card per action, `tl.set(card,{autoAlpha:1},t).set(card,{autoAlpha:0},t+hold)` with hold 3-6 s and 1-2 s gaps.
- No music drop or logo; let the real splash be the loudest sound.
