# 2025 ESPN College Football Music Anthem  (ESPN College Football, uploaded 2025-07-31, 95.3 s, 16:9, YouTube / ESPN College Football channel)
URL: https://www.youtube.com/watch?v=YxUGEh_Vclg
Purpose: season anthem / season-launch title package (a licensed pop-rock single cut as a music video over a season of footage; versions run as the broadcast season open)
One-sentence point: college football is a wild, loud, local world, and it is back on a named date.

Structure (times from metrics.json):
- 0.0–4.1 HOOK: aerial of a stadium ringed by red pyro, tunnel shot of players under fireworks; a music-video credit (artist / song / label) sits bottom-left 1.2–4.1 s.
- 4.1–12.7 SET-UP: artist performance shots (riding a motorbike, singing in a field) cut into walk-outs, helmets, mascots, a signing-day press table.
- 12.7–17.6 COLLAGE: one 4.9 s mixed-media section of cut-out photo stickers (coaches, bowl signage, mascots, team pins) sliding and stacking; it reads as ≈7 beats of 0.6–0.8 s, but is not hard-cut (counted as one shot).
- 17.6–86.8 MONTAGE: traditions (signs such as stadium slogans), fans, bands, mascots, B&W mirrored archive (29.5 s), game-winning plays, coaches screaming, field storms, Gatorade bath; artist cutaways every ≈10–20 s.
- 86.8–91.0 TITLE: "THE WILD WORLD OF COLLEGE FOOTBALL" + the CFB shield over a drone shot of a stadium; 4 footage cuts continue under the type.
- 91.0–95.3 END CARD 4.4 s: shield centred over darkened confetti/trophy footage, "THE SEASON BEGINS <date>", network logos. Music ends at 92 s, 0.6 s silence.

Cut rhythm: 117 shots in 95.3 s, ASL 0.81 s, median 0.67 s, 86 % under 1 s, 74 shots/min, only 1.7 % over 3 s. ASL per quarter 0.85 / 0.64 / 0.79 / 0.95 = flat. Cuts per 10 s: 12, 8, 19, 15, 11, 13, 14, 11, 12. The two detectors disagreed (dark tunnels, smoke, flashes); the metrics use the union of both (adaptive 105 + 11 scene-only cuts), checked on the sheet. Cuts sit slightly more on onsets than chance (12 % vs 8 %): mostly cut on the pulse, not every hit.

Typography:
- Music credit: 3 lines, plain grotesk, sentence/lower case, white, ≈2.5 % H line height, left 10 %, lines at 73–84 % height, quoted song title. Closest free: Inter 500.
- Title: very condensed heavy sans caps, white, two lines, cap ≈14 % H, left-aligned block across 10–70 % of width; shield logo at ≈37 % H right of it; over moving footage, hard on, no animation. Closest free: "Anton" or "Bebas Neue" (ESPN's own condensed face is not free).
- End card: shield ≈40 % H centred above the middle; date line in a wide heavy sans caps, cap ≈3.5 % H, white; network logos ≈4 % H below. Closest free: Montserrat 800 for the date.

Colour/grade: high contrast, punchy saturation, crushed blacks; night games dominate (red pyro, stadium light). Some music-video sections are warm and faded; a few B&W mirrored archive shots. Background of the end card = the same footage darkened ≈60 %.

Camera/shots: drone over stadiums, tunnel walk-outs from behind, helmets in close-up, fans in the stands, mascots, bands, traditions (painted signs), broadcast game action, slow-motion celebrations, artist performance plates. Huge variety: almost no shot repeats a set-up.

Transitions: hard cuts (≈115); one cut-out collage section; mirror effect once; title and end card sit over footage. No dissolves.

Sound: the licensed single is the whole soundtrack. Measured: flat wall −9 to −15 LUFS momentary for 92 s (LRA 3.6 LU), integrated −12.4 LUFS (very loud), true peak +0.3 dBTP (over −1). Only one notable rise inside the film (≈69 s, after a near-black shot at 68.9 s: a 0.5 s visual "breath"). Loudest 0.5 s at 89.7 s = under the title. Music out at 92 s; −30 LUFS on the end card. Lyrics carry the voice; no sports commentary measured as separate (not verified by listening).

What makes it premium:
- It is a music video first: a real single with an on-screen credit, the artist inside the film, cut on the song's pulse.
- Variety is the message: 117 shots, almost all different places, teams, traditions and people.
- One designed break (the sticker collage) gives a texture change without slowing the rhythm.
- The title arrives at the loudest point and sits over action, then a calm logo + date card ends it.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- Music: one licensed upbeat rock/pop track, 90–95 s edit, mastered loud (−12 to −14 LUFS) with a flat wall; end the song 3 s before the film ends.
- Cut grid: 0.6–0.8 s per shot, 12–19 cuts per 10 s, every 10–20 s an artist or "host" cutaway; no shot longer than 3 s except the title and end card.
- Credit: `.credit{position:absolute;left:10%;top:73%;font:500 26px/1.15 Inter;color:#fff}` with 3 lines, on 1.2–4.1 s, hard on/off.
- Collage break (5 s): 6–8 PNG cut-outs with white 6 px outline + `drop-shadow(0 6px 10px rgba(0,0,0,.4))`, each sliding in from an edge (`x ±40%→0`, 0.25 s `back.out(1.4)`), stacked every 0.6–0.8 s over a B&W crowd plate.
- Title: Anton 150 px caps (cap ≈14 % H), 2 lines, left 10 %, logo 400 px tall right; hard on at the music peak, keep cutting footage underneath for 4 s.
- End card: footage `brightness(.4)`, logo 430 px tall centred at 45 %, date line Montserrat 800 38 px caps; hold 4 s, music decays.
- Stock queries: "stadium aerial night fireworks", "football players tunnel walk out", "marching band stadium", "college football fans cheering", "mascot crowd celebration", "confetti trophy celebration slow motion".
