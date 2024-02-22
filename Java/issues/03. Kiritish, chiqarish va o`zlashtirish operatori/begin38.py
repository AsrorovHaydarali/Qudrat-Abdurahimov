"""
Masala: a va b koeffitsiyentlar berilgan.
a * x + b = 0 tenglamaning yechimini topuvchi dastur tuzilsin (a != 0);
Bajaradi: Haydarali Asrorov;
Sana: 18.02.2024;
"""

a = input("\nNoldan farqli a koeffitsiyentni kiriting: ")
b = input("b koeffitsiyentni kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a != 0:
        x = -b / a
        natija = f"\n{a} * x + {b} = 0 tenglamaning ildizi:\
            \nx = {x}"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
