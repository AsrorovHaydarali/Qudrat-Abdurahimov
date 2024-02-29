"""
Masala: Temperatura Fahrenheit da berilgan.
Temperatura qiymatini Celsius ga o`tkazuvchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 17.02.2024;
"""

temp_f = input("\nTemperatura qiymatini Fahrenheit da kiriting: ")

try:
    temp_f = float(temp_f)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    temp_c = (temp_f - 32) * 5 / 9
    natija = f"\n{temp_f} F = {temp_c} C"

print(natija)
