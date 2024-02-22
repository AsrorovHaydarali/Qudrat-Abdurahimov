"""
Masala: Kvadratning tomoni a berilgan. Uning perimetri aniqlansin;
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
        p = 4 * a
        natija = f"\nTomoni {a} ga teng bo`lgan kvadratning perimetri {p} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
