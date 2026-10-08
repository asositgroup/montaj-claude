# Asror — uslub pasporti

Manba: Instagram @asror.iskandar0v. 2025-11-16 dan 2026-10-04 gacha chiqqan so'nggi 100 ta reels ko'rildi:
84 tasi o'zining, 16 tasi hamkorlik (Vizier, asoschilar_podcast va boshqalar; ularda boshqa montajchi ishlagan, pasportga olinmadi).
Asl fayllar 720×1280 (Instagram veb shunday beradi), 25/30 fps. Hamma o'lchov **1080×1920 ga o'tkazilgan**.

Qanday o'lchandi:
- Har video 1 s qadamli varaq va birinchi 3 s ning 0.2 s qadamli varag'i (`referens/varaq/`, `referens/hook/`).
- Kesishlar ffmpeg scene > 0.3 bilan sanaldi (`referens/olchov.json`).
- 4 ta tahlilchi 25 tadan ko'rdi, asosiy kadrlar pikselda o'lchandi (`referens/kadrlar/`).
- Shrift nomlari ko'z bilan tanlangan eng yaqin Google Font.

**Qisqasi.** Iliq studiyada **talking head** (gapiruvchi odam), birinchi soniyalarda **50/50 split** (tepada odam, pastda B-roll).
Split chizig'i ustida **oq plashka + emoji** (hook savoli), ko'krak balandida **kichik ko'k chip subtitr**. Grafika kam va aniq:
katta raqam, «#1» bo'lim, IG/YouTube kartochkasi, CTA kalit so'z. Kesish faqat keng ↔ yaqin plan. Effekt deyarli yo'q.

O'z videolari bo'yicha medianlar: davomiylik **89 s** (75–102), kesish 12 ta, o'rtacha sahna **6.3 s**.
Keng↔yaqin almashuvlar bir kadrdan crop bo'lgani uchun sanoqqa kirmagan: amalda har **2–6 s** da.

## 1. Ranglar

