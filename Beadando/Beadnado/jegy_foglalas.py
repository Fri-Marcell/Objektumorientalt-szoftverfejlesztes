from datetime import datetime, timedelta
import uuid

class JegyFoglalas:
    def __init__(self, utas_nev, jarat, datum, ulohely):
        self._foglalas_azonosito = self._generate_id()
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.datum = datum
        self.ulohely = ulohely
        self.statusz = "Foglalt"
        self.foglalas_ideje = datetime.now()

    @property
    def foglalas_azonosito(self):
        return self._foglalas_azonosito

    def _generate_id(self):
        return f"FOG-{uuid.uuid4()}"

    def torles(self):
        self.statusz = "Törölve"

    def __str__(self):
        return f"{self.foglalas_azonosito} – {self.utas_nev} – {self.jarat.jaratszam}"

    def get_foglalas_info(self):
        return {
            "azonosito": self.foglalas_azonosito,
            "utas": self.utas_nev,
            "jarat": self.jarat.jaratszam,
            "celallomas": self.jarat.celallomas,
            "datum": self.datum,
            "ulohely": self.ulohely,
            "statusz": self.statusz
        }


# Foglalások kezelése

def foglalas_ellenorzes(foglalas, legitarsasag):
    try:
        if "-" in foglalas.datum:
            datum = datetime.strptime(foglalas.datum, "%Y-%m-%d").date()
        else:
            datum = datetime.strptime(foglalas.datum, "%Y.%m.%d").date()
    except ValueError:
        print(" Hibás dátumformátum!")
        return False

    if foglalas.jarat not in legitarsasag.jaratok:
        return False

    if datum <= datetime.now().date():
        return False

    return True


def jegy_foglalas(legitarsasag):
    utas_nev = input("Név: ")

    print("\nElérhető járatok:")
    for j in legitarsasag.jaratok:
        print(f"{j.jaratszam} – {j.celallomas} – {j.get_vegso_ar()} Ft")

    jaratszam = input("Járatszám: ")
    jarat = next((j for j in legitarsasag.jaratok if j.jaratszam == jaratszam), None)

    if not jarat:
        print(" Érvénytelen járatszám.")
        return

    datum = input("Dátum (YYYY-MM-DD vagy YYYY.MM.DD): ")
    ulohely = input("Ülőhely: ")

    foglalas = JegyFoglalas(utas_nev, jarat, datum, ulohely)

    if foglalas_ellenorzes(foglalas, legitarsasag):
        legitarsasag.foglalasok.append(foglalas)
        print(f"\n Sikeres foglalás! Azonosító: {foglalas.foglalas_azonosito}")
        print(f" Foglalás végösszege: {jarat.get_vegso_ar()} Ft")
    else:
        print(" A foglalás nem érvényes.")


def foglalasok_listazasa(legitarsasag):
    if not legitarsasag.foglalasok:
        print("Nincs foglalás.")
        return

    print("\nAktuális foglalások:")
    for f in legitarsasag.foglalasok:
        print(f.get_foglalas_info())


def foglalasok_torles(legitarsasag):
    foglalasok_listazasa(legitarsasag)
    keresett = input("\nAdja meg a törlendő foglalás azonosítóját: ")

    for f in legitarsasag.foglalasok:
        if f.foglalas_azonosito == keresett:
            legitarsasag.foglalasok.remove(f)
            print(" Foglalás törölve.")
            return

    print(" Nem található ilyen azonosító.")