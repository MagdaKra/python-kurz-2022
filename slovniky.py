
# typ int
cislo = 15
print(f"typ int: {cislo}, {type(cislo)}")

# typ float
sleva = 0.20
print(f"typ float: {sleva}")

# typ str / string
jmeno = "Alzbeta"
print(f"typ str: {jmeno}")

# typ bool
venku_snezi = False
print(f"typ bool: {venku_snezi}")
# typ list (seznam)
ubehnuto = [2,5,4,8,9]

zaznam = ["Romeo a Julie", 189, False]

jazykovy_slovnik = {
    "ahoj": ["hello", "hi"],
    "jablko": ["apple"],
    "auto": ["car", "vehicle"]
}

cz_slovo = input("Jake slovo chcete prelozit? ")

if cz_slovo in jazykovy_slovnik:
    print(f"Preklad slova {cz_slovo} je {jazykovy_slovnik[cz_slovo]}.")
else:
    print(f"Bohuzel, slovo {cz_slovo} neni v nasem slovniku.")

jazykovy_slovnik = {
    "ahoj": "hello",
    "jablko": "apple",
    "auto": "car"
}

en_slovo = "apple"
if en_slovo in jazykovy_slovnik.values():
    print(f"Slovo {en_slovo} mame v nasem slovniku.")

# pridani noveho zaznamu
jazykovy_slovnik["hruska"] = "pear"

# zmena hodnoty existujiciho zaznamu
jazykovy_slovnik["ahoj"] = "hi"

print(jazykovy_slovnik)
