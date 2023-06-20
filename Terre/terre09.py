############### Terre : ok ###############

import sys

### Function ###

def square_root(base):

    resultat = pow(base, 0.5)
    return resultat


def handle_error():
    
    if int(sys.argv[1]) <= 0:
        print("erreur")
        exit()

### Error ###

handle_error()

### Parsing ###

base = int(sys.argv[1])

### Problem solving ###

resultat_square = square_root(base)


### Result ###

print(f"Le résultat est : {resultat_square}")