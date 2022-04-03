auta = {
    '1': {'registracni_znacka': '4A2 3020', 'typ_vozidla': 'Peugeot 403 Cabrio', 'pocet_najetych_kilometru': '47534'},
    '2': {'registracni_znacka': '1P3 4747', 'typ_vozidla': 'Skoda Octavia', 'pocet_najetych_kilometru': '41253'},
}

class Auto:
  def __init__(self, registracni_znacka, typ_vozidla, pocet_najetych_kilometru, dostupnost = True):
    self.registracni_znacka = registracni_znacka
    self.typ_vozidla = typ_vozidla
    self.pocet_najetych_kilometru = pocet_najetych_kilometru
    self.dostupnost = dostupnost

  def vypis_auto(self):
    return f"Auto {self.typ_vozidla} s registrační značkou {self.registracni_znacka} má najeto {self.pocet_najetych_kilometru} km"
    
  def pujc_auto (self):
    if self.dostupnost is True:
      self.dostupnost = "volne"
      return f"Potvrzuji zapůjčení vozidla"
    else:
      return f"Vozidlo není k dispozici"

  def __str__(self):
    return f"Auto {self.typ_vozidla} s registrační značkou {self.registracni_znacka}"

skoda = Auto("1P3 4747", "Skoda Octavia", "41253")
skoda.registracni_znacka = "1P3 4747"
skoda.typ_vozidla = "Skoda Octavia"
skoda.pocet_najetych_kilometru = "41253"
skoda.dostupnost = True
print(skoda.vypis_auto())

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
peugeot.registracni_znacka = "4A2 3020"
peugeot.typ_vozidla = "Peugeot 403 Cabrio"
peugeot.pocet_najetych_kilometru = "47534"
peugeot.dostupnost = True
print(peugeot.vypis_auto())

auto = input("Chcete si vypůjčit auto značky Peugeot nebo Skoda - zadejte značku: ")

auto = Auto("registracni_znacka", "typ_vozidla", "pocet_najetych kilometru")
auto.__str__()
print(auto.pujc_auto())
