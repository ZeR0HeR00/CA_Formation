############### Terre : ok ###############
"""

Nombre premier

Créez un programme qui affiche si un nombre est premier ou pas.

"""

import sys

### Function ###

def first_number(number):

    i= 2
    while i < number and number % i != 0:
        i += 1
    
    if i == number:
        return f"Oui, {number} est un nombre premier."
    else:
        return f"Non, {number} n'est pas un nombre premier."


def error():

    if len(sys.argv) != 2:
        print("erreur")
        exit()

### Error ###

error()

### Parsing ###

number = int(sys.argv[1])


### Problem solving ###


resultat_first_number = first_number(number)

### Result ###

print(f"{resultat_first_number}")