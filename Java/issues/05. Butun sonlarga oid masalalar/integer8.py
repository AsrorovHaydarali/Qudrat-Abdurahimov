"""
Masala: 2 xonali son berilgan. Uning raqamlari o`rnini
almashtirishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
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
        son_teskari = int(str(son)[::-1])
        natija = f"\n{son} sonining raqamlari o`rni almashtirilishidan {son_teskari} soni hosil bo`ladi."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
