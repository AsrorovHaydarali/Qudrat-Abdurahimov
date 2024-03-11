"""
Masala: n natural soni berilgan. Dastlabki n ta Fibonachchi sonlaridan
tashkil topgan massivni hosil qiling va elementlarini chiqaring.
Bajardi: Haydarali Asrorov
Sana: 05.03.2024
"""

n = input("\nNatural son kiriting: ")

try:
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0:
        fibonacci_squence = []
        f_i_2 = 1
        f_i_1 = 1

        if n == 1:
            fibonacci_squence.append(f_i_2)
        else:
            fibonacci_squence.append(f_i_2)
            fibonacci_squence.append(f_i_1)

            while True:
                if len(fibonacci_squence) == n:
                    break

                f_i = f_i_1 + f_i_2
                fibonacci_squence.append(f_i)

                f_i_2 = f_i_1
                f_i_1 = f_i

        natija = f"\nDastlabki {n} ta Fibonachchi sonlaridan tashkil topgan ro`yxat:\n{fibonacci_squence}"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."


print(natija)