| Token | Hex | Qayerda |
|---|---|---|
| plashka | `#FFFFFF` (`#FDFDFB`) | hook sarlavha plashkasi, split chizig'i, IG kartochkalar |
| siyoh | `#111111` | plashkadagi matn |
| kok | `#043BA2` (o'lchandi: `#043BA2`, `#023BA2`, `#073BB3`) | subtitr chipi, to'liq kenglikdagi polosa, CTA plashka |
| kok-toq | `#033392` | katta raqam ostidagi yirtiq polosa («500$») |
| kok-yorqin | `#1F4FD6` | «#1…#5» raqam, ikonka kartochkalari (`#1C46C8`, qog'oz teksturasi) |
| oq-matn | `#FFFFFF` | subtitr, katta so'zlar |
| raqam-gradient | `#D4D3D8 → #3F4247` (vertikal) | ulkan raqam/yil («2026», «90%», «28») |
| shisha | to'q teal, ~40% shaffof + och 1 px kontur | pill ro'yxat, chip, karta (faqat premium rejim) |

**Grade:** iliq studiya (amber lampa, yog'och, kitob javoni, bokeh), soyalarda yengil teal, qora biroz ko'tarilgan (matt).
Hissiy yoki «yomon» gapdagi B-roll oq-qora. Urg'u rangi bitta: **ko'k**. Sariq, yashil va qizil urg'u yo'q.

## 2. Shriftlar

- **Plashka (hook):** Inter 800 (asli SF Pro Display Bold'ga o'xshaydi), 44–48 px. Ko'pincha KATTA HARF, ba'zan savol shaklida.
  Boshida yoki oxirida 1 ta Apple emoji (😳 😊 😅 🤔 🙌 💰 🧠 ✅ 😏). Tracking 0.
- **Subtitr chipi:** Inter 600, 28–32 px, kichik harf.
- **Qavsli subtitr** (2026-07 dan): Inter 300, 36–40 px, `[ so'z so'z ]`.
- **Katta so'z:** Inter Tight 800 Italic (yoki Plus Jakarta Sans 800 Italic), 150–230 px, oxirida nuqta yoki «?» / «!».
  Misollar: «Aslida.», «Savol.», «Hook!». Ostidagi qator Inter 500, 44 px.
- **Ulkan raqam:** Inter 800 / Montserrat 800, harf balandligi ~180 px, gradient (1-bo'lim).
- **Iqtibos so'z:** Inter 700 Italic, ~120 px, qo'shtirnoq bilan: «“Master gruppa”», «“Tadbirkor”».
- Serif kursiv faqat juda kam (Instrument Serif Italic: «Tarixi»). Kontur, qalin soya, karaoke sariq va Montserrat Black **yo'q**.

## 3. Harakat lug'ati (uchrash tartibida)

1. **Split hook** (o'z talking head videolarining aksariyatida): kadr 50/50, tepada spiker, pastda B-roll, orasida 6 px oq chiziq.
   Rubrika va selfi videolarda teskari: tepada B-roll yoki mehmon, pastda spiker.
   Split 3–17 s turadi, keyin hard cut bilan to'liq kadrga o'tiladi. Har 15–20 s da qayta kelishi mumkin.
2. **Oq plashka** split chizig'i ustida, 0.0 s dan **animatsiyasiz** turadi, split bilan birga yo'qoladi.
3. **Ko'k chip subtitr:** 1–3 so'z, ibora bo'yicha **animatsiyasiz** almashadi. Urg'u yo'q, karaoke yo'q.
4. **Keng ↔ yaqin plan:** gap chegarasida hard cut, yaqin plan 1.3–1.6× (bir kadrdan crop). Asosiy «montaj» shu.
5. **B-roll:** split'ning pastida (kliplar 0.4–2 s da almashadi) yoki to'liq ekran 2–4 s.
   Manba: AI-generatsiya (masalan UFC'dagi Ronaldo/Messi), mashhur odamlar kliplari, o'z tadbirlari, ekran yozuvi.
6. **Kartochkalar:** IG profil skrinshoti (oq, radius 24, eni ~70%, ba'zan obunachi soni sanaladi), IG izoh kartochkasi
   (hook sifatida: «izohga javob»), YouTube thumbnail kartochkasi (oq ramka, radius 16).
7. **Ulkan raqam/yil:** «2026», «90%», «40». Chok ustida yoki ko'krakda, odamning oldida, belgilarma-belgi 0.3–0.4 s da paydo bo'ladi.
8. **«#N» bo'lim:** «#1 qaror», «#2», «#1 Sabab.». Ko'k heavy italic, oq kontur ~6 px, yozish kursori bilan yoziladi. Ro'yxatli videolarda bo'lim ochadi.
9. **Ko'k polosa, bitta so'z** (rubrika seriyasi): chokda to'liq kenglik, balandligi ~78 px, oq 56 px so'z.
10. **Katta italic so'z + qator:** chapga tekislangan (x≈70, y≈1270), ostidagi qator so'zma-so'z chiqadi.
11. **Ikonka kartochkalari:** ko'k plitka + oq line-ikonka + yorliq pill, punktirli tanlov ramkasi (Canva uslubi), kursor qo'li «Like», «Taklif» va «Follow» ni bosadi.
    Ikonkalar qatori 0.1 s qadam bilan scale-pop qiladi.
12. **Oq-qora urg'u:** «yomon» gapda kadr oq-qora bo'ladi, ko'krakda emoji (💀) chiqadi.
13. **Light leak + oq flash:** 0.1 s leak, 0.1 s oq, keyin cut. Videoda ko'pi bilan 1 marta.
14. **Ochilish effekti** (0–0.6 s, ixtiyoriy): blur-in 0.2 s yoki zoom-out 1.25 → 1.0×.
15. **CTA:** kalit so'z («“ Ayol ”», «“3”», «KOMENTARIYADA "5" YOZING») ko'k plashkada, IG profil kartochkasi + kursor «Follow».
    Ba'zan oxirida qora ekran va kichik «Asror_Iskandarov».

**O'tishlar:** 90%+ hard cut. Whip, zoom-transition va glitch faqat premium rejimda va kam ishlatiladi.

## 4. Kadrma-kadr o'lchovlar

- **Split chizig'i:** y = 957–963, oq, 6 px, butun kenglik. Ikkala yarmi 1080×957 cover.
- **Oq plashka:**
  - Markazi aynan y = 960 (chiziq ustida, chiziqni yopadi).
  - Balandlik 80–111 px (1 qator), 2 qatorli bo'lsa ~160 px. Kenglik matnga mos, 71–81% (765–873 px).
  - Radius ~12 px, padding ~20×12. Soya yo'q.
  - 0.0 s da tayyor holda turadi (0.2 s qadamli varaqlarda kirish animatsiyasi ko'rinmadi).
- **Ko'k chip:**
  - Balandlik ~57 px, radius ~4 px. Ichida tepadan pastga yengil yorug'lik (gradient `#1A4FC0 → #043BA2`) va pastda 2 px to'qroq qirra.
  - Eni matnga mos (~180–330 px).
  - Joyi: split'da chiziq ustida yoki ostida (y≈930–1010), to'liq kadrda ko'krakda (y≈1100–1440).
  - Ibora almashishi 0.4–0.6 s, kesib almashadi.
- **Qavsli subtitr:** y≈1000–1380, almashishi 0.4–0.6 s, animatsiyasiz.
- **Ulkan raqam:** eni 51–55%, belgilar stagger ~0.08 s (jami 0.3–0.4 s), fade + yengil yuqoriga siljish.
- **Ikonka pop:** 0.1 s oraliq, scale 0.6 → 1.05 → 1.
- **Katta italic so'z:** o'ngdan yoki chapdan blur-slide 0.2–0.3 s, qatorlar orasida 0.2 s. Chiqishi ham blur-slide.
- **Light leak/flash:** jami 0.2 s.
- **Keng/yaqin almashuvi:** har 2–6 s, faqat gap tugagan joyda.

## 5. Kompozitsiya (9:16, 1080×1920)

- **To'liq kadr:** odam markazda, beldan yoki ko'krakdan yuqori, boshi y≈20–35%. Fon: kitob javoni, lampa, sayoz DOF.
  Mikrofon (SM7B tipi) shtangada yoki yoqada DJI lav. Bir rangli kiyim.
- **Split:** spiker yarmida boshi chiziqdan ~150 px yuqorida tugaydi (plashka yuzni yopmasin).
- **Matn hech qachon pastki 450 px ga tushmaydi:** subtitr ko'krakda, CTA kartochka y ≤ 1470. Xavfsiz zona: tepa 250, past 450, o'ng 120.
- Bir vaqtda ekranda: plashka + subtitr + ko'pi bilan 1 ta grafik element.

## 6. Ovoz

Ovoz hali o'lchanmadi (faqat vizual tahlil qilindi). Vizualdan bilinadigani:
- ikonka pop, ro'yxat skroli va kursor bosishi SFX bilan (taxmin);
- nutq birinchi o'rinda, musiqa sezilmas darajada.
Birinchi montajda: SFX faqat grafik element chiqqanda (pop/click/whoosh, 0.2–0.3), musiqa 5% (`/montaj` 6-qadam).

## 7. Tekshiruv

- `hyperframes check`: Lint 0, Runtime 0, Layout 0 (bir-birini yopgan matn yo'q), Contrast ≥ 3:1.
- Kadrlarni `referens/kadrlar/` bilan yonma-yon solishtir. Asosiy referenslar:
  - `g3_DYr7Vj7tu2N_1.0.jpg` va `g1_DXSHlUJDZHZ_0.5.jpg`: split + plashka.
  - `g1_DW_reQMjQus_12.7.jpg`: «2026» + ko'k chip.
  - `g1_DSAX15eDQ0h_55.jpg`: «500$» polosa.
  - `g3_DbiwtlhN-BX_7.2.jpg`: qavsli subtitr.
  - `g4_Dcly2DatBlq_4.6.jpg`: «Aslida.».
  - `g4_DR4fuikDZ1P_28.8.jpg`: ikonka kartochka.
  - `g3_DXHaLazDWVm_88.jpg`: YouTube CTA.
  - `g3_strip_flash.jpg`: light leak, 10 fps.

## 8. Ikki rejim

- **`asror` (asosiy, standart):** 1–9, 12, 13, 15-elementlar. Split hook + oq plashka + ko'k chip + keng/yaqin + B-roll + 1–3 ta grafik (raqam, «#N», kartochka) + CTA.
- **`asror premium`** (2026-07 dan chiqqan videolar): qavsli subtitr, katta italic so'zlar, shisha pill/kartochkalar, ochilish effekti (14), ikonka kartochkalari (11).
  Faqat foydalanuvchi «premium» desa ishlatiladi.

## 9. Nima ishlaydi (layk bo'yicha, 100 video)

To'rtala tahlilchi bir xil xulosaga keldi:
- **Grafikani ko'paytirish layk keltirmagan.** Eng boy motion-grafikali videolar (DSAX, DcbON, Dciq, Dbs_J, DctdM) pastki 30% da.
  #1 (164k) faqat bitta plashka bilan qilingan.
- **Ishlaydigani — hook kontseptsiyasi:** birinchi kadrda tanish yoki kutilmagan yuz (AI Ronaldo, Shaxzod Kasimov), real voqea (hovli, farzand),
  izohga javob. Faqat odam va savolli plashka kuchsizroq.
- **Dalil:** DR_Z (25k layk) va DSCD (3.3k layk) bir kun farq bilan chiqqan, montaji deyarli bir xil. Farqni mavzu va hook bergan.
- **Ehtiyot:** kam layklilarning ko'pi yangi videolar (2026-08). Vaqt omilini to'liq ajratib bo'lmaydi.

**Montajga qoida:** standart rejim sodda bo'lsin. Kuch hookka sarflanadi (B-roll tanlash va plashka matni), grafikaga emas.
