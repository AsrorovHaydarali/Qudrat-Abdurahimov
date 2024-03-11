"""
Masala: Qaysidir yil berilgan. Berilgan yilning qaysi
yuz yillikka kirishini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 29.02.2024
"""

# import math

yil = input("\nYilni kiriting: ")

try:
    yil = int(yil)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if yil > 0:
        # asr = math.ceil(yil / 100)
        asr = (yil - 1) // 100 + 1
        natija = f"\n{yil}-yil {asr}-asrga tegishli yil bo`lib hisoblanadi."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)

"""
yuz yillik == asr

1-asr:
[1 ; 100]

2-asr:
[101 ; 200]

3-asr:
[201 ; 300]

...

20-asr:
[1901 ; 2000]
"""
