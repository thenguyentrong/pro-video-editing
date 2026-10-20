# Unitree Robotics - style

Examples (official @UnitreeRobotics uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [h2-destiny-awakening](h2-destiny-awakening/notes.md) | 2025-10 | 0:50 | 13 | 3.84 s | 2.12 s | humanoid launch teaser: one-take dance orbit → runway montage |
| [a2-stellar-explorer](a2-stellar-explorer/notes.md) | 2025-08 | 2:07 | 23 | 5.52 s | 5.32 s | quadruped field film: one stunt or spec per real take, speed labels |
| [wvla-conference-room-cleanup](wvla-conference-room-cleanup/notes.md) | 2026-05 | 3:31 | 3 (one 208.8 s take) | 70.5 s | - | AI-model test: one take + split screen with robot cams and logs |
| [ai-model-manufactures-robots](ai-model-manufactures-robots/notes.md) | 2026-02 | 0:45 | 4 (two takes 22.7 + 19.4 s) | 11.2 s | 10.8 s | factory proof: raw sound, "real, not AI, 2x" label |

Shot counts include Unitree's 0.32 s thumbnail frame at the start and the 1.6-2.4 s disclaimer end card.

## Sub-styles
1. **Launch teaser (humanoid):** the product does its most fluid move in one long gimbal orbit (13.9 s), then a fast montage (1-2 s) beside a human, one CGI beat, end card. No text apart from the title frame. Music very loud (-6.9 LUFS).
2. **Field film (quadruped):** 5-9 s real takes in hard terrain (quarry, scree, slopes, stairs), one stunt or number per take, flat ASL ≈5.5 s all film long, labels top-left, a speed statement on frame 1 and a labelled time-lapse for the endurance claim.
3. **Model test:** a single uncut 3-4 minute take, third-person view beside the robot's own camera feeds and live logs. Title frame, then no edit at all.
4. **Factory clip:** two 20 s takes of real assembly, raw line sound (-27.9 LUFS, no music), a one-line honesty label.

## House rules
- **Thumbnail frame:** every film studied opens with 8 frames (0.32 s) of a title card with a purple/gold or purple/cyan gradient title. It works as the YouTube preview frame, then the film starts on real footage.
- **Disclaimer end card:** UNITREE wordmark (≈18 % H) over 5 lines of safety text (≈2.3-3.3 % H): extreme testing, do not imitate, features vary, understand the limits before buying. No CTA, no URL.
- **Speed is stated in words, sentence case, in the picture:** "No Speed-Up in This Video", "Only This Part 100+× Speed-Up", "Real factory footage, not AI-generated, 2x speed". Top-left or bottom-left, ≈4.5-6 % H, white, no box. Much bigger than the US "2X" badges (≈2 % H).
- **Spec = `Label: value UNIT`** in the same frame as the thing measured (1 m block, 100 kg man, 30 kg plate), sometimes with a white arrow or a dotted measuring line.
- **No voice-over, no interviews, no named people.** Music carries the brand films; the factory clip uses raw sound.
- **Price is part of the product name** in upload titles ("Price from $16K", "from $4,900", "from $650,000"); none of the four films studied puts a price on screen.
- **Spectacle first:** dance, martial arts, flips, glass-breaking, fashion runway, combat events. Proof films (model test, factory) are a separate, plainer track.

## How they show a real machine working / keep it credible
- Long takes: 13.9 s dance orbit, 14.2 s labelled time-lapse, 19.4-22.7 s factory takes, one 208.8 s model test.
- Honest speed labelling is the strongest Unitree habit: a global "no speed-up" claim, plus the exact factor on any part that is sped up.
- The "not AI-generated" claim is written on screen (answering doubts about generated video).
- Machine view: in the model test, robot camera feeds + inference logs share the frame with the third-person view for the whole take.
- **Autonomy vs teleoperation is almost never labelled.** Stunt and dance films say nothing about how the motion is made; the model test implies autonomy through its title and logs but has no "autonomous" or "1x" label; Unitree also publishes full-body teleoperation demos on the same channel, so a viewer cannot assume autonomy.
- People are props for scale and stress (jumping on the robot, walking beside it, moving the bin), never speakers.

## Compared with US/EU makers (studied: Boston Dynamics, Figure, Tesla, ABB, Siemens)
- US/EU: claims by named people or careful captions, small "Autonomous" / "2X" corner labels, datasheet cards, restrained music. Unitree: no people speaking, large plain-English sentence labels, spectacle stunts, loud music, a legal disclaimer card instead of a CTA.
- US/EU proof films rarely state "real footage"; Unitree and AgiBot both write "not AI / no CGI" on screen.
- Unitree releases many short films (0:30-1:00) at high frequency; the launch film is a teaser, not a spec film.

## Recipe (real footage + HTML/GSAP)
1. One claim per take, 5-9 s, full body + measured object in frame; for a stunt add a person for scale.
2. Labels: `font: 500 6vh Inter; left:2vw; top:3vh; color:#fff; text-shadow:0 1px 6px rgba(0,0,0,.5)`; on frame 1 "No speed-up in this video"; swap the text only on sped-up parts (`tl.set(lbl,{textContent:'Only this part 100x speed-up'},t)`).
3. Spec: `Climb height: 1 m` at 5vh, plus an SVG arrow (2 px, white) to the object.
4. For a model or software claim: one uncut take, `grid-template-columns:61fr 39fr`, right side = 2x2 robot camera feeds + a real log panel (JetBrains Mono 1.5vh).
5. Add what Unitree leaves out: a "1x · autonomous" or "teleoperated" corner label, and a mastering target of -14 LUFS (theirs reach -6.9 to -9.9 LUFS with true peaks above 0 dBTP).
