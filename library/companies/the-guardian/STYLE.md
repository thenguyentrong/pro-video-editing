# The Guardian — house style (video explainers)

## Examples
| Folder | Title | Analysed | Shots | ASL / median | Integrated loudness |
|---|---|---|---|---|---|
| us-midterms-explainer | US Midterms: What are they and why do presidents dread them? | full 3:37 | 41 | 5.29 / 3.64 s | -21.3 LUFS |
| journalist-ambulances-explainer | Israel bombed journalist at work and appeared to attack ambulances aiding her, NGOs say – explainer | full 3:33 | 52 | 4.09 / 3.48 s | -27.1 LUFS |
| spain-housing-face | How an 87-year-old Spanish woman became the face of the fight for affordable housing | full 2:49 | 57 | 2.97 / 2.76 s | -21.9 LUFS |

## In one line
Short (2.5-4 min) news explainers that put a real person or a real object first, use one colour (Guardian yellow) and one serif for every label, credit every borrowed frame top left, and cut calmly (no shot under 0.8 s, max 5 cuts per 10 s).

## Sub-styles
1. **Tabletop primer** (midterms): no presenter; every graphic is a real object on one black desk (paper labels, trading cards, a road map, tokens placed by stop-motion); news archive plays inside walnut "TV" props. Slowest (ASL 5.3 s, one 30 s set-up).
2. **Correspondent + evidence** (journalist/ambulances): a correspondent at a newsroom desk (two angles) is the guide; NGO reports, user video, a dark relief map with one yellow area, and the army's own posts with a yellow highlighter. Quiet mix (-27 LUFS), closes on a portrait grid held 13 s.
3. **Agency-footage explainer** (Spain housing): opens on the subject in her own voice (subtitled), a remote correspondent on a video call as guide (6 appearances, 2-7 s), all text as black serif on yellow boxes (names, demands, statistics). Fastest (ASL 3.0 s).

## Measured numbers
| | midterms | journalist | Spain |
|---|---|---|---|
| ASL quarters (s) | 4.17 / 5.43 / 4.52 / 6.03 | 3.32 / 3.32 / 4.43 / 4.84 | 2.82 / 2.35 / 3.25 / 3.02 |
| Shots < 1 s / > 3 s | 0 % / 59 % | 0 % / 56 % | 9 % / 39 % |
| Max cuts per 10 s | 4 | 5 (cold open) | 5 |
| Longest shot | 30.1 s tabletop list | 13.1 s portrait grid | 9.5 s opening testimony |
| Drop-outs | 8 × 0.3-1.5 s; 0.95 s and 1.5 s before chapters | 5 × 0.3-1.2 s | 4 × 0.4-0.65 s before chants |
| Loudness / LRA | -21.3 LUFS / 4.7 LU | -27.1 LUFS / 7.1 LU | -21.9 LUFS / 6.2 LU |
| Cuts on onsets | 50 % (chance 57 %) | 43 % (47 %) | 61 % (58 %) |

## Type & graphics
- Masthead: two-line serif "The Guardian" top right, ≈8 % H, white (sometimes at reduced opacity), always on.
- One serif family for all labels (Guardian Headline / Text Egyptian look; closest free "Merriweather" / "Source Serif 4").
- Credit: bold serif ≈2.4 % H, top left at x 5 % W ("Reuters", "Video provided", "Alamy", NGO names); an optional place line under it ≈3.3 % H.
- Lower third: no box; bold serif name ≈4 % H + regular serif role ≈3 % H ending in "| *The Guardian*" (italic), placed in the open side of the frame, ≈80-90 % H.
- Yellow cards (≈#FFE500): black bold serif, one box per line; keyword/stat cap ≈9 % H, name tag ≈4.3 % H; a number gets its own line.
- Highlighter: flat yellow over one phrase in a document or social post.
- Subtitles only for foreign speech: white sans ≈3.6 % H, no box, bottom ≈93 % H.
- Tabletop variant: bold sans caps on cream/navy/mint paper strips, physically lit.
- End credits: small serif, role bold ≈2.3 % H, flush left.

## Rules
1. Open on the person or the object, not on a title (testimony 9.5 s; archive inside a prop 10.7 s; agency footage 9 s).
2. Keep footage at 2.8-3.5 s median; never cut faster than 0.8 s; max 5 cuts per 10 s.
3. One accent colour (yellow) for every label, highlight and map fill. No second colour.
4. Credit every borrowed frame top left in the serif; leave other broadcasters' chyrons on.
5. The guide (correspondent) appears between evidence, 2-12 s at a time; for remote correspondents a webcam frame is enough.
6. Put statistics on top of the place they describe, one card per number, ≈5 s each.
7. Mark chapters with silence (0.4-1.5 s), then a loud re-entry.
8. End on the widest consequence (a portrait grid, a crowd) and hold it 7-13 s.

## Recipe (real footage + HTML/GSAP, Hyperframes)
```css
:root{--gyellow:#FFE500;--ink:#111}
.mast{position:absolute;right:3%;top:3%;font:700 4vh/0.9 "Merriweather",serif;color:#fff;text-align:right}
.credit{position:absolute;left:5%;top:5%;font:700 2.4vh "Merriweather",serif;color:#fff;text-shadow:0 1px 4px rgba(0,0,0,.5)}
.place{font:700 3.3vh "Merriweather",serif}
.lt{position:absolute;left:55%;bottom:10%;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.5)}
.lt .n{font:700 4vh "Merriweather"} .lt .r{font:400 3vh "Merriweather"} .lt .r i{font-style:italic}
.yc span{background:var(--gyellow);color:var(--ink);font:900 9vh/1.12 "Merriweather",serif;padding:0 1.2vh;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sub{position:absolute;bottom:5%;width:100%;text-align:center;font:600 3.6vh "Source Sans 3";color:#fff;text-shadow:0 1px 4px #000}
.hl{background:var(--gyellow)}
```
```js
// yellow card: hard on with the word, 4-5 s
tl.set(".yc",{autoAlpha:1},t).set(".yc",{autoAlpha:0},t+4.8);
// highlighter on a document line
tl.fromTo(".hl",{scaleX:0,transformOrigin:"left"},{scaleX:1,duration:.5,ease:"power2.out"},t2);
// tabletop stop-motion placement (cards appear, no tween)
cards.forEach((c,i)=>tl.set(c,{autoAlpha:1,rotation:gsap.utils.random(-4,4)},t3+i*.32));
```
Mix: voice ≈-18 to -20 LUFS short-term; bed ≈12 dB under (or none in the hardest stories); 0.4-1.5 s silence before chapters; master -21 LUFS (quiet investigations -27; web/social -16).

## Caveats
- Fonts are guesses (Guardian Headline/Egyptian are proprietary).
- In the tabletop film the clips inside the "TV" props change without a full-frame cut; the 41 shots count desk set-ups plus 6 verified inner cuts.
- Whether the journalist film has a music bed is not confirmed by ear (the numbers suggest little or none).
