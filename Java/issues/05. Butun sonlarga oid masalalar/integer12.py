"""
Masala: 3 xonali natural son berilgan.
Uning raqamlarini teskari tartibda yozishdan
hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 27.02.2024;
"""

son = input("\n3 xonali natural son kiriting: ")

try:
    son = int(son)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if son >= 100 and son <= 999:
        natija = f"\n{son} sonining raqamlarini teskari tartibda yozsak, {int(str(son)[::-1])} soni hosil bo`ladi."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
