#!/bin/bash
# Referens videolar: 360p (faqat tasvir) + avto-subtitr — tahlil uchun, keyin o'chiriladi
cd "$(dirname "$0")"
T="hLtFXXK71uQ NTwn9YFAuio Djh6KrQE5r8 4OcvmFsFPF8 SKvbTPne2rg gKs-20jiXy8 2yja0juOMII qmFv2dBb5QM GhzEw2GiWOA SIAM5Aje6jI JIXS04GejZI z7VXGy_3O4M"
U="md7d8g8iv9k -AWNk8VPOY0 HgSnAI5OO1I lU-OKrNUUl4 85vBPNCb794 eMVhTvHNx04 0Gwz338XVp0 SoZ5ErLLkqc 9GBW69Vh8JM U_x5to1vpwM KmvLsa7x_Ck Fpo6w6RiUV8 aa1DajmiBoQ"
for id in $U $T; do
  d=umida; [[ " $T " == *" $id "* ]] && d=timochko
  mkdir -p $d
  yt-dlp -q --no-warnings -f "bv*[height<=360][ext=mp4]/bv*[height<=360]" -N 4 \
    -o "$d/%(id)s.%(ext)s" -- "$id" || echo "XATO $id"
  echo "OK $d $id"; sleep 5
done
