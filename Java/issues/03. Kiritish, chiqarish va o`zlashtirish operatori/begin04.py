"""
Masala: Aylananing diametri d berilgan.
Uning uzunligi aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 16.02.2024;
"""

from math import pi

d = input("\nAylananing diametrini kiriting: ")

try:
    d = float(d)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if d > 0:
        l = pi * d
        natija = f"\nDiametri {d} ga teng bo`lgan aylananing uzunligi {l} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
