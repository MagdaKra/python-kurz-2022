polozky = {
    '1': {'nazev': 'Daring Greatly', 'zanr': 'krimi'},
    '2': {'nazev': 'Dog Nasty S1E1', 'zanr': 'komedie'},
}

cislo_polozky = '1'
polozka = polozky[cislo_polozky]

class Polozka:
    def __init__(self, nazev, zanr):
      self.nazev = nazev
      self.zanr = zanr
    def __str__(self):
        return f"Název filmu je {self.nazev} a žánr: {self.zanr}."

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def __str__(self):
        return (super().__str__() + " " f"Délka filmu je {self.delka} minut.")

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody=55):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody
    def __str__(self):
        return (super().__str__() + " " f"Seriál má {self.pocet_epizod} epizod a délka epizody je {self.delka_epizody} minut.")

film = Film("Daring Greatly", "krimi", 105)
film.__str__()
print(film)

serial = Serial("Dog Nasty S1E1", "komedie", 15, 55)
serial.__str__()
print(serial)
