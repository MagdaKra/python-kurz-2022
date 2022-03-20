# Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů.

sales = {
  "Zkus mě chytit": 4165, 
  "Vrah zavolá v deset": 5681, 
  "Zločinný steh": 2565,
  "Noc, která mě zabila" : 0
}

# Zkopíruj si slovník do svého programu. Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů. U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100.

sales = {
  "Zkus mě chytit": 4165, 
  "Vrah zavolá v deset": 5681, 
  "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100


# kontrola:
print(sales)

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

number = int(input("Zadejte číslo lístku: "))
if number in tombola:
  # Zde je jedna věc, co jsem neřekl v kurzu. Funkce pop odstraní hodnotu ze slovníku
  # a tuto odstraňovanou hodnotu vrací, můžeme ji tedy uložit do proměnné a nemusíme načítat
  # výhru pomocí hranatých závorek.
  win = tombola.pop(number)
  print(f"Vyhráváš: {win}.")
else:
  print("Bohužel nevyhráváš nic.")

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
name = input("Zadej jméno: ")
if name in passwords:
  password = input("Zadej heslo: ")
  if password == passwords[name]:
    print("Smíš vstoupit.")
  else:
    password = input("Nesprávné heslo. Zadej heslo znovu: ")
    if password == passwords[name]:
      print("Smíš vstoupit.")
    else:
      print("Neznáš heslo, vstup zakázán.")
else:
  print("Nejsi na seznamu hostů.")

