############### Terre : ok ###############
"""

L'alphabet à partir de

Créez un programme qui affiche l'alphabet à partir de la lettre donnée en argument en 
lettres minuscules suivi d'un retour à la ligne.

"""

import sys

### Function ###

def alphabet(letter):
    
    alphabet = [chr(i) for i in range(ord(letter), ord("z") + 1)]
    return alphabet

def error(arg):

    if len(arg) != 2:
        print("erreur")
        exit()

    if ord(arg[1]) < 97 or ord(arg[1]) > 123:
        print("erreur")
        exit()
    
### Error ###

error(sys.argv)

### Parsing ###

letter = sys.argv[1]

### Problem solving ###

resultat = "".join(alphabet(letter))

### Result ###

print(resultat)