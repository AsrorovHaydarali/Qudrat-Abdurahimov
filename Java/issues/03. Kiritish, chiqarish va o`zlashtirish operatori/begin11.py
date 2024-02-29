"""
Masala: 0 ga teng bo`lmagan 2 ta haqiqiy son berilgan.
Ularning yig`indisi, ko`paytmasi va har birining moduli aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

a = input("\n1-noldan farqli haqiqiy sonni kiriting: ")
b = input("2-noldan farqli haqiqiy sonni kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a != 0 and b != 0:
        natija = f"\n{a} + {b} = {a + b}\
            \n{a} * {b} = {a * b}\
            \n|{a}| = {abs(a)}\
            \n|{b}| = {abs(b)}"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
