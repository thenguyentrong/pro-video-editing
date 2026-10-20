# MKBHD (Marques Brownlee) — house style (creator tech reviews)

## Examples
| folder | title | analysed | shots | ASL / median | % < 1 s | LUFS |
|---|---|---|---|---|---|---|
| `xiaomi-18-fold/` | Xiaomi 18 Fold: How Does This Happen? (2026-10, 10:47) | first 300 s | 38 | 7.89 / 5.91 s | 2.6 | −17.9 |
| `nothing-headphone-1-pro/` | Nothing Headphone 1 Pro: They Copied the Wrong Thing! (2026-09, 14:20) | first 300 s | 43 | 6.98 / 6.11 s | 0 | −19.6 |
| `apple-watch-problem/` | The Apple Watch Has a Problem (2026-09, 15:06) | first 300 s (10 cuts added by eye) | 52 | 5.77 / 4.91 s | 3.8 | −20.0 |

## In one line
A calm, slow, very clean tech review: one person talking straight to camera for long takes, broken up by smooth, neutral-surface product shots in hand, with the primary source (a scale, a web page, the maker's keynote) as proof and almost no graphics.

## Sub-styles
1. **Silent-demo open review** (`xiaomi-18-fold`): music-only overhead hands-on take for ≈12 s before any voice, then a reveal line; rival comparison and press-release page as evidence.
2. **Thesis-first review** (`nothing-headphone-1-pro`): host on camera from 2.4 s, thesis in the first 10 s, a rival montage (1.3–2.7 s per product) as he lists the category, then physical tests (scale + spec card, macro, wearing outdoors) and long verdict takes (22–39 s).
3. **Analysis / commentary** (`apple-watch-problem`): products named over b-roll in sentence one, a two-part promise by ≈25 s, chapter title cards, article headlines and keynote clips as proof; two-angle talking head.

## Measured numbers (first 300 s each)
- ASL 5.77–7.89 s, median 4.91–6.11 s; 0–3.8 % of shots under 1 s; 71–90 % over 3 s; 7.6–10.4 shots/min.
- Cuts per 10 s: typical 1–2, peak 3–5 (rival montage 10–20 s; keynote payoff chapter). Never above 5.
- Longest shots are talking heads: 16.7–38.9 s; product takes up to 19.8 s (Xiaomi opening).
- Per-quarter ASL moves in both directions: the review slows towards the verdict (4.7 → 9.4 s), the analysis speeds up in its payoff chapter (8.3 → 3.6 s).
- Cuts sit on sentences, not beats: cut-on-onset 59–65 % vs 59–61 % chance.
- Loudness −17.9 to −20.0 LUFS integrated, LRA only 4.1–4.4 LU (steady, compressed voice), true peak −0.1 to −1.0 dBTP.
- Voice median −24.7 to −27.1 dBFS (50 ms RMS); p10 −53.5 to −54.5 dBFS → pauses 27–29 dB under the voice: no music bed under talking. 15–16 % of 50 ms windows below −45 dBFS.
- Frame 2:1 (854x428 at 480p), shown letterboxed in the 16:9 player.

## Hook (first 30 s)
Common pattern, measured in all three:
| time | beat |
|---|---|
| 0.0–2.4 s | channel logo sting (glossy red 3D logo strokes on black, shrinks to the mark, dip to black 1.5–2.4 s); loudest 0.5 s at 0.85 s in two films |
| 2.4–2.9 s | iris (circle) opens from the logo onto the first shot |
| 2.4–2.5 s | voice starts (2 of 3); the product and its category or rival are named in the first sentence. Exception: Xiaomi holds music-only hands-on until ≈14.9 s and names the product at ≈19.7 s |
| 2.4–13 s | first picture is the product in his hands (overhead/45° on a neutral desk) or the host to camera |
| 11–27 s | the stakes: a rival montage (5 cuts in 10 s), or a two-part promise with a twist ("the second one is surprising"), or a "this is not X, this is Y" reveal |
| 26–34 s | first proof or structure: a chapter title card (analysis), price + stakes on camera (review), a press-release or headline page soon after |
- Cuts in 0–30 s: 3 / 8 / 6. No sponsor, no subscribe ask, no lower third in the first 30 s. The title is never shown as a title card.

## Graphics restraint
- Most screen time has no added type at all (the Xiaomi film has none of its own in 300 s).
- Allowed graphics: one rounded white info card (spec list), one chapter title card per chapter, a small black source tag on borrowed footage.
- Evidence is shown whole and unstyled: the maker's press-release page with the cursor visible, an article headline full frame, an image-search wall of leaks, the maker's keynote with its own titles.

## Picture
- Talking head: locked off, centred, eye level, very shallow focus, one coloured set per film (deep red wall with toy-like props; dark studio with purple-pink light and mesh panels; bright office with a big plant). The analysis film cuts between a wide and a tight angle on sentence ends.
- Product: hands doing real actions on neutral surfaces (white desk, grey felt, blue desk) with one accent colour (orange keycaps); smooth, slow, motion-control-like moves; macro with very shallow focus; product as still life on a saturated single colour (red fabric, orange, pink).
- Physical tests on camera: kitchen scale, thickness, wearing outdoors.
- Clean, bright, natural grade; no grain, no film looks, no letterbox beyond the 2:1 frame.

## Sound
- Voice dry and up front; no music under talking.
- Music under product b-roll and montages only; the Xiaomi open is music-only with stop-start hits every ≈2.2 s and two 0.9 s digital silences.
- Borrowed clips keep their own sound and enter hard (+50 to +53 dB in 50 ms).

## Rules
1. Open with the 2.4 s channel sting and an iris onto the product or the host; no cold-open montage of other people.
2. Name the product in the first sentence (by 2.5 s) or after a silent demo of at most ≈15 s.
3. State the stakes by 25–30 s: the rival set, a twist promise, or the price.
4. Pace slow: ASL 5.8–7.9 s, median 4.9–6.1 s, at most 5 cuts per 10 s, under 4 % of shots shorter than 1 s.
5. Give the verdict to one long talking-head take (17–39 s).
6. Prove claims with objects and primary sources (scale, macro, the maker's page or keynote), not with motion graphics.
7. One accent colour per product set; neutral surfaces elsewhere.
8. Graphics: at most one info card style and one chapter-card style per film; credit borrowed footage with a small tag.
9. Mix: −18 to −20 LUFS integrated, LRA ≈4 LU, no bed under the voice.

## Recipe: real footage + HTML/GSAP (Hyperframes)
Layer stack: footage (2:1 inside 16:9, black bars 6.25 % H top and bottom) → optional chapter colour wash → card/tag → nothing else.
```css
:root{--wash-a:rgba(178,58,166,.75);--wash-b:rgba(59,44,156,.75)}
.frame{position:absolute;inset:6.25% 0;overflow:hidden}            /* 2:1 picture in 16:9 */
.wash{background:linear-gradient(90deg,var(--wash-a),var(--wash-b))}
.chapter{font:500 13.5vh/1 Oswald,sans-serif;color:#fff;text-transform:uppercase;letter-spacing:.01em;text-align:center}
.spec{position:absolute;left:4%;bottom:8%;background:rgba(255,255,255,.94);border-radius:2vh;padding:1.6vh 2.2vh;font:400 4.6vh/1.4 Inter;color:#1d1d1f}
.src{position:absolute;right:3%;bottom:4%;background:#000;color:#fff;font:800 2.6vh Inter;text-transform:uppercase;padding:.3em .8em;transform:skewX(-12deg)}
```
```js
// sting -> iris onto the first shot
tl.fromTo('.shot1',{clipPath:'circle(0% at 50% 50%)'},{clipPath:'circle(75% at 50% 50%)',duration:.5,ease:'power2.out'},2.4);
// slow product drift on the opening take
tl.fromTo('.shot1 video',{scale:1},{scale:1.04,duration:18,ease:'none'},2.4);
// chapter card: hard on, 4.4 s, hard off
tl.set('.chapter-card',{autoAlpha:1},t).set('.chapter-card',{autoAlpha:0},t+4.4);
// spec card pops in next to the scale, holds 5 s
tl.from('.spec',{autoAlpha:0,y:12,duration:.3,ease:'power2.out'},t2).set('.spec',{autoAlpha:0},t2+5);
```
Timing template (first 60 s): 0–2.4 sting → 2.4 iris → product in hand 6–11 s with the first sentence naming it → host on camera 4–14 s → stakes (rival montage of 5 shots × 1.3–2.7 s, or a two-part promise) by 25 s → chapter card 4.4 s or price on camera → first primary source (page, headline) 3–6 s → product test 4–7 s.

## Caveats
- Only the first 300 s of each film were measured; endings and sponsor reads (none appear before 300 s) are not covered.
- The scene detector missed 10 talking-head angle switches and screen changes in `apple-watch-problem` (added by eye). Jump cuts with identical framing inside long talking-head takes cannot be seen at 1 frame/s, so the longest-shot values may hide a few such cuts.
- Fonts are guesses (chapter card reads as a condensed grotesque; spec card as SF-Pro-like). Colours are eyeballed from 480p frames.
- Motion-control rig for product moves is inferred from the smoothness, not confirmed.
