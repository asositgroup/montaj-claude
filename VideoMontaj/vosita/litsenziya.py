#!/usr/bin/env python3
"""Montaj tizimi litsenziyasi (o'quvchi kompyuteri tomoni, Mac va Windows). Faqat stdlib.

  python3 litsenziya.py faollash          — kalitni shu Mac'ga bog'laydi (ornatish.sh chaqiradi)
  python3 litsenziya.py tekshir           — kalit faolmi (montaj skilli har ishda chaqiradi); xato → kod 1
  python3 litsenziya.py aktiv <nom> <fayl> — yopiq aktivni (model, referens, namuna) yuklab oladi

Kalit `~/VideoMontaj/.litsenziya` da (shaxsiy zip bilan keladi). Bitta kalit ko'pi bilan 2 ta kompyuterda (Mac/Windows) ishlaydi.
Internet bo'lmasa — oxirgi muvaffaqiyatli tekshiruvdan 7 kun ishlayveradi.
Egasining o'z nusxasida TARQATILGAN=False — tekshiruv o'chiq; tarqatish yig'uvchisi uni True qiladi.
"""
import hashlib
import json
import platform
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

TARQATILGAN = False
SERVER = "https://litsenziya.161-35-78-244.sslip.io"
ASOS = Path(__file__).resolve().parent.parent
KALIT_F = ASOS / ".litsenziya"
KESH_F = Path.home() / ".config" / "montaj" / "litsenziya.json"
OFLAYN_KUN = 7


class Xato(Exception):
    pass


def qurilma_id():
    """Kompyuterning doimiy ID'si (Mac: IOPlatformUUID, Windows: MachineGuid) → sha256 qisqasi."""
    try:
        if sys.platform == "win32":
            import winreg
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography",
                                0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as k:
                uuid = winreg.QueryValueEx(k, "MachineGuid")[0]
        else:
            out = subprocess.run(["ioreg", "-rd1", "-c", "IOPlatformExpertDevice"], capture_output=True, text=True).stdout
            uuid = next(l.split('"')[3] for l in out.splitlines() if "IOPlatformUUID" in l)
    except Exception:
        raise Xato("Kompyuter ID'sini o'qib bo'lmadi (tizim macOS va Windows'da ishlaydi).")
    return hashlib.sha256(("montaj:" + uuid).encode()).hexdigest()[:32]


def kalit():
    try:
        return json.loads(KALIT_F.read_text())["kalit"]
    except Exception:
        raise Xato(f"Litsenziya fayli yo'q yoki buzilgan: {KALIT_F}\nTizim faqat shaxsiy havola orqali olingan nusxada ishlaydi.")


def _post(yol, data):
    req = urllib.request.Request(SERVER + yol, data=json.dumps(data).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            raise Xato(json.loads(e.read()).get("xato") or f"Server xatosi {e.code}")
        except ValueError:
            raise Xato(f"Server xatosi {e.code}")


def _kesh_yoz():
    KESH_F.parent.mkdir(parents=True, exist_ok=True)
    KESH_F.write_text(json.dumps({"kalit": kalit(), "qurilma": qurilma_id(), "oxirgi_ok": time.time()}))


def faollash():
    d = _post("/api/faollash", {"kalit": kalit(), "qurilma": qurilma_id(), "nom": platform.node()})
    _kesh_yoz()
    return d.get("ism", "")


def tekshir():
    try:
        _post("/api/tekshir", {"kalit": kalit(), "qurilma": qurilma_id()})
    except OSError:  # URLError, timeout — HTTP javoblari _post'da Xato'ga aylangan
        # internet yo'q: oxirgi muvaffaqiyatli tekshiruv yaqin bo'lsa — ishlayveradi
        try:
            k = json.loads(KESH_F.read_text())
            if k["kalit"] == kalit() and k["qurilma"] == qurilma_id() and time.time() - k["oxirgi_ok"] < OFLAYN_KUN * 86400:
                return
        except Exception:
            pass
        raise Xato("Litsenziya serveriga ulanib bo'lmadi. Internetni tekshiring.")
    _kesh_yoz()


def aktiv(nom, chiqish):
    req = urllib.request.Request(f"{SERVER}/api/aktiv/{nom}",
                                 headers={"X-Kalit": kalit(), "X-Qurilma": qurilma_id()})
    chiqish = Path(chiqish)
    chiqish.parent.mkdir(parents=True, exist_ok=True)
    vaqtincha = chiqish.with_suffix(chiqish.suffix + ".yuklanmoqda")
    try:
        with urllib.request.urlopen(req, timeout=60) as r, open(vaqtincha, "wb") as f:
            jami, n, oxirgi = int(r.headers.get("Content-Length") or 0), 0, -1
            while b := r.read(1 << 20):
                f.write(b)
                n += len(b)
                if jami and n * 100 // jami != oxirgi:
                    oxirgi = n * 100 // jami
                    print(f"\r  {nom}: {oxirgi}% ({n >> 20}/{jami >> 20} MB)", end="", flush=True)
        print()
    except urllib.error.HTTPError as e:
        vaqtincha.unlink(missing_ok=True)
        try:
            raise Xato(json.loads(e.read()).get("xato") or f"Server xatosi {e.code}")
        except ValueError:
            raise Xato(f"Server xatosi {e.code}")
    vaqtincha.replace(chiqish)


def talab():
    """Skriptlar boshida chaqiriladi: tarqatilgan nusxada litsenziya yo'q/o'chirilgan bo'lsa to'xtatadi."""
    if not TARQATILGAN:
        return
    try:
        tekshir()
    except Xato as e:
        sys.exit(f"⛔ Litsenziya: {e}")


if __name__ == "__main__":
    buyruq = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        if buyruq == "faollash":
            ism = faollash()
            print(f"✓ Litsenziya faollashtirildi{': ' + ism if ism else ''}")
        elif buyruq == "tekshir":
            tekshir()
            print("✓ Litsenziya faol")
        elif buyruq == "aktiv" and len(sys.argv) == 4:
            aktiv(sys.argv[2], sys.argv[3])
        else:
            sys.exit(__doc__)
    except Xato as e:
        sys.exit(f"⛔ Litsenziya: {e}")
