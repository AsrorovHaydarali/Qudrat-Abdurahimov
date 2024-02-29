"""
Masala: 2 xonali son berilgan. Oldin uning o`nlar xonasidagi raqamni,
so`ng birlar xonasidagi raqamni chiqaruvchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 21.02.2024;
"""

son = input("\n2 xonali natural son kiriting: ")

try:
    son = int(son)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if son >= 10 and son <= 99:
        natija = f"\n{son} sonining:\nO`nlar xonasida {son // 10} raqami mavjud;\
            \nBirlar xonasida {son % 10} raqami mavjud;"
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
