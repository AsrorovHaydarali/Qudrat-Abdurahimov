"""
Masala: Berilgan a va b sonlarining qiymatlarini almashtiring.
a va b ning yangi qiymati ekranga chiqarilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

from time import sleep

a = input("\na sonini kiriting: ")
b = input("b sonini kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    print(f"\na = {a}\nb = {b}\n\nEndi, ushbu qiymatlar almashadi:")
    sleep(3)

    c = a
    a = b
    b = c

    natija = f"\na = {a}\nb = {b}"

print(natija)
