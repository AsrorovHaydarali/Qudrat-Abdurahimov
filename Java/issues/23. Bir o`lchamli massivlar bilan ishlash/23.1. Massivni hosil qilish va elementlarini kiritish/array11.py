"""
Masala: n ta elementdan tashkil topgan massiv va k butun soni berilgan.
Massiv elementlari orasidan indeksi k ga karralilarini chiqaruvchi dastur tuzilsin.
Shart operatori ishlatilmasin.
Bajardi: Haydarali Asrorov
Sana: 05.03.2024
"""

n = input("\nRo`yxat nechta elementdan tashkil topgan?\n>>> ")
k = input(
    "Ro`yxatdan indekslari qaysi natural songa karrali elementlarni chiqarmoqchisiz?\n>>> "
)

try:
    n = int(n)
    k = int(k)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0 and k > 0:
        print()  # Shunchaki, chiroyliroq chiqishi uchun.
        elementlar = [input(f"{i}-indeksli elementni kiriting: ") for i in range(n)]
        natija = f"\n{n} ta elementdan tashkil topgan ro`yxat:\n{elementlar}"

        # Shart operatori ishlatilganda:
        # elementlar_k = [elementlar[j] for j in range(len(elementlar)) if j % k == 0]

        elementlar_k = [elementlar[j] for j in range(0, len(elementlar), k)]
        natija += f"\n\nRo`yxatdan indekslari {k} ga karrali bo`lgan elementlar:\n{elementlar_k}"

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
