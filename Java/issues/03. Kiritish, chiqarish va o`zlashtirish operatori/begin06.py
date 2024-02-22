"""
Masala: Parallelepipedning tomonlari a, b, c berilgan.
Uning hajmi va to`la sirti aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 16.02.2024;
"""

a = input("\nParallelepipedning enini kiriting: ")
b = input("Parallelepipedning bo`yini kiriting: ")
c = input("Parallelepipedning balandligini kiriting: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a > 0 and b > 0 and c > 0:
        v = a * b * c
        s = 2 * (a * b + b * c + a * c)
        natija = f"\nTomonlari {a}, {b}, {c} ga teng bo`lgan parallelepipedning hajmi {v} ga va to`la sirti {s} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
