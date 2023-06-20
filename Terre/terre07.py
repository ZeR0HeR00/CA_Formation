############### Terre : ok ###############
"""

Taille d'une chaîne

Créez un progamme qui affiche le nombre de caractères d'une chaîne de caractères passée en argument.

"""

import sys 

### Function ###

def chain_size(number_of_arguments):

    size = len(number_of_arguments)
    return size
    

def error():

    arguments = "".join(sys.argv[1:])

    if len(sys.argv) != 2 or arguments.isdigit():
        print("erreur")
        exit()

### Error ###

error()

### Parsing ###

number_of_arguments = "".join(sys.argv[1:])

### Problem solving ###

resultat = chain_size(number_of_arguments)

### Result ###

print(resultat)