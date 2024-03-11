"""
Masala: 3 xonali natural son berilgan.
Uning raqamlari yig`indisini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 27.02.2024;
"""

son = input("\n3 xonali natural son kiriting: ")

try:
    son = int(son)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if son >= 100 and son <= 999:
        natija = f"\n{son} sonining raqamlari yig`indisi {son // 100 + son // 10 % 10 + son % 10} ga teng."
        # natija = f"\n{son} sonining raqamlari yig`indisi {sum([int(raqam) for raqam in str(son)])} ga teng."
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
