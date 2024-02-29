"""
Masala: Doiraning radiusi r berilgan.
Uning uzunligi va yuzasi aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 16.02.2024;
"""

from math import pi

r = input("\nDoiraning radiusini kiriting: ")

try:
    r = float(r)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if r > 0:
        l = 2 * pi * r
        s = pi * r**2
        natija = f"\nRadiusi {r} ga teng bo`lgan doiraning uzunligi {l} ga va yuzasi {s} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
