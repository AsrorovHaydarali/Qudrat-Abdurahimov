"""
Masala: Og`irlik m kilogramda berilgan. Undagi to`liq tonnalar sonini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 21.02.2024;
"""

m = input("\nOg`irlikni kg da kiriting: ")

try:
    m = float(m)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if m >= 0:
        natija = f"\n{m} kg da to`liq {int(m / 1000)} t mavjud."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
