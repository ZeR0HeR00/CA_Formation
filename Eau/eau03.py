############### Eau : ok ###############

import sys

### Function ###

def fibonacci(number):

    if  number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

def handle_error():

    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Veuillez entrer un nombre")
        exit()
    
    if  int(sys.argv[1]) < 0:
        print("-1")
        exit()

### Error ###

handle_error()


### Parsing ###

number = int(sys.argv[1])

### Problem solving ###

resultat = fibonacci(number)

### Result ###

print(resultat)