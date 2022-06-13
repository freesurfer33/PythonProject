import random

number_to_find = random.randint(1, 100)
nb_essai = 5

print('*** Le jeu du nombre mystère ***')
while nb_essai > 0:
    if nb_essai == 1:
        txt_essai = "essai"
    else:
        txt_essai = "essais"
    print(f"Il te reste {nb_essai} {txt_essai}")
    essai=input('Devine le nombre : ')
    if essai.isdigit():
        if int(essai) > number_to_find:
            print(f"Le nombre mystère est plus petit que {essai}")
        elif int(essai) < number_to_find:
            print(f"Le nombre mystère est plus grand que {essai}")
        else:
            print(f"Bravo ! Le nombre mystère était bien {essai} !")
            print(f"Tu as trouvé le nombre en {6-nb_essai} essai")
            print("Fin du jeu.")
            break
        nb_essai = nb_essai - 1
    else:
        print('Veuillez entrer un nombre valide')  

    if nb_essai == 0:
        print(f"Dommage ! Le nombre mystère était {number_to_find}")
        print("Fin du jeu.")
