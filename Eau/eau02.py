############### Eau : ok ###############

import sys 

### Function ###

def reverse(argument):

    get_argument = argument
    print("\n".join(get_argument[::-1]))
    exit()

def handle_error():

    if len(sys.argv) < 2:
        print("Il n'y a aucun arguemnt")
        exit()

### Error ###

handle_error()

### Parsing ###

argument = sys.argv[1:]

### Problem solving ###

resultat = reverse(argument)

### Result ###

print(resultat)