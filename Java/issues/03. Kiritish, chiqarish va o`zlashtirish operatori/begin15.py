"""
Masala: Doiraning yuzasi s berilgan.
Uning radiusi va diametri aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

from math import pi

s = input("\nDoiraning yuzasini kiriting: ")

try:
    s = float(s)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if s > 0:
        r = (s / pi) ** 0.5
        d = 2 * r

        natija = f"\nYuzasi {s} ga teng bo`lgan doiraning radiusi {r} ga va diametri {d} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
