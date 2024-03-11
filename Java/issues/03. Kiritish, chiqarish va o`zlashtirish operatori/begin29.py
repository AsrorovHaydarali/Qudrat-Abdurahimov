"""
Masala: a burchak gradusda berilgan.
Berilgan burchakning qiymatini radianga o`tkazuvchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

from math import pi

a_gradus = input("\na burchakning gradus o`lchovini kiriting: ")

try:
    a_gradus = float(a_gradus)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    a_radian = a_gradus * pi / 180
    natija = f"\n{a_gradus} gradus = {a_radian} radian"

print(natija)
