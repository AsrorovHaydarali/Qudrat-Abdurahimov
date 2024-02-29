"""
Masala: Tekislikda uchburchakning 3 ta uchi koordinatalari berilgan.
Ushbu uchburchakning perimetri va yuzasi topilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

# A(x_1 ; y_1)
x_1 = input("\nx_1 koordinatani kiriting: ")
y_1 = input("y_1 koordinatani kiriting: ")

# B(x_2 ; y_2)
x_2 = input("\nx_2 koordinatani kiriting: ")
y_2 = input("y_2 koordinatani kiriting: ")

# C(x_3 ; y_3)
x_3 = input("\nx_3 koordinatani kiriting: ")
y_3 = input("y_3 koordinatani kiriting: ")

try:
    x_1 = float(x_1)
    y_1 = float(y_1)

    x_2 = float(x_2)
    y_2 = float(y_2)

    x_3 = float(x_3)
    y_3 = float(y_3)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    # Hech qaysi nuqtalar ustma-ust tushmasligi kerak.
    if (
        ((x_1 == x_2) and (y_1 == y_2))
        or ((x_2 == x_3) and (y_2 == y_3))
        or ((x_1 == x_3) and (y_1 == y_3))
    ):
        natija = f"\nBerilgan A({x_1} ; {y_1}), B({x_2} ; {y_2}), C({x_3} ; {y_3}) nuqtalardan uchburchak yasab bo`lmaydi.\
            \nNuqtalar ustma-ust tushib qolgan, bu mumkin emas."
    else:
        # Nuqtalar bir to`g`ri chiziq ustida ham yotmasligi kerak.
        if (x_1 == x_2 and x_2 == x_3) or (y_1 == y_2 and y_2 == y_3):
            natija = f"\nBerilgan A({x_1} ; {y_1}), B({x_2} ; {y_2}), C({x_3} ; {y_3}) nuqtalardan uchburchak yasab bo`lmaydi.\
            \nNuqtalar bir to`g`ri chiziq ustida yotibdi, bu mumkin emas."
        else:
            # y = kx + l
            try:
                k = (y_1 - y_2) / (x_1 - x_2)
            except:
                pass

            try:
                k = (y_2 - y_3) / (x_2 - x_3)
            except:
                pass

            try:
                k = (y_1 - y_3) / (x_1 - x_3)
            except:
                pass

            l = y_1 - k * x_1
            # y = kx + l
            # C(x_3 ; y_3) nuqta ushbu to`g`ri chiziqga tegishli bo`lmasligi kerak.

            if y_3 == k * x_3 + l:
                natija = f"\nBerilgan A({x_1} ; {y_1}), B({x_2} ; {y_2}), C({x_3} ; {y_3}) nuqtalardan uchburchak yasab bo`lmaydi.\
                \nNuqtalar bir to`g`ri chiziq ustida yotibdi, bu mumkin emas."
            else:
                ab = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
                bc = ((x_2 - x_3) ** 2 + (y_2 - y_3) ** 2) ** 0.5
                ac = ((x_1 - x_3) ** 2 + (y_1 - y_3) ** 2) ** 0.5

                p = ab + bc + ac
                p_yarim = p / 2
                s = (p_yarim * (p_yarim - ab) * (p_yarim - bc) * (p_yarim - ac)) ** 0.5

                natija = f"\nUchlari A({x_1} ; {y_1}), B({x_2} ; {y_2}), C({x_3} ; {y_3}) nuqtalarda bo`lgan\
                    \nuchburchakning perimetri {p} ga va yuzasi {s} ga teng."

print(natija)
