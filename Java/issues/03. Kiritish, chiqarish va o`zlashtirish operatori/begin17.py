"""
Masala: Sonlar o`qida A, B, C nuqtalar berilgan.
AC va BC kesmalar uzunligi va ularning yig`indisi aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

a = input("\nA nuqtaning koordinatasini kiriting: ")
b = input("B nuqtaning koordinatasini kiriting: ")
c = input("C nuqtaning koordinatasini kiriting: ")


try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    ac = abs(a - c)
    bc = abs(b - c)
    s = ac + bc

    natija = f"\nAC kesmaning uzunligi {ac} ga va BC kesmaning uzunligi {bc} ga teng.\
        \nUshbu kesmalar uzunligining yig`indisi esa {s} ga teng."

print(natija)
