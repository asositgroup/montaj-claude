#!/usr/bin/env python3
"""Instagram akkauntdan yuklangan reelslarni o'lchash (uslub pasporti uchun).

Ishlatish: python3 vosita/akkaunt_tahlil.py <reels papkasi> <chiqish papkasi>
Har video uchun: davomiylik, kesishlar (scene > 0.3), o'rtacha sahna uzunligi, birinchi kesish,
1 s qadamli varaq va birinchi 3 s ning 0.2 s qadamli varag'i. Natija: <chiqish>/olchov.json
"""
import json, subprocess, sys, re
from pathlib import Path

FF = "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg"  # Mac (drawtext shunda); boshqa joyda PATH dagi ffmpeg
if not Path(FF).exists():
    import shutil
    FF = shutil.which("ffmpeg") or "ffmpeg"


def davomiylik(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(f)], capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def kesishlar(f):
    r = subprocess.run([FF, "-hide_banner", "-i", str(f), "-an", "-vf",
                        "scale=270:-2,select='gt(scene,0.3)',showinfo", "-f", "null", "-"],
                       capture_output=True, text=True)
    return [round(float(t), 2) for t in re.findall(r"pts_time:([\d.]+)", r.stderr)]


def varaq(f, chiqish, fps, boshi=None, uzunlik=None, ustun=8, eni=240, qator=6):
    vaqt = "drawtext=text='%{pts\\:hms}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6"
    kirish = []
    if boshi is not None:
        kirish += ["-ss", str(boshi), "-t", str(uzunlik)]
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *kirish, "-i", str(f), "-vf",
                    f"fps={fps},scale={eni}:-2,{vaqt},tile={ustun}x{qator}:padding=4",
                    "-frames:v", "1", "-q:v", "4", str(chiqish)], check=False)


def main():
    import litsenziya  # vosita/ yonida; tarqatilgan nusxada litsenziyani tekshiradi
    litsenziya.talab()
    papka, chiqish = Path(sys.argv[1]), Path(sys.argv[2])
    (chiqish / "varaq").mkdir(parents=True, exist_ok=True)
    (chiqish / "hook").mkdir(parents=True, exist_ok=True)
    natija_f = chiqish / "olchov.json"
    natija = json.loads(natija_f.read_text()) if natija_f.exists() else {}
    for f in sorted(papka.glob("*.mp4")):
        kod = f.stem.split("_", 1)[1]
        if kod in natija:
            continue
        m = json.loads(Path(str(f) + ".json").read_text()) if Path(str(f) + ".json").exists() else {}
        d = davomiylik(f)
        k = kesishlar(f)
        natija[kod] = {
            "sana": m.get("date", "")[:10], "egasi": m.get("username"), "layk": m.get("likes"),
            "davomiylik": round(d, 1), "kesishlar": len(k),
            "sahna_ortacha": round(d / (len(k) + 1), 2),
            "birinchi_kesish": k[0] if k else None, "kesish_vaqtlari": k,
            "matn": (m.get("description") or "").split("\n")[0][:120],
        }
        varaq(f, chiqish / "varaq" / f"{kod}.jpg", fps=round(min(1, 48 / max(d, 1)), 3))  # ≤48 kadr
        varaq(f, chiqish / "hook" / f"{kod}.jpg", fps=5, boshi=0, uzunlik=3, ustun=5, eni=216, qator=3)
        natija_f.write_text(json.dumps(natija, ensure_ascii=False, indent=1))
        print(kod, natija[kod]["davomiylik"], "s,", len(k), "kesish", flush=True)


if __name__ == "__main__":
    main()
