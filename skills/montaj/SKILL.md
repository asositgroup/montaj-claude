---
name: montaj
description: Professional Reels montaj (har videoga $100 oladigan montajchi darajasi) — «Claude bilan PROFESSIONAL montaj» darsi usuli: namuna (reference) video → uslub pasporti (styles/<nom>/STYLE.md) → o'z video + matn → HyperFrames'da kod bilan yig'ish → avto-tekshiruv (overlap, kontrast, xavfsiz zona) → SFX va referensdagi silliqlik (0.1 s qadam) → Mixkit musiqa bitga, 5%. Uslublar nom bilan saqlanadi («green minimal qil»). Foydalanuvchi "/montaj <video>" desa, video tashlab "montaj qil"/"reels qil" desa, «<uslub nomi> qil» desa, namuna video berib «shu uslubni yodla» desa yoki montajni tuzatishni so'rasa ishlatiladi.
---

# Professional montaj (~/VideoMontaj) — darsdagi 6 qadam

Dvigatel: **HyperFrames** (HTML → video; skill'lar `~/.claude/skills/hyperframes*`, `media-use`, `general-video`).

## Qat'iy qoidalar
- **O'zingdan uslub to'qima.** Har bir rang, shrift, harakat, o'tish va SFX faqat tanlangan `styles/<nom>/STYLE.md` pasportidan olinadi.
  Pasportda yo'q element (emoji, stiker, sariq karaoke subtitr, Montserrat Black, kontur, «hook» plashka) — **qo'shilmaydi**.
- Uslub nomi aytilmagan va namuna berilmagan bo'lsa → `ls ~/VideoMontaj/styles/` ro'yxatini ko'rsatib, qaysi biri yoki yangi namuna so'ra.
- Ekranda hech qachon >0.5 s «o'lik» joy (markaz bo'sh) qolmasin; bir vaqtda bitta g'oya.
- Har kadr tekshiruvdan o'tmaguncha «tayyor» dema (4-qadam).
- **Oddiy narsalarni ham ko'r (2026-10-07, egasi):** har kesish chegarasini ±0.4 s, 0.1 s qadamli varaqda tekshir — gap oxiri/boshida
  boshini burib, kameradan qarab ketgan, ko'zini yumib qolgan, qo'l bilan yuzni yopgan joy qolmasin. Ovoz kerak bo'lsa **L-cut**:
  tasvir keyingi planga ertaroq o'tadi, ovoz qoladi (`ish/fayz6oy/kes.py` → `bolaklar.json` 5-maydon). Video va audio alohida
  concat qilinadi (birga concat A/V ni 0.3 s gacha siljitgan).
- **CTA standart emas:** gap tugashi bilan video tugaydi (Follow kartochkasi, «izohga yozing» — faqat egasi so'rasa).
- **Shrift oddiy ko'rinmasin:** bitta oddiy shrift (Noto Serif / Montserrat yolg'iz) — «o'ta oddiy». Premium = juftlik va ierarxiya:
  grotesk (Inter Tight 600–800, minus tracking) + urg'u so'z serif italic (Instrument Serif), kichik eyebrow (caps, tracking 0.18em),
  raqamlar katta serif italic, shisha (frosted) plashka, so'zma-so'z blur kirish.

## 1. Namuna → kadrlar tahlili (yangi uslub bo'lsa)
Foydalanuvchi Instagram/Pinterest/YouTube namunasini beradi («shu stilni yodlab ol»). Havola bo'lsa `yt-dlp` bilan yukla.
Videoni **tomosha qilma, o'lcha**:
- Umumiy: `ffmpeg-full` (`/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg`, drawtext shunda) bilan `fps=2` → `tile` varaqlar (vaqt yozuvi bilan).
  zsh'da `$F:text` → `${F}:text` yoz (`:t` modifikator).
- Harakat: asosiy o'tishlarni `fps=10` (0.1 s qadam) bilan, kerak bo'lsa `crop` qilib ko'r: kirish/chiqish davomiyligi, blur, stagger, ease, sanoq tezligi.
- Shriftlarni referens bilan yonma-yon solishtirib, eng yaqinini tanla (Google Fonts, OFL).

