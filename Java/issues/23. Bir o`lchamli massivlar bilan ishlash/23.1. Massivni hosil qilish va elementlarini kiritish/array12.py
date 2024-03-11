"""
Masala: n ta elementdan tashkil topgan massiv berilgan.
Massivning juft indeksli elementlarini chiqaruvchi dastur tuzilsin.
Shart operatori ishlatilmasin.
Bajardi: Haydarali Asrorov
Sana: 05.03.2024
"""

n = input("\nRo`yxat nechta elementdan tashkil topgan?\n>>> ")

try:
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0:
        print()  # Shunchaki, chiroyliroq chiqishi uchun.
        elementlar = [input(f"{i}-indeksli elementni kiriting: ") for i in range(n)]
        natija = f"\n{n} ta elementdan tashkil topgan ro`yxat:\n{elementlar}"

        juft_indeksli_elementlar = [elementlar[j] for j in range(0, len(elementlar), 2)]
        natija += (
            f"\n\nRo`yxatdagi juft indeksli elementlar:\n{juft_indeksli_elementlar}"
        )

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
