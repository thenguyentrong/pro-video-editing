# Apollo Tote Picking  (Apptronik, 2023-08-23, 0:48, 16:9, YouTube Apptronik)
URL: https://www.youtube.com/watch?v=SN3GQQCTY4Y
Purpose: capability demo (raw lab clip, published with the launch)
One-sentence point: Apollo lifts a tote from a bench, carries it and sets it back, again and again, while a person resets the task.

## Structure (studied from the sheet and metrics)
- One locked-off take, 0.0-48.2 s, no title, no logo.
- Cycle ≈15.5 s: reach and grip (0-3 s), lift and hold the tote at chest height (4-7 s), set down and release (8-9 s). Repeated at ≈19-22 s and ≈35-38 s (3 visible cycles).
- A person in a company T-shirt stands at frame left holding a tablet (from ≈8.5 s) and twice pushes the tote back into place by hand (≈10 s and ≈25 s) - a reset, also a small disturbance.

## Cut rhythm
- 1 shot, 0 cuts, 48.24 s. Both detectors agree (0 cuts).

## Typography
- None. No speed label, no autonomy label, no caption.

## Colour/grade
- Ungraded lab: grey wall with a diagonal shadow, grey totes, blue parts bins, white robot. Mean luma 0.30.

## Camera/shots
- Tripod, medium-wide, robot upper body + bench + all three totes in frame, eye level. The whole task area stays visible.

## Transitions
- None.

## Sound
- Silent: the file has an audio stream at digital silence (-70 LUFS measured, true peak -inf). No music, no room tone.

## What makes it credible
- One uncut take with three repeat cycles - the strongest proof format there is.
- A human resets the object by hand, so the starting pose changes slightly each cycle.

## What is unclear
- Real time is not stated (motion looks plausible for real time but is not verified).
- The person holds a tablet the whole time; the film does not say whether the robot runs autonomously, from a script, or is driven from that tablet.
- No sound removes the motor and contact noise that would help prove the speed.

## Recipe (real footage + HTML/GSAP)
- Tripod, medium-wide, lock exposure; record 3+ full task cycles without stopping (45-60 s).
- Keep the operator in frame but say what they do: corner label `AUTONOMOUS · 1X` or `TELEOPERATED · 1X` (Inter 600 2vh caps, top-right, `rgba(0,0,0,.55)` pill), set at 0 s and held for the whole take.
- Keep the room sound (motors, contacts) at about -30 LUFS instead of muting it.
