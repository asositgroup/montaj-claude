"""varaq.py <video> <chiqish_papka> — kadr varaqlari: boshlanish (0–120 s, har 4 s) + butun video (36 kadr teng oraliqda)
+ kesimlar statistikasi (ffmpeg scene). Har kadr ostida vaqt yoziladi."""
import json, pathlib, subprocess, sys
from PIL import Image, ImageDraw
FF = "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg"
v, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(v)], capture_output=True, text=True).stdout)
def kadr(t):
    r = subprocess.run([FF, "-v", "error", "-ss", f"{t:.2f}", "-i", str(v), "-frames:v", "1", "-vf", "scale=384:216", "-f", "image2pipe", "-c:v", "png", "-"], capture_output=True)
    from io import BytesIO
    return Image.open(BytesIO(r.stdout)).convert("RGB") if r.stdout else Image.new("RGB", (384, 216))
def varaq(vaqtlar, nom, ust=6):
    W, H = 384, 216 + 18
    s = Image.new("RGB", (W * ust, H * ((len(vaqtlar) + ust - 1) // ust)), "black"); d = ImageDraw.Draw(s)
    for k, t in enumerate(vaqtlar):
        x, y = (k % ust) * W, (k // ust) * H
        s.paste(kadr(t), (x, y)); d.text((x + 4, y + 218), f"{int(t // 60)}:{int(t % 60):02d}", fill="yellow")
    s.save(out / nom, quality=78)
varaq([t for t in range(0, min(120, int(dur)), 4)], f"{v.stem}_bosh.jpg")
varaq([dur * (i + 0.5) / 36 for i in range(36)], f"{v.stem}_butun.jpg")
# kesimlar (sahna almashuvi) soni
r = subprocess.run([FF, "-i", str(v), "-vf", "select='gt(scene,0.3)',showinfo", "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
cuts = [float(l.split("pts_time:")[1].split()[0]) for l in r.splitlines() if "pts_time:" in l]
json.dump({"davomiylik": dur, "kesimlar": len(cuts), "orta_shot_s": round(dur / (len(cuts) + 1), 1),
           "bosh_120s_kesim": sum(c < 120 for c in cuts), "vaqtlar": [round(c, 1) for c in cuts]}, open(out / f"{v.stem}_kesim.json", "w"))
print(v.stem, round(dur), "s, kesim", len(cuts))
