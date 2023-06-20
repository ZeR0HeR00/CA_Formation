############### Terre : ok ###############
"""

Pair ou impair

Créez un programme qui permet de déterminer si l'argument donné est un entier pair ou impair.

"""

import sys

### Function ###

def is_even_or_odd(number):

    val = int(number)

    if val % 2 == 0:
        return "pair"
    else:
        return "impair"


def handle_error():

    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("erreur.")
        exit()

### Error ###

handle_error()

### Parsing ###

number = sys.argv[1]

### Problem solving ###

resultat = is_even_or_odd(number)


### Result ###

print(resultat)