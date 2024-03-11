"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha to`liq daqiqa o`tganini aniqlovchi dastur tuzilsin;
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
        natija = f"\n{soniya} soniyada to`liq {toliq_daqiqa} daqiqa mavjud."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
