############### Terre : ok ###############
""" 

Afficheur d'argument

Créer un programme qui affiche les arguments qu'il reçoit ligne par ligne,
peu importe le nombre d'arguments.

"""

import sys

### Function ###

def get_argument(user_term):

    for argument in user_term:
        print(argument)
    exit()



### Error ###

### Parsing ###

user = sys.argv[1:]

### Problem solving ###

resultat = get_argument(user)

### Result ###

print(resultat)