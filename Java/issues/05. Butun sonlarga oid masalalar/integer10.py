"""
Masala: 3 xonali natural son berilgan.
Uning birlar xonasidagi va o`nlar xonasidagi raqamni aniqlovchi dastur tuzilsin;
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
        natija = f"\n{son} sonining birlar xonasida {son % 10} raqami, o`nlar xonasida {son // 10 % 10} raqami kelgan."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
