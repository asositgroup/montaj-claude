# Green Minimal — uslub pasporti

Manba: «02 - Claude bilan PROFESSIONAL montaj qilish» darsi (Isroiljon Abdullayev, youtube.com/watch?v=j_xznSoc2Q8).
Asl video: `~/Kurslar/Nuvi/02 - Claude bilan PROFESSIONAL montaj qilish.mp4`. Reels namunasi 0:00–0:19 da (o'ng panel),
16:9 namunasi 4:25–7:00 da. Kadrma-kadr varaqlar `referens/` papkasida.
Pasportning 1–3-bo'limlari darsda Claude yozgan `styles/green-minimal/STYLE.md` dan ko'chirilgan (ekrandan o'qildi),
4-bo'lim esa shu yerda 0.1 s qadam bilan o'lchangan.

Qisqasi: oq fonda **yuzsiz motion-grafika**, bitta urg'u rangi (yashil). Kameradagi yuz faqat o'rtada 2–3 s
(viewfinder ramka ichida) chiqadi, qolgan vaqtda ekranda gapirilayotgan gapning grafikasi turadi.

## 1. Ranglar

| Token | Hex | Ishlatilishi |
|---|---|---|
| fon | `#FDFDFD` | butun video, deyarli oq |
| siyoh | `#0B0B0B` | asosiy matn, qora ikonka |
| yashil | `#10BE00` | yagona urg'u: to'ldirilgan pill, hexagon, ring, chiziq |
| yashil-matn | `#27A01A` | matndagi urg'u so'z |
| yashil-glow | `#10BE00` 10–18% | so'z ortidagi yumshoq radial nur, xira halqalar |
| kulrang | `#9A9A9A` | o'tib ketgan / ikkinchi darajali so'z, ring treki |

Boshqa rang yo'q. Urg'u bitta: yashil. Gradient, soya-plashka, sariq, qizil yo'q.

## 2. Shriftlar

- **Sans (asosiy):** Inter Tight (yoki Geist) 500–600, tracking −0.045em (v2 da shu tanlangan). Matn markazda,
  kichik-o'rta o'lcham: sarlavha 64–90 px (1080 kenglikda). **Hech qachon ulkan emas.**
- **Italic serif (urg'u):** Instrument Serif Italic (yoki Playfair Display Italic). Faqat 1–2 so'z, sans qatorning
  ichida yoki ostida («Bu montajni *men* qilmadim», «Mijozlaringiz bilan / *gaplashadi*»). Urg'u so'z yashil yoki qora.
- **Mayda izoh qatori:** sans 400, 22–26 px, 2 qator, markazda.
- Kontur, qalin soya, CAPS, emoji **yo'q**.

## 3. Harakat lug'ati (referensdagi tartibda)

1. **So'zma-so'z chiqish:** so'z blur(12px) + opacity 0 dan aniqlashadi; ketishda blur bilan eriydi.
2. **Urg'u so'z + glow:** urg'u so'z yashil, orqasida katta yumshoq yashil radial nur; atrofida mayda `$` yoki ikonkalar suzadi.
3. **Xira yashil halqalar:** burchaklarda katta blur qilingan yashil yoylar va ingichka kulrang doira chiziqlari sekin aylanadi (fon dekori, har sahnada).
4. **Soat strelkasi:** yaqin kadrda soat yuzi, strelka «tik» qilib siljiydi, motion blur bilan; ostida matn.
5. **Viewfinder ramka:** to'rt burchakli yashil qavs ramka; ichida sarlavha + ikonkalar qatori (yashil odamchalar, markazdagisi qora va qavsda) + mayda izoh. **Odamning videosi ham shu ramka ichida chiqadi.**
6. **Progress ring:** kulrang trek + yashil yoy, markazda raqam sanaydi (14 → 24 → «24/7»), ostida mayda matn.
7. **Hexagon tugunlar:** yashil hexagon ichida oq chiziqli ikonka, ingichka qora leader-chiziq bilan label; tugunlar birin-ketin «pop» bo'ladi.
8. **Pill buluti:** yashil to'ldirilgan va qora konturli pill'lar birin-ketin o'ngdan sirpanib kirib joylashadi.
9. **Typewriter + scroll:** gap harf-harf yoziladi, chapga suriladi, eski qism kulrang bo'ladi.
10. **Ellips highlight:** yakuniy ibora atrofida yashil ellips chiziladi + glow (masalan, «"agent"»).
11. **Logo end card:** markazda kichik logo + handle.

**O'tishlar:** tez blur/whip (motion blur), qattiq kesish yo'q. Kamera ba'zan 3D qiyshayib yaqinlashadi (soat sahnasi).
Kamera to'xtamaydi: har sahnada juda sekin (≈2–4%) zoom yoki suzish bor.

## 4. Kadrma-kadr o'lchovlar (0.1 s qadam, `referens/varaq_0.1s_07-10s.jpg`)

- **Sarlavha kirishi:** 0.3 s ichida blur 12 → 0, opacity 0 → 1 (0.3 s da xira, 0.5 s da tiniq). Tepada qoladi, sahnalar almashganda ham.
- **Element chiqishi:** 0.1–0.2 s ichida blur bilan eriydi (1.0 s tiniq → 1.1 s xira → 1.2 s yo'q). Ease: power2.in.
- **Keyingi element:** oldingisi ketgach ≈0.1 s bo'sh joy, keyin keladi. Ekranda bir vaqtda **bitta g'oya**.
- **Typewriter:** ≈0.03 s / harf (stagger 0.02–0.045 s), har harf blur'dan chiqadi. Ikkinchi qator (italic yashil) birinchisi tugagach boshlanadi.
- **Ring sanog'i:** 0.1 s ga +1 (22 → 23 → 24), keyin «24/7» ga almashadi; yoy raqam bilan birga to'ladi; atrofida yashil glow.
- **Hexagon pop:** 0.2 s: scale 0.6 → 1.08 → 1, opacity 0 → 1; keyin leader-chiziq 0.15 s da chiziladi, label harf-harf.
  Keyingi hexagon ≈0.5 s keyin.
- **Sahnaga kirish:** asosiy element 0.34–0.4 s; qolganlari ekran tashqarisidan whip bilan (yo'nalishli motion blur 80 px → 0).
- **Pill'lar:** o'ngdan (x: +26 px → 0) sirpanib, 0.12 s oraliq bilan.

## 5. Kompozitsiya (9:16, 1080×1920)

- Sarlavha tepada (y ≈ 250–330, Instagram xavfsiz zonasi ichida), markazda 1 ta g'oya-grafika, pastda bo'sh.
- Grafika o'lchami kichik-o'rta: ekranning ≈30–45% kengligi. Atrofida havo ko'p.
- Odam videosi: faqat viewfinder ramka ichida, ≈2–3 s, gapning eng shaxsiy/emotsional joyida (masalan, «men qilmadim»).
  Butun video davomida yuz to'liq ekranda **turmaydi**.
- Xavfsiz zona: tepa 250 px, past 450 px, o'ng 120 px — matn va grafika shu zonada.

## 6. Ovoz

- **SFX:** har kirish/pop/whip/sanoqqa mos mayda effekt (darsda 24.8 s rolikda 32 ta SFX). Yumshoq, past, nutqdan baland emas.
  Turlari: whoosh (whip), pop (hexagon/pill), tick (soat, sanoq), soft click (typewriter bloki), shimmer (ellips/glow).
- **Musiqa:** Mixkit, elektron/minimal (darsda «Trap Electro Vibes», 140 BPM). Trek bitga moslanadi: sahna almashuvlari
  bitga tushadigan joydan boshlanadi. Balandligi **≈5%** (asl darajadan ≈−26 dB), nutqda yana pasayadi, oxirida fade.

## 7. Tekshiruv (render oldidan, majburiy)

`hyperframes check`: Lint 0, Runtime 0, Layout — 0 ta bir-birini yopgan matn, Motion, Contrast — barcha matn WCAG AA dan o'tadi.
So'ng tekshiruv kadrlari ko'rib chiqiladi va referens varaqlari bilan **yonma-yon** solishtiriladi.

## 8. Premium ishlov (2026-10-05, egasi: «premium darajani bermayapti»)

v2 (faqat pasportning 1–7) egasiga arzon ko'rindi: elementlar kichik (~35% kenglik), bo'sh oq fonda bitta narsa suzadi,
soya/chuqurlik yo'q, hamma animatsiya bir xil. v3 (`videos/c0038-500-dollar`) qabul qilingan daraja — har yangi videoda majburiy:
- **O'lcham:** asosiy grafika kenglikning 65–75% (halqa 700 px, narx kartochkasi 760 px, soat 800 px). Sarlavha 112 px, 600, tracking −0.055em, kursiv so'z 1.14em.
  Sarlavha ustida **eyebrow**: 28 px, 600, UPPERCASE, tracking 0.32em, kulrang + yashil nuqta (sahna mavzusi: «Savol», «Natija», «Yo'l xaritasi»…).
- **3 qatlam har sahnada:** orqada ulkan xira raqam/belgi (`$500`, `?`, `$3000`, 470–1200 px, yashil 5–7%, kadrdan chiqib turadi, sekin suriladi),
  o'rtada qahramon element, oldinda aksent (tegcha, lower-third kartochka, zarrachalar).
- **Chuqurlik:** oq kartochkalar ko'p qatlamli soya bilan (`0 50px 100px /13%, 0 14px 30px /7%, 0 2px 6px /5%`), yashil to'ldirilgan narsalar
  gradient (`#2BB51B → #1F8F12`) + yashil soya. 3D kirish: `transformPerspective` + rotationX/rotationY (halqa 55°→0, yuz kartochkasi −28°→−6°→5°, soat 38°/−26° → 6°/4°).
- **Tekstura:** butun kadrga feTurbulence grain (7%, multiply) + juda yengil vinyetka + sekin suzuvchi yashil nur.
- **Harakat xilma-xilligi:** har sahnaning o'z chiqishi (whip chap/o'ng, scale-down blur, kamera push-through, yuqoriga ketish, hard cut).
  Kirish ease `expo.out` 0.4–0.7 s, chiqish `power3.in` 0.16–0.24 s. Kirgandan keyin ham tirik: hexagon'lar suzadi, glow nafas oladi, yuz kartochkasi sekin aylanadi.
- **Motion blur** (`npx hyperframes add motion-blur`, `data-hf-motion-blur`) faqat 1–3 keskin zarbada ($2 000 kartochka slam, soat strelkasi). Video bor elementga qo'yilmaydi.
- **Yuz kartochkasi:** 800×820, radius 44, soya, burchak qavslari, «● LIVE» yorlig'i, ostida lower-third oq kartochka (gapning davomi).
- **CTA:** katta gradient tugma (880×210) + strelka, ustidan yaltiroq nur o'tadi (2 marta), kursor kirib bosadi (to'lqin), ellips chiziladi.
- **Hook:** birinchi 0.4 s ichida markazda qahramon element bo'lsin.
- Typewriter harflari **so'z bo'yicha guruhlanadi** (`.soz{white-space:nowrap}`) — aks holda qator so'z o'rtasidan bo'linadi.
- Bezak matnlarga `data-layout-ignore aria-hidden="true"` (tekshiruv ularni o'qiladigan matn deb hisoblamasin).
- Uzun gap boshida grafika hali kelmasa (ro'yxat, progress) — elementlarni **oldindan bo'sh holatda** chiqar (skelet chiziq / 0%) va so'z aytilganda to'ldir;
  shunda markaz hech qachon >0.5 s bo'sh qolmaydi (2026-10-05, kosmetolog videosi).
