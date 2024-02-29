"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha soat va soniya o`tganini aniqlovchi dastur tuzilsin;
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
        toliq_soat = int(soniya / 3600)
        qoldiq_soniya = soniya - toliq_soat * 3600

        natija = f"\n{soniya} soniya = {toliq_soat} soat {qoldiq_soniya} soniya"
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
