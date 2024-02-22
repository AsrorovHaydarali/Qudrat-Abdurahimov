"""
Masala: Doiraning uzunligi l berilgan.
Uning radiusi va yuzasi aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

from math import pi

l = input("\nDoiraning uzunligini kiriting: ")

try:
    l = float(l)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if l > 0:
        r = l / (2 * pi)
        s = pi * r**2

        natija = f"\nUzunligi {l} ga teng bo`lgan doiraning radiusi {r} ga va yuzasi {s} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
