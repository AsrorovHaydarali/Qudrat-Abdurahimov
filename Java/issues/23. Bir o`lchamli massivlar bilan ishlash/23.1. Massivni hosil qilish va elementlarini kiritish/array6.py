"""
Masala: n natural soni va a,b butun sonlari berilgan.
f_1 = a; f_2 = b. Boshqa elementlari o`zidan oldingi
barcha elementlari yig`indisiga teng bo`lgan, n ta elementdan
tashkil topgan massivni hosil qiling va elementlarini chiqaring.
Bajardi: Haydarali Asrorov
Sana: 05.03.2024
"""

a = input("\n1-hadni butun son ko`rinishida kiriting: ")
b = input("2-hadni butun son ko`rinishida kiriting: ")
n = input("Hadlar sonini natural son ko`rinishida kiriting: ")

try:
    a = int(a)
    b = int(b)
    n = int(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if n > 0:
        special_squence = []

        if n == 1:
            special_squence.append(a)
        else:
            special_squence.append(a)
            special_squence.append(b)

            while True:
                if len(special_squence) == n:
                    break

                f_i = sum(special_squence)
                special_squence.append(f_i)

        natija = f"\nBirinchi hadi {a}, ikkinchi hadi {b} bo`lgan, qolgan hadlari o`zidan oldingi\
        \nbarcha hadlar yig`indisiga teng bo`lgan ketma-ketlikning {n} ta hadi ro`yxati:\n{special_squence}"

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
