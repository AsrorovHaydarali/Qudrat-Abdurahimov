"""
Masala: Kubning tomoni a berilgan
Uning hajmi va to`la sirti aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 16.02.2024;
"""

a = input("\nKubning tomonini kiriting: ")

try:
    a = float(a)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a > 0:
        v = a**3
        s = 6 * a**2
        natija = f"\nTomoni {a} ga teng bo`lgan kubning hajmi {v} ga va to`la sirti {s} ga teng."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
