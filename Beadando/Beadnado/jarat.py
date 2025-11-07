from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._jegyar = jegyar

    @property
    def jaratszam(self):
        return self._jaratszam

    @property
    def celallomas(self):
        return self._celallomas

    @property
    def jegyar(self):
        return self._jegyar

    @abstractmethod
    def get_vegso_ar(self):
        pass

    def __str__(self):
        return f"{self._jaratszam} → {self._celallomas} ({self._jegyar} Ft)"