"""
Masala: Sonlar o`qida A, B, C nuqtalar berilgan.
C nuqta A va B nuqtalar orasida joylashgan.
AC va BC kesmalar uzunligining ko`paytmasi aniqlansin;
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
    if (a <= c and c <= b) or (b <= c and c <= a):
        ac = abs(a - c)
        bc = abs(b - c)

        natija = f"\nAC * BC = {ac} * {bc} = {ac * bc}"
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi.\
            \nC({c}) nuqta A({a}) va B({b}) nuqtalarning orasida joylashmagan."

print(natija)
