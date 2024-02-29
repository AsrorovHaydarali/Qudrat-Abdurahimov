`"""
Masala: 2 xonali son berilgan. Uning raqamlari yig`indisini aniqlovchi dastur tuzilsin;
Bajardi: Haydarali Asrorov;
Sana: 21.02.2024;
"""

son = input("\n2 xonali natural son kiriting: ")

try:
    son = int(son)
except:
    natija = f"\nNoto`g`ri qiymat kiritildi."
else:
    if son >= 10 and son <= 99:
        natija = (
            f"\n{son} sonining raqamlari yig`indisi {son // 10 + son % 10} ga teng."
        )
    else:
        natija = f"\nNoto`g`ri qiymat kiritildi."

print(natija)
