"""
Masala: a1, b1, c1 va a2, b2, c2 koeffitsiyentlar berilgan.
a1 * x + b1 * y = c1
a2 * x + b2 * y = c2
tenglamalar sistemasining yechimlarini aniqlaydigan dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 20.02.2024;
"""

a1 = input("\na1 koeffitsiyentni kiriting: ")
b1 = input("b1 koeffitsiyentni kiriting: ")
c1 = input("c1 koeffitsiyentni kiriting: ")

a2 = input("\na2 koeffitsiyentni kiriting: ")
b2 = input("b2 koeffitsiyentni kiriting: ")
c2 = input("c2 koeffitsiyentni kiriting: ")

try:
    a1 = float(a1)
    b1 = float(b1)
    c1 = float(c1)

    a2 = float(a2)
    b2 = float(b2)
    c2 = float(c2)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    natija = f"\n{a1} * x + {b1} * y = {c1}\
            \n{a2} * x + {b2} * y = {c2}"

    if a1 * b2 == a2 * b1 and b1 * c2 != b2 * c1:
        natija = "\n\nUshbu tenglamalar sistemasi yechimga ega emas."
    elif a1 * b2 == a2 * b1 and b1 * c2 == b2 * c1:
        natija = "\n\nUshbu tenglamalar sistemasi cheksiz ko`p yechimga ega."
    else:
        d = a1 * b2 - a2 * b1
        x = (b2 * c1 - b1 * c2) / d
        y = (a1 * c2 - a2 * c1) / d

        natija = f"\n\nUshbu tenglamalar sistemasi yagona yechimga ega.\
            \n({x}, {y})"

print(natija)
