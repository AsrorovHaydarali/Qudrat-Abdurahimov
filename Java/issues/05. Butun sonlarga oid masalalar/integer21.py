"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha daqiqa va soniya o`tganini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 27.02.2024;
"""

soniya = input("\nVaqtni soniya hisobida kiriting: ")

try:
    soniya = float(soniya)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if soniya >= 0:
        toliq_daqiqa = int(soniya / 60)
        qoldiq_soniya = soniya - toliq_daqiqa * 60

        natija = f"\n{soniya} soniya = {toliq_daqiqa} daqiqa {qoldiq_soniya} soniya"
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
