"""
Masala: n natural soni hamda geometrik progressiyaning dastlabki hadi b_1
va maxraji q berilgan. Ushbu geometrik progressiyaning dastlabki n ta 
hadidan tashkil topgan massivni hosil qiling va elementlarini chiqaring.
Bajardi: Haydarali Asrorov
Sana: 04.03.2024
"""

b_1 = input("\nGeometrik progressiyaning dastlabki hadini kiriting: ")
q = input("Geometrik progressiyaning maxrajini kiriting: ")
n = input("Geometrik progressiyaning hadlari sonini kiriting: ")

try:
    b_1 = float(b_1)
    q = float(q)
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0 and q != 0:
        # gp -> geometrik progressiya
        gp_hadlari = [b_1 * q ** (i - 1) for i in range(1, n + 1)]

        natija = f"\n1-hadi {b_1}, maxraji {q} ga teng bo`lgan geometrik progressiyaning daslabki {n} ta hadlari ro`yxati:\n{gp_hadlari}"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
