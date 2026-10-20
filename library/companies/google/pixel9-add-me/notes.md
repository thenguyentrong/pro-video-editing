# Google Pixel 9 With Add Me  (Google, 22 Aug 2024, 0:30, 16:9, YouTube @madebygoogle)
URL: https://www.youtube.com/watch?v=x65VVs-aSUI
Purpose: ad (Pixel AI camera feature spot, Best Take / Magic Editor family)
One-sentence point: the photographer is always missing from the family photo - Add Me lets the others "leave the photo" so he can pop in.

## Structure
- 0-2.75 s name card: off-white background, a hand holds the phone centred, "Google" left, "Pixel 9" right. VO starts at 0.25 s: "This is the Google Pixel 9..."
- 2.75-7.15 s setup: over-the-shoulder POV, the phone frames mother + daughter in a park, shutter tap (4.5 s). VO "...and this is another family photo without the person taking the photo in it."
- 7.15-13.9 s the trick: locked-off wide of the two; from ~9 s they turn half-transparent ("could leave the photo"), ghost-like.
- 13.3-14.5 s: the father walks past very close to the lens - a body wipe (frame full of out-of-focus shirt colour), a hidden cut at 13.9 s.
- 14.5-19.9 s: father steps into the empty spot, the ghosts fade back to solid (17 s), all three pose, arms open.
- 19.9-25 s: back to POV, the merged photo on the phone screen. VO "I'll stop saying photo now. Pretty cool huh?"
- 25-28.35 s: phone slides out with a soft whip/blur into the end card "Pixel [phone in hand] 9 Pro".
- 28.35-30 s: Google "G" + "Learn more at GoogleStore.com" on off-white.

## Cut rhythm (cuts2 + 5 soft transitions added; 2 cut triggers inside the body wipe dropped)
- 8 shots, ASL 3.75 s, median 3.66 s. Quarters 2.50 / 3.75 / 2.50 / 2.50.
- 0% < 1 s, 62% > 3 s. Longest 6.7 s (7.15 s, the locked-off "leave the photo" wide), shortest 1.7 s (logo).
- 2-3 cuts per 10 s. Cuts on onsets 43% vs 59% chance: cut to the VO jokes, not the music.

## Typography
- Google Sans regular, dark grey on off-white #F5F3EF; name card words line ~13% H incl. descender (cap ~9% H), placed left/right of the hand-held phone. No other text except legal line and the URL (line 2.9-4% H).

## Colour / grade
- Natural daylight park, real greens, soft contrast; end cards warm off-white with a porcelain phone. Nothing stylised.
- 25% of samples >= 70% empty (all on light - the end cards).

## Camera / shots
- Real people, real location; locked-off tripod wide for the effect (needed for the ghost compositing); POV over-the-shoulder phone shots; product held by a real hand on the end cards.

## Transitions
- Body wipe (person crossing close to the lens) to hide the cut; opacity "ghost" fades as the effect; a blurred push out of the phone to the end card. Only 3 plain hard cuts.

## Sound
- Comic deadpan VO (one narrator, talks fast, self-aware joke "I'll stop saying photo now"), licensed song bed (captions: "Just Cool" by Obongjayar). Integrated -14.5 LUFS. Hits +26-30 dB at 1.3, 8.45, 24.1 s (song accents). Music ends 29.5 s.

## What makes it premium
- One feature, one human problem, one funny line - the joke carries it.
- The effect is shown in real time on real people, no UI clutter.
- Very few cuts; the long locked-off shot lets you watch the magic happen.

## Recipe (real footage + HTML/GSAP)
- Shoot a locked-off wide on a tripod: plate A (mother + child), plate B (father in place), clean plate. Composite: A at `opacity 1 -> 0.4` over 1.5 s (`power1.inOut`), then B fades in, then A back to 1.
- Hide a cut with a foreground body wipe (someone walks 0.5 m from the lens, 1 s).
- End card: off-white #F5F3EF, hand + phone centred, name split left/right, Google Sans/DM Sans 400 cap ~9% H, dark grey #3C4043; logo + URL card 1.7 s.
- VO: write a joke that names the problem plainly; cut on the punchlines; ASL ~3.5 s.
