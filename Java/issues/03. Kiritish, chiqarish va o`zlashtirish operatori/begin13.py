"""
Masala: Umumiy markazga ega bo`lgan 2 ta doira berilgan.
Ularning yuzalari va ularning ayirmasi aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

from math import pi

r1 = input("\n1-doiraning radiusini kiriting: ")
r2 = input("2-doiraning radiusini kiriting: ")

try:
    r1 = float(r1)
    r2 = float(r2)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if r1 > 0 and r2 > 0:
        s1 = pi * r1**2
        s2 = pi * r2**2
        s3 = abs(s1 - s2)

        natija = f"\nRadiusi {r1} ga teng bo`lgan doiraning yuzasi {s1} ga teng.\
            \nRadiusi {r2} ga teng bo`lgan doiraning yuzasi {s2} ga teng.\
            \nUlarning yuzalari farqi {s3} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
