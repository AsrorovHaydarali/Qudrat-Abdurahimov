"""
Masala: Uzunlik l santimetrda berilgan. Undagi to`liq metrlar sonini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 21.02.2024;
"""

l = input("\nUzunlikni sm da kiriting: ")

try:
    l = float(l)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if l >= 0:
        natija = f"\n{l} sm da to`liq {int(l / 100)} m mavjud."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
