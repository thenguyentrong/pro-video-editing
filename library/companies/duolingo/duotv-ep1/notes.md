# Episode 1 - Welcome to DuoMart! (DuoTV)  (Duolingo, 2026-10-12, 84.7 s, 9:16, YouTube Shorts / TikTok)
URL: https://www.youtube.com/shorts/Jf2eZ7tI3Os
Purpose: social reel (episodic 2D animated sitcom, episode 1 of 6)
One-sentence point: Lily takes a job at Duo's shop, and the episode ends on a mystery (what is in the basement?) to pull you into episode 2.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-4.9 hook: the whole frame is a phone chat. A photo of a green frog with a "#1 BOSS" mug, then reply bubble "Why is he green tho?" (1.0 s), typing dots (2.5 s). Format = "you are reading someone's phone", native to vertical.
- 4.9-21.0 cold open: incoming video call "Mother" (4.9 s), then Lily on FaceTime in front of a HELP WANTED poster, chat banner "help!!!!!!! a frog is chasing me hehe :P" on top. Dialogue "Ugh. Mom? Yes." "Look, Zari's here." "Look, Mom, I gotta go."
- 21.0-29.3: call ended screen, Lily's CV card, Duo at the interview desk, a bear chases Zari, Duo close-up "Now?".
- 29.3-34.2 title card: "DUO tv / Episode one / 'Welcome to DuoMart!'" (title arrives after 29 s, like a TV cold open).
- 34.2-55: establishing shot of the store, shop-floor dialogue ("Zari's one of your only employees", "Look, I'm only here for the paycheck").
- 55-67 turn: Duo monologue in a dramatic yellow spotlight ("I know this little shop... bringing people together from all over the world").
- 67-74: the bear (Falstaff) at the basement door with flashing green/pink/blue light: "Took care of that... thing downstairs."
- 74-82.7 payoff: Lily and Zari: "What role does Falstaff play?" "I'm too afraid to ask."
- 82.7-84.7 end card: "To Be Continued" handwritten on lime green with a doodle heart.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 28 shots (27 verified cuts; 15 false detections dropped: chat bubble pop-ins and basement light flashes), ASL 3.03 s, median 1.84 s.
- Quarters 2.65 / 2.12 / 5.30 / 2.35. Longest holds are dialogue 2-shots (39.0 s 11.7 s, 6.5 s 10.8 s, 58.2 s 8.9 s); shortest 0.5-0.9 s reaction inserts. Densest 17-30 s (montage into the title).

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Burned-in subtitles, sentence case, Inter / IBM Plex Sans medium-like, cap 1.9-2.2 % H, 1-2 lines, in a rounded dark plum box (~#2A2033, ~85 % opacity) at 73-80 % H, x 25-75 % W. Speaker colour-coded: Lily white, Duo lime green. One spoken line per box, cut with the line.
- Diegetic UI text does most of the hooking: chat bubbles (blue #1CB0F6), call screens, CV card, shop posters ("FREE EDUCATION FOR ALL", "SNACKS").
- Title card: "DUO tv" in chunky lime green with star, episode name in handwritten marker type.

Colour/grade: palette, contrast, grain, letterbox
- Flat 2D, thick dark outlines, warm orange/yellow shop palette with checkerboard floor; purple (Lily) and lime (Duo) as character colours. The basement scene goes dark brown with saturated coloured light flashes.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- 2D animation with TV-sitcom grammar: establishing exterior, 2-shots, close-up reactions, a fake phone screen as the opening "shot". Small push-ins on the monologue.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Almost all hard cuts; title card pops in with a squash-and-stretch of Duo; light flashes in the basement are in-shot effects.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Voice cast dialogue + light sitcom music bed + SFX (snorts, throat clears). Integrated -13.2 LUFS. Original audio.

What makes it premium (3-5 bullets)
- Starts inside a phone UI, the most native possible first frame for a vertical feed.
- Real sitcom craft (cold open, title card at 29 s, cliffhanger) squeezed into 85 s.
- Speaker-coloured subtitles keep it watchable on mute.
- Episode numbering + "To Be Continued" turns a feed into a series (binge loop on the profile).

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 85 s. Act 1 = HTML phone UI (status bar, blue header 7 % H, chat bubbles 42 px text) over the first 5 s; bubbles pop with `back.out(2)` 0.15 s, typing dots loop 0.6 s.
- Then real footage in sitcom grammar: 2-shot holds 6-12 s for dialogue, 0.6-1 s reaction inserts, ASL ~3 s.
- Subtitles: `background: rgba(42,32,51,.85); border-radius: 14px; padding: 10px 22px; font: 500 40px Inter; color: #fff` (Duo/brand speaker #89E219), bottom edge at 1540 px (80 % H), max 2 lines, width <= 50 % W.
- Title card at ~30 s for 4-5 s; end card "To Be Continued" handwritten (Caveat 110 px) on #89E219 for 2 s.