## 2. Uslub pasporti (nom bilan saqlash)
`~/VideoMontaj/styles/<nom>/STYLE.md` + `referens/` (varaqlar). Namuna: `styles/green-minimal/STYLE.md`. Bo'limlar:
1 Ranglar (token | hex | qayerda), 2 Shriftlar, 3 Harakat lug'ati (referensdagi tartibda), 4 Kadrma-kadr o'lchovlar (0.1 s),
5 Kompozitsiya (9:16, xavfsiz zona tepa 250 / past 450 / o'ng 120 px, yuz qachon va qanday chiqadi), 6 Ovoz (SFX turlari, musiqa janri/BPM/balandlik), 7 Tekshiruv.
Keyin foydalanuvchi faqat nomini aytadi: «green minimal qil».

## 3. O'z video + matn
```bash
cd ~/VideoMontaj && python3 vosita/tayyorla.py "<video>"   # jimlik/parazit kesish → ish/<nom>/toza.mp4 + toza_transkript.txt
```
- So'z vaqtlari: `ish/<nom>/toza_transkript.txt` (`so'z@soniya`, aniqlik ≈0.3 s → grafikani so'zdan 0.05–0.1 s oldin chiqar).
- **Matnni foydalanuvchidan so'ra** (yoki `ish/<nom>/matn.txt` bo'lsa o'sha): Whisper o'zbekchani xato yozadi, ekrandagi so'zlar to'g'ri bo'lishi shart.
- Takror/yomon dubl bo'lsa `reja.json` `olib_tashlash` → qayta `tayyorla.py`.

## 4. Yig'ish (HyperFrames) + o'zini tekshirish
```bash
cd ~/VideoMontaj/videos && npx hyperframes init <nom> --non-interactive --example=blank --skill=general-video
cd <nom> && mkdir -p assets/fonts assets/sfx renders && cp ../../ish/<video>/toza.mp4 assets/video.mp4
```
- Avval `/hyperframes-core` qoidalarini o'qi (bitta paused timeline `window.__timelines["main"]`, `.clip` ga autoAlpha yo'q, `<audio>` da `id`,
  `<video data-start>` timed ota-ichida bo'lmasin, CSS transform + GSAP bir xususiyatda yo'q, `@font-face` lokal faylga).
- **Sahna rejasi** (yozishdan oldin, foydalanuvchiga ko'rsat): `vaqt | aytilgan so'zlar | pasportdagi element`. Har gapga bitta grafik g'oya;
  yuz faqat pasportda aytilgan joyda (green-minimal: viewfinder ichida 2–3 s, eng shaxsiy gapda).
- Yuz kerak bo'lmagan joyda ham ovoz videodan keladi: `<video id="aroll" data-has-audio="true">` butun davomga, ko'rinishini timed bo'lmagan o'rovchi `opacity` boshqaradi.
- **Premium daraja majburiy**: uslub pasportining «Premium ishlov» bo'limi (green-minimal: 8-bo'lim) — o'lcham 65–75%, eyebrow, 3 qatlam, soya/3D, grain, har sahna o'z chiqishi, motion blur 1–3 zarbada.
- Tayyor namuna (premium v3, egasi qabul qilgan daraja): `videos/c0038-500-dollar/index.html` (green-minimal, 9 sahna) — tuzilmani shundan ol: `.w[data-at]` so'zma-so'z blur kirish,
  `[data-type]` typewriter, `ring()` sanoq, pill/hexagon/soat/qadamlar/ellips, sahna oxirida blur+whip chiqish, fon yoylari doim aylanadi.
- Tekshiruv: `npx hyperframes check` → Lint 0 error, Runtime 0, Layout 0 overlapping text, Contrast (WCAG; to'liq ko'ringan holatda ≥3:1).
  Fon dekori kanvasdan chiqsa `data-layout-allow-overflow`. Glow elementlar matn ostida bo'lsin (`.markaz > *:not(.glow){position:relative}`).
