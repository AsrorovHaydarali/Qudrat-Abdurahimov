"""
Masala: n ta sondan tashkil topgan massiv berilgan.
Massivning oxirgi elementidan kichik bo`lgan birinchi kelgan elementni aniqlovchi dastur tuzilsin.
Agar bunday element mavjud bo`lmasa, bunday element mavjud emas ko`rinishida xabar chiqarilsin.
Bajardi: Haydarali Asrorov
Sana: 05.03.2024
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

        oxirgi_son = sonlar[-1]
        natija = f"\n{n} ta sondan tashkil topgan ro`yxat:\n{sonlar}"
        natija += f"\n\nRo`yxatdagi oxirgi son: {oxirgi_son}."
        birinchi_kichik = None

        for son in sonlar:
            if son < oxirgi_son:
                birinchi_kichik = son
                break

        if birinchi_kichik:
            natija += (
                f"\nUshbu sondan kichik bo`lgan birinchi kelgan son: {birinchi_kichik}."
            )
        else:
            natija += "\nUshbu sondan kichik bo`lgan son ro`yxatda mavjud emas ekan."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
