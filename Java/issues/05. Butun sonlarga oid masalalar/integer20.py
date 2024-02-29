"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha to`liq soat o`tganini aniqlovchi dastur tuzilsin;
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
        natija = f"\n{soniya} soniyada to`liq {toliq_soat} soat mavjud."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
