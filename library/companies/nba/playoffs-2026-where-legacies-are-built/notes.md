# 2026 NBA Playoffs | Where Legacies Are Built  (NBA, uploaded 2026-04-18, 90.1 s, 16:9, YouTube / NBA channel)
URL: https://www.youtube.com/watch?v=he-BYmve4-M
Purpose: season-stage promo / tournament launch (:90), with sponsor and all broadcast partners on the end card
One-sentence point: today's players walk the same tunnels and make the same moments as the legends, so this postseason is where their legacy is made.

Structure (times from metrics.json):
- 0.0–1.9 HOOK: pyro fountains around a backboard and shot clock (arena show), music in at 0.5 s.
- 1.9–24.5 RITUAL / ARCHIVE BLEND: tunnel walks, warm-up jackets, huddles, hands, low-key faces; archive legends (1980s–2000s broadcast tape) intercut with today's stars, all in the same treatment. Overhead centre-court logos (three franchises) at 18.8–21.6 as a "map" of the league.
- 24.5–64.6 ACTION: game moments, shots, buzzer-beaters, crowd reactions; archive and current mixed.
- 64.6–69.6 BREATH: arena wide build (one 5.0 s shot, the second-longest), lights up on a packed bowl.
- 69.6–84.8 CLIMAX: big moments, crowd explosions, a final dunk + scream.
- 84.8–90.1 END CARD 5.3 s: league logo + "PLAYOFFS" wordmark, "Presented by" sponsor, "TAP TO WATCH" + app, row of five broadcaster logos; two spotlights in haze.

Cut rhythm: 70 shots in 90.1 s, ASL 1.29 s, median 1.03 s, 43 % under 1 s, 47 shots/min. ASL per quarter 0.90 / 1.07 / 1.50 / 1.88: the edit SLOWS DOWN (cuts per 10 s: 11, 10, 9, 8, 9, 7, 5, 6, 4). The opening ritual is the fastest part; the climax is built with longer, bigger moments, not with more cuts. Footage has heavy light leaks and vignettes, so the scene detector missed 17 cuts; the adaptive detector was used (verified on the cut sheet) plus one scene cut (26.96 s). Cuts on audio onsets 4 % vs 10 % chance: picture is not cut to the beat.

Typography: no text over footage at all (arena signage words appear only because they are in the shot). End card only:
- "PLAYOFFS": heavy italic condensed caps, white with a slight metallic sheen, cap ≈25 % of frame height, beside the league logo at the same height; together ≈70 % of frame width, upper third. Closest free: Barlow Condensed 800 Italic or Oswald 700 + `skewX(-8deg)`.
- "Presented by" + sponsor logo ≈5 % H, left-aligned under the wordmark.
- "TAP TO WATCH" + app: condensed caps ≈2.5 % H, centred.
- Broadcaster logos in one row at ≈4 % H, white, evenly spaced, bottom 15 %.

Colour/grade: one treatment over everything: warm, high-contrast, strong oval vignette (corners near black) plus bright white edge glow / light leaks that flare in at the frame edges every few shots. This makes 1980s tape and 2026 HD footage look like one film. End card cool steel blue (#1d2a38-ish) haze with two white spotlights.

Camera/shots: tunnel follows, close-ups of hands and faces, overhead centre-court logo shots, rim-cam, broadcast action, crowd. No interviews.

Transitions: hard cuts, many with a light-leak flash on the cut; arena wide uses a slow build. No graphic wipes.

Sound: one music cue (character not verified, I did not listen), levels steady: −16 to −20 LUFS momentary for the whole film, slowly rising from ≈−18 in the middle to −15/−16 in the last 15 s (loudest 0.5 s at 78.3 s, in the climax), LRA 4.5 LU, integrated −18.9 LUFS, true peak −7.1 dBTP. The end card fades: −20 at 86 s, −34 at 88 s, 0.9 s silence at the end. No drop-outs.

What makes it premium:
- One "memory" grade (vignette + light leaks) unifies 40 years of footage: archive is not a separate section, it is the same story.
- Pacing inverts the usual promo: fast ritual montage first, bigger longer moments at the end.
- Zero supers: names and stats are not needed; recognition is assumed.
- One long arena wide (5 s) as the breath before the climax.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- Treat every clip with the same layer stack: `filter: contrast(1.15) saturate(0.9) sepia(0.12)`; vignette div `radial-gradient(ellipse at 50% 50%, transparent 45%, rgba(0,0,0,.75) 100%)`; light leak = blurred white/amber ellipse (`blur(40px)`, opacity 0→0.8→0 over 0.35 s) on ≈1 cut in 4, entering from a frame edge.
- Rhythm: first 20 s at 1.0 s shots (ritual: tunnels, hands, faces), 20–65 s at 1.0–1.5 s, one 5 s wide at 70 %, last 15 s at 1.5–2.5 s per big moment.
- End card 5 s: hazy blue background (#1d2a38 + two radial white spots at 20 %/10 % and 75 %/10 %), wordmark Barlow Condensed 800 Italic caps at 25 % cap height, partner row at 4 %; fade the music out over the last 3 s.
- Stock queries: "basketball tunnel walk players", "basketball hands huddle close up", "arena pyrotechnics basketball", "basketball crowd celebration slow motion", "film light leak overlay" (licensed only; archive game footage needs a league licence).
