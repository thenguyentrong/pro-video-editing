# How does raising interest rates control inflation?  (The Economist, "The Essentials", 2022-06-09, 8:14 full / first 150 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=R8VBRCs2jTU
Purpose: narrated explainer (series "The Essentials"), presenter-led, 3D metaphors + archive
One-sentence point: Central banks raise rates to make saving more attractive and borrowing more expensive, which cools spending and, slowly, prices.

Why this example: the three debate examples are the channel's 2026 format; this is the older narrated, designed explainer format (3.4 M views) so the library has both.

Structure (first 150 s):
- 0.0–4.7 cold open on a white, vignetted paper ground: a 3D old TV set with static spins in, 3D "%" signs orbit it.
- 4.7–16.6 news proves it's happening: Sky News clip played inside the 3D TV ("BREAKING NEWS — Bank of England has hiked interest rate to 1%…"), CNBC Treasury-yield board, ABC "HOME BUYERS SET TO FACE RISING INTEREST RATES"; each with "Source: Sky News / CNBC / ABC" top right.
- 16.6–19.9 back to the TV, dashed rings ripple outward (cartoon "broadcast" waves).
- 19.9–27.9 a single 8.0 s 3D shot: "HIRING / APPLY INSIDE" and "HELP WANTED" signs and banknote bricks floating in grey, dusty light.
- 27.9–32.6 presenter Soumaya Keynes on a grey seamless backdrop, front then profile camera.
- 32.6–37.0 3D "%" spins on the white ground; 37.0–42.3 series title: giant serif letters "THE ESSENTIALS" pull back to a centred two-line title on a dark grey ground. Sound drops 2.5 s (42.5–45 s, −12.7 → −43.5 LUFS) then +32 LU.
- 42.3–45.5 stock macro of a miniature house with a "for SALE" sign, white serif caption "Interest rates".
- 45.5–62.4 1940s sepia archive film (a bank teller, a loan officer) — 5 shots, 2–7 s.
- 62.4–69.4 presenter, lower third (63–67 s).
- 69.4–83.5 one 14.1 s 3D metaphor: a plumbing system — tank "BANK INTEREST RATES" with a pressure gauge, blue pipe fills the "SAVINGS" tank as the gauge rises.
- 83.5–94.9 presenter (front, then close); 94.9–104 stock of the ECB, Bank of England, the Fed, B&W archive of a bank counter (6 cuts in 90–100 s = densest).
- 104–110.6 vintage cartoon (piggy-bank/fish, a banker in a 1950s animation style); 110.6–124.8 presenter front + profile (7.9 s).
- 124.8–134 archive slapstick, B&W bars/sacks, night street with an LED "0.13%" ticker, blueprint drawing; 134–142 the plumbing again: gauge close-up "INTEREST RATES", a "PRICES" tank with a hand on the tap; 142–146 Channel 4 clip of a shopper (Source label), 146–150 presenter.

Cut rhythm: 47 shots in 150 s, ASL 3.19 s, median 2.40 s. ASL by quarter 3.12 / 3.12 / 2.68 / 3.12 s (even). 11 % under 1 s, 38 % over 3 s. Longest: plumbing metaphor 14.1 s (69.4 s), 3D signs 8.0 s, presenter profile 7.9 s, archive 7.2 s. Shortest 0.24 s (126.8 s). Cuts per 10 s: 2 5 1 5 3 3 3 0 2 6 4 2 4 3 3. Cuts on onsets below chance (46 % vs 51 %). Much faster than the Economist debate format (ASL 7.5–8.8 s).

