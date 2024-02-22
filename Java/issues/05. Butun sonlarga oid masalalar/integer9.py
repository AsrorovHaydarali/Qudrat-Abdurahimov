"""
Masala: 3 xonali son berilgan.
Uning yuzlar xonasidagi raqamni aniqlovchi dastur tuzilsin.;
Bajardi: Haydarali Asrorov;
Sana: 21.02.2024;
"""

son = input("\n3 xonali natural son kiriting: ")

try:
    son = int(son)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if son >= 100 and son <= 999:
        natija = f"\n{son} sonining yuzlar xonasida {son // 10} raqami kelgan."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
