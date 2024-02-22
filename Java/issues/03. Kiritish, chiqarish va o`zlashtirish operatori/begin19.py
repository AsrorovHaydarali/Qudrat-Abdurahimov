"""
Masala: To`g`ri to`rtburchakning qarama-qarshi uchlari koordinatalari berilgan.
Uning tomonlari koordinata o`qlariga parallel.
To`g`ri to`rtburchakning perimetri va yuzasi aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

x_a = input("\nx_a koordinatani kiriting: ")
y_a = input("y_a koordinatani kiriting: ")

x_c = input("\nx_c koordinatani kiriting: ")
y_c = input("y_c koordinatani kiriting: ")


try:
    x_a = float(x_a)
    y_a = float(y_a)

    x_c = float(x_c)
    y_c = float(y_c)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if x_a != x_c and y_a != y_c:
        a = abs(x_a - x_c)
        b = abs(y_a - y_c)

        p = 2 * (a + b)
        s = a * b

        natija = f"\nQarama-qarshi uchlari A({x_a} ; {y_a}) va C({x_c} ; {y_c}) nuqtalarda bo`lgan\
          \nto`g`ri to`rtburchakning perimetri {p} ga va yuzasi {s} ga teng."
    else:
        natija = f"\nA({x_a} ; {y_a}) va C({x_c} ; {y_c}) nuqtalar to`g`ri to`rtburchakning qarama-qarshi uchlari bo`la olmaydi."

print(natija)
