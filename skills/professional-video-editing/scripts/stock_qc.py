#!/usr/bin/env python3
"""Stock footage / photo quality gate: decides ACCEPT, ACCEPT-WITH-NOTES or REJECT for one clip.

    python stock_qc.py <file-or-URL> [--json] [--out result.json] [--photo] [--max-seconds 20]
                       [--meta-duration S] [--allow-vertical] [--ua UA]

Output: a one-line verdict plus REJECT / NOTE / info lines on stdout, or the full metrics as
JSON (--json to stdout, --out to a file). stock_find.mjs calls it with --json for every download.
Needs Python 3.8+ (standard library only) and ffmpeg + ffprobe on PATH (with vidstabdetect,
blurdetect and scdet, i.e. a "full" build). URLs are read with range requests, no full download.

Video checks (verdict ACCEPT / ACCEPT-WITH-NOTES / REJECT):
  resolution   REJECT below 1920x1080 (landscape) ; prefer >= 2560x1440, best 4K
  frame rate   REJECT below 23.976 ; note 48/50/60 (slow-mo headroom) and VFR
  bitrate      warn below ~8 Mbit/s at 1080p / ~20 Mbit/s at 4K (H.264-equivalent,
               scaled for HEVC/VP9/AV1 and fps) ; REJECT below 40 % of that (starved)
  duration     REJECT below 4 s
  codec        notes (VP9/AV1/webm -> transcode for the NLE, 10-bit, HDR transfer)
  interlacing  REJECT if ffprobe field_order or ffmpeg idet says interlaced
  letterbox    cropdetect ; REJECT if the active picture cropped to 16:9 is < 1080 lines
  shakiness    vidstabdetect motion vectors -> high-pass residual of the camera path
  sharpness    Laplacian variance (sharpest tile, 1080-normalised) + ffmpeg blurdetect
               + /2 round-trip PSNR (detail at native resolution; catches soft/upscaled 4K)
  exposure     % clipped highlights / crushed blacks on sampled frames (notes only)
  watermark    edges that keep their sign in every sampled frame while the picture moves
               (static overlay). REJECT only for a bright text-like band across the middle
               (classic stock-preview watermark); bright corner mark = note; locked-off camera
               (block matching) = inconclusive, because static scene parts look the same
  cuts/freeze  scdet + freezedetect (notes)
  AI metadata  container tags mentioning Sora/Veo/Runway/Kling/C2PA etc. (note)
Photo variant (--photo, or auto for jpg/png/webp/tif): REJECT if long side < 2400 px;
prefer >= 3840 (4K frame without upscale), sharpness, exposure, JPEG compression.
"""
import json
import math
import os
import re
import shutil
import statistics as st
import subprocess
import sys
import tempfile

BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")
PHOTO_EXT = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp", ".heic", ".avif"}
AI_WORDS = re.compile(r"\b(sora|veo|runway|kling|hailuo|luma ?ai|pika|midjourney|firefly|dall-?e|"
                      r"stable diffusion|c2pa|synthid|ai[- ]generated|generated (by|with) ai)\b", re.I)

# ---------------------------------------------------------------- helpers

def run(args, cwd=None, binary=False, timeout=600):
    p = subprocess.run(args, cwd=cwd, capture_output=True, timeout=timeout)
    if binary:
        return p.stdout, p.stderr.decode("utf-8", "replace"), p.returncode
    return p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace"), p.returncode


def in_args(src, ua):
    """ffmpeg/ffprobe input options for a file or URL."""
    if re.match(r"^https?://", src):
        return ["-user_agent", ua, "-reconnect", "1", "-reconnect_streamed", "1", "-i", src]
    return ["-i", src]


def frac(s):
    try:
        if "/" in str(s):
            a, b = str(s).split("/")
            return float(a) / float(b) if float(b) else 0.0
        return float(s)
    except Exception:  # noqa: BLE001
        return 0.0


def ffprobe(src, ua):
    args = ["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams"]
    if re.match(r"^https?://", src):
        args += ["-user_agent", ua]
    out, err, rc = run(args + [src], timeout=180)
    if rc != 0 or not out.strip():
        raise RuntimeError("ffprobe failed: " + err.strip()[:300])
    return json.loads(out)


def gray_frame(src, ua, t, vf, w, h):
    """One gray full-range frame as bytes (len w*h) or None."""
    args = ["ffmpeg", "-hide_banner", "-v", "error", "-ss", f"{t:.3f}"] + in_args(src, ua) + [
        "-frames:v", "1", "-vf", vf + ",format=gray", "-f", "rawvideo", "-pix_fmt", "gray", "pipe:1"]
    data, _, rc = run(args, binary=True, timeout=180)
    if rc != 0 or len(data) < w * h:
        return None
    return data[: w * h]


def even(x):
    return max(2, int(round(x / 2.0)) * 2)

# ---------------------------------------------------------------- pixel maths (pure Python)

