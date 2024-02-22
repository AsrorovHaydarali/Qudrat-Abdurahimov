"""
Masala: To`g`ri to`rtburchakning tomonlari a va b berilgan.
Uning perimetri va yuzasi aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 16.02.2024;
"""

a = input("\nTo`g`ri to`rtburchakning enini kiriting: ")
b = input("To`g`ri to`rtburchakning bo`yini kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a > 0 and b > 0:
        p = 2 * (a + b)
        s = a * b
        natija = f"\nTomonlari {a} va {b} ga teng bo`lgan to`g`ri to`rtburchakning perimetri {p} ga va yuzasi {s} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
