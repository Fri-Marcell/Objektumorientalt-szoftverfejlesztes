from legi_tarsasag import LegiTarsasag
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from jegy_foglalas import JegyFoglalas, jegy_foglalas, foglalasok_torles, foglalasok_listazasa

#  Légitársaság és járatok

legitarsasag = LegiTarsasag("Magyar Légitársaság")

b1 = BelfoldiJarat("HU123", "Debrecen", 15000, "Hajdú-Bihar")
b2 = BelfoldiJarat("HU456", "Szeged", 17000, "Csongrád-Csanád")
n1 = NemzetkoziJarat("INT789", "Bécs", 45000, "Ausztria")

legitarsasag.jaratok = [b1, b2, n1]

# Alapértelmezett 6 foglalás

f1 = JegyFoglalas("Horváth Ádám", b1, "2026-04-11", "5B")
f2 = JegyFoglalas("Hadházi Gergő", n1, "2026.02.18", "12F")
f3 = JegyFoglalas("Nagy Alexandra", b2, "2026-11-07", "9C")
f4 = JegyFoglalas("Tóth Éva", b1, "2026-03-29", "13A")
f5 = JegyFoglalas("Kiss Alex", n1, "2026.09.09", "7D")
f6 = JegyFoglalas("Lovag Eszter", b2, "2026-01-26", "19E")

legitarsasag.foglalasok = [f1, f2, f3, f4, f5, f6]

# Menü

def menu():
    while True:
        print("\n===== Repülőjegy Foglalási Rendszer =====")
        print("1. Jegy foglalása")
        print("2. Foglalás törlése")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        val = input("Választás (1–4): ")

        if val == "1":
            jegy_foglalas(legitarsasag)
        elif val == "2":
            foglalasok_torles(legitarsasag)
        elif val == "3":
            foglalasok_listazasa(legitarsasag)
        elif val == "4":
            print("Kilépés...")
            break
        else:
            print(" Érvénytelen választás.")

menu()