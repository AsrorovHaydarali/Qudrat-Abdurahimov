"""
Masala: n ta elementdan tashkil topgan massiv berilgan.
Massiv elementlarini quyidagicha tartibda chiqaruvchi dastur tuzilsin:
a[0], a[n-1], a[1], a[n-2], a[2], a[n-3] ...
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
        special_list = []

        nusxa_elementlar = elementlar[:]
        while nusxa_elementlar:
            special_list.append(nusxa_elementlar.pop(0))
            nusxa_elementlar.reverse()

        natija += f"\n\nUshbu ro`yxatni maxsus ko`rinishga keltiramiz:\n{special_list}"

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
