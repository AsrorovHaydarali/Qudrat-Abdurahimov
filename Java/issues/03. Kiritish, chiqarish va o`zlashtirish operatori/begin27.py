"""
Masala: a soni berilgan. a^2, a^4, a^8 ni aniqlovchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

a = input("\na haqiqiy sonini kiriting: ")

try:
    a = float(a)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    natija = f"\n{a}^2 = {a**2}\
        \n{a}^4 = {a**4}\
        \n{a}^8 = {a**8}"

print(natija)
