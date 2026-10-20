#!/usr/bin/env bash
# Loudness measuring + mastering and poster-frame baking, with ffmpeg only.
#
#   bash loudness.sh measure <in>                     integrated LUFS, LRA, true peak (EBU R128 / ebur128)
#   bash loudness.sh master  <in> <out> [I] [TP] [LRA] two-pass loudnorm, default -14 LUFS / -1.5 dBTP / 11 LU
#   bash loudness.sh poster  <in> <image> <out>       replace frame 0 with a poster image (thumbnail frame)
#
# master: pass 1 measures, pass 2 applies a LINEAR gain with the measured values (no pumping when
# the input already fits the range). Video is stream-copied, audio becomes AAC 320k / 48 kHz.
# Then it re-measures the output. Targets: -14 LUFS for YouTube/Instagram/TikTok/LinkedIn web
# delivery, -23 LUFS (EBU R128) or -24 LKFS (ATSC A/85) for broadcast, true peak <= -1 dBTP.
# poster: the image is scaled/padded to the video size and shown on frame 0 only, so duration and
# audio sync stay unchanged. Video is re-encoded (H.264 CRF 16), audio is copied.
#
# Same as one-liners:
#   ffmpeg -hide_banner -nostats -i in.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12
#   ffmpeg -hide_banner -i in.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -
#   ffmpeg -i in.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=<input_i>:measured_TP=<input_tp>:\
#          measured_LRA=<input_lra>:measured_thresh=<input_thresh>:offset=<target_offset>:linear=true \
#          -c:a aac -b:a 320k -ar 48000 out.mp4
#   ffmpeg -i in.mp4 -i poster.png -filter_complex "[1:v][0:v]scale2ref[p][v];[v][p]overlay=enable='eq(n,0)'" \
#          -c:v libx264 -crf 16 -pix_fmt yuv420p -c:a copy -movflags +faststart out.mp4
set -euo pipefail

die() { echo "error: $*" >&2; exit 1; }
command -v ffmpeg >/dev/null || die "ffmpeg not on PATH"

measure() {
  ffmpeg -hide_banner -nostats -i "$1" -map 0:a:0 -af ebur128=peak=true -f null - 2>&1 |
    awk '/Summary:/{s=1} s && /I:|LRA:|Peak:/{gsub(/^ +/,""); sub(/^Peak:/,"True peak:"); sub(/dBFS/,"dBTP"); print}'
}

json_val() {  # json_val <key> <text>
  printf '%s\n' "$2" | sed -n "s/.*\"$1\" *: *\"\{0,1\}\([-0-9.inf]*\)\"\{0,1\}.*/\1/p" | head -1
}

master() {
  local in="$1" out="$2" I="${3:--14}" TP="${4:--1.5}" LRA="${5:-11}"
  [ -f "$in" ] || die "no such file: $in"
  echo "pass 1: measuring $in" >&2
  local js
  js=$(ffmpeg -hide_banner -nostats -i "$in" -map 0:a:0 \
        -af "loudnorm=I=$I:TP=$TP:LRA=$LRA:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
  local mi mtp mlra mth off
  mi=$(json_val input_i "$js"); mtp=$(json_val input_tp "$js"); mlra=$(json_val input_lra "$js")
  mth=$(json_val input_thresh "$js"); off=$(json_val target_offset "$js")
  [ -n "$mi" ] || die "loudnorm pass 1 gave no measurement (no audio stream?)"
  echo "  input: I=$mi LUFS  TP=$mtp dBTP  LRA=$mlra LU  thresh=$mth  offset=$off" >&2
  case "$mi" in -inf*) die "input is silent";; esac
  echo "pass 2: normalising to I=$I TP=$TP LRA=$LRA -> $out" >&2
  ffmpeg -hide_banner -loglevel error -y -i "$in" -map 0:v? -map 0:a:0 -c:v copy \
    -af "loudnorm=I=$I:TP=$TP:LRA=$LRA:measured_I=$mi:measured_TP=$mtp:measured_LRA=$mlra:measured_thresh=$mth:offset=$off:linear=true" \
    -c:a aac -b:a 320k -ar 48000 -shortest -movflags +faststart "$out"
  echo "result:" >&2
  measure "$out"
}

poster() {
  local in="$1" img="$2" out="$3"
  [ -f "$in" ] && [ -f "$img" ] || die "need <in> <image> <out>"
  local wh W H
  wh=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$in")
  W=${wh%x*}; H=${wh#*x}
  [ -n "$W" ] && [ -n "$H" ] || die "no video stream in $in"
  ffmpeg -hide_banner -loglevel error -y -i "$in" -i "$img" -filter_complex     "[1:v]scale=$W:$H:force_original_aspect_ratio=decrease,pad=$W:$H:(ow-iw)/2:(oh-ih)/2,setsar=1[p];[0:v][p]overlay=enable='eq(n,0)':eof_action=pass,format=yuv420p[v]"     -map "[v]" -map 0:a? -c:v libx264 -crf 16 -preset slow -c:a copy -movflags +faststart "$out"
  echo "wrote $out (frame 0 = $img)" >&2
}

cmd="${1:-}"; shift || true
case "$cmd" in
  measure) [ $# -ge 1 ] || die "usage: loudness.sh measure <in>"; measure "$1" ;;
  master)  [ $# -ge 2 ] || die "usage: loudness.sh master <in> <out> [I] [TP] [LRA]"; master "$@" ;;
  poster)  [ $# -ge 3 ] || die "usage: loudness.sh poster <in> <image> <out>"; poster "$@" ;;
  -h|--help|"") sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//' ;;
  *) die "unknown command '$cmd' (measure | master | poster | --help)" ;;
esac