Typography:
- Logo bug: "The Economist" white serif in a red box (brand red; sampled #AB1924 through compression, brand #E3120B), top left, ~10 % H tall, on every shot.
- Source labels: top right, white sans ~3 % H, "Source:" in bold + outlet name.
- Lower third: no box; name in white bold serif ~5 % H, role in sans ~3.3 % H, "The Economist" in italic sans below; left-aligned at x ≈ 6 %, bottom at ~88 % H.
- Keyword captions: white bold serif, sentence case, ~5 % H, centred ("Interest rates").
- 3D labels: white bold condensed caps on black bands wrapped around the tanks ("SAVINGS", "PRICES", "BANK INTEREST RATES").
- Series title: high-contrast display serif caps, letterspaced, two lines.
Closest free: Economist Milo Serif → Merriweather / Source Serif 4 Bold; sans → Source Sans 3 (guess).

Colour/grade: three looks. (1) Designed world: white/light-grey vignetted paper ground (#BDBCB8 at the edges) with photoreal 3D objects in steel grey, with one colour per metaphor (blue water #192974 = money, magenta/red pipes). (2) Presenter: dark grey seamless (#343436), warm skin, a single green top. (3) Archive: sepia/black-and-white film with grain, vignettes; modern stock natural and saturated.

Camera/shots: two-camera presenter (front medium, 90° profile close-up) on a seamless; photoreal 3D renders with slow camera drift; stock miniatures; archive newsreel and 1940s instructional film; vintage cartoon; news clips framed inside a 3D TV.

Transitions: hard cuts; the TV screen is a frame-in-frame transition (news plays inside the set); the title is a scale-down reveal. No wipes.

Sound: integrated −15.4 LUFS, loudest −9.6 LUFS momentary at 23.5 s. 50 ms RMS median −22.6 dBFS, p10 −33.7 dBFS, only 1 % of windows below −45 dBFS → a continuous music bed ~11 dB under the voice (unlike the debate format, which has no music). One designed drop: 2.5 s after the series title (42.5–45 s) then +32 LU into the first chapter. Biggest 50 ms rises (+20…+31 dB) at 2.1, 3.5, 18.8, 23.3 s = SFX on the 3D motion (whooshes/pops; inferred, not heard).

What makes it premium:
- One physical metaphor (plumbing with gauges and tanks) carries the mechanism and comes back later — the viewer learns it once.
- Every outside clip says where it came from (Source: top right) and is framed inside a designed object rather than dumped full screen.
- Mixed textures — photoreal 3D, sepia archive, vintage cartoon, crisp presenter — held together by one logo, one serif and a white ground.
- An expert-presenter (the paper's economics editor) gives authority without a studio set.

Recipe (real footage + HTML/GSAP):
- Ground: `background: radial-gradient(ellipse at center, #F4F4F2 40%, #BDBCB8 100%)` + paper grain at 8 %.
- Frame-in-frame news: a TV PNG with a transparent screen; the clip underneath in the screen rect, `filter: contrast(1.05)`; whole TV `scale .9→1, rotate -3→0, 0.8 s, power3.out`. Source label `font:700 2.8vh 'Source Sans 3'` "Source:" + `400` outlet, top 3 % right 4 %.
- Logo bug: `background:#E3120B; color:#fff; font:600 2.6vh/1 'Merriweather'; padding:.5vh 1vh` top-left 4 %/6 %.
- Lower third: `font:700 5vh 'Merriweather'` white name, `400 3.3vh 'Source Sans 3'` role, italic masthead line; `gsap.from(lines,{y:'1vh',opacity:0,stagger:.12,duration:.4,ease:'power2.out'})`, hold 4 s.
- Metaphor machine: render (or use stills of) tanks + pipes; animate the "money" as a blue `#192974` rect clipped to the tank shape: `gsap.to(fill,{scaleY:.55,transformOrigin:'bottom',duration:6,ease:'sine.inOut'})`; gauge needle `rotation:-40→35, 6 s`; label bands as HTML `font:700 4vh 'Oswald'` white on black.
- Archive: `filter: sepia(.6) contrast(1.1)` + film grain + vignette; 2–7 s per shot.
- Mix: bed ~11 dB under the voice the whole time; drop to near-silence for 2–2.5 s after the series title.
