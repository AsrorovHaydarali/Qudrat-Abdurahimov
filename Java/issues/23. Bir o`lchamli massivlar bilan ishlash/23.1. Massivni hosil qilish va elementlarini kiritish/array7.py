"""
Masala: n ta elementdan tashkil topgan massiv berilgan.
Uning elementlarini teskari tartibda chiqaruvchi dastur tuzilsin.
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
        special_list = [input(f"{i}-elementni kiriting: ") for i in range(1, n + 1)]
        natija = f"\nKiritilgan elementlardan hosil bo`lgan ro`yxat:\n{special_list}"

        special_list.reverse()
        natija += (
            f"\n\nUshbu ro`yxatning teskari tartibdagi ko`rinishi esa:\n{special_list}"
        )
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
