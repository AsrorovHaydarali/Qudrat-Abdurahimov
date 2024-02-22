"""
Masala: 1-avtomobilning tezligi v1, 2-avtomobilning tezligi v2.
Ular orasidagi dastlabki masofa s0. Avtomobillar bir-biridan uzoqlasha boshlasa,
t vaqtdan keyin ular orasidagi s1 masofani aniqlab beruvchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 18.02.2024;
"""

v1 = input("\n1-avtomobilning tezligini kiriting (km/soat): ")
v2 = input("2-avtomobilning tezligini kiriting (km/soat): ")

s0 = input("\nUlar orasidagi dastlabki masofani kiriting (km): ")
t = input("Ularning bir-biridan uzoqlashish vaqtni kiriting (soat): ")

try:
    v1 = float(v1)
    v2 = float(v2)

    s0 = float(s0)
    t = float(t)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if v1 >= 0 and v2 >= 0 and s0 >= 0 and t >= 0:
        s1 = s0 + (v1 + v2) * t

        natija = f"\n{s0} km masofadan bir-biridan {v1} km/soat va {v2} km/soat tezlikda uzoqlashayotgan avtomobillarning orasidagi masofa {t} soatdan keyin {s1} km ga teng bo`ladi."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
