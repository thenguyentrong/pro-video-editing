# How an 87-year-old Spanish woman became the face of the fight for affordable housing | Explainer  (The Guardian, uploaded 2026-10-03 per yt-dlp, 2:49, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=4J6160hChbk
Purpose: explainer (news explainer from agency footage, remote correspondent as guide)
One-sentence point: The eviction of one elderly tenant in Madrid turned years of rising rents into a national protest movement and forced the government to respond.

Analysed: the full film (169 s).

Structure:
- 0.0-9.5 cold open: the woman herself speaks Spanish at a protest, subtitled (one 9.5 s shot, the longest).
- 9.5-15 her name on a yellow label over a wheelchair shot; four quick cuts 12.2-14.9 s (0.8-0.9 s, posters with her name).
- 15-46 what happened: the eviction (police, stretcher, ambulance), then protest crowds chanting, subtitled ("Murderers! Murderers!").
- 46-48 contrast: a property-investment conference banner.
- 48-53 the guide: European correspondent on a remote video call (beige wall), lower third.
- 53-70 the camp in Puerta del Sol (wide aerials, tents, night), correspondent again.
- 70-74 the demands as yellow keyword boxes over the crowd ("Rent freezes", "Automatic renewals of contracts").
- 74-84 her building and the plaque.
- 89-104 the numbers: four stat cards over b-roll, two lines of text + a percentage, each held ≈5 s: Spain rent +80 %, Spain house prices +63 %, EU property prices +53 %, EU rent +25 % (EU flags, a new-build street).
- 105-133 the response: correspondent, camp, government press conference, parliament.
- 134-162 protests montage (the densest stretch is 30-70 s; 144-162 s is cut at ≈2-4 s).
- 162-169 credits over a crowd shot.

Cut rhythm: 57 shots in 169 s, ASL 2.97 s, median 2.76 s, 9 % under 1 s, 39 % over 3 s, 20.2 shots/min. ASL per quarter 2.82 / 2.35 / 3.25 / 3.02 s. Cuts per 10 s: 1, 4, 3, 5, 4, 5, 5, 2, 3, 2, 3, 4, 4, 3, 3, 4, 1. Longest 9.5 s (open), 6.9 s (credits), 5.9 s. Shortest 0.8 s.

Typography:
- Masthead: "The Guardian" two-line serif top right, ≈8 % H, white, partly transparent.
- Credit top left, bold serif ≈2.4 % H: "Reuters", "Alamy", "JNA/ZUMA Press Wire/Shutterstock"; a place line under it in bold white serif ≈3.3 % H ("Barcelona").
- Name label: bold serif in black on a tight yellow box (≈#FFE500), cap ≈4.3 % H, lower centre-right.
- Keyword and stat cards: bold serif (Guardian Headline look; closest free "Merriweather" Black / "Source Serif 4" Black) in black on yellow, one box per line, cap ≈9 % H, centred in the open part of the frame; the number on its own line in the same size ("+80%").
- Lower third: as in the other Guardian films, no box, white serif name ≈4 % H bold + role ≈3 % H with italic masthead.
- Subtitles: white sans (Guardian Text Sans look; closest free "Open Sans"/"Source Sans 3"), ≈3.6 % H, centred at ≈93 % H, no box, used only for Spanish speech and chants.
- Credits: small serif, role bold ≈2.3 % H, flush left at x 5 % W, bottom half, masthead below.

Colour/grade: agency footage kept as shot (bright Madrid daylight, sodium nights); the only graphic colour is Guardian yellow with black text.

Camera/shots: agency footage (handheld street, aerials of the square), stills from photo agencies, one remote interview (webcam-like framing, beige wall), press-conference and parliament feeds.

Transitions: hard cuts only. Yellow cards appear with a hard cut-on (no animation visible at 1 fps).

Sound: integrated -21.9 LUFS, LRA 6.2 LU, true peak -2.5 dBTP. Correspondent VO + natural sound of chants; 4 short drop-outs (0.4-0.65 s at 38.0, 47.2, 51.75 and 63.85 s) that set up a loud re-entry (+43 to +48 dB from the gap floor); the loudest moment is the woman's own voice in the first second (-16.1 dBFS RMS). Cuts sit at chance on onsets (61 % vs 58 %).

What makes it premium:
- It opens on the person, in her own voice, before any explanation.
- One colour and one font do every job: names, demands and statistics are all black serif on yellow.
- Statistics are put on top of the place they describe (rent number over the protest camp), held long enough to read twice.
- A remote correspondent is enough as a guide when the footage is strong; she appears 6 times, 2-7 s each.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Cold open: one subject shot 8-10 s with subtitles `font:600 3.6vh "Source Sans 3"; bottom:5%; text-align:center; color:#fff; text-shadow:0 1px 4px #000`.
- Yellow card: `.yc span{background:#FFE500;color:#111;font:900 9vh/1.12 "Merriweather",serif;padding:0 1.2vh;box-decoration-break:clone;-webkit-box-decoration-break:clone}`; hard on, hold 4-5 s; number on its own line.
- Name tag: same, `4.3vh`, one line.
- Credit: `font:700 2.4vh "Merriweather"; left:5%; top:5%`; place line `3.3vh` under it.
- Cut agency footage at 2.5-3 s (median 2.8 s); a 4-cut burst of 0.8-0.9 s shots after the name; guide clips 2-7 s.
- Mix: VO about -18 LUFS short-term, chants up to -14 dBFS; 0.4-0.65 s silences before a new chant or section; master -22 LUFS (web: -16).
