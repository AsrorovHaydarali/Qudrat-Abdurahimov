"""
Masala: 3 xonali natural son berilgan.
Uning o`nlar xonasidagi raqam bilan yuzlar xonasidagi raqamni
almashtirishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
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
        son = str(son)
        yangi_son = int(f"{son[1]}{son[0]}{son[2]}")
        son = int(son)
        # yangi_son = (son % 100 - son % 10) * 10 + (son // 100) * 10 + son % 10
        natija = f"\n{son} sonining o`nlar xonasidagi raqam bilan yuzlar xonasidagi raqamni almashtirsak {yangi_son} soni hosil bo`ladi."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
