"""
Masala: a burchak radianda berilgan. 
erilgan burchakning qiymatini gradusga o`tkazuvchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

from math import pi

a_radian = input("\na burchakning radian o`lchovini kiriting: ")

try:
    a_radian = float(a_radian)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    a_gradus = a_radian * 180 / pi
    natija = f"\n{a_radian} radian = {a_gradus} gradus"

print(natija)
