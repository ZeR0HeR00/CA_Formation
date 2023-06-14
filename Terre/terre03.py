############### Terre : ok ###############
"""

L'alphabet à partir de

Créez un programme qui affiche l'alphabet à partir de la lettre donnée en argument en 
lettres minuscules suivi d'un retour à la ligne.

"""

import sys

### Function ###

def alphabet(l):

    a = 97
    z = 123

    alphabet = [chr(i) for i in range(a, z)]
    
    lettre = alphabet.index(l)
    resultat = "".join(alphabet[lettre:])
    print(resultat)
    exit()
### Error ###


### Parsing ###

letter = sys.argv[1]

### Problem solving ###

res = alphabet(letter)

### Result ###

print(res)