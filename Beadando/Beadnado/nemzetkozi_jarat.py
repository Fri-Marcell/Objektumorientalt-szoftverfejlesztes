from jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, orszag):
        super().__init__(jaratszam, celallomas, jegyar)
        self._orszag = orszag
        self._biztositas = 5000

    def get_vegso_ar(self):
        return self.jegyar + self._biztositas

    def __str__(self):
        return f"[Nemzetközi] {super().__str__()} – Ország: {self._orszag}"