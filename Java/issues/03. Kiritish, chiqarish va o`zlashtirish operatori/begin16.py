"""
Masala: Sonlar o`qida 2 nuqta orasidagi masofa aniqlansin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

a = input("\n1-nuqtaning koordinatasini kiriting: ")
b = input("2-nuqtaning koordinatasini kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    l = abs(a - b)
    natija = f"\nSonlar o`qida A({a}) va B({b}) nuqtalari orasida {l} masofa bor."

print(natija)
