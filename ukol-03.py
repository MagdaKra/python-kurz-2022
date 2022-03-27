# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.



def verify_format(number):
  if len(number_of_recipient) == 9:
    return True
  elif len(number_of_recipient) == 13:
    return True
  else:
    return False
    print ("Zadané číslo je neplatné")
  
number_of_recipient = input("Zadejte číslo pro zaslání zprávy: ")
text_of_message = input ("Napište zprávu: ")

verify_format(number_of_recipient)
print (f"Vaše zpráva bude odslána na toto číslo: {number_of_recipient}")
print (text_of_message)

price_per_message = 3
def total_price_of_message(price: int):
  if len(text_of_message) <= 180:
    return text_of_message * price_per_message

total_price_of_message (text_of_message)
print (f"Celková cena tvé zprávy je {total_price_of_message}")

