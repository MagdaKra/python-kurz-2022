baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

code = input("Zadej kód balíku: ")
if "code" in baliky:
  true = baliky['B541X','B501X']
  print(f"Balík byl předán kurýrovi: {true}.")
else:
  print("Balík zatím nebyl předán kurýrovi")