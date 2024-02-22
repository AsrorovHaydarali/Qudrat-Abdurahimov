"""
Masala: Qayiqning tezligi v, daryo oqimining tezligi u.
Qayiqning daryo oqimi bo`yicha harakatlanish vaqti t1,
daryo oqimiga qarshi harakatlanish vaqti t2.
Qayiqning yurgan yo`lini aniqlovchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 18.02.2024;
"""

v = input("\nQayiqning tezligini kiriting (km/soat): ")
u = input("Oqimning tezligini kiriting (km/soat): ")

t1 = input("\nOqim bo`yicha harakatlanish vaqtini kiriting (soat): ")
t2 = input("Oqimga qarshi harakatlanish vaqtini kiriting (soat): ")

try:
    v = float(v)
    u = float(u)

    t1 = float(t1)
    t2 = float(t2)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if v >= 0 and u >= 0 and t1 >= 0 and t2 >= 0:
        s1 = (v + u) * t1
        s2 = abs(v - u) * t2
        s = s1 + s2

        natija = f"\n{v} km/soat tezlikda harakatlanuvchi qayiq {u} km/soat tezlikda oquvchi daryoda\
            \noqimga yo`nalishi bo`yicha {t1} soat va oqimga qarshi {t2} soat harakatlansa,\
            \nja'mi bo`lib {s} km masofani bosib o`tadi."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
