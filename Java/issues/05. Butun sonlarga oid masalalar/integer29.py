"""
Masala: a, b, c musbat sonlar berilgan. Tomonlari a va b bo`lgan to`g`ri to`rtburchakka
tomoni c ga teng bo`lgan kvadrat eng ko`p joylashtirilsin. To`g`ri to`rtburchakka eng ko`p
joylashgan kvadratlar soni va joylashmay qolgan qismi yuzasini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 29.02.2024
"""

a = input("\nTo`g`ri to`rtburchakning enini kiriting: ")
b = input("To`g`ri to`rtburchakning bo`yini kiriting: ")

c = input("\nKvadratning tomonini kiriting: ")

try:
    a = float(a)
    b = float(b)

    c = float(c)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if a > 0 and b > 0 and c > 0:
        # To`g`ri to`rtburchakning yuzasi:
        s = a * b

        # Unga eng ko`p joylashtirish mumkin bo`lgan kvadratlar soni:
        n = int(a / c) * int(b / c)

        # Ortib qolgan yuza:
        s_qoldiq = s - n * c**2

        natija = f"\nTomonlari {a} va {b} ga teng bo`lgan to`g`ri to`rtburchakka tomoni {c} ga teng bo`lgan kvadratdan eng ko`pi bilan {n} ta joylashtirish mumkin."
        natija += f"\nBunda ortib qolgan joy yuzasi {s_qoldiq} ga teng bo`ladi."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
