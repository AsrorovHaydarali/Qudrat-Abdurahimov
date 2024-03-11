"""
Masala: Ikkita haqiqiy a va b sonlari berilgan.
Ularning o`rta arifmetik qiymati aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 16.02.2024;
"""

a = input("\n1-haqiqiy sonni kiriting: ")
b = input("2-haqiqiy sonni kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    orta_arifmetik = (a + b) / 2
    natija = (
        f"\n{a} va {b} sonlarining o`rta arifmetik qiymati {orta_arifmetik} ga teng."
    )

print(natija)
