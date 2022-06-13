from pathlib import Path

fichier_prenoms = 'prenoms.txt'
fichier_prenoms_tries = 'prenomstries.txt'
dossier_courant = Path.cwd()
file_prenoms = dossier_courant / fichier_prenoms
file_prenoms_tries = dossier_courant / fichier_prenoms_tries

str_prenom = file_prenoms.read_text().splitlines()

print (str_prenom)

liste_prenoms = []

for prenom_line in str_prenom:
    prenom_line = prenom_line.split(' ')
    liste_prenoms.extend(prenom_line)


print(liste_prenoms)

for i in range(len(liste_prenoms)):
    liste_prenoms[i] = liste_prenoms[i].strip(",. ")



liste_prenoms.sort()

print(liste_prenoms)

with open(file_prenoms_tries, "a") as f:
    for prenom in liste_prenoms:
        if prenom != '':
            f.write(prenom + "\n")

f.close()



    
