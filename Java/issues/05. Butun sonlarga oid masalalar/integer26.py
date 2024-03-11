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
Agar 1-yanvar seshanba bo`lsa, kiritilgan k - kun haftaning qaysi
kuniga to`g`ri kelishini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 29.02.2024;
"""

k = input("\nYilning nechanchi kuni ekanligini kiriting: ")

try:
    k = int(k)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if k >= 1 and k <= 366:
        hafta_kunlari = [
            "dushanba",
            "seshanba",
            "chorshanba",
            "payshanba",
            "juma",
            "shanba",
            "yakshanba",
        ]

        natija = f"\n1-kuni seshanba bo`lgan yilning {k}-kuni {hafta_kunlari[k % 7]}ga to`g`ri keladi."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
