baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

number = input("Zadej kód balíku: ")
handed = number[True]
for item in baliky:
  if item ["number"] == True:
    handed == item ["True"]
    print(f"Balík číslo {handed} byl předán kurýrovi.")
  else:
    print("Balík zatím nebyl předán kurýrovi")
