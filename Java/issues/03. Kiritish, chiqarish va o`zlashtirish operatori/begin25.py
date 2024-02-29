"""
Masala: x ning qiymati berilganda y = 3x^6 - 6x^2 - 7 funksiyaning qiymati aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

x = input("\nx ning qiymatini kiriting: ")

try:
    x = float(x)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    y = 3 * x**6 - 6 * x**2 - 7
    natija = f"\ny = 3x^6 - 6x^2 - 7 funksiya uchun y({x}) = {y} bo`ladi."

print(natija)
