"""
Masala: x ning qiymati berilganda y = 4(x - 3)^6 - 7(x - 3)^3 + 2 funksiyaning qiymati aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

x = input("\nx ning qiymatini kiriting: ")

try:
    x = float(x)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    y = 4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2
    natija = f"\ny = 4(x - 3)^6 - 7(x - 3)^3 + 2 funksiya uchun y({x}) = {y} bo`ladi."

print(natija)
