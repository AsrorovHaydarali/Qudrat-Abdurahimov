"""
Masala: Faylning hajmi baytlarda berilgan.
Bo`lib, butunni olish operatoridan foydalanib fayl hajmini
to`liq kilobaytlarda ifodalovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 21.02.2024;
"""

i = input("\nMa'lumot hajmini B (bayt) da kiriting: ")

try:
    i = float(i)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if i >= 0:
        natija = f"\n{i} B (bayt) da to`liq {int(i / 1024)} kB (kilobayt) mavjud."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
