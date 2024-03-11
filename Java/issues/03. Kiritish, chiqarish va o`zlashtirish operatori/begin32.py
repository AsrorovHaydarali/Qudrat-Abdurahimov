"""
Masala: Temperatura Celsius da berilgan.
Temperatura qiymatini Fahrenheit ga o`tkazuvchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

temp_c = input("\nTemperatura qiymatini Celsius da kiriting: ")

try:
    temp_c = float(temp_c)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    temp_f = temp_c * 9 / 5 + 32
    natija = f"\n{temp_c} C = {temp_f} F"

print(natija)
