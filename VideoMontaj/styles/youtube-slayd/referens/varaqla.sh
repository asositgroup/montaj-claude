#!/bin/bash
# Yuklangan har videoga varaq yasaydi (yuklash tugaguncha kutadi)
cd "$(dirname "$0")"
while true; do
  for f in umida/*.mp4 timochko/*.mp4; do
    [ -f "$f" ] || continue
    d=$(dirname "$f"); id=$(basename "$f" .mp4)
    [ -f "varaq/$d/${id}_kesim.json" ] || python3 varaq.py "$f" "varaq/$d"
  done
  pgrep -f yukla.sh >/dev/null || break
  sleep 20
done
for f in umida/*.mp4 timochko/*.mp4; do d=$(dirname "$f"); id=$(basename "$f" .mp4); [ -f "varaq/$d/${id}_kesim.json" ] || python3 varaq.py "$f" "varaq/$d"; done
echo HAMMASI
