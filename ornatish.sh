#!/bin/bash
# Montaj tizimi o'rnatuvchisi (macOS). Ishga tushirish: repo papkasida, Terminal'da  bash ornatish.sh
# Nima qiladi: dasturlar (brew) → ~/VideoMontaj (kod, uslublar, namuna) → model (GitHub Release'dan)
#              → Mixkit ovoz effektlari va musiqa → Claude skill'lari → HyperFrames brauzeri → tekshiruv.
set -euo pipefail
MANBA="$(cd "$(dirname "$0")" && pwd)"
VM="$HOME/VideoMontaj"
MODEL_URL="https://github.com/asositgroup/montaj-claude/releases/download/model-v1/ggml-rubaistt.bin"
MODEL_SHA="1b02df434902015e1464611a7748927e42fcb55c49791c85239cf713c8edc1a3"
xato() { echo "⛔ $*" >&2; exit 1; }
qadam() { echo; echo "▶ $*"; }

qadam "Tizim"
[ "$(uname)" = "Darwin" ] || xato "Faqat macOS uchun."
[ "$(uname -m)" = "arm64" ] || echo "  ⚠️  Intel Mac: ishlashi mumkin, lekin Apple Silicon (M1+) tavsiya."
xcode-select -p >/dev/null 2>&1 || { xcode-select --install || true; xato "Xcode Command Line Tools o'rnatilmoqda. Tugagach skriptni qayta ishga tushiring."; }
command -v brew >/dev/null || xato "Homebrew yo'q. Avval o'rnating (https://brew.sh):
  /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
echo "  ✓ macOS, Xcode CLT, Homebrew"

qadam "Dasturlar (brew)"
for p in ffmpeg ffmpeg-full whisper-cpp node yt-dlp gallery-dl; do
  if brew list --formula "$p" >/dev/null 2>&1 || { [ "$p" = node ] && command -v node >/dev/null; }; then echo "  ✓ $p"; else echo "  … $p o'rnatilmoqda"; brew install "$p"; fi
done

qadam "~/VideoMontaj"
mkdir -p "$VM"
# kod yangilanadi; ish/, videos/ dagi o'z ishlaringiz va yuklangan aktivlar o'chirilmaydi
rsync -a --exclude 'styles/' "$MANBA/VideoMontaj/" "$VM/"
rsync -a --ignore-existing "$MANBA/VideoMontaj/styles/" "$VM/styles/"   # o'zingiz tuzatgan STYLE.md ustidan yozilmaydi
echo "  ✓ $VM"

qadam "Model va namunalar"
M="$VM/modellar/ggml-rubaistt.bin"
if [ ! -s "$M" ]; then
  echo "  … model yuklanmoqda (823 MB, bir marta)"
  mkdir -p "$VM/modellar"
  curl -fL --progress-bar -o "$M.yuklanmoqda" "$MODEL_URL" || xato "Model yuklanmadi: $MODEL_URL"
  [ "$(shasum -a 256 "$M.yuklanmoqda" | cut -d' ' -f1)" = "$MODEL_SHA" ] || { rm -f "$M.yuklanmoqda"; xato "Model fayli buzilgan (sha256 mos emas)."; }
  mv "$M.yuklanmoqda" "$M"
fi
echo "  ✓ model"
[ -d "$VM/videos/c0038-500-dollar" ] && echo "  ✓ namuna" || xato "Namuna yo'q (repo to'liq emas)."

qadam "Ovoz effektlari va musiqa (Mixkit, bepul litsenziya)"
python3 "$VM/vosita/mixkit.py"
# namuna loyihaning SFX va musiqasi ham Mixkit'dan (repoda tarqatilmaydi); video.mp4 — o'zingizniki
N="$VM/videos/c0038-500-dollar/assets"
mkdir -p "$N/sfx"
for f in whoosh_pop click sweep tugma pop sehr ding tanga whoosh_tez zarba pop_quruq yozish; do
  [ -f "$N/sfx/$f.mp3" ] || cp "$VM/assets/ovoz/$f.mp3" "$N/sfx/"
done
[ -s "$N/musiqa.mp3" ] || curl -fsSL -o "$N/musiqa.mp3" https://assets.mixkit.co/music/126/126.mp3
echo "  ✓ namuna loyiha SFX + musiqa"

qadam "Claude skill'lari → ~/.claude/skills"
mkdir -p "$HOME/.claude/skills"
ZAXIRA="$HOME/.claude/skills-zaxira-$(date +%Y%m%d-%H%M%S)"
for d in "$MANBA"/skills/*/; do
  n="$(basename "$d")"
  if [ -d "$HOME/.claude/skills/$n" ]; then mkdir -p "$ZAXIRA"; mv "$HOME/.claude/skills/$n" "$ZAXIRA/"; fi
  cp -R "$d" "$HOME/.claude/skills/$n"
  echo "  ✓ $n"
done
[ -d "$ZAXIRA" ] && echo "  (eski nusxalar: $ZAXIRA)"
# HyperFrames skill'lari (hyperframes*, media-use, general-video, talking-head-recut) — rasmiy CLI, eng yangi versiya
npx --yes hyperframes@latest skills update general-video talking-head-recut && echo "  ✓ HyperFrames skill'lari"

qadam "HyperFrames brauzeri"
cd "$VM/videos/c0038-500-dollar"
npx --yes hyperframes@0.8.134 browser ensure >/dev/null && echo "  ✓ brauzer"

qadam "Tekshiruv"
command -v whisper-cli >/dev/null && echo "  ✓ whisper-cli"
npx --yes hyperframes@0.8.134 check >/dev/null 2>&1 && echo "  ✓ namuna loyiha tekshiruvdan o'tdi" || echo "  ⚠️  namuna tekshiruvi ogohlantirish berdi (npx hyperframes check)"
echo
echo "✅ Tayyor. Claude Code'ni oching va yozing:  /montaj <video yo'li>   (README.md da batafsil)"
