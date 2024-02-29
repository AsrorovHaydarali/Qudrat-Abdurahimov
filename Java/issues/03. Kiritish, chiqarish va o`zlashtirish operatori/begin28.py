"""
Masala: a soni berilgan. a^2, a^3, a^5, a^10, a^15 ni aniqlovchi dastur tuzilsin;
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
        \n{a}^3 = {a**3}\
        \n{a}^5 = {a**5}\
        \n{a}^10 = {a**10}\
        \n{a}^15 = {a**15}"

print(natija)
