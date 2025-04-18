from __future__ import annotations
from dataclasses import dataclass
from math import gcd

@dataclass(frozen=True)
class Bruch():

    zaehler: int
    nenner: int

    def __init__(self, zaehler: int, nenner: int) -> None:
        if nenner == 0:
            raise ValueError("nenner == 0")
        faktor = 1 if nenner > 0 else -1
        object.__setattr__(self, "zaehler", zaehler * faktor)
        object.__setattr__(self, "nenner", nenner * faktor)

    def kuerze(self) -> Bruch:
        teiler = gcd(self.zaehler, self.nenner)
        return Bruch(self.zaehler // teiler, self.nenner // teiler)

    def inverses(self) -> Bruch:
        return Bruch(-self.zaehler,self.nenner)
    
    def kehrwert(self) -> Bruch:
        return Bruch(self.nenner,self.zaehler)
    
    def addiere(self, b: Bruch) -> Bruch:
        return Bruch(self.zaehler * b.nenner + self.nenner * b.zaehler, self.nenner * b.nenner).kuerze()
    
    def subtrahiere(self, b: Bruch) -> Bruch:
        return self.addiere(b.inverses())
    
    def multipliziere(self, b: Bruch) -> Bruch:
        return Bruch(self.zaehler * b.zaehler, self.nenner * b.nenner).kuerze()
    
    def dividiere(self, b: Bruch) -> Bruch:
        return self.multipliziere(b.kehrwert())
