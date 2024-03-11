"""
Masala: n natural soni berilgan.
Dastlabki n ta toq sondan tashkil topgan
massivni hosil qiling va elementlarini chiqaring.
Bajardi: Haydarali Asrorov
Sana: 02.03.2024
"""

n = input("\nNatural son kiriting: ")

try:
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0:
        toq_sonlar = list(range(1, 2 * n, 2))
        natija = f"\nDastlabki {n} ta toq sondan tashkil topgan sonlar ro`yxati:\n{toq_sonlar}"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
