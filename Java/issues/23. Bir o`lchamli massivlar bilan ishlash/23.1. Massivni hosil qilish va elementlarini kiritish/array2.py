"""
Masala: n natural soni berilgan.
2 sonining dastlabki n ta natural darajalaridan tashkil
topgan massivni hosil qiling va elementlarini chiqaring.
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
        ikkining_darajalari = []
        for i in range(1, n + 1):
            ikkining_darajalari.append(2**i)

        # i = 1
        # while i <= n:
        #     ikkining_darajalari.append(2**i)
        #     i += 1

        natija = f"\n2 ning dastlabki {n} ta natural darajalaridan tashkil topgan sonlar ro`yxati:\n{ikkining_darajalari}"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
