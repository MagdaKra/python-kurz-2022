from datetime import datetime, timedelta, date

vysoka_cena_start = datetime(2021, 7, 1)
vysoka_cena_konec = datetime(2021, 8, 10)
delka_vysoka_cena = vysoka_cena_konec - vysoka_cena_start
print(delka_vysoka_cena)

nizka_cena_start = datetime(2021, 8, 11)
nizka_cena_konec = datetime(2021, 8, 31)
delka_nizka_cena = nizka_cena_konec - nizka_cena_start
print(delka_nizka_cena)

if delka_nizka_cena: cena1_vstupenek=180
if delka_vysoka_cena: cena2_vstupenek=250

datum_vstupenek = input("Zadejte požadované datum: ")
print(datum_vstupenek)
pocet_osob = input("Zadejte počet vstupenek: ")
datum = datetime.strptime(datum_vstupenek, '%d.%m.%Y')
print(datum)

cena1_vstupenek = delka_nizka_cena * pocet_osob
cena2_vstupenek = delka_vysoka_cena * pocet_osob

if datum_vstupenek < vysoka_cena_start:
    print("Letní kino je v té době uzavřené")
if datum_vstupenek > nizka_cena_konec:
    print("Letní kino je v té době uzavřené")
else:
    print("Cena za vstupenky je {cena1_vstupenek}.")
    print("Cena za vstupenky je {cena2_vstupenek}.")
