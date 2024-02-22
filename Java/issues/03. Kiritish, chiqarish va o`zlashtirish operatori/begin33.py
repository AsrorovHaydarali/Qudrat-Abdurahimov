"""
Masala: x kg konfet a so`m turadi.
1 kg va y kg konfet qancha turishini aniqlovchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 18.02.2024;
"""

x = input("\nKonfetning massasini kg da kiriting: ")

try:
    x = float(x)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if x > 0:
        a = input(f"{x} kg konfet necha so`m bo`ldi?\n>>> ")

        try:
            a = float(a)
        except:
            natija = "\nNoto`g`ri qiymat kiritildi."
        else:
            if a > 0:
                print(f"\n1 kg konfet {a / x} so`m turadi.")
                y = input("Ushbu konfetdan necha kg xarid qilmoqchisiz?\n>>> ")

                try:
                    y = float(y)
                except:
                    natija = "\nNoto`g`ri qiymat kiritildi."
                else:
                    if y > 0:
                        natija = f"\n{y} kg konfet {y * a / x} so`m bo`ladi."
                    else:
                        natija = "\nNoto`g`ri qiymat kiritildi."

            else:
                natija = "\nNoto`g`ri qiymat kiritildi."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
