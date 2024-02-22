"""
Masala: x kg shokolad a so`m turadi va y kg konfet b so`m turadi.
1 kg shokolad 1 kg konfetdan qancha qimmat turishini aniqlovchi dastur tuzilsin;
Bajaradi: Haydarali Asrorov;
Sana: 18.02.2024;
"""

x = input("\nShokoladning massasini kg da kiriting: ")
y = input("Konfetning massasini kg da kiriting: ")

try:
    x = float(x)
    y = float(y)
except:
    natija = "\nNoto`g`ri qiymat kiritildi."
else:
    if x > 0 and y > 0:
        a = input(f"\n{x} kg shokolad necha so`m bo`ldi?\n>>> ")
        b = input(f"{y} kg konfet necha so`m bo`ldi?\n>>> ")

        try:
            a = float(a)
            b = float(b)
        except:
            natija = "\nNoto`g`ri qiymat kiritildi."
        else:
            if a > 0 and b > 0:
                natija = f"\nShokoladning 1 kg i {a / x} so`m turadi.\
                    \nKonfetning 1 kg i {b / y} so`m turadi.\
                    \n\n1 kg shokolad va 1 kg konfet narxlarining farqi {abs(a / x - b / y)} so`m ekan."
            else:
                natija = "\nNoto`g`ri qiymat kiritildi."

    else:
        natija = "\nNoto`g`ri qiymat kiritildi."

print(natija)
