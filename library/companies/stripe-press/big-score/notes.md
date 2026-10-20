# The Big Score: The Billion-Dollar Story of Silicon Valley  (Stripe / Stripe Press, 2021-04-20, 1:00, 16:9, YouTube / Stripe channel)
URL: https://www.youtube.com/watch?v=8E1TYPifmiM
Purpose: book trailer built as a micro-documentary (author interview recorded remotely + archive-style inserts)
One-sentence point: the tech industry did not begin with today's giants; it began with a few unusual people decades earlier, and the reissued book tells that story.

Structure:
- 0–3.0 PUBLISHER MARK: the looped-S monogram + "Stripe Press" in dark ink, centred on a flat burnt-orange ground (`#a8380f`-like). It draws on line by line (≈1 s).
- 3.0–17.35 AUTHOR: a webcam recording of the author in front of bookshelves, shown slightly zoomed with a rounded-screen look; name tag left of his head (bold name + "Author, *book title*" in italic), subtitles at the bottom. Two shots (8.6 s, 5.8 s); slow push-ins inside each (soft transition candidates every ≈0.7–1 s are the zoom).
- 17.35–28.2 INSERTS: a false-colour satellite map of the valley (purple water, cyan-green fields), slow drift (6.2 s); an aerial from a plane window over the valley (4.7 s). The author's voice continues over them.
- 28.2–49.8 AUTHOR AGAIN: 9.7 s, then a 13.7 s shot that pulls back to reveal the webcam feed is on a monitor on a desk in a bright room (the "remote interview" made physical).
- 49.8–51.6 white flash-out (score 5.3, the only stylised transition).
- 51.6–60.2 PACKSHOT CARD: the book cover (navy circuit-board pattern) at left-centre with a soft shadow on the same orange ground; italic title + author and "Now available for pre-order." at right (4.1 s), then the monogram draws again (4.5 s).

Cut rhythm: 10 shots in 60.3 s (9 real + a 2-frame tail), ASL 6.03 s, median 5.23 s (adaptive detector). Shots 3.0–13.7 s. Cuts per 10 s ≈1–2. 22 % of cuts on an audio onset vs 49 % by chance: cuts sit between the author's sentences.

Typography:
- Name tag: bold humanist sans name (closest free: Source Sans 3 700) cap ≈3 % H + role line regular/italic ≈2.3 % H, white, left of the face at x ≈7 %, y ≈48–53 %, no box.
- Subtitles: white sans ≈2.8 % H, bottom centre, for every spoken line (sound-off viewing).
- Packshot text: italic title + regular author name, ≈2.7 % H, white, left-aligned at x ≈76 %; CTA line one size below the title block.

Colour/grade: two worlds: the flat brand orange for open and end cards, and the author's warm webcam picture; inserts are false-colour satellite and natural aerial. 16:9.

Camera/shots: a remote webcam interview (low-res, bookshelves) treated with a slow digital push-in and a reveal of the monitor in a room; satellite image; plane-window aerial; book packshot render.

Transitions: hard cuts; one white flash into the packshot; the monogram draws itself.

Sound: (I could not listen; from level data.) Integrated -17.6 LUFS, LRA 15.9 LU (wide: voice vs music tail), true peak 0.0 dBTP (too hot). Voice-led at -17…-24 dBFS (2 s RMS); biggest rise +31.6 dB at 13.45 s; falls to -32…-38 dBFS under the packshot.

What makes it premium (and where it is limited):
- The remote-interview look is accepted and made physical (the monitor reveal) instead of hidden.
- One flat brand colour frames the film; the publisher mark is the only branding.
- Limits: low-res webcam picture and long talking-head holds; it works as a 60 s promo, not as a film. Use it as the minimum version of the founder mini-doc.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- Card ground `#a8380f`; mark drawn with SVG `stroke-dashoffset` 1 s, `power2.inOut`.
- Remote interview: scale the webcam clip to 110 %, `border-radius: 2vh` inner screen look, push `scale 1.1 → 1.16` over each 6–9 s hold; name tag `700 3vh "Source Sans 3"` + `italic 400 2.3vh`, fade 0.4 s, hold 4 s.
- Two inserts of 5–6 s each over the voice (satellite map with a false-colour `hue-rotate(200deg) saturate(1.6)` grade, a plane-window aerial).
- Last interview shot: start full-frame and pull back to the clip playing on a monitor in a room (`scale 1 → .55` over 10 s, `power1.inOut`, composite the clip into a monitor photo).
- White flash 0.4 s, packshot card 4 s, mark 4 s. Master -16 to -18 LUFS, true peak ≤ -1 dBTP.
- Stock queries: `silicon valley satellite`, `airplane window view city aerial`, `computer monitor on desk bright room`, `bookshelf background`.
