############### Terre : ok ###############
"""

Inverser une chaîne

Créez un programme qui affiche l'inverse de la chaîne de caractères donnée en argument.

"""

import sys

### Function ###

def reverse_word(word):
    print(word[::-1])
    exit()

def error():
    
    if len(sys.argv[1]) == 0 or len(sys.argv) != 2:
        print("erreur.")
        exit()

### Error ###

error()

### Parsing ###

word = sys.argv[1]


### Problem solving ###

resultat_reverse = " ".join(reverse_word(word))

### Result ###

print(resultat_reverse)