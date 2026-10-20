# Introducing Linear Diffs  (Linear, 2026-05-28, 51.9 s, 16:9, YouTube / web)
URL: https://www.youtube.com/watch?v=7gZBxBTapDQ
Purpose: launch film (software feature, rendered-UI product film)
One-sentence point: Code review now happens inside Linear: open the diff from the issue, read it, ask an agent to change it, approve.

Structure: beats with timestamps
- 0.0-6.7 hook: sidebar macro (Inbox, Pulse, Reviews), the cursor lands on "Reviews"; tilted list of reviews.
- 6.7-15.0 open: a diff in red/green sweeps past in a long diagonal move; macro on the issue header with tabs (Activity / Guide / Diff), the "Guide" pill highlights.
- 15.0-25.3 read: flat, almost frontal split view (explanation left, diff right), the view scrolls through files; the longest shot (10.3 s).
- 25.3-27.6 act: macro on a purple "Submit review" button. Music steps up here (≈+8 dB).
- 27.6-40.8 change: close-up of code, an agent prompt is typed into a comment box, the agent's reply appears, the code updates.
- 40.8-44.1 approve: Approve + Submit review buttons over the changed code.
- 44.1-47.3 tagline card on black (fades in over ≈2 s, fades out 0.5 s).
- 47.3-51.9 logo mark + wordmark on black, 0.9 s silent tail.

Cut rhythm (verified)
- Scene detection 0 cuts (mean luma 0.06); adaptive 8, all real hard cuts between camera set-ups. Two added by eye: 44.1 s (0.4 s dip to black into the tagline card) and 47.25 s (cut to the logo).
- 11 shots, ASL 4.72 s, median 3.73 s, 0 % under 1 s, 73 % over 3 s, 12.7 shots/min. Per quarter 3.24 / 4.33 / 4.33 / 3.24. Range 2.2-10.3 s.

Typography
- UI type only in the body (the product's own sans and a code mono), seen in perspective. Red/green diff colour is the main graphic.
- Tagline card: one line, white, regular weight, centred at ≈50 % H; line box ≈10.4 % H incl. descender (cap ≈7 % H), 51 % of the width. 3 words. Fade in ≈2 s, hold ≈0.5 s at full, fade out ≈0.5 s.
- Logo: mark + "Linear" wordmark, centred, line box ≈10 % H, 23 % of the width, hard cut in, hold 4.6 s.
- Closest free font: Inter (400 for the tagline, 500-600 for the wordmark); code: JetBrains Mono or Geist Mono.

Colour/grade
- Black world (#000), UI greys, diff colours green ≈#2ea043 / red ≈#c93c37 at reduced opacity, one purple accent ≈#5e6ad2 (Linear's indigo) on buttons. Deep vignette, the UI falls off into black at the frame edges.

Camera/shots
- 100 % rendered UI in 3-D space: tilted macros (≈20-35°), one frontal wide, long diagonal tracking moves, rack focus on button macros. No people, no device.

Transitions
- Hard cuts between set-ups; one fast dip to black (0.4 s) into the end card. Scrolling and typing happen inside shots.

Sound
- No voice. Electronic music bed in two halves: ≈−20 dBFS RMS for 0-24 s, then a lift to ≈−12 dBFS from the "Submit review" macro (≈25 s) to 44 s, then down under the end card. No drop-outs.
- Integrated −13.9 LUFS, loudness range 7.6 LU, true peak +0.1 dBTP. Cuts are not on onsets (0 % vs 2 % chance): picture follows the camera moves, not the beat.

What makes it premium
- The UI is photographed like a product: tilt, depth of field, darkness, slow tracking.
- A clear verb chain (open → read → change → approve) with no explaining text.
- One music lift at the midpoint exactly on the action button.
- A 3-word tagline as the only line of copy.

Recipe (Hyperframes, 1920×1080)
- Same 3-D card build as the Linear Agent recipe; colour the diff lines with `rgba(46,160,67,.25)` / `rgba(201,60,55,.25)` backgrounds.
- 9 body shots of 2-10 s: macro (2-3 s) → long diagonal track (6-10 s) → macro → frontal wide (10 s) → button macro (2.3 s) → typing close-up (4-9 s) → approve (3 s).
- Music: two-part bed; place the lift (+6 to +8 dB) on the action shot at ≈50 % of the runtime.
- End: 0.4 s dip to black, tagline `400 5vh Inter` fade-in 2 s (`opacity` only), fade out 0.5 s, hard cut to logo for 4.5 s; master −14 LUFS.