def laplacian_var(buf, w, h, x0, y0, tw, th):
    """Variance of the 4-neighbour Laplacian inside a tile of a gray frame."""
    s = 0.0
    s2 = 0.0
    n = 0
    for y in range(y0 + 1, y0 + th - 1):
        r = y * w
        ru = r - w
        rd = r + w
        for x in range(x0 + 1, x0 + tw - 1):
            v = buf[r + x - 1] + buf[r + x + 1] + buf[ru + x] + buf[rd + x] - 4 * buf[r + x]
            s += v
            s2 += v * v
            n += 1
    if n == 0:
        return 0.0
    m = s / n
    return s2 / n - m * m


def sharpness_tiles(buf, w, h):
    """Laplacian variance on a 4x3 grid of tiles; returns (max, median)."""
    vals = []
    tw, th = w // 4, h // 3
    # use the middle 60 % of each tile to keep it cheap in pure Python
    for gy in range(3):
        for gx in range(4):
            x0 = gx * tw + tw // 5
            y0 = gy * th + th // 5
            vals.append(laplacian_var(buf, w, h, x0, y0, tw * 3 // 5, th * 3 // 5))
    return max(vals), st.median(vals)


def exposure_stats(frames):
    """frames: list of gray full-range bytes. Returns averages in %."""
    clip_hi, crush, means = [], [], []
    for f in frames:
        n = len(f)
        hi = sum(1 for v in f if v >= 250)
        lo = sum(1 for v in f if v <= 4)
        clip_hi.append(100.0 * hi / n)
        crush.append(100.0 * lo / n)
        means.append(sum(f) / n)
    return {
        "clipped_highlights_pct": round(st.mean(clip_hi), 2),
        "clipped_highlights_max_pct": round(max(clip_hi), 2),
        "crushed_blacks_pct": round(st.mean(crush), 2),
        "crushed_blacks_max_pct": round(max(crush), 2),
        "mean_luma": round(st.mean(means), 1),
    }


def watermark_check(frames, w, h, active=None):
    """Static overlay detector. frames: >= 8 gray frames (w x h) spread over the clip.
    Signed-gradient temporal median (idea from Dekel et al., CVPR 2017): as the picture moves,
    scene gradients change sign and cancel out; an overlay's edges keep the same sign in every
    frame. A pixel counts as 'overlay-like' if its median signed gradient is >= 75 % of its mean
    absolute gradient, there is an edge (>= 12 levels), AND the picture around it changes over
    time (neighbour std >= 5), which excludes static scene parts (e.g. the centre of a push-in)."""
    k = len(frames)
    if k < 8:
        return {"status": "skipped", "reason": "too few frames"}
    x_lo, y_lo, x_hi, y_hi = 2, 2, w - 2, h - 2
    if active:  # exclude letterbox bars
        ax, ay, aw, ah = active
        x_lo, y_lo = max(x_lo, ax + 2), max(y_lo, ay + 2)
        x_hi, y_hi = min(x_hi, ax + aw - 2), min(y_hi, ay + ah - 2)
    mid = k // 2
    gx_n, gy_n = 8, 6
    tw, th = w / gx_n, h / gy_n
    tiles = [[0, 0, 0, 0.0, 0.0] for _ in range(gx_n * gy_n)]  # [hits, dynamic, n, hit_luma, tile_luma]
    dyn_total = 0
    n_total = 0
    for y in range(y_lo, y_hi):
        r = y * w
        ti_y = min(gy_n - 1, int(y / th))
        for x in range(x_lo, x_hi):
            i = r + x
            t = tiles[ti_y * gx_n + min(gx_n - 1, int(x / tw))]
            vals = [f[i] for f in frames]
            mn = sum(vals) / k
            t[2] += 1
            t[4] += mn
            n_total += 1
            if sum((v - mn) ** 2 for v in vals) / k > 36:  # std > 6 levels: picture changes here
                t[1] += 1
                dyn_total += 1
            gx = [f[i + 1] - f[i - 1] for f in frames]
            gy = [f[i + w] - f[i - w] for f in frames]
            mabs = (sum(abs(a) for a in gx) + sum(abs(b) for b in gy)) / k
            if mabs < 12:
                continue
            gx.sort()
            gy.sort()
            if abs(gx[mid]) + abs(gy[mid]) < 0.75 * mabs:
                continue
            nb = [(f[i - 1] + f[i + 1] + f[i - w] + f[i + w]) * 0.25 for f in frames]
            nm = sum(nb) / k
            if sum((a - nm) ** 2 for a in nb) / k < 25:
                continue
            t[0] += 1
            t[3] += mn
    dyn_frac = dyn_total / max(1, n_total)
    cam = camera_motion(frames, w, h)
    dens = {}
    for idx, t in enumerate(tiles):
        if t[2]:
            dens[idx] = t[0] / t[2]
    base = st.median(dens.values()) if dens else 0.0
    elevated = {i for i, d in dens.items() if d >= 0.10 and d >= 3 * base + 0.05}
    flagged = []
    for i in sorted(elevated):
        gx_, gy_ = i % gx_n, i // gx_n
        t = tiles[i]
        bright = (t[3] / max(1, t[0])) - (t[4] / t[2]) > 10
        corner = gy_ in (0, gy_n - 1) and gx_ in (0, 1, gx_n - 2, gx_n - 1)
        flagged.append({"tile": i, "density": round(dens[i], 3), "where": tile_name(gx_, gy_, gx_n, gy_n),
                        "corner": corner, "bright": bright})
    # classic stock-preview watermark: a bright, text-like band of >= 3 adjacent tiles in the middle rows
    band = False
    for gy_ in range(1, gy_n - 1):
        run = []
        for gx_ in range(gx_n + 1):
            i = gy_ * gx_n + gx_
            if gx_ < gx_n and i in elevated:
                run.append(i)
                continue
            if len(run) >= 3 and sum(1 for f in flagged if f["tile"] in run and f["bright"]) >= 2:
                band = True
            run = []
    corner_logo = [f for f in flagged if f["corner"] and f["bright"] and f["density"] >= 0.12]
    res = {"dynamic_fraction": round(dyn_frac, 2), "baseline_density": round(base, 4), "flagged_tiles": flagged,
           "camera": cam}
    if cam.get("locked_off"):
        res["status"] = "inconclusive"
        res["reason"] = "locked-off camera: static scene parts look like an overlay"
    elif dyn_frac < 0.35:
        res["status"] = "inconclusive"
        res["reason"] = "camera and scene mostly static, cannot separate overlay from scene"
    elif len(elevated) > 14:
        res["status"] = "inconclusive"
        res["reason"] = "many persistent edges (slow or static footage)"
    elif band:
        res["status"] = "strong"
        res["pattern"] = "bright text-like band across the middle"
    elif corner_logo:
        res["status"] = "weak"
        res["pattern"] = "bright static mark in a corner (logo bug?)"
    elif flagged:
        res["status"] = "minor"  # static edges, no bright band/corner mark: usually scene parts
        res["pattern"] = "static edges"
    else:
        res["status"] = "clear"
    return res


def _half(f, w, h):
    w2, h2 = w // 2, h // 2
    out = bytearray(w2 * h2)
    for y in range(h2):
        r0 = 2 * y * w
        r1 = r0 + w
        for x in range(w2):
            out[y * w2 + x] = (f[r0 + 2 * x] + f[r0 + 2 * x + 1] + f[r1 + 2 * x] + f[r1 + 2 * x + 1]) >> 2
    return bytes(out), w2, h2


def _zero_shift_blocks(a, b, w, h, R=4, bx=4, by=3):
    """Block matching (zero-mean SAD, +-R px) between two frames; counts textured blocks whose
    best shift is within +-1 px, i.e. parts of the picture that did not move."""
    bw, bh = w // bx, h // by
    zero = tex = 0
    for j in range(by):
        for i in range(bx):
            x0, y0 = i * bw + R, j * bh + R
            x1, y1 = (i + 1) * bw - R, (j + 1) * bh - R
            pa = [a[y * w + x] for y in range(y0, y1, 2) for x in range(x0, x1, 2)]
            ma = sum(pa) / len(pa)
            if (sum((p - ma) ** 2 for p in pa) / len(pa)) ** 0.5 < 10:
                continue
            tex += 1
            best = None
            for dy in range(-R, R + 1):
                for dx in range(-R, R + 1):
                    pb = [b[(y + dy) * w + x + dx] for y in range(y0, y1, 2) for x in range(x0, x1, 2)]
                    mb = sum(pb) / len(pb)
                    sad = sum(abs((p - ma) - (q - mb)) for p, q in zip(pa, pb))
                    if best is None or sad < best[0]:
                        best = (sad, dx, dy)
            if abs(best[1]) <= 1 and abs(best[2]) <= 1:
                zero += 1
    return zero, tex


def camera_motion(frames, w, h):
    """Locked-off test on first/middle/last sampled frames (half of the 384-px analysis size)."""
    if len(frames) < 3:
        return {"locked_off": False, "reason": "too few frames"}
    a, w2, h2 = _half(frames[0], w, h)
    m, _, _ = _half(frames[len(frames) // 2], w, h)
    b, _, _ = _half(frames[-1], w, h)
    z1, t1 = _zero_shift_blocks(a, m, w2, h2)
    z2, t2 = _zero_shift_blocks(m, b, w2, h2)
    f1 = z1 / t1 if t1 else 0.0
    f2 = z2 / t2 if t2 else 0.0
    return {"locked_off": max(f1, f2) >= 0.5, "static_blocks": [f"{z1}/{t1}", f"{z2}/{t2}"]}


def tile_name(gx, gy, nx, ny):
    v = "top" if gy < ny / 3 else ("bottom" if gy >= ny * 2 / 3 else "middle")
    hz = "left" if gx < nx / 3 else ("right" if gx >= nx * 2 / 3 else "center")
    return f"{v}-{hz}"

# ---------------------------------------------------------------- video passes

def motion_pass(src, ua, seconds, fps):
    """One decode of the first `seconds`: idet, cropdetect, vidstabdetect, signalstats,
    freezedetect, scdet. Returns dict."""
    tmp = tempfile.mkdtemp(prefix="qc_")
    try:
        vf = ("idet,cropdetect=limit=0.1:round=2:reset=0,scale=640:-2,"
              "vidstabdetect=result=t.trf:shakiness=8:accuracy=9:fileformat=1,"
              "freezedetect=n=0.002:d=1.5,scdet=threshold=12,"
              "metadata=mode=print:file=meta.txt")
        args = ["ffmpeg", "-hide_banner", "-nostats", "-loglevel", "info", "-t", f"{seconds:.2f}"] + \
            in_args(src, ua) + ["-an", "-vf", vf, "-f", "null", "-"]
        _, err, rc = run(args, cwd=tmp, timeout=1200)
        out = {"window_s": seconds}
        ms = re.findall(r"Multi frame detection:\s*TFF:\s*(\d+)\s*BFF:\s*(\d+)\s*Progressive:\s*(\d+)\s*Undetermined:\s*(\d+)", err)
        if ms:  # ffmpeg 8 prints a dummy all-zero summary first; the last one is real
            tff, bff, prog, und = map(int, ms[-1])
            out["idet"] = {"tff": tff, "bff": bff, "progressive": prog, "undetermined": und}
        crops = re.findall(r"crop=(\d+):(\d+):(\d+):(\d+)", err)
        if crops:
            out["crop"] = tuple(map(int, crops[-1]))
        # vidstab: per-frame median local motion
        trf = os.path.join(tmp, "t.trf")
        vx, vy = [], []
        if os.path.exists(trf):
            with open(trf, "r", encoding="ascii", errors="ignore") as fh:
                for line in fh:
                    if not line.startswith("Frame"):
                        continue
                    lms = re.findall(r"\(LM (-?\d+) (-?\d+) ", line)
                    if len(lms) >= 6:
                        xs = sorted(int(a) for a, _ in lms)
                        ys = sorted(int(b) for _, b in lms)
                        vx.append(xs[len(xs) // 2])
                        vy.append(ys[len(ys) // 2])
                    else:
                        vx.append(None)
                        vy.append(None)
        out["shake"] = shake_metric(vx, vy, 640, fps)
        meta = os.path.join(tmp, "meta.txt")
        cuts, freezes = [], []
        if os.path.exists(meta):
            txt = open(meta, "r", encoding="utf-8", errors="ignore").read()
            cuts = [float(x) for x in re.findall(r"lavfi\.scd\.time=([\d.]+)", txt)]
            freezes = [float(x) for x in re.findall(r"lavfi\.freezedetect\.freeze_duration=([\d.]+)", txt)]
        out["cuts"] = [round(c, 2) for c in cuts if c > 0.2]
        out["freeze_s"] = round(sum(freezes), 2)
        out["ffmpeg_rc"] = rc
        return out
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def shake_metric(vx, vy, width, fps):
    """High-frequency residual of the camera path, in % of frame width per frame.
    Smooth pans/drone moves have a smooth velocity -> small residual; handheld jitter -> large."""
    pts = [(a, b) for a, b in zip(vx, vy) if a is not None]
    if len(pts) < 12:
        return {"status": "unknown", "frames": len(pts)}
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    win = max(3, int(round((fps or 25) * 0.4)) | 1)  # ~0.4 s centred moving average of velocity
    half = win // 2

    def resid(v):
        out = []
        for i in range(len(v)):
            lo, hi = max(0, i - half), min(len(v), i + half + 1)
            out.append(v[i] - sum(v[lo:hi]) / (hi - lo))
        return out
    rx, ry = resid(xs), resid(ys)
    rms = math.sqrt(sum(a * a + b * b for a, b in zip(rx, ry)) / len(rx))
    speed = st.mean(math.hypot(a, b) for a, b in zip(xs, ys))
    return {"status": "ok", "jitter_pct": round(100.0 * rms / width, 3),
            "mean_speed_pct": round(100.0 * speed / width, 3), "frames": len(pts)}


def detail_pass(src, ua, t, w, h):
    """One frame: /2 lanczos round-trip PSNR at native resolution (luma), blurdetect on a
    1080-normalised copy (its thresholds were calibrated at 1080p; native 4K reads ~1 point
    blurrier), plus a 1080-normalised gray frame for the Laplacian."""
    norm = "scale=-2:1080:flags=area" if w >= h else "scale=1080:-2:flags=area"
    fc = ("[0:v]format=gray,split=3[a][b][d];"
          "[b]scale=iw/2:ih/2:flags=lanczos,scale=iw*2:ih*2:flags=lanczos[c];[a][c]psnr[p];"
          f"[d]{norm},blurdetect[e]")
    args = ["ffmpeg", "-hide_banner", "-nostats", "-ss", f"{t:.3f}"] + in_args(src, ua) + [
        "-filter_complex", fc, "-map", "[p]", "-frames:v", "1", "-f", "null", "-",
        "-map", "[e]", "-frames:v", "1", "-f", "null", "-"]  # -frames is per output
    _, err, _ = run(args, timeout=300)
    blur = re.search(r"blur mean:\s*([\d.]+)", err)
    psnr = re.search(r"PSNR y:([\d.]+|inf)", err)
    res = {"blur": float(blur.group(1)) if blur else None,
           "rt2_psnr": (99.0 if psnr and psnr.group(1) == "inf" else float(psnr.group(1))) if psnr else None}
    # 1080-normalised gray frame
    if w >= h:
        nh = min(1080, h)
        nw = even(w * nh / h)
    else:
        nw = min(1080, w)
        nh = even(h * nw / w)
    buf = gray_frame(src, ua, t, f"scale={nw}:{nh}:flags=area:out_range=full", nw, nh)
    if buf:
        mx, md = sharpness_tiles(buf, nw, nh)
        res["lap_max"] = round(mx, 1)
        res["lap_median"] = round(md, 1)
    return res

# ---------------------------------------------------------------- main QC

def qc_video(src, ua, max_seconds=20.0, meta_duration=None, allow_vertical=False):
    info = ffprobe(src, ua)
    vs = [s for s in info.get("streams", []) if s.get("codec_type") == "video"
          and not (s.get("disposition") or {}).get("attached_pic")]
    if not vs:
        raise RuntimeError("no video stream")
    v = vs[0]
    fmt = info.get("format", {})
    w, h = int(v.get("width", 0)), int(v.get("height", 0))
    rot = 0
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd:
            rot = int(abs(float(sd["rotation"]))) % 180
    if rot == 90:
        w, h = h, w
    afr = frac(v.get("avg_frame_rate"))
    rfr = frac(v.get("r_frame_rate"))
    fps = afr or rfr
    dur = float(fmt.get("duration") or v.get("duration") or 0)
    full_dur = float(meta_duration) if meta_duration else dur
    codec = v.get("codec_name", "?")
    pix = v.get("pix_fmt", "")
    vbr = frac(v.get("bit_rate")) or 0
    if not vbr:
        tot = frac(fmt.get("bit_rate"))
        abr = sum(frac(s.get("bit_rate")) for s in info["streams"] if s.get("codec_type") == "audio")
        vbr = max(0.0, tot - abr) if tot else 0
        if not vbr and dur and fmt.get("size"):
            vbr = 8 * float(fmt["size"]) / dur
    tags = " ".join(f"{k}={val}" for k, val in {**(fmt.get("tags") or {}), **(v.get("tags") or {})}.items())

    R = {"source": src, "kind": "video", "width": w, "height": h, "fps": round(fps, 3),
         "duration_s": round(dur, 2), "codec": codec, "profile": v.get("profile"), "pix_fmt": pix,
         "video_bitrate_mbps": round(vbr / 1e6, 2), "field_order": v.get("field_order"),
         "color_transfer": v.get("color_transfer"), "container": fmt.get("format_name"),
         "size_mb": round(float(fmt.get("size", 0)) / 1e6, 1) if fmt.get("size") else None,
         "has_audio": any(s.get("codec_type") == "audio" for s in info["streams"]),
         "reasons": [], "notes": [], "info": [], "metrics": {}}
    rej, warn, inf = R["reasons"], R["notes"], R["info"]
    if meta_duration and abs(full_dur - dur) > 1:
        inf.append(f"file is a {dur:.0f}s excerpt of a {full_dur:.0f}s clip")

    # resolution
    longs, shorts = max(w, h), min(w, h)
    px = w * h
    if h > w and not allow_vertical:
        rej.append(f"vertical {w}x{h} (not usable in a 16:9 film; --allow-vertical to override)")
    if longs < 1910 or shorts < 1075:
        rej.append(f"resolution {w}x{h} below 1920x1080")
        tier = "SD/HD"
    elif px >= 3840 * 2160 * 0.95:
        tier = "4K+"
        inf.append(f"{w}x{h}: 4K, room to reframe/punch in")
    elif px >= 2560 * 1440 * 0.95:
        tier = "QHD"
        inf.append(f"{w}x{h}: above 1080p, some room to reframe")
    else:
        tier = "FHD"
        warn.append(f"{w}x{h}: 1080p only, no headroom to reframe or stabilise")
    R["tier"] = tier

    # frame rate
    if fps < 23.9:
        rej.append(f"frame rate {fps:.2f} below 24")
    elif fps >= 47:
        inf.append(f"{fps:.2f} fps: slow-motion headroom ({fps / 25:.1f}x at 25p, {fps / 24:.1f}x at 24p)")
    if rfr and afr and abs(rfr - afr) / max(rfr, afr) > 0.02:
        warn.append(f"variable frame rate (r={rfr:.2f}, avg={afr:.2f}): phone-style footage, convert to CFR")
    R["fps_family"] = "24" if abs(fps - 24) < 0.1 or abs(fps - 23.976) < 0.05 else (
        "25/50" if abs(fps % 25) < 0.05 else ("30/60" if abs(fps - 30) < 0.1 or abs(fps - 29.97) < 0.05 or abs(fps - 60) < 0.1 or abs(fps - 59.94) < 0.05 else "other"))

    # bitrate (H.264 reference: 8 Mbit/s @1080p, 20 @2160p; exponent from those two points)
    eff = {"h264": 1.0, "hevc": 0.6, "vp9": 0.65, "av1": 0.5, "prores": 3.0, "dnxhd": 3.0,
           "mpeg4": 1.4, "mpeg2video": 2.0, "mjpeg": 4.0}.get(codec, 1.0)
    thr = 8e6 * (px / (1920 * 1080)) ** 0.661 * max(0.9, math.sqrt(min(max(fps, 24), 60) / 30.0)) * eff
    R["metrics"]["bitrate_threshold_mbps"] = round(thr / 1e6, 1)
    if vbr:
        ratio = vbr / thr
        R["metrics"]["bitrate_ratio"] = round(ratio, 2)
        if ratio < 0.4:
            rej.append(f"bitrate {vbr / 1e6:.1f} Mbit/s is starved for {w}x{h} {codec} (wanted >= {thr / 1e6:.0f})")
        elif ratio < 1.0:
            warn.append(f"low bitrate {vbr / 1e6:.1f} Mbit/s (wanted >= {thr / 1e6:.0f} for {w}x{h} {codec}): banding/blocking risk when graded")

    # duration
    if full_dur < 4:
        rej.append(f"duration {full_dur:.1f}s below 4s")
    elif full_dur > 120:
        inf.append(f"long clip ({full_dur:.0f}s): pick a section")

    # codec / colour
    if codec in ("vp9", "av1", "vp8", "theora") or (fmt.get("format_name") or "").startswith(("matroska", "ogg")):
        inf.append(f"{codec} in {fmt.get('format_name')}: transcode to ProRes/DNxHR or H.264 before editing")
    if "10" in pix or "12" in pix:
        inf.append(f"{pix}: 10/12-bit, good for grading")
    if (v.get("color_transfer") or "") in ("smpte2084", "arib-std-b67"):
        warn.append(f"HDR transfer ({v.get('color_transfer')}): needs tone mapping in an SDR timeline")
    if AI_WORDS.search(tags):
        warn.append("container metadata mentions an AI generator / C2PA: " + AI_WORDS.search(tags).group(0))

    # analysis passes
    win = min(max_seconds, dur) if dur else max_seconds
    mp = motion_pass(src, ua, win, fps)
    R["metrics"]["motion_pass"] = {k: mp[k] for k in mp if k not in ("crop",)}
    fo = (v.get("field_order") or "").lower()
    idet = mp.get("idet")
    interlaced = fo in ("tt", "bb", "tb", "bt")
    if idet:
        il = idet["tff"] + idet["bff"]
        tot = il + idet["progressive"]
        if tot and il > 0.35 * tot and il > 20:
            interlaced = True
    if interlaced:
        rej.append(f"interlaced (field_order={fo or '?'}, idet={idet}): deinterlacing halves vertical detail")

    active = None
    if mp.get("crop"):
        cw, ch, cx, cy = mp["crop"]
        top, bottom = cy, h - ch - cy
        left, right = cx, w - cw - cx
        lb = top > 0.02 * h and bottom > 0.02 * h and abs(top - bottom) <= max(8, 0.01 * h)
        pb = left > 0.02 * w and right > 0.02 * w and abs(left - right) <= max(8, 0.01 * w)
        if lb or pb:
            aw, ah = (w if not pb else cw), (h if not lb else ch)
            active = (0 if not pb else cx, 0 if not lb else cy, aw, ah)
            # the 16:9 area you can cut out of the active picture
            fill_h = min(ah, aw * 9 / 16)
            R["metrics"]["active_picture"] = f"{aw}x{ah}"
            msg = f"baked-in {'letterbox' if lb else 'pillarbox'} bars, active picture {aw}x{ah}"
            if fill_h < 1075:
                rej.append(msg + f": filling a 16:9 frame leaves only {fill_h:.0f} lines")
            else:
                warn.append(msg + ": crop/zoom to fill 16:9")

    sh = mp.get("shake", {})
    if sh.get("status") == "ok":
        j = sh["jitter_pct"]
        if j >= 0.6:
            rej.append(f"very shaky camera (jitter {j:.2f}% of width per frame)")
        elif j >= 0.25:
            warn.append(f"handheld shake (jitter {j:.2f}% of width per frame): stabilise or use as handheld style")
    if mp.get("cuts"):
        warn.append(f"contains {len(mp['cuts'])} cut(s) at {mp['cuts'][:5]}s: use one shot only")
    if mp.get("freeze_s", 0) >= 1.5:
        warn.append(f"frozen / duplicated frames for {mp['freeze_s']}s")

    # sampled frames
    t0, t1 = 0.05 * dur, 0.95 * dur
    n_low = 16
    times = [t0 + (t1 - t0) * i / (n_low - 1) for i in range(n_low)] if dur > 1 else [0.0]
    lw, lh = (384, even(384 * h / w)) if w >= h else (even(384 * w / h), 384)
    low = [f for f in (gray_frame(src, ua, t, f"scale={lw}:{lh}:flags=area:out_range=full", lw, lh) for t in times) if f]
    if low:
        act_low = None
        if active:
            sx, sy = lw / w, lh / h
            act_low = (int(active[0] * sx), int(active[1] * sy), int(active[2] * sx), int(active[3] * sy))
            ax, ay, aw_, ah_ = act_low
            ex = exposure_stats([b"".join(f[(ay + r) * lw + ax:(ay + r) * lw + ax + aw_] for r in range(ah_)) for f in low])
        else:
            ex = exposure_stats(low)
        R["metrics"]["exposure"] = ex
        if ex["clipped_highlights_pct"] >= 8:
            warn.append(f"clipped highlights on {ex['clipped_highlights_pct']}% of the frame (blown sky/windows?)")
        if ex["crushed_blacks_pct"] >= 25:
            warn.append(f"crushed blacks on {ex['crushed_blacks_pct']}% of the frame (night/low-key or underexposed)")
        if ex["mean_luma"] < 35:
            warn.append(f"very dark overall (mean luma {ex['mean_luma']})")
        wm = watermark_check(low, lw, lh, act_low)
        R["metrics"]["watermark"] = wm
        where = sorted({f["where"] for f in wm.get("flagged_tiles", []) if f["bright"]} or
                       {f["where"] for f in wm.get("flagged_tiles", [])})
        if wm["camera"].get("locked_off"):
            inf.append("locked-off camera")
        if wm["status"] == "strong" and dur >= 6:
            rej.append(f"suspected watermark ({wm['pattern']}) at {', '.join(where)}: check by eye")
        elif wm["status"] in ("strong", "weak"):
            warn.append(f"possible overlay/logo ({wm.get('pattern', '')}) at {', '.join(where)}: check by eye")
        elif wm["status"] == "minor":
            inf.append(f"some static edges at {', '.join(where)} (probably scene, glance at them)")
        elif wm["status"] == "inconclusive":
            inf.append("watermark check inconclusive (" + wm.get("reason", "") + "): check corners by eye")

    dts = [dur * f for f in (0.2, 0.4, 0.6, 0.8)] if dur > 2 else [0.0]
    det = [detail_pass(src, ua, t, w, h) for t in dts]
    blurs = [d["blur"] for d in det if d.get("blur") is not None]
    rts = [d["rt2_psnr"] for d in det if d.get("rt2_psnr") is not None]
    laps = [d["lap_max"] for d in det if d.get("lap_max") is not None]
    sharp = {"blurdetect_median": round(st.median(blurs), 2) if blurs else None,
             "rt2_psnr_median": round(st.median(rts), 2) if rts else None,
             "laplacian_max_tile_median": round(st.median(laps), 1) if laps else None}
    R["metrics"]["sharpness"] = sharp
    b = sharp["blurdetect_median"]
    rt = sharp["rt2_psnr_median"]
    lap = sharp["laplacian_max_tile_median"]
    luma = (R["metrics"].get("exposure") or {}).get("mean_luma", 100)
    if b is not None and lap is not None:
        # Shallow depth of field, low light and haze also read as "soft": only reject when every
        # signal agrees and the frame is bright enough that low contrast does not explain it.
        if luma >= 60 and ((lap < 10 and (rt or 0) >= 51) or (b >= 12 and lap < 15 and (rt or 0) >= 53)):
            rej.append(f"out of focus / very soft (blurdetect {b}, sharpest-tile Laplacian {lap}, round-trip PSNR {rt} dB)")
        elif b >= 7.5 or lap < 25:
            warn.append(f"soft image (blurdetect {b}, sharpest-tile Laplacian {lap}); fine only for background/defocus shots")
    if rt is not None and tier != "SD/HD":
        if rt >= 50:
            half = f"{w // 2}x{h // 2}"
            if shorts / 2 < 1075:
                warn.append(f"little detail at native resolution (round-trip PSNR {rt} dB): looks like ~{half}, soft focus, heavy compression or upscale")
            else:
                warn.append(f"little detail at native resolution (round-trip PSNR {rt} dB): effectively ~{half}, still >= 1080p")
        elif rt >= 47.5 and tier == "4K+":
            inf.append(f"4K with modest fine detail (round-trip PSNR {rt} dB): possible upscale or soft lens")

    R["score"] = score(R)
    R["verdict"] = "REJECT" if rej else ("ACCEPT-WITH-NOTES" if warn else "ACCEPT")
    return R


def score(R):
    s = {"4K+": 30, "QHD": 20, "FHD": 10}.get(R.get("tier"), 0)
    m = R["metrics"]
    s += 15 * min(1.5, m.get("bitrate_ratio", 0.7)) / 1.5
    sh = m.get("sharpness", {})
    b = sh.get("blurdetect_median")
    if b is not None:
        s += 20 * max(0.0, min(1.0, (10.0 - b) / 4.5))
    jit = m.get("motion_pass", {}).get("shake", {}).get("jitter_pct")
    s += 15 * (max(0.0, min(1.0, (0.8 - jit) / 0.7)) if jit is not None else 0.5)
    ex = m.get("exposure")
    if ex:
        s += 10 - min(5, ex["clipped_highlights_pct"] / 3) - min(5, max(0, ex["crushed_blacks_pct"] - 10) / 5)
    if R.get("fps", 0) >= 23.9:
        s += 5
    if R.get("duration_s", 0) >= 8:
        s += 5
    s -= 5 * len(R["notes"])
    return round(max(0.0, min(100.0, s)), 1)


def qc_photo(src, ua):
    info = ffprobe(src, ua)
    v = [s for s in info["streams"] if s.get("codec_type") == "video"][0]
    fmt = info.get("format", {})
    w, h = int(v["width"]), int(v["height"])
    R = {"source": src, "kind": "photo", "width": w, "height": h, "codec": v.get("codec_name"),
         "pix_fmt": v.get("pix_fmt"), "reasons": [], "notes": [], "info": [], "metrics": {}}
    rej, warn, inf = R["reasons"], R["notes"], R["info"]
    longs = max(w, h)
    if longs < 2400:
        rej.append(f"long side {longs}px below 2400")
    elif longs < 3840:
        warn.append(f"long side {longs}px: fills a 1080p frame, not a 4K frame without upscale")
    else:
        inf.append(f"long side {longs}px: fills a 4K frame" + (" with room for a Ken Burns move" if longs >= 5000 else ""))
    size = float(fmt.get("size") or 0)
    if size and v.get("codec_name") == "mjpeg":
        bpp = size / (w * h)
        R["metrics"]["jpeg_bytes_per_pixel"] = round(bpp, 3)
        if bpp < 0.08:
            warn.append(f"heavy JPEG compression ({bpp:.3f} bytes/pixel)")
    d = detail_pass(src, ua, 0.0, w, h)
    R["metrics"]["sharpness"] = d
    lap = d.get("lap_max")
    if lap is not None and lap < 15:
        rej.append(f"out of focus / very soft (sharpest-tile Laplacian {lap})")
    elif (lap is not None and lap < 25) or (d.get("blur") or 0) >= 7.5:
        warn.append(f"soft image (blurdetect {d.get('blur')}, Laplacian {lap})")
    if d.get("rt2_psnr") and d["rt2_psnr"] >= 50:
        warn.append(f"little detail at native resolution (round-trip PSNR {d['rt2_psnr']} dB): effectively ~{w // 2}x{h // 2}")
    lw, lh = (384, even(384 * h / w)) if w >= h else (even(384 * w / h), 384)
    f = gray_frame(src, ua, 0.0, f"scale={lw}:{lh}:flags=area:out_range=full", lw, lh)
    if f:
        ex = exposure_stats([f])
        R["metrics"]["exposure"] = ex
        if ex["clipped_highlights_pct"] >= 8:
            warn.append(f"clipped highlights on {ex['clipped_highlights_pct']}% of the image")
        if ex["crushed_blacks_pct"] >= 25:
            warn.append(f"crushed blacks on {ex['crushed_blacks_pct']}% of the image")
    tags = " ".join(f"{k}={val}" for k, val in (fmt.get("tags") or {}).items())
    if AI_WORDS.search(tags):
        warn.append("metadata mentions an AI generator / C2PA: " + AI_WORDS.search(tags).group(0))
    inf.append("watermark check not automated for photos: check corners by eye")
    R["verdict"] = "REJECT" if rej else ("ACCEPT-WITH-NOTES" if warn else "ACCEPT")
    return R


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", help="video/photo file or http(s) URL")
    ap.add_argument("--json", action="store_true", help="print JSON only")
    ap.add_argument("--out", help="write JSON to this file")
    ap.add_argument("--photo", action="store_true", help="photo rules (auto for jpg/png/webp/tif/...)")
    ap.add_argument("--max-seconds", type=float, default=20.0, help="motion-analysis window, s")
    ap.add_argument("--meta-duration", type=float, help="full clip length if the file is an excerpt")
    ap.add_argument("--allow-vertical", action="store_true", help="do not reject 9:16 footage")
    ap.add_argument("--ua", default=None, help="User-Agent for URLs (default: a desktop browser)")
    a = ap.parse_args(argv)
    ua = a.ua or BROWSER_UA
    if not re.match(r"^https?://", a.src):
        a.src = os.path.abspath(a.src)  # motion pass runs ffmpeg from a temp dir
    ext = os.path.splitext(re.sub(r"[?#].*$", "", a.src))[1].lower()
    try:
        if a.photo or ext in PHOTO_EXT:
            R = qc_photo(a.src, ua)
        else:
            R = qc_video(a.src, ua, a.max_seconds, a.meta_duration, a.allow_vertical)
    except Exception as e:  # noqa: BLE001
        R = {"source": a.src, "verdict": "REJECT", "reasons": [f"could not analyse: {e}"], "notes": [], "info": []}
    js = json.dumps(R, indent=1)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(js)
    if a.json:
        print(js)
    else:
        extra = (f"{R.get('fps')}fps  {R.get('video_bitrate_mbps')}Mbit/s  score {R.get('score')}  "
                 if R.get("kind") == "video" else "")
        print(f"{R['verdict']}  {R.get('width', '?')}x{R.get('height', '?')}  {extra}{a.src}")
        for k, lab in (("reasons", "REJECT"), ("notes", "NOTE"), ("info", "info")):
            for r in R.get(k, []):
                print(f"  [{lab}] {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
