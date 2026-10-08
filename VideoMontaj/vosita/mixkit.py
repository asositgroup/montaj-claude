#!/usr/bin/env python3
"""Mixkit ovoz effektlari (assets/ovoz, −18 LUFS ga tekislanadi) va musiqasini (assets/musiqa) royxat.json bo'yicha yuklaydi.
Mixkit fayllari tarqatilmaydi (litsenziya) — o'rnatuvchilar (ornatish.sh / ornatish.ps1) shu skriptni chaqiradi. Bor fayl qayta yuklanmaydi.
"""
import json
import shutil
import subprocess
import urllib.request
from pathlib import Path

VM = Path(__file__).resolve().parent.parent
FF = "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg"
if not Path(FF).exists():
    FF = shutil.which("ffmpeg") or "ffmpeg"


def ol(url, f):
    if f.exists() and f.stat().st_size > 0:
        return
    f.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, f)


ovoz = VM / "assets/ovoz"
for e in json.loads((ovoz / "royxat.json").read_text(encoding="utf-8"))["effektlar"]:
    i, asl, f = e["mixkit_id"], ovoz / "asl" / e["fayl"], ovoz / e["fayl"]
    ol(f"https://assets.mixkit.co/active_storage/sfx/{i}/{i}-preview.mp3", asl)
    if not f.exists():
        subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(asl), "-af", "loudnorm=I=-18:TP=-1.5:LRA=11",
                        "-ar", "44100", str(f)], check=True)
    print("  ✓", e["fayl"])
musiqa = VM / "assets/musiqa"
for t in json.loads((musiqa / "royxat.json").read_text(encoding="utf-8"))["treklar"]:
    ol(f"https://assets.mixkit.co/music/{t['mixkit_id']}/{t['mixkit_id']}.mp3", musiqa / t["fayl"])
    print("  ✓", t["fayl"])
