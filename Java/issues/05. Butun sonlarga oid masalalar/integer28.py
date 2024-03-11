"""
Masala: Hafta kunlari quyidagicha tartibda berilgan:
1 - dushanba
2 - seshanba
3 - chorshanba
4 - payshanba
5 - juma
6 - shanba
7 - yakshanba
[1 ; 366] oralig`ida yotuvchi k soni berilgan.
Agar 1-yanvar haftaning n - kuniga to`g`ri kelsa (n => [1 ; 7]),
kiritilgan k - kun haftaning qaysi kuniga to`g`ri kelishini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 29.02.2024;
"""

print(
    "\nYilning 1-kuni haftaning nechanchi kuniga to`g`ri kelyapti?\
    \n(Haftaning 1-kuni dushanba deb hisoblansin.)"
)

n = input(">>> ")
k = input("\nYilning biror kunini kiriting: ")

try:
    n = int(n)
    k = int(k)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if 1 <= n <= 7 and 1 <= k <= 366:
        hafta_kunlari = [
            "dushanba",
            "seshanba",
            "chorshanba",
            "payshanba",
            "juma",
            "shanba",
            "yakshanba",
        ]
        index = ((k - 1) % 7 + n - 1) % 7

        natija = f"\n1-kuni {hafta_kunlari[n - 1]} bo`lgan yilning {k}-kuni {hafta_kunlari[index]}ga to`g`ri keladi."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)


"""
n = 1

k | index
1 - 0
2 - 1
3 - 2
4 - 3
5 - 4
6 - 5
7 - 6
8 - 0
9 - 1
10 - 2

index = ((k - 1) % 7 + n - 1) % 7
index = ((k - 1) % 7 + 0) % 7
"""

"""
n = 2

k | index
1 - 1
2 - 2
3 - 3
4 - 4
5 - 5
6 - 6
7 - 0
8 - 1
9 - 2
10 - 3

index = ((k - 1) % 7 + n - 1) % 7
index = ((k - 1) % 7 + 1) % 7
"""

"""
n = 3

k | index
1 - 2
2 - 3
3 - 4
4 - 5
5 - 6
6 - 0
7 - 1
8 - 2
9 - 3
10 - 4

index = ((k - 1) % 7 + n - 1) % 7
index = ((k - 1) % 7 + 2) % 7
"""

"""
n = 7

k | index
1 - 6
2 - 0
3 - 1
4 - 2
5 - 3
6 - 4
7 - 5
8 - 6
9 - 0
10 - 1

index = ((k - 1) % 7 + n - 1) % 7
index = ((k - 1) % 7 + 6) % 7
"""
