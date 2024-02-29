"""
Masala: 3 xonali natural son berilgan.
Uning chapdan birinchi raqamini o`chirib, o`ng tarafga
yozishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 27.02.2024;
"""

son = input("\n3 xonali natural son kiriting: ")

try:
    son = int(son)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if son >= 100 and son <= 999:
        yangi_son = int(f"{str(son)[1:]}{str(son)[0]}")
        # yangi_son = (son - (son // 100) * 100) * 10 + son // 100
        natija = f"\n{son} sonining chapdan birinchi raqamini o`chirib, o`ng tarafga yozsak, {yangi_son} soni hosil bo`ladi."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
