############### Terre : ok ###############
"""

Divisions

Créez un programme qui affiche le résultat et le reste d'une division entre deux nombres.

"""

import sys

### Function ###


def divisions(first_number, second_number):

    first_number, second_number = int(first_number), int(second_number)

    quotient = first_number // second_number

    reste = first_number % second_number

    return [quotient, reste]


def error():

    if len(sys.argv) != 3:
        print("erreur.")
        exit()

    if not sys.argv[1].lstrip("-+").isdigit() or not sys.argv[2].lstrip("-+").isdigit():
        print("erreur.")
        exit()

    if int(sys.argv[2]) == 0:
        print("erreur.")
        exit()


### Error ###

error()

### Parsing ###

first_number = int(sys.argv[1])
second_number = int(sys.argv[2])

### Problem solving ###

resultat_divisions = divisions(first_number, second_number)
quotient = resultat_divisions[0]
reste = resultat_divisions[1]

### Result ###

print(f"résultat : {quotient} \nreste : {reste}")
