"""
Masala: Ikkita manfiy bo`lmagan a va b sonlari berilgan.
Ularning o`rta geometrik qiymati aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

a = input("\n1-manfiy bo`lmagan haqiqiy sonni kiriting: ")
b = input("2-manfiy bo`lmagan haqiqiy sonni kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a >= 0 and b >= 0:
        orta_geometrik = (a * b) ** 0.5
        natija = f"\n{a} va {b} sonlarining o`rta geometrik qiymati {orta_geometrik} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
