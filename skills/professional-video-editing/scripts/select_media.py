#!/usr/bin/env python3
"""Rank candidate images/clips for ONE shot, the way an editor picks selects.

Usage:
  python select_media.py <file>[@x,y,w,h] ... --frame 1920x1080 [--zoom 1.08] [--at 2.0]
                         [--focus 0.5,0.45] [--look dark|bright] [--sheet selects.jpg] [--json]

  file@x,y,w,h  the part of the source the shot will really show (0..1 of width/height), e.g.
                photo.jpg@0.25,0.05,0.4,0.9 when the robot fills only that part. Always give it when
                the subject is small in a wide photo: that crop is where blown-up softness hides.

For every candidate it simulates how the shot will really be used: scaled to cover the output
frame (--frame), then pushed in by --zoom (the largest scale your move reaches), cropped around
--focus (x,y as 0..1 of the source, default centre). Videos are sampled at --at seconds
(default: middle). Then it measures:

  upscale    output pixels per source pixel after crop + zoom. <= 1.0 = real detail; > 1.0 the
             shot is blown up; > 1.15 is visibly soft on a 1080p screen (not a hero shot).
             A file that was already upscaled or re-cropped before (an old export) hides its
             softness here; the sharp value catches it.
  sharp      detail at OUTPUT scale (variance of the Laplacian on a 1:1 crop of the subject area).
             < 40 soft, 40-120 ok, > 120 crisp (content dependent: fog, sky and bokeh read low).
  clutter    how busy the frame edges are (edge density of the outer ring), how many strong
             different hues fight in the frame (stage lights, signage, costumes) and how much of
             the frame is loud saturated colour (patterned carpet, purple stage light).
             0 = calm, 1 = very busy. > 0.55 = distracting background.
  exposure   mean luma 0..255, % clipped highlights, % crushed shadows.
  fit_look   distance of the frame's mean colour/brightness from the --look (dark|bright|any).

Verdict per candidate: HERO (fit for a held hero shot), USE (fine for a short or small shot),
WEAK (only if nothing else exists), REJECT. A ranked table is printed, and --sheet writes a
labelled contact sheet so you look at the picks side by side before you choose. The numbers
never replace looking; they stop you from defaulting to the first image you found.

Needs ffmpeg/ffprobe on PATH. Standard library only.
"""
import argparse, json, math, os, subprocess, sys


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height:format=duration", "-of", "json", path],
                         capture_output=True, text=True).stdout
    d = json.loads(out or "{}")
    s = (d.get("streams") or [{}])[0]
    dur = float((d.get("format") or {}).get("duration") or 0)
    return int(s.get("width", 0)), int(s.get("height", 0)), dur


