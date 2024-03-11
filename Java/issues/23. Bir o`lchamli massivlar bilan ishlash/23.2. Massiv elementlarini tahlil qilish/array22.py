"""
Masala: n ta sondan tashkil topgan massiv hamda index1 va index2 butun sonlar berilgan.
Massivning index1 va index2 indexlar orasidagi sonlardan tashqari qolgan sonlar yig`indisini chiqaruvchi dastur tuzilsin.
Bajardi: Haydarali Asrorov
Sana: 07.03.2024
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

        while True:
            index1 = input(
                f"\n1-indeksni [{-n} ; {n-1}] oralig`idagi butun son ko`rinishida kiriting: "
            )

            index2 = input(
                f"2-indeksni [{-n} ; {n-1}] oralig`idagi butun son ko`rinishida kiriting: "
            )

            try:
                index1 = int(index1)
                index2 = int(index2)
            except:
                print("\nNoto`g`ri qiymat kiritildi. Qiymatni qaytadan kiriting.")
            else:
                if -n <= index1 <= n - 1 and -n <= index2 <= n - 1:
                    break
                else:
                    print("\nNoto`g`ri qiymat kiritildi. Qiymatni qaytadan kiriting.")

        natija += f"\n\n{index1} va {index2} oralig`idagi sonlar tashqari qolgan sonlar ro`yxati esa:"

        if index1 < 0:
            index1 += n
        if index2 < 0:
            index2 += n

        indexes = [index1, index2]
        min_index = min(indexes)
        max_index = max(indexes)

        qolgan_sonlar = sonlar[:min_index] + sonlar[max_index + 1 :]
        yigindi = sum(qolgan_sonlar)

        natija += f"\n{qolgan_sonlar}\n\nBu sonlarning yig`indisi {yigindi} ga teng."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