- Kadrlar: `npx hyperframes snapshot --at <har sahna o'rtasi> --no-end -o <scratchpad>` → bitta varaqqa yig'ib ko'r, referens varaqlari bilan **yonma-yon** solishtir.

## 5. SFX + silliqlik
- Har kirish/pop/whip/sanoq/typewriter'ga mos effekt (`~/VideoMontaj/assets/ovoz/`, Mixkit, ro'yxat `royxat.json`): ≈1 effekt / element,
  25 s rolikda ~30–36 ta. Ovoz 0.2–0.4, har `<audio>` ga `data-duration` (fayl uzunligi, ≤1.6 s) va ustma-ust tushmaydigan `data-track-index` (3–9 aylanib).
- Harakatlar pasportning 4-bo'limidagi o'lchovlarga mos bo'lsin (kirish 0.3–0.4 s blur 12→0, chiqish 0.15–0.2 s, typewriter 0.03–0.045 s/harf, pop back.out).

## 6. Musiqa bitga, 5%
- Mixkit (bepul, atributsiyasiz): uslub pasportidagi janr; foydalanuvchiga 3–4 trek taklif qil. Green-minimal: `assets.mixkit.co/music/126/126.mp3` («Trap Electro Vibes», 140 BPM).
- `<audio id="musiqa" data-timeline-role="music" ...>` → `npx hyperframes beats` → `python3 ~/VideoMontaj/vosita/bit_moslash.py --davom <s>`
  → tavsiya qilingan `data-media-start` (sahna kesimlari bitga tushadigan, eng baland qism).
- Balandlik **5%**: `data-volume="0.05"` + `data-automation` lane `0 → 0.05 (0.6 s) … 0.05 → 0 (oxirgi 1.2 s)`. Foydalanuvchi «baland» desa — bitta xabar bilan pasaytir.

## Render va topshirish
```bash
npx hyperframes render --quality delivery --output renders/<nom>-v<N>.mp4
```
- Tekshir: `ffprobe` (1080×1920, davomiylik = root `data-duration`, audio bor), `ebur128` (nutq ≈ asl videodagidek, −14…−16 LUFS),
  `fps=2` varaq bilan butun videoni ko'r — bo'sh joy, kesilgan matn, yopilgan yuz yo'qmi.
- Natijani asl video yoniga `<asl nomi>_<uslub>.mp4` qilib nusxala va yo'lini ayt. Har versiyani (v1, v2…) saqla.

## Tuzatishlar
Foydalanuvchi oddiy so'z bilan aytadi («SFX qo'sh», «animatsiya referensdagidek silliq bo'lsin», «musiqa baland»). Tuzatgach, takrorlanadigan
qoida bo'lsa — o'sha uslubning `STYLE.md` oxiriga «Tuzatishlar» bo'limiga sana bilan yoz.

## Windows'da (Claude Code buyruqlarni Git Bash'da bajaradi)
- `python3` o'rniga **`python`** yoz (Windows'da `python3` Microsoft Store yorlig'ini ochadi).
- `~/VideoMontaj` Git Bash'da ishlaydi (= `%USERPROFILE%\VideoMontaj`); Python'ga yo'lni `~/...` yoki `C:/Users/...` ko'rinishida ber.
- ffmpeg: `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` o'rniga oddiy **`ffmpeg`** (o'rnatuvchi qo'ygan to'liq build, drawtext bor).
  `drawtext` da `fontfile=` kerak bo'lsa: `fontfile='C\:/Windows/Fonts/arial.ttf'` (ikki nuqta ekranlanadi).
- whisper-cli `MONTAJ_WHISPER` muhit o'zgaruvchisidan topiladi (o'rnatuvchi qo'ygan) — yangi terminalda ishlaydi.
- Nutqni matnga o'girish CPU'da bajariladi, Mac'dagidan sekinroq — uzun videoda foydalanuvchini ogohlantir.
