# Meet Google Pixel 11 Pro | Attention-Grabbing. Not Attention-Seeking.  (Google, 12 Aug 2026, 0:30, 16:9, YouTube @madebygoogle)
URL: https://www.youtube.com/watch?v=1xw8-y4duDQ
Purpose: ad (hero product spot for the launch)
One-sentence point: three features (HiLight, Magic Capture, Gemini Intelligence) in 30 s, each as a calm product macro + one short sentence + one real proof shot - "Ask more of your phone."

## Structure
- 0-2.5 s name card: coral phone centred, "Google" left, "Pixel 11 Pro" right, tiny "with ✦ Gemini Intelligence" under; phone turns to its side (2.4 s) and wipes the card.
- 2.5-4.5 s promise: "Get more done." then "Be more present." appended on the same line (~3 s).
- 4.5-8.2 s HiLight: side macro of the camera bar, "Meet / HiLight" right (2 lines); LED glows teal (6-8 s).
- 8.2-9.7 s: "Screen calls without looking at your screen." - the sentence is revealed as the phone slides out of frame.
- 9.7-13.8 s Magic Capture: curved black glass pushes in (edge wipe), "Magic Capture" in white on the glass; "Capture video and photos at the same time." on coral.
- 13.8-18.3 s proof: real birthday footage with the capture frame overlaid, photo thumbnails pop out; three thumbnails on black (16.9 s).
- 18.3-21.1 s Gemini: "Gemini Intelligence" between out-of-focus camera-bar curves, blur-swaps into "Tap less. Do more." (19.5 s).
- 21.1-25.8 s proof: screen macro - notification "Did you book Cove Grill for 7PM?" -> Gemini OpenTable card -> finger taps "Confirm Reservation".
- 25.8-27.3 s: black, "Ask more of your phone." (warm grey text).
- 27.3-29.2 s: phone rises on black with reflection, same split name card.
- 29.2-30 s: Google "G" on black.

## Cut rhythm (cuts2 + 3 soft transitions added after checking by eye)
- 14 shots, ASL 2.15 s, median 1.97 s. Quarters 1.88 / 1.50 / 1.88 / 1.88 - flat.
- 7% < 1 s, 14% > 3 s. Longest 4.5 s (13.8 s, the party proof), shortest 0.79 s (logo).
- 3-5 cuts per 10 s. Cuts on onsets 46% vs 35% chance.

## Typography
- Google Sans (regular/medium), sentence case with full stops, centred, white on coral or warm grey on black.
- Sentence cards: line 5.8% H incl. descenders (cap ~3.5% H), 4-7 words, hold 1.5-2 s; text builds by appending the second sentence.
- Feature names larger: "Meet / HiLight" 2 lines ~8-10% H, "Magic Capture" ~6% cap, "Gemini Intelligence" line 5.6% H.
- End line "Ask more of your phone." line 10.4% H (cap ~6% H).
- Name card splits around the product: "Google" | phone | "Pixel 11 Pro" (line 10.4% H).
- Text change = blur dissolve (~0.3 s), not a cut.

## Colour / grade
- One colour world: coral-pink gradient (#E9B0AC centre, measured) + rose-gold phone, then black for the close. Party footage warm and natural.
- 15% of samples >= 70% empty (on dark); median empty share 54% - large calm areas.

## Camera / shots
- Product macros with very shallow focus (camera bar, curved glass), slow slides and rotations; one handheld real-life clip; one UI macro with a real finger.

## Transitions
- Product-edge wipes (the phone or glass curve crosses the frame), blur text swaps, UI thumbnails pop. No flashes, no whips.

## Sound
- Upbeat instrumental, no VO. Integrated -16.1 LUFS. Hits spread every 3-5 s (+16 dB at 11.45, 18.3, 25.15, 28.6 s) - one per feature.

## What makes it premium
- Apple-level restraint: one colour, one sentence per card, product macros, black close.
- Each feature = macro + one sentence + one real proof. Nothing else.
- The type is quiet; the product colour carries the brand.

## Recipe (real footage + HTML/GSAP)
- Background `radial-gradient(circle at 50% 45%, #F0C3BF, #D98F88)`; product macro footage or renders.
- Sentence card: Google Sans / DM Sans 400, cap 3.5% H, centred, white; `opacity 0 -> 1` 0.4 s; append sentence 2 after 0.6 s.
- Text swap: outgoing `filter: blur(0 -> 10px), opacity 1 -> 0` 0.3 s, incoming the reverse, overlap 0.15 s.
- Edge wipe: a product PNG slides across 0.5 s `power3.inOut` while the next shot is revealed behind its edge (`clip-path` follows the PNG x).
- ASL ~2 s, 30 s = 14 shots; close on black with a 6% H line, then name card, then logo 0.8 s. Mix -16 LUFS.
