# Toy Story 5 | "Showdown Event" TV spot  (Walt Disney Studios Singapore, official regional channel, 23 Jun 2026, 30.1 s, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=UejxUxLNlko
Purpose: post-release TV spot ("in cinemas now"), regional version
One-sentence point: the epic toys-versus-tablet showdown is in cinemas now, be the first to see it.

## Structure (beats with timestamps; % of 30.1 s)
- 0.0–3.6 **cold open on action**: the cowgirl and horse leap, toys rush across the floor (6 shots, ASL 0.6 s), no logo.
- 3.6–5.1 **card built word by word**: "BE" → "BE THE FIRST" (1.5 s, at 12 %); each word appears in its final position, so the line grows from left to right.
- 5.1–7.2 4 shots (0.4–0.7 s). 7.2–8.1 **card "TO EXPERIENCE"** (0.9 s, 24 %).
- 8.1–10.8 5 shots (0.2–0.5 s). 10.8–12.3 **card "THE" → "THE / EPIC SHOWDOWN"** (1.5 s, 36 %).
- 12.3–24.3 **montage at ASL ≈0.6 s** (densest: 16 cuts in the first 10 s, 14 in the next 10 s): the tablet villain, a flame, a chase, toys in the garden, a small black dip at 14.0.
- 24.3–26.9 the villain tablet laughing (2.6 s, the longest story shot).
- 26.9–28.6 **title** "TOY STORY 5" with character cut-outs left and right (at 90 %). 28.6–30.1 "IN CINEMAS / NOW / TICKETS AVAILABLE NOW".

## Cut rhythm
- 39 shots (cards included, card builds counted as one shot). **ASL 0.77 s**, median 0.58 s.
- **82 % of shots under 1 s**; one shot over 3 s (the title/end block). 77.9 shots per minute, the fastest piece in the trailer set.
- Cuts per 10 s: 16 · 14 · 8. Shortest 0.21 s.
- Cuts on audio onsets 45 % vs 39 % chance (the music is busy: 2 onsets per second).
- Speech in ≈26 s of 30 s: short character lines over every few shots.

## Typography
- The tagline "BE THE FIRST / TO EXPERIENCE / THE EPIC SHOWDOWN" is split into three black cards (0.9–1.5 s each) between bursts of 4–6 shots.
- Condensed bold caps (closest free: Oswald 700), white on black; two sizes: small lead word ≈7.5 % H, main line ≈12–14 % H, centred at ≈40 % and ≈53 % H. (The main trailer uses a wider humanist face; regional spots change the type.)
- **Word-by-word build**: each new word cuts in at its final place, ≈0.4–1.1 s apart.
- End card: franchise logo centred with character renders at the frame edges; call to action in the same condensed caps.

## Colour / grade
Same animated palette as the trailer: warm bedroom, green tablet, dark blue garden at night.

## Camera / shots
Only action and reaction shots; no setup scenes. The villain gets the only held shot.

## Transitions
Hard cuts; cards on black; one short dip to black.

## Sound
- Integrated **−21.3 LUFS**, LRA 2.9 LU, true peak −5.5 dBTP: this regional upload is quiet and flat (≈7 LU below the main trailer), so its loudness is not a mastering target.
- No silences or drop-outs; small hits (+15…+18 dB) on the first card and the title.

## What makes it premium
- A three-card tagline that builds word by word keeps the energy of a 30 s spot.
- The villain gets the longest shot just before the title.
- The end card is a poster (logo plus characters), not a plain date.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. 0–3.6 s: 5–6 action shots of 0.4–0.7 s.
2. Card 1: put every word in a `<span>` at its final position with `opacity:0`; `tl.set(word,{opacity:1}, t + i*0.45)`; `font:700 120px Oswald; color:#fff; text-transform:uppercase` on `#000`.
3. Alternate: 4–6 shots (0.2–0.7 s), a card (0.9–1.5 s), three times.
4. 12 s montage at ≈0.6 s per shot, then one 2.5 s shot of the antagonist.
5. Title 1.7 s with character cut-outs at the edges, call to action 1.5 s.
6. Master −14 LUFS for web, true peak −1 dBTP (do not copy the −21 LUFS upload).
