"""
Masala: 3 xonali natural son berilgan.
Uning o`ngdan birinchi raqamini o`chirib, chap tarafga
yozishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 27.02.2024;

input: 156
output: 615
"""

son = input("\n3 xonali natural son kiriting: ")

try:
    son = int(son)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if son >= 100 and son <= 999:
        yangi_son = son // 10 + (son % 10) * 100
        # yangi_son = int(f"{str(son)[-1]}{str(son)[:-1]}")
        natija = f"\n{son} sonining o`ngdan birinchi raqamini o`chirib, chap tarafga yozsak, {yangi_son} soni hosil bo`ladi."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
