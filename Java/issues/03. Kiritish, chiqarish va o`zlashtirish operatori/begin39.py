"""
Masala: a, b, c koeffitsiyentlar berilgan.
ax^2 + bx + c = 0 tenglamaning ildizlarini topuvchi dastur tuzing;
Bajaradi: Haydarali Asrorov;
Sana: 18.02.2024;
"""

a = input("\nNoldan farqli a koeffitsiyentni kiriting: ")
b = input("b koeffitsiyentni kiriting: ")
c = input("c koeffitsiyentni kiriting: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a != 0:
        d = b**2 - 4 * a * c

        if d > 0:
            x1 = (-b + d**0.5) / (2 * a)
            x2 = (-b - d**0.5) / (2 * a)

            natija = f"\n{a} * x^2 + {b} * x + {c} = 0 kvadrat tenglama 2 ta haqiqiy ildizga ega:\
                \nx1 = {x1}\nx2 = {x2}"
        elif d == 0:
            x = -b / (2 * a)
            natija = f"\n{a} * x^2 + {b} * x + {c} = 0 kvadrat tenglama 1 ta haqiqiy ildizga ega:\
                \nx = {x}"
        else:
            natija = f"\n{a} * x^2 + {b} * x + {c} = 0 kvadrat tenglama haqiqiy ildizga ega emas."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
