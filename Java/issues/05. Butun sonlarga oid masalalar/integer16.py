"""
Masala: 3 xonali natural son berilgan.
Uning birlar xonasidagi raqam bilan o`nlar xonasidagi raqamni
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
        yangi_son = int(f"{son[0]}{son[2]}{son[1]}")
        son = int(son)

        natija = f"\n{son} sonining birlar xonasidagi raqam bilan o`nlar xonasidagi raqamni almashtirsak {yangi_son} soni hosil bo`ladi."

        # yangi_son = (son // 100) * 100 + son % 100 // 10 + (son % 10) * 10
        # natija += f"\n{son} sonining birlar xonasidagi raqam bilan o`nlar xonasidagi raqamni almashtirsak {yangi_son} soni hosil bo`ladi."

    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)

"""
input: 153;
output: 135;

___    ___
abc => acb

100a + 10b + c
100a + 10c + b

a = son // 100
b = son % 100 // 10
c = son % 10
"""
