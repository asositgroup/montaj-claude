# Uslub pasporti: `youtube-slayd` — uzun YouTube dars, slayd + kamera (2026-10-08)

Manba: @umida_asrolova (3-avlod: U_x5to1vpwM, lU-OKrNUUl4, md7d8g8iv9k, 85vBPNCb794) + @mikhail.timochko (15 video,
AI mavzusidagi 5 tasi: SKvbTPne2rg, JIXS04GejZI, n5dFP5xLmcc, eE1hYPSBB0o, Pm8LHNINkpg). Xom tahlil: `tahlil-umida.md`,
`tahlil-timochko.md`; misol kadrlar: `kitob/index.html`. Shu pasportdan tashqari element qo'shilmaydi.

## 0. Egasining qarorlari (2026-10-08)
- **Asos — Timochko uslubi** (formula, palitra, fokus-ro'yxat, bo'lim kartalari, ekran usullari); Umida — misol/qo'shimcha (intro motion hiylalari).
- Kompozitsiya: slayd CHAPDA, egasi O'NGDA (egasi aytgan; Timochko'da ham S2 varianti bor).
- Palitra — **Timochko** (pastda §3).
- Slayd ichidagi elementlar **gap bilan sinxron** chiqadi (Timochko «fokus-ro'yxat»), Umida kabi birdaniga emas.
- **Subtitr yo'q.**
- **Musiqa faqat intro va yakunda**; dars qismida yo'q.
- Ekran yozuvi qismlarida (egasi C0051 ~14:50 da aytgan): butun ekranda ko'rsatiladigan narsa, egasi o'ng chetda doira videoda.

## 1. Vaqt chizig'i (formula)
| Qism | Uzunlik | Nima |
|---|---|---|
| Hook + motion-intro | 30–60 s | To'liq kamera; har 2–4 s yangi motion hodisa (§5 intro instrumentlari). Birinchi gap = va'da. Zastavka yo'q. Musiqa bor. |
| O'tish | ~0.5 s | Light leak → 1 kadr oq flash → split (butun videoda 1–2 marta, boshqa joyda yo'q). |
| Sarlavha kartasi | 6–9 s | Qorong'i karta (§3) slayd maydonida: video nomi CAPS, oxirgi qator gradient. |
| Reja slaydi | 8–15 s | «Bu videoda:» — bo'limlar ro'yxati/ilon-yo'l, har band aytilganda chiqadi. |
| Bo'limlar | asosiy | Har bo'lim: **bo'lim kartasi** (qora, katta raqam, 4–6 s) → tushuntirish slaydlari → ekran bloklari (≤20 s) → kerak bo'lsa qorong'i «Xulosa:» slaydi. |
| Taklif + CTA | 1–2 daq | Taklif slaydlari → qorong'i «HAVOLA TAVSIFDA ↓» kartasi → to'liq kamera xayr. Musiqa qaytadi. |

## 2. Kompozitsiya (1920×1080)
| Rejim | Geometriya | Qachon |
|---|---|---|
| **S — split (asosiy)** | Slayd `x 0–1080, y 0–1080` (kvadrat, ramkasiz, chokda soya yo'q). Kamera `x 1080–1920` (840×1080), yuz panel markazida (x≈1500), ko'zlar y≈380. | Dars qismining asosiy vaqti |
| **K — to'liq kamera** | 1920×1080; punch-in 1.0 ↔ 1.25–1.4 (manba 4K — sifat yo'qolmaydi) | Intro, hikoya, xayr |
| **E1 — ekran + doira** | Ekran yozuvi/skrinshot to'liq kadr; doira kamera Ø420, `right 30, bottom 30`, qora fon, yuz markazda | ERP/bot/dashboard ko'rsatilganda |
| **E2 — spotlight** | E1 ustida qolgan ekran `rgba(0,0,0,.5)`, fokus to'rtburchak radius 14; ko'chish 0.5 s ease-in-out | Kerakli raqam/tugma/prompt |
| **E3 — hero-oyna** | Qorong'i fon (#0B0B0B + yashil-moviy nur), ekran oynasi 1400×790, radius 24, oq glow 16 px; kirish blur 8→0 + scale 0.92→1, 0.5 s | Eng muhim 2–4 ekran lahzasi |
| **C — karta kamera ustida** | To'liq kamera, ustida oq karta ~700×650 (prompt matni ≥28 px) | Prompt/ko'rsatma |

Kamera: bitta kamera → burchak almashuvi raqamli punch-in bilan. Split'da slayd turganda ham kamera har 4–8 s da keng↔yaqin kesiladi (yuz markazda qoladi).