def grab(path, at, vf, w, h, pix="gray"):
    cmd = ["ffmpeg", "-v", "error"]
    if at is not None:
        cmd += ["-ss", f"{at:.3f}"]
    cmd += ["-i", path, "-frames:v", "1", "-vf", vf, "-f", "rawvideo", "-pix_fmt", pix, "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    need = w * h * (3 if pix == "rgb24" else 1)
    return raw[:need] if len(raw) >= need else None


def plan(sw, sh, fw, fh, zoom, focus):
    """Source rectangle that ends up on screen (cover + zoom around focus)."""
    scale = max(fw / sw, fh / sh) * zoom
    cw, ch = fw / scale, fh / scale
    cx = min(max(focus[0] * sw, cw / 2), sw - cw / 2)
    cy = min(max(focus[1] * sh, ch / 2), sh - ch / 2)
    return scale, int(cx - cw / 2), int(cy - ch / 2), int(cw), int(ch)


def laplacian_var(g, w, h):
    vals, n, s, s2 = [], 0, 0.0, 0.0
    for y in range(1, h - 1):
        row = y * w
        for x in range(1, w - 1):
            i = row + x
            v = 4 * g[i] - g[i - 1] - g[i + 1] - g[i - w] - g[i + w]
            s += v; s2 += v * v; n += 1
    m = s / n
    return s2 / n - m * m


def edge_density(g, w, h, inner):
    """Fraction of strong gradients in the outer ring vs inside the centre box."""
    o = c = on = cn = 0
    x0, y0, x1, y1 = inner
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            i = y * w + x
            e = abs(g[i + 1] - g[i - 1]) + abs(g[i + w] - g[i - w]) > 60
            if x0 <= x < x1 and y0 <= y < y1:
                cn += 1; c += e
            else:
                on += 1; o += e
    return o / max(on, 1), c / max(cn, 1)


def hue_clutter(rgb, n):
    bins = [0] * 12
    strong = 0
    for i in range(0, n * 3, 3):
        r, g, b = rgb[i] / 255, rgb[i + 1] / 255, rgb[i + 2] / 255
        mx, mn = max(r, g, b), min(r, g, b)
        if mx < 0.25 or mx - mn < 0.35:
            continue
        strong += 1
        d = mx - mn
        if mx == r:
            hh = ((g - b) / d) % 6
        elif mx == g:
            hh = (b - r) / d + 2
        else:
            hh = (r - g) / d + 4
        bins[int(hh * 2) % 12] += 1
    loud = strong / n  # share of the frame in strong, saturated colour
    if strong < n * 0.02:
        return 0.0, 0, loud
    used = sum(1 for v in bins if v > strong * 0.08)
    return min(1.0, (used - 1) / 4) * min(1.0, strong / (n * 0.25)), used, loud


def analyse(spec, a):
    fw, fh = a.frame
    path, box = spec, None
    if "@" in spec and not os.path.isfile(spec):
        path, b = spec.rsplit("@", 1)
        box = [float(v) for v in b.split(",")]
    sw, sh, dur = probe(path)
    if not sw:
        return {"file": path, "verdict": "REJECT", "why": ["unreadable (not an image/video?)"], "score": 0}
    at = a.at if a.at is not None else (dur / 2 if dur > 0.5 else None)
    if box:  # crop the box first, then cover the frame from it
        bx, by, bw, bh = int(box[0] * sw), int(box[1] * sh), int(box[2] * sw), int(box[3] * sh)
        scale, x, y, cw, ch = plan(bw, bh, fw, fh, a.zoom, (0.5, 0.5))
        x += bx; y += by
    else:
        scale, x, y, cw, ch = plan(sw, sh, fw, fh, a.zoom, a.focus)
    upscale = scale  # output px per source px
    # 1:1 detail crop of the subject area at output scale (480x270 of the final frame)
    dw, dh = 480, 270
    vf = f"crop={cw}:{ch}:{x}:{y},scale={fw}:{fh}:flags=bicubic,crop={dw}:{dh}:{int(fw*0.5-dw/2)}:{int(fh*0.45-dh/2)}"
    g = grab(path, at, vf, dw, dh)
    sharp = laplacian_var(g, dw, dh) if g else 0
    # whole-frame stats on a small version
    tw, th = 192, int(192 * fh / fw)
    vf2 = f"crop={cw}:{ch}:{x}:{y},scale={tw}:{th}"
    g2 = grab(path, at, vf2, tw, th)
    rgb = grab(path, at, vf2, tw, th, "rgb24")
    n = tw * th
    outer, centre = edge_density(g2, tw, th, (int(tw * .3), int(th * .25), int(tw * .7), int(th * .8)))
    hc, hues, loud = hue_clutter(rgb, n)
    clutter = min(1.0, 0.5 * min(1.0, outer / 0.22) + 0.25 * hc + 0.25 * min(1.0, loud / 0.3))
    mean = sum(g2) / n
    clip = sum(1 for v in g2 if v > 250) / n * 100
    crush = sum(1 for v in g2 if v < 6) / n * 100
    why = []
    if upscale > 1.15: why.append(f"blown up {upscale:.2f}x")
    elif upscale > 1.0: why.append(f"slightly blown up {upscale:.2f}x")
    if sharp < 40: why.append("soft at output size")
    if clutter > 0.55: why.append("busy background" + (f" ({hues} competing colours)" if hues > 2 else " (edges/pattern)"))
    if loud > 0.3: why.append(f"loud colour behind the subject ({loud*100:.0f}% saturated)")
    if clip > 3: why.append(f"{clip:.0f}% clipped")
    if crush > 25: why.append(f"{crush:.0f}% crushed")
    if a.look == "dark" and mean > 140: why.append("too bright for a dark film")
    if a.look == "bright" and mean < 90: why.append("too dark for a bright film")
    bad = (upscale > 1.15) + (sharp < 40) + (clutter > 0.55) + (clip > 8)
    if upscale > 1.6 or sharp < 15 or bad >= 3: verdict = "REJECT"
    elif bad == 2: verdict = "WEAK"
    elif bad == 1 or why: verdict = "USE"
    else: verdict = "HERO"
    score = (min(1.0, 1 / max(upscale, 0.01)) * 30 + min(sharp, 200) / 200 * 30 + (1 - clutter) * 30
             + (10 - min(10, clip + crush / 3)))
    return {"file": path, "source": f"{sw}x{sh}", "upscale": round(upscale, 2), "sharp": round(sharp),
            "clutter": round(clutter, 2), "luma": round(mean), "clip_pct": round(clip, 1),
            "crush_pct": round(crush, 1), "score": round(score, 1), "verdict": verdict, "why": why,
            "_crop": (x, y, cw, ch), "_at": at}


def find_font():
    windir = os.environ.get("WINDIR", r"C:\Windows")
    cands = [os.path.join(windir, "Fonts", f) for f in ("arial.ttf", "segoeui.ttf")] + [
        "/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans.ttf"]
    f = next((c for c in cands if os.path.isfile(c)), None)
    return f.replace("\\", "/").replace(":", "\\:") if f else None


FONT = find_font()


def sheet(results, a):
    fw, fh = a.frame
    tw = 480; th = int(tw * fh / fw)
    tiles = []
    for k, r in enumerate(results):
        if "_crop" not in r:
            continue
        x, y, cw, ch = r["_crop"]
        label = f"{k+1}. {r['verdict']} {r['score']}  up {r['upscale']}x  sharp {r['sharp']}  busy {r['clutter']}"
        label = label.replace(":", "\\:")
        tiles.append((r, x, y, cw, ch, label))
    if not tiles:
        return
    inputs, filters = [], []
    for i, (r, x, y, cw, ch, label) in enumerate(tiles):
        if r["_at"] is not None:
            inputs += ["-ss", f"{r['_at']:.3f}"]
        inputs += ["-i", r["file"]]
        ff = f"fontfile='{FONT}':" if FONT else ""
        filters.append(f"[{i}:v]crop={cw}:{ch}:{x}:{y},scale={tw}:{th},pad={tw}:{th+28}:0:0:black,"
                       f"drawtext={ff}text='{label}':x=8:y={th+7}:fontsize=15:fontcolor=white[t{i}]")
    cols = min(3, len(tiles)); rows = math.ceil(len(tiles) / cols)
    layout = "|".join(f"{(i % cols) * tw}_{(i // cols) * (th + 28)}" for i in range(len(tiles)))
    if len(tiles) == 1:
        fc = ";".join(filters) + ";[t0]null[o]"
    else:
        fc = ";".join(filters) + ";" + "".join(f"[t{i}]" for i in range(len(tiles))) + \
             f"xstack=inputs={len(tiles)}:layout={layout}:fill=black[o]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[o]",
                    "-frames:v", "1", a.sheet], check=False)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("files", nargs="+")
    p.add_argument("--frame", default="1920x1080", help="output frame WxH (default 1920x1080)")
    p.add_argument("--zoom", type=float, default=1.0, help="largest push-in the shot reaches (e.g. 1.08)")
    p.add_argument("--focus", default="0.5,0.5", help="subject centre in the source, x,y in 0..1")
    p.add_argument("--at", type=float, default=None, help="time for video candidates (default middle)")
    p.add_argument("--look", choices=["any", "dark", "bright"], default="any")
    p.add_argument("--sheet", default=None, help="write a labelled contact sheet (jpg)")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    a.frame = tuple(int(v) for v in a.frame.lower().split("x"))
    a.focus = tuple(float(v) for v in a.focus.split(","))
    res = [analyse(f, a) for f in a.files]
    res.sort(key=lambda r: (["HERO", "USE", "WEAK", "REJECT"].index(r["verdict"]), -r.get("score", 0)))
    if a.sheet:
        sheet(res, a)
    if a.json:
        print(json.dumps([{k: v for k, v in r.items() if not k.startswith("_")} for r in res], indent=1))
        return
    print(f"{'#':>2} {'verdict':7} {'score':>5} {'source':>10} {'up':>5} {'sharp':>5} {'busy':>5} {'luma':>4}  file / why")
    for k, r in enumerate(res):
        print(f"{k+1:>2} {r['verdict']:7} {r.get('score',0):>5} {r.get('source',''):>10} {r.get('upscale',0):>5} "
              f"{r.get('sharp',0):>5} {r.get('clutter',0):>5} {r.get('luma',0):>4}  {os.path.basename(r['file'])}"
              + (f"  [{'; '.join(r['why'])}]" if r.get("why") else ""))


if __name__ == "__main__":
    main()
