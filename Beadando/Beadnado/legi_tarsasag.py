class LegiTarsasag:
    def __init__(self, nev):
        self._nev = nev
        self.jaratok = []
        self.foglalasok = []

    @property
    def nev(self):
        return self._nev

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def __str__(self):
        return f"Légi társaság: {self._nev} – {len(self.jaratok)} járat"