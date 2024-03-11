"""
Masala: n ta sondan tashkil topgan massiv berilgan.
Massivning oxirgi elementidan kichik va dastlabki elementidan
katta bo`lgan oxirgi kelgan elementni va uning indeksini aniqlovchi dastur tuzilsin.
Agar bunday element mavjud bo`lmasa, bunday element mavjud emas ko`rinishida xabar chiqarilsin.
Bajardi: Haydarali Asrorov
Sana: 06.03.2024
"""

n = input("\nRo`yxat nechta sondan tashkil topgan?\n>>> ")

try:
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0:
        print()  # Shunchaki, chiroyliroq chiqishi uchun.
        sonlar = []

        for i in range(1, n + 1):
            while True:
                son_i = input(f"{i}-sonni kiriting: ")

                try:
                    son_i = float(son_i)
                except:
                    print("\nNoto`g`ri qiymat kiritildi. Qaytadan kiriting.")
                else:
                    sonlar.append(son_i)
                    break

        birinchi_son = sonlar[0]
        oxirgi_son = sonlar[-1]

        natija = f"\n{n} ta sondan tashkil topgan ro`yxat:\n{sonlar}"
        natija += (
            f"\n\nRo`yxatdagi birinchi son: {birinchi_son}; oxirgi son: {oxirgi_son}."
        )

        oxirgi_orta = None

        for son in sonlar:
            if birinchi_son < son < oxirgi_son:
                oxirgi_orta = son

        if oxirgi_orta:
            nusxa_sonlar = sonlar
            nusxa_sonlar.reverse()
            oxirgi_index = len(sonlar) - 1 - nusxa_sonlar.index(oxirgi_orta)

            natija += f"\nRo`yxatdagi birinchi sondan katta va oxirgi sondan kichik bo`lgan, oxirgi "
            natija += f"o`rinda kelgan son {oxirgi_orta}; uning uning indeksi esa: {oxirgi_index}."
        else:
            natija += "\nRo`yxatdagi birinchi sondan katta va oxirgi sondan kichik bo`lgan son mavjud emas ekan."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
