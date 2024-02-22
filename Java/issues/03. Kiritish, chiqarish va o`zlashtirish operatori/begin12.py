"""
Masala: To`g`ri burchakli uchburchakning katetlari a va b berilgan.
Uning gipotenuzasi va perimetri aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

a = input("\nTo`g`ri burchakli uchburchakning 1-katetini kiriting: ")
b = input("To`g`ri burchakli uchburchakning 2-katetini kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a > 0 and b > 0:
        c = (a**2 + b**2) ** 0.5
        p = a + b + c
        natija = f"\nKatetlari {a} va {b} ga teng bo`lgan to`g`ri burchakli uchburchakning gipotenuzasi {c} ga va perimetri {p} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
