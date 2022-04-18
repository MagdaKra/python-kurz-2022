nazev_souboru = "auta.txt"

with open(nazev_souboru, encoding='utf-8') as vstup:
    auta = vstup.readlines()

print(auta)

radky = [line.strip() for line in auta]
print(radky)

seznam_jizd= [line.split() for line in radky]
print(seznam_jizd)

kilometry = [items[1] for items in seznam_jizd]
print(kilometry)

citelne_kilometry = [kilometr.replace(",", ".") for kilometr in kilometry]
print(citelne_kilometry)

ujete_kilometry = [float(kilometr) for kilometr in citelne_kilometry]

soucet_ujetych_kilometrů = sum(ujete_kilometry)
print(soucet_ujetych_kilometrů)