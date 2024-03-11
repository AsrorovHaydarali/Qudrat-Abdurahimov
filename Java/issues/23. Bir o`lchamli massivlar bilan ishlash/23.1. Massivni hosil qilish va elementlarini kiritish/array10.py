"""
Masala: n ta butun sonlardan tashkil topgan massiv berilgan.
Ushbu sonlar ichidan juft sonlar nechtaligini aniqlovchi
va ularni o`sish tartibida chiqaruvchi undan so`ng esa
ushbu sonlar ichidan toq sonlar nechtaligini aniqlovchi
va ularni kamayish tartibida chiqaruvchi dastur tuzilsin.
Bajardi: Haydarali Asrorov
Sana: 05.03.2024
"""

n = input("\nRo`yxat nechta butun sondan tashkil topgan?\n>>> ")

try:
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0:
        sonlar = []

        for i in range(1, n + 1):
            while True:
                son_i = input(f"{i}-butun sonni kiriting: ")

                try:
                    son_i = int(son_i)
                except:
                    print("\nButun son kiritilmadi. Qiymatni qayta kiriting.")
                else:
                    sonlar.append(son_i)
                    break

        natija = f"\n{n} ta butun sonlardan tashkil topgan sonlar ro`yxati:\n{sonlar}"
        juft_sonlar = [son for son in sonlar if son % 2 == 0]
        toq_sonlar = [son for son in sonlar if son % 2 == 1]

        if juft_sonlar:
            juft_sonlar.sort()
            natija += f"\n\nRo`yxatda {len(juft_sonlar)} ta juft son mavjud.\nUlarning to`g`ri saralangan ro`yxati:\n{juft_sonlar}"
        else:
            natija += f"\n\nRo`yxatda {len(juft_sonlar)} ta juft son mavjud."

        if toq_sonlar:
            toq_sonlar.sort(reverse=True)
            natija += f"\n\nRo`yxatda {len(toq_sonlar)} ta toq son mavjud.\nUlarning teskari saralangan ro`yxati:\n{toq_sonlar}"
        else:
            natija += f"\n\nRo`yxatda {len(toq_sonlar)} ta toq son mavjud."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
