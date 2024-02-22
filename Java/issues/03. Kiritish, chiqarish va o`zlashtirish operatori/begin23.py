"""
Masala: a, b va c sonlari berilgan.
a ning qiymati b ga, b ning qiymati c ga, c ning qiymati a ga almashtirilsin.
a, b va c ning yangi qiymatlari ekranga chiqarilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

from time import sleep

a = input("\na sonini kiriting: ")
b = input("b sonini kiriting: ")
c = input("c sonini kiriting: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    print(
        f"\na = {a}\nb = {b}\nc = {c}\n\nEndi, ushbu qiymatlar mos ravishda almashadi:"
    )
    sleep(3)

    d = a
    a = b
    b = c
    c = d

    natija = f"\na = {a}\nb = {b}\nc = {c}"

print(natija)
