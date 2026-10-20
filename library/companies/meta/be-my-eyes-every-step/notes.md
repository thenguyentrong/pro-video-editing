# Ray-Ban Meta & Be My Eyes: Every Step of the Way  (Meta, 10 Oct 2024, 1:56, 16:9, YouTube @meta)
URL: https://www.youtube.com/watch?v=YAGVg7b3bNc
Purpose: human demo / short documentary ("Community Voices story")
One-sentence point: a blind woman uses her glasses to call a sighted volunteer through three small everyday tasks, and ends up dancing at a salsa night.

## Structure (cut times from metrics.json)
- 0-6.2 s (5 %) cold open: 0.2 s black, then one 6 s extreme close-up of her eyes in soft focus; her interview voice starts at 2.9 s after 3.3 s of silence.
- 6.2-10.5 s: the glasses come out of the Ray-Ban case; she puts them on and smiles.
- 10.5-42.7 s (28 %) task 1, record player: wide of her sunny room, hands on the vinyl, macro of the glasses' camera, she says the wake phrase to call a volunteer; the volunteer's phone view appears as a 9:16 phone inset (≈3-4 s) on a blurred copy of the POV; real dialogue; the needle drops, music starts in the room.
- 42.7-64 s (18 %) task 2, mail: cane on a garden path, porch, she sorts envelopes; the volunteer reads a "Salsa Night" invitation.
- 64-83 s (16 %) task 3, outfit check: she dresses, glasses on, mirror; phone inset of the volunteer's view; "you look amazing" type reaction; she leaves the house.
- 83-108.7 s (22 %) payoff: candle-lit bar, friends, cocktails, salsa music takes over (+32.6 dB at 90.75 s), she dances and laughs; her interview voice closes the thought at 108 s.
- 108.7-113.9 s: picture dissolves to white, "A Community Voices story" (2 s), Meta logo (2 s), black.

## Cut rhythm
- 46 shots in 115.7 s, ASL 2.51 s, median 2.04 s, 2 % < 1 s, 20 % > 3 s, 24 shots/min.
- ASL per quarter 2.63 / 2.22 / 2.07 / 2.63 s: a gentle speed-up through the tasks, then longer holds for the dance.
- Cuts per 10 s: 3 / 4 / 3 / 5 / 5 / 4 / 3 / 4 / 6 / 5 / 2 / 1 - never more than 6.
- Longest: the end card block 9.1 s (104.7 s, includes the last dance shot), the opening eyes close-up 6.0 s, a mail close-up 5.0 s.
- Adaptive detector suggests 4 more cuts (19.4, 41.6, 102.9, 105.6 s); visually plausible (hand inserts), not added - ASL would be ≈2.3 s.
- Cuts on music onsets 53 % vs 47 % chance: cut on her sentences, not the beat.

## Typography
- No text during the story at all.
- End: "A Community Voices story" in grey (#5F6670-ish) regular sans with wide tracking (≈ +0.08 em), cap ≈4.4 % H, left-aligned at x ≈5.6 % W, vertically centred, on pure white, ≈2 s; then the Meta logo (infinity mark in blue gradient + black "Meta"), ≈10 % H tall, centred on white, ≈2 s. Closest free font: **Inter** / **Figtree** Regular (Meta uses Optimistic, proprietary).

## Colour / grade
- Warm natural daylight, soft contrast, shallow focus; green plants, cream walls, wood. Mean luma 0.32.
- Payoff at night: tungsten candle light, orange-amber with deep shadows; red dress and red cocktails as accents.
- End on white (brand), then black.

## Camera / shots
- Documentary: handheld and slow slider moves, long lenses, shallow focus; extreme close-ups of eyes, hands, the glasses' camera, the record needle.
- The product is always worn, never shown alone except one case shot and one macro of the frame.
- The glasses' POV video is shown inside a phone frame (the volunteer's screen): 9:16 inset ≈25 % W × 96 % H, centred, with call UI (red end-call button) on a blurred, darkened copy of the same view.

## Transitions
- Hard cuts; one dissolve to white at the end. The phone inset is cut in and out with no animation.

## Sound
- Her interview voice (not on camera) carries the film: ≈290 words in 115 s incl. dialogue, with pauses.
- Diegetic dialogue with the volunteers through the glasses is the demo; the wake phrase and the volunteer's greeting are heard clearly.
- Soft score under the story; the record in the room and then salsa music become the soundtrack (source music).
- Integrated −14.8 LUFS, LRA 8.3 LU, true peak −0.2 dBTP. 3.3 s silence at the start; small 0.3-0.5 s drops at 6.7, 13.8 and 34.65 s (breaths before a sentence or call). Biggest rise +32.6 dB at 90.75 s (salsa starts), loudest 83 s (bar).
- End cards with 1.3 s silence.

## What makes it premium
- The person is the hero; the product is only the way she reaches another person.
- Three small, real tasks, each shown fully (problem -> call -> answer -> done) with real dialogue.
- Phone inset makes the invisible (what the glasses see) visible without graphics.
- An emotional payoff that is not about the product at all (dance, friends), then a quiet brand end.

## Recipe (real footage + HTML/GSAP)
- Shoot 3 small tasks with one person, each 15-30 s: wide -> hands -> face -> device POV. Record a long interview; cut 1-2 sentences per task.
- Pace: ASL ≈2.3-2.5 s, at most 5-6 cuts per 10 s; open on one 5-6 s close-up in silence.
- POV inset: `position:absolute; left:50%; top:2%; width:25%; height:96%; transform:translateX(-50%); border-radius:18px; overflow:hidden` with the clip; behind it the same clip `filter: blur(18px) brightness(.7)`; red round end-call button 6 % W at 86 % H of the inset.
- Grade: warm daylight, `contrast(.95) saturate(1.05)`; night payoff in tungsten.
- End: white card, grey tracked line `font: 400 4.4vh Inter; letter-spacing:.08em; color:#5F6670; left:5.6%`, 2 s; logo card 2 s; dissolve to white 0.6 s.
- Mix ≈ −15 LUFS; voice on top, room sound real, let source music take over for the payoff.
