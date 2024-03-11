"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha soat, daqida, soniya o`tganini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 29.02.2024;
"""

soniya = input("\nVaqtni soniya hisobida kiriting: ")

try:
    soniya = float(soniya)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if soniya >= 0:
        qism_soat = int(soniya / 3600)
        qism_daqiqa = int((soniya - qism_soat * 3600) / 60)
        qism_soniya = (soniya - qism_soat * 3600) - qism_daqiqa * 60

        natija = f"\n{soniya} soniya = {qism_soat} soat {qism_daqiqa} daqiqa {qism_soniya} soniya"
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
