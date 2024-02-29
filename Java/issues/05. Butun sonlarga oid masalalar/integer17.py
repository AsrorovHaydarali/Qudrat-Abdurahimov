"""
Masala: 999 dan katta bo`lgan natural son berilgan.
Bir marta bo`lib butun qismini va bo`lib qoldiq qismini olish operatorlaridan
foydalanib berilgan sonning yuzlar xonasidagi raqamni aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 27.02.2024;
"""

son = input("\n999 dan katta natural son kiriting: ")

try:
    son = int(son)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if son > 999:
        # yuzlar_xonasidagi_raqam = str(son)[-3]
        yuzlar_xonasidagi_raqam = son // 100 % 10
        natija = (
            f"\n{son} sonining yuzlar xonasida {yuzlar_xonasidagi_raqam} raqami mavjud."
        )
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
