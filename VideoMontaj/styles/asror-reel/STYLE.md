# asror-reel — uslub pasporti

Manba: Instagram reel `Dc_Xx-BtZs1` (@asror.iskandar0v, 88.8 s, 1080×1920, 25 fps), egasi 2026-10-07 da berdi:
«animatsiyalari va rang berishi yoqdi, qo'llab ko'r». Asl video `referens/reel-Dc_Xx-BtZs1.mp4` (gitignore), varaqlar
`referens/varaq_1s.jpg` (umumiy), `yaqin.jpg` (12 asosiy kadr), `harakat_0.1s.jpg` (katta so'z, 3D stak, tugma — 0.1 s qadam).
Birinchi qo'llanishi: `videos/ai-seminar-body` (mix pro + green-minimal bilan aralash).

## 1. Ranglar
| Token | Hex | Qayerda |
|---|---|---|
| kul | `#ECECEC` | minimal sahnalar foni (chat, tugma, yillar g'ildiragi) |
| siyoh | `#111111` | kulrang fondagi matn, bosilgan tugma |
| kok-chuqur | `#05041A` → `#0A0840` → `#1412A8` → `#2A2DFF` | 3D sahnalar: pastki-chap burchakdan radial gradient |
| kok-kv | `#2B33FF` (20–90%) | suzuvchi piksel kvadratlar (90 px), kartochka to'plami |
| yashil | `#3FA34D`-ga yaqin | mahsulot kartochkalari (green-minimal yashili bilan almashtirsa bo'ladi) |
| oq | `#FFFFFF` | spiker ustidagi matn |

## 2. Shriftlar
Og'ir grotesk (SF Pro / Inter Tight 700–800, tracking −0.05em) + ingichka italic urg'u (Instrument Serif). Spiker ustida:
kichik italic qator (60–70 px) tepada, ostida katta so'z (150–170 px). Kichik subtitr: bitta-ikki so'z, 60 px, 700, oq, ko'krak balandligida.

## 3. Harakat lug'ati
1. **Katta so'z harfma-harf** (0.06 s/harf, har harf blur'dan), kichik italic avval turadi; keyingi so'zga qattiq almashadi.
2. **So'z g'ildiragi** (iOS picker): chapda qalin so'z • o'ngda vertikal ro'yxat, faol so'z oq, qolganlari 35%, tepa-past mask.
3. **Piksel-mozaika o'tish**: 90 px kvadratlar tasodifiy tartibda ≈0.2 s da qoplaydi, sahna almashadi, ≈0.22 s da ochiladi (urug'li tartib!).
4. **3D kartochka to'plami**: ko'k kartochkalar pastki-chapdan perspektiv bilan uchib kiradi (≈0.6 s, katta → kichik), keyin markazda rasm/telefon pop.
5. **Tugma + kursor**: oq tugma, kursor kiradi, bosilganda 0.1 s da qoraga o'tadi, kursor chiqib ketadi.
6. **Chat/izoh kartochkasi** oq, yumshoq soya, matn harf-harf yoziladi.
7. **Spiker oval/kartochkada** kulrang fon ustida (shaxsiy tanishtiruv).
8. **Yashil mahsulot kartochkalari** rasm + «Next →», bir-birining ustiga motion blur bilan almashadi.
9. Viewfinder burchak qavslari spiker ustida.

## 4. Rang berish (spiker)
Sovuq kino grade: soyalar teal, to'yinganlik past, o'rta tonlar yorug', qora biroz ko'tarilgan. ffmpeg (iliq studiyadagi A7 III uchun sinalgan):
`eq=contrast=1.03:saturation=0.78:gamma=1.12:brightness=0.02,colorbalance=rs=-0.07:gs=0.01:bs=0.08:rm=-0.03:gm=0.005:bm=0.02,curves=all='0/0.05 0.25/0.28 0.6/0.66 1/0.97',unsharp=5:5:0.3:5:5:0`
(`ish/fayz-ai-seminar/kes.py` GRADE). Qorong'iroq variant (vinyetli) egasining iliq fonida juda xira chiqdi — ishlatilmaydi.

## 5. Kompozitsiya
Spiker ≈50% vaqt, qolgani to'liq ekran kulrang yoki ko'k sahnalar. Matn tepada 290–560 px (eyebrow + sarlavha), qahramon element markazda,
pastki 450 px bo'sh (Instagram xavfsiz zonasi).
