#!/usr/bin/env python3
"""Musiqani bitga moslash: sahna almashuvlari bitga tushadigan trek boshlanish nuqtasini (data-media-start) topadi.

Ishlatish (HyperFrames loyihasi papkasida, avval `npx hyperframes beats` ishga tushirilgan bo'lsin):
    python3 ~/VideoMontaj/vosita/bit_moslash.py --davom 25.36 3.42 5.57 8.32 ...
Kesimlar berilmasa, index.html dagi `.sahna` larning data-start qiymatlari olinadi.
"""
import argparse
import bisect
import glob
import json
import re
import subprocess
from pathlib import Path


def ovoz_balandligi(fayl, boshi, davom):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-ss", str(boshi), "-t", str(davom), "-i", fayl,
                        "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"mean_volume: ([-\d.]+)", r.stderr)
    return float(m.group(1)) if m else -99.0


def main():
    import litsenziya  # vosita/ yonida; tarqatilgan nusxada litsenziyani tekshiradi
    litsenziya.talab()
    a = argparse.ArgumentParser()
    a.add_argument("kesimlar", nargs="*", type=float)
    a.add_argument("--davom", type=float, required=True, help="video davomiyligi, s")
    a.add_argument("--chegara", type=float, default=0.035, help="bitga tushdi deb hisoblanadigan farq, s")
    o = a.parse_args()

    kesim = o.kesimlar
    if not kesim:
        html = Path("index.html").read_text()
        kesim = sorted({float(x) for x in re.findall(r'class="sahna[^"]*"[^>]*data-start="([\d.]+)"', html)} - {0.0})
    fayllar = glob.glob("beats/**/*.json", recursive=True)
    if not fayllar:
        raise SystemExit("beats/ yo'q — avval: npx hyperframes beats (musiqa <audio> da data-timeline-role=\"music\")")
    d = json.load(open(fayllar[0]))
    bitlar = [b if isinstance(b, (int, float)) else b.get("time", b.get("t")) for b in d["beats"]]
    trek = d.get("audio", "")

    natija = []
    for b in bitlar:
        for sh in range(0, 44):
            m = b + sh / 100
            if m + o.davom > bitlar[-1]:
                break
            xato, tushdi = 0.0, 0
            for s in kesim:
                t = s + m
                j = bisect.bisect_left(bitlar, t)
                e = min(abs(bitlar[k] - t) for k in (j - 1, j) if 0 <= k < len(bitlar))
                xato += e
                tushdi += e < o.chegara
            natija.append((tushdi, round(-xato, 3), round(m, 2)))
    natija.sort(reverse=True)
    eng = natija[0][:2]
    nomzod = sorted({n[2] for n in natija if n[:2] == eng})[:6]
    print(f"Kesimlar: {kesim}")
    print(f"Eng yaxshi moslik: {eng[0]}/{len(kesim)} kesim bitga tushadi")
    for m in nomzod:
        bal = ovoz_balandligi(trek, m, o.davom) if trek else None
        print(f"  data-media-start=\"{m}\"  o'rtacha balandlik {bal} dB")
    print("Eng baland (asosiy qism) nomzodni tanla; intro jimligidan qoch.")


if __name__ == "__main__":
    main()
