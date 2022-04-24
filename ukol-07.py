import re

nadepsat_zasilku = "posta.html"

with open(nadepsat_zasilku, encoding='utf-8') as vstup:
    nadepsat_zasilku = vstup.read()

# print(nadepsat_zasilku)

nadepsat_zasilku.replace("\n'", " ")

print(re.sub('\s+', ' ', 'nadepsat_zasilku'))

reg_vyraz_psc = re.compile("\d{3}\s+\d{2}")
psc = reg_vyraz_psc.findall(nadepsat_zasilku)

reg_vyraz_mesto = re.compile("[A-Z]|+\s+\d+")
mesto = reg_vyraz_mesto.findall(nadepsat_zasilku)

print(psc)
print(mesto)

