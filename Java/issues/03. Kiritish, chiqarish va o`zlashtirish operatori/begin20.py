"""
Masala: Tekislikdagi berilgan 2 nuqta orasidagi masofa topilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

x_1 = input("\nx_1 koordinatani kiriting: ")
y_1 = input("y_1 koordinatani kiriting: ")

x_2 = input("\nx_2 koordinatani kiriting: ")
y_2 = input("y_2 koordinatani kiriting: ")


try:
    x_1 = float(x_1)
    y_1 = float(y_1)

    x_2 = float(x_2)
    y_2 = float(y_2)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    d = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
    natija = f"\nTekislikdagi berilgan A({x_1} ; {y_1}) va B({x_2} ; {y_2}) nuqtalar orasidagi masofa {d} ga teng."

print(natija)
