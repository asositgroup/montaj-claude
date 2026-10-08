# montaj-claude — Claude bilan professional Reels montaj

Claude Code skill + `~/VideoMontaj` tizimi. Video tashlaysiz → Claude uni tanlangan uslubda (uslub pasporti) professional
montaj qiladi: jimlik/parazit kesish, o'zbekcha transkript, so'zma-so'z grafika, ovoz effektlari, bitga tushgan musiqa.
Montaj kod bilan [HyperFrames](https://github.com/heygen-com/hyperframes)'da yig'iladi va avto-tekshiruvdan o'tadi
(overlap, kontrast, xavfsiz zona).

Ish tartibi (`skills/montaj/SKILL.md`): namuna video → uslub pasporti (`styles/<nom>/STYLE.md`) → o'z video + matn →
HyperFrames'da yig'ish → tekshiruv → SFX va silliqlik (0.1 s qadam) → Mixkit musiqa bitga, 5%.

## Talablar
- **Mac** (Apple Silicon M1+ tavsiya) yoki **Windows 10/11** (64-bit, Intel/AMD).
- **Claude Code** va Claude obunasi (Pro yoki Max).
- Internet: faqat o'rnatishda (dasturlar, model, ovoz effektlari yuklanadi).
- Windows'da nutqni matnga o'girish protsessorda bajariladi — Mac'dagidan sekinroq.

## O'rnatish — Mac
```bash
git clone https://github.com/asositgroup/montaj-claude.git ~/montaj-claude
```
```bash
bash ~/montaj-claude/ornatish.sh
```
Oxirida «✅ Tayyor» chiqadi. Homebrew yoki Xcode so'ralsa — ko'rsatilgan buyruqni bajaring va skriptni qayta ishga tushiring.

## O'rnatish — Windows
1. Repo'ni yuklab oling: **Code → Download ZIP**, keyin o'ng tugma → «Извлечь все / Extract All».
2. Ochilgan papkadagi **`ornatish.cmd`** ni ikki marta bosing. «Himoya» oynasi chiqsa: «Подробнее / More info» → «Выполнить / Run anyway».
3. Dasturlar (Python, Node.js, ffmpeg, Git, yt-dlp) o'zi o'rnatiladi — so'ralsa «Да / Yes» bosing. Oxirida yashil «TAYYOR» chiqadi.
4. **Yangi** terminal oching va Claude Code'ni ishga tushiring.

O'rnatuvchi nima qiladi:
- dasturlar: brew / winget (ffmpeg, whisper.cpp, Node.js, yt-dlp, gallery-dl);
- `VideoMontaj/` → `~/VideoMontaj` (o'zingiz tuzatgan `STYLE.md` ustidan yozilmaydi);
- nutq modeli → `~/VideoMontaj/modellar/` ([Release](https://github.com/asositgroup/montaj-claude/releases/tag/model-v1)'dan, sha256 tekshiriladi);
- Mixkit ovoz effektlari va musiqa → `~/VideoMontaj/assets/`;
- `skills/montaj` → `~/.claude/skills/`, HyperFrames skill'lari (`hyperframes*`, `media-use`, `general-video`,
  `talking-head-recut`) → rasmiy `npx hyperframes skills update` orqali, eng yangi versiyada.

## Ishlatish (Claude Code'da)
- `/montaj ~/Desktop/video.mp4` — uslubni so'raydi, keyin montaj qiladi.
- «green minimal qil» / «asror uslubida qil» — tayyor uslublar (`~/VideoMontaj/styles/`).
- Namuna video havolasini berib: «shu uslubni yodlab ol, nomi <nom>» — yangi uslub pasporti.
- Tuzatish oddiy so'z bilan: «SFX qo'sh», «musiqa baland», «subtitr kattaroq».

## Tayyor uslublar
| Nom | Qisqacha |
|---|---|
| `green-minimal` | oq fon, bitta yashil urg'u, yuzsiz motion-grafika; yuz faqat viewfinder ichida 2–3 s |
| `asror` | @asror.iskandar0v'ning 100 ta reelsi o'lchab tuzilgan pasport |
| `asror-reel` | bitta reelning animatsiyasi va rang berishi (katta so'z, 3D stak, tugma) |
| `youtube-slayd` | uzun YouTube dars: slayd chapda, spiker o'ngda, gap bilan sinxron fokus-ro'yxat |

## Repoda nima yo'q (va nega)
- **Referens videolar va kadr varaqlari** (`styles/*/referens/`) — boshqa mualliflarning videolari; har uslubda
  `STYLE.md` o'lchovlari yetarli. O'zingizda qayta yasash: `ffmpeg` bilan `fps=2` → `tile` varaq (SKILL.md, 1-qadam).
- **Nutq modeli** (823 MB) — GitHub fayl chegarasidan katta, shuning uchun Release'da.
- **Mixkit audio** — litsenziya tarqatishga ruxsat bermaydi; o'rnatuvchi `vosita/mixkit.py` bilan Mixkit'dan o'zi yuklaydi.
- **Namuna loyihaning `video.mp4` va render'i** — shaxsiy video. `videos/c0038-500-dollar/index.html` (green-minimal, 9 sahna)
  tuzilma namunasi sifatida qoladi; ko'rish uchun `assets/video.mp4` ga o'z videongizni qo'ying.

## Litsenziyalar va manbalar
- Nutq modeli: [RubaiSTT v2 medium](https://huggingface.co/islomov/rubaistt_v2_medium) (Apache-2.0) asosidagi whisper.cpp ggml.
- Ovoz effektlari va musiqa: [Mixkit](https://mixkit.co/license/) (bepul, atributsiyasiz; qayta tarqatilmaydi).
- Shriftlar: Montserrat, Inter Tight, Instrument Serif — SIL Open Font License.
- Montaj dvigateli: [HyperFrames](https://github.com/heygen-com/hyperframes).
