"""
Masala: n natural soni hamda arifmetik progressiyaning dastlabki hadi a_1
va ayirmasi d berilgan. Ushbu arifmetik progressiyaning dastlabki n ta 
hadidan tashkil topgan massivni hosil qiling va elementlarini chiqaring.
Bajardi: Haydarali Asrorov
Sana: 02.03.2024
"""

a_1 = input("\nArifmetik progressiyaning dastlabki hadini kiriting: ")
d = input("Arifmetik progressiyaning hadlari ayirmasini kiriting: ")
n = input("Arifmetik progressiyaning hadlari sonini kiriting: ")

try:
    a_1 = float(a_1)
    d = float(d)
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0:
        # ap -> arifmetik progressiya
        ap_hadlari = [a_1 + (i - 1) * d for i in range(1, n + 1)]

        # ap_hadlari = []

        # for i in range(1, n + 1):
        #     a_i = a_1 + (i - 1) * d
        #     ap_hadlari.append(a_i)

        # i = 1
        # while i <= n:
        #     a_i = a_1 + (i - 1) * d
        #     ap_hadlari.append(a_i)
        #     i += 1

        natija = f"\n1-hadi {a_1}, hadlari ayirmasi {d} ga teng bo`lgan arifmetik progressiyaning daslabki {n} ta hadlari ro`yxati:\n{ap_hadlari}"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
