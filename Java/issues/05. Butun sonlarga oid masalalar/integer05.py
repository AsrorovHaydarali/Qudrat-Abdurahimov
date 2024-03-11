"""
Masala: a va b musbat sonlar berilgan.
a uzunlikdagi kesmada b uzunlikdagi kesmani necha marta
joylashtirish mumkinligini va oxirgi kesmaning joylashmay
qoladigan qismini ham aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 21.02.2024;
"""

a = input("\na kesmaning uzunligini kiriting: ")
b = input("b kesmaning uzunligini kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if a > 0 and b > 0:
        natija = f"\nUzunligi {a} bo`lgan kesma ichida uzunlikdagi {b} bo`lgan kesmadan {int(a / b)} tasini joylashtirish mumkin.\
            \nEng oxirida {int(a / b) + 1}-kesmaning yoshlashishi uchun esa {a % b} birlik uzunlik yetmay qolar ekan."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
