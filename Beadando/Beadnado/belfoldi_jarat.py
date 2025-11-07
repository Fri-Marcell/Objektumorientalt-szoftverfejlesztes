from jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, megye):
        super().__init__(jaratszam, celallomas, jegyar)
        self._megye = megye
        self._kedvezmeny = 0.20

    def get_vegso_ar(self):
        return int(self.jegyar * (1 - self._kedvezmeny))

    def __str__(self):
        return f"[Belföldi] {super().__str__()} – Megye: {self._megye}"