"""
Masala: Kvadratning tomoni a berilgan. Uning yuzasi aniqlansin;
Bajardi: Haydarali Asrorov;
Sana: 16.02.2024;
"""

a = input("\nKvadratning tomonini kiriting: ")

try:
    a = float(a)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a > 0:
        s = a**2
        natija = f"\nTomoni {a} ga teng bo`lgan kvadratning yuzasi {s} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
