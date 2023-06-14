############### Terre : ok ###############
"""

Inverser une chaîne

Créez un programme qui affiche l'inverse de la chaîne de caractères donnée en argument.

"""

import sys

### Function ###

def reverse_word(word):

    return word[::-1]

def error():
    
    if len(sys.argv[1]) == 0:
        print("erreur.")
        exit()

### Error ###

error()

### Parsing ###

word = sys.argv[1:]


### Problem solving ###

resultat_reverse = " ".join(reverse_word(word))

### Result ###

print(resultat_reverse)