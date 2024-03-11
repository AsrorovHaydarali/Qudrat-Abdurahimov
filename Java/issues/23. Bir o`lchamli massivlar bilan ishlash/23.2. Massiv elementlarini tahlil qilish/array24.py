"""
Masala: n ta sondan tashkil topgan massiv berilgan.
Massiv elementlari arifmetik progressiyani tashkil qilsa, arifmetik progressiyaning ayirmasini chiqaring.
Agar bu sonlar arifmetik progressiyaning ketma-ket hadlari bo`lmaydigan bo`lsa, ogohlantirish xabarini chiqaring.
Bajardi: Haydarali Asrorov
Sana: 08.03.2024
"""

n = input("\nRo`yxat nechta sondan tashkil topgan?\n>>> ")

try:
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0:
        print()
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

        natija = f"\nUshbu {n} ta sondan tashkil topgan sonlar ro`yxati:\n{sonlar}"

        if n == 1:
            natija += "\n\nBerilgan son arifmetik progressiyaning birinchi hadi bo`lishi mumkin.\nLekin bunda arifmetik progressiyaning ayirmasi qanday ekanligini bilish ilojsiz."
        elif n == 2:
            natija += f"\n\nBerilgan sonlar arifmetik progressiyaning ketma-ket hadlari bo`ladi.\nBunda arifmetik progressiyaning ayirmasi {sonlar[1] - sonlar[0]} ga teng bo`ladi."
        else:
            d = sonlar[1] - sonlar[0]
            arifmetik_progressiyami = True

            for j in range(n - 1):
                if sonlar[j + 1] - sonlar[j] != d:
                    arifmetik_progressiyami = False
                    break

            if arifmetik_progressiyami:
                natija += f"\n\nBerilgan sonlar arifmetik progressiyaning ketma-ket hadlari bo`ladi.\nBunda arifmetik progressiyaning ayirmasi {d} ga teng bo`ladi."
            else:
                natija += f"\n\nBerilgan sonlar arifmetik progressiyaning ketma-ket hadlari bo`la olmaydi."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
