#!/usr/bin/python3
# -*- coding : utf-8 -*-

# Un dictionnaire d'association nom de mois / jour
months = {
    "janvier": 31,
    "fevrier": 28,
    "mars": 31,
    "avril": 30,
    "mai": 31,
    "juin": 30,
    "juillet": 31,
    "aout": 31,
    "septembre": 30,
    "octobre": 31,
    "novembre": 30,
    "decembres": 31
}

# test modification
# Un second dictionnaire d'association des noms de mois français / anglais
frTranslator = {
    "janvier": "january",
    "février": "february",
    "mars": "march",
    "avril": "april",
    "mai": "may",
    "juin": "june",
    "juillet": "july",
    "août": "august",
    "septembre": "september",
    "octobre": "october",
    "novembre": "november",
    "décembre": "december"
}

print("Month requester - V1.0 :-)")

while True:
    month_name = input("Please enter a month name: ").lower()
    if month_name == "exit":
        break
    if month_name in months:
        print(f"Month {month_name} contains {months[month_name]} days")
    elif month_name in frTranslator:
        month_name = frTranslator[month_name]
        print(f"Month {month_name} contains {months[month_name]} days")
    else:
        print("Unknown month", month_name)
    
    
print("Bye bye")