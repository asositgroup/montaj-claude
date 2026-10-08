#!/usr/bin/env python3
"""Videoni HyperFrames montajiga tayyorlash: jimlik/parazit kesish → ish/<nom>/toza.mp4 + toza_transkript.txt (so'z@soniya).

  python3 ~/VideoMontaj/vosita/tayyorla.py <video> [--til uz|en|ru|auto]

montaj.py'ning reel_tayyorla() bosqichini avto_sahna'gacha bajaradi (eski Reel Studio sahnasi kerak emas).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import litsenziya  # noqa: E402
import montaj  # noqa: E402


class _Toxta(Exception):
    pass


def _toxta(*a, **k):
    raise _Toxta


def main():
    litsenziya.talab()
    args = sys.argv[1:]
    if "--til" in args:
        i = args.index("--til")
        montaj.TIL = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1 or not Path(args[0]).exists():
        sys.exit(__doc__)
    video = Path(args[0]).resolve()
    montaj.avto_sahna = _toxta
    try:
        montaj.reel_tayyorla(video)
    except _Toxta:
        pass
    papka = montaj.ish_papka(video)
    print(f"✓ {papka / 'toza.mp4'}\n✓ {papka / 'toza_transkript.txt'}")


if __name__ == "__main__":
    main()