## 3. Palitra va shrift (Timochko)
| Rol | Qiymat |
|---|---|
| Slayd foni | `#EFEFEF` |
| Karta | `#FFFFFF`, radius 18, soya `0 8px 24px rgba(0,0,0,.08)` |
| Bo'sh band (sharpa) | `#E6E6E6` |
| Urg'u gradient (matn, pill) | `#22C08A → #1870A0` (chapdan o'ngga) |
| «Qadam N» pill | `#20B0A0`, oq matn |
| Salbiy / ijobiy | qizil ✗ `#F02830` / yashil ✅ |
| Qorong'i karta | `#0B0B0B` + yuqorida radial nur `#1E9A78 → #1870A0` (40–60 %) |
| Glow matn (kamera ustida) | oq yoki och sariq `#F2EE9A`, text-shadow 20 px |
| Matn | `#111317`, ikkinchi darajali `#6B7078` |

- Shrift: **Inter** (sarlavha 800, 56–64 px 1080 slaydda, line-height 1.1, markazga; matn 500/600, 28–36 px; kalit so'z bold yoki gradient).
- Kamera ustidagi urg'u caps: **Bebas Neue** (condensed) glow bilan — faqat intro/CTA.
- Emoji: Apple 3D, har kartaga bitta. Ilova logolari (Claude, Telegram, Instagram, amoCRM…) — haqiqiy.
- Slayd chap-yuqorisida: dumaloq avatar 40 px + «fayzullaxon» handle (14–16 px), chetdan 80 px.

## 4. Slayd tuzilishi (1080×1080)
- Sarlavha y≈130–220, markazda; kontent bloki vertikal markazda, kenglik 700–860, kartalar oralig'i 16–24.
- Komponentlar: fokus-ro'yxat (sharpa kartalar), ✗/✅ solishtirish (2 ustun), raqam kartalari (katta raqam gradientda),
  ilon-yo'l/diagramma (kartalar + ingichka gradient o'q), «oldin → hozir», bloknot-karta (katakli fon + 📎) — prompt va «Xulosa» uchun,
  skrinshot kartasi (radius 18, soya).
- Bo'lim kartasi: qorong'i, katta raqam ~200 px + 2 qator nom.
- Bir slayd 10–45 s turadi.

## 5. Animatsiya instrumentlari
**Dars qismi (5 ta + ekran):**
1. Split kirishi — hard cut.
2. Fokus-ro'yxat — yangi band sharpa joyida opacity 0→1 + y 12→0, **0.3 s ease-out**, aytilgan so'zdan 0–0.2 s oldin; oldingi faol band 0.85 ga kichrayadi, soyasi ketadi.
3. Diagramma qurish — tugun 0.3 s fade, o'q-chiziq chizilishi 0.4 s.
4. Raqam sanash — 0.8 s ease-out (statik raqam o'rniga).
5. Slayd almashuvi — header/avatar joyida qoladi; eski kontent 0.2 s (y −12, fade), yangi 0.3 s (y +12 → 0). Bo'lim kartasiga — hard cut.
6. Ekran: virtual kamera pan + zoom 1.0→1.15–1.3 (1–2 s, ease-in-out), spotlight ko'chishi 0.5 s, hero-oyna kirishi 0.5 s.

**Intro/CTA (qo'shimcha):** blur-typewriter (15–25 belgi/s), so'zma-so'z blur-in (0.3 s), kamera kartaga kichrayishi (0.4 s) va qaytishi (0.6 s),
raqam sanash + grafik chizilishi, glow caps typewriter, glass pill, focus pull (kamera xira, matn aniq), light leak + flash (1–2 marta).

## 6. Ritm
- **Egasi (2026-10-08): motion ko'proq** — har 2–3 s da harakat, slayd fonida doimiy yengil harakat, slayd almashuvi animatsiyali, to'liq kamerada kinetik kalit so'zlar (batafsil `videos/yt1-slaydlar/ANIMATSIYA.md` «Zichlik qoidasi»).
- Har 3–6 s da kamida bitta vizual o'zgarish (band, kesim, punch-in, spotlight ko'chishi).
- To'liq kamera bo'lagi 25 s dan oshsa — punch-in yoki slayd.
- Ekran bloki ≤20 s; kutish/yuklanish kesiladi, uzun generatsiya 2–4× tezlashtiriladi.
- Intro va birinchi 1.5 daqiqa 2× zichroq.

## 7. Ovoz
- Musiqa: intro (−20…−24 LUFS atrofida, gap ostida sidechain) va CTA/xayr; dars qismida yo'q.
- SFX: slayd almashuvida yengil whoosh/tick, raqam sanashda tick — juda past.
- Gap: −14 LUFS (YouTube).

## 8. Nima QILINMAYDI
Zastavka/logo-intro; so'zma-so'z subtitr; meme, begona reelslar, stok kliplar; ekranga strelka/qizil doira chizish (spotlight va zoom bor);
har bo'limda light leak/flash; intro'da slayd tizimidan boshqa ranglar (Timochko palitrasi butun videoda).
