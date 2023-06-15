############### Eau : ok ###############
"""

Trié ou pas

Créez un programme qui détermine si une liste d'entiers est triée ou pas.

"""

import sys

### Function ###

def sorted_not_sorted(first_number, second_number, third_number):

    if int(first_number) < int(second_number) and int(second_number) < int(third_number):
        print("Triée !")
        exit()
    else:
        print("Pas triée !")
        exit()


### Error ###




### Parsing ###

first_number = sys.argv[1]
seconde_number = sys.argv[2]
third_number= sys.argv[3]

### Problem solving ###

resultat = sorted_not_sorted(first_number, seconde_number, third_number)

### Result ###

print(resultat)