"""
Masala: n ta sondan tashkil topgan massiv berilgan.
Massiv elementlari geometrik progressiyani tashkil qilsa, geometrik progressiyaning maxrajini chiqaring.
Agar bu sonlar geometrik progressiyaning ketma-ket hadlari bo`lmaydigan bo`lsa, ogohlantirish xabarini chiqaring.
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
            natija += "\n\nBerilgan son geometrik progressiyaning birinchi hadi bo`lishi mumkin.\nLekin bunda geometrik progressiyaning maxraji qanday ekanligini bilish ilojsiz."
        elif n == 2:
            if sonlar.count(0) == 2:
                natija += f"\n\nBerilgan sonlar geometrik progressiyaning ketma-ket hadlari bo`ladi.\nBunda geometrik progressiyaning maxraji 0 dan farqli ixtiyoriy haqiqiy songa teng desa bo`ladi."
            else:

            # try:
            #     q = sonlar[1] / sonlar[0]
            # except:
            #     if sonlar[1] == 0:
            #         natija += f"\n\nBerilgan sonlar geometrik progressiyaning ketma-ket hadlari bo`ladi.\nBunda geometrik progressiyaning maxraji 0 dan farqli ixtiyoriy haqiqiy songa teng desa bo`ladi."
            #     else:
            #         natija += f"\n\nBerilgan sonlar geometrik progressiyaning ketma-ket hadlari bo`la olmaydi."
            # else:
            #     if q != 0:
            #         natija += f"\n\nBerilgan sonlar geometrik progressiyaning ketma-ket hadlari bo`ladi.\nBunda geometrik progressiyaning maxraji {q} ga teng bo`ladi."
            #     else:
            #         natija += f"\n\nBerilgan sonlar geometrik progressiyaning ketma-ket hadlari bo`la olmaydi."
        else:

            try:
                q = sonlar[1] / sonlar[0]
            except:
                natija += f"\n\nBerilgan sonlar geometrik progressiyaning ketma-ket hadlari bo`la olmaydi."
            else:
                geometrik_progressiyami = True

                for j in range(n - 1):
                    if sonlar[j + 1] / sonlar[j] != q:
                        geometrik_progressiyami = False
                        break

            # d = sonlar[1] - sonlar[0]
            # arifmetik_progressiyami = True

            # for j in range(n - 1):
            #     if sonlar[j + 1] - sonlar[j] != d:
            #         arifmetik_progressiyami = False
            #         break

            # if arifmetik_progressiyami:
            #     natija += f"\n\nBerilgan sonlar arifmetik progressiyaning ketma-ket hadlari bo`ladi.\nBunda arifmetik progressiyaning ayirmasi {d} ga teng bo`ladi."
            # else:
            #     natija += f"\n\nBerilgan sonlar arifmetik progressiyaning ketma-ket hadlari bo`la olmaydi."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)

"""
Geometrik Progressiyaning maxraji:
0 ga teng bo`lishi mumkin emas ekan.
1 ga va -1 ga teng bo`lishi esa mumkin ekan.

0, 0, 0, 0 ... => Geometrik Progressiya ekan.
4, 0, 0, 0 ... => Geometrik Progressiya emas ekan. 
5, 5, 5, 5 ... => Geometrik Progressiya ekan.

0, 0, 0, 0 ... => Geometrik Progressiyaning maxraji nechaga tengligini bilmadim.
(Nol dan farqli ixtiyoriy son bo`lsa kerak.)
"""
