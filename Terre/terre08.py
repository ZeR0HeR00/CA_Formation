############### Terre : ok ###############
"""

Puissance d'un nombre

Créez un programme qui affiche le résultat d'une puissance
l'exposant ne pourra pas être négatif.

"""

import sys

### Function ###

def power_of_number(base, exposant):

    resultat = 1

    for i in range(exposant):
        resultat *= base
        return resultat

def error():
    
    if int(sys.argv[1]) < 0 or int(sys.argv[2]) < 0:
        print("erreur")
        exit()

### Error ###

error()

### Parsing ###

base, exposant = int(sys.argv[1]), int(sys.argv[2])

### Problem solving ###

resultat_puissance = power_of_number(base, exposant)


### Result ###

print(f"Le résultat est : {resultat_puissance}")