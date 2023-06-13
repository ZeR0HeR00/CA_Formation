############### Terre : ok ###############

import sys

### Function ###

def find_middle_number(first, second, third):


    if first > second and first < third or first < second and first > third:
        return first
    elif second > first and second < third or second < first and second > third:
        return second
    else:
        return third

def error():

    if len(sys.argv) != 4:
        print("Le nomnbre d'argument n'est pas correct")
        exit()

    if not sys.argv[1].lstrip("-+").isdigit() or not sys.argv[2].lstrip("-+").isdigit() or not sys.argv[3].lstrip("-+").isdigit():
        print("erreur.")
        exit()

### Error ###

error()

### Parsing ###

first_number = int(sys.argv[1])
second_number = int(sys.argv[2])
third_number = int(sys.argv[3])

### Problem solving ###

resultat = find_middle_number(first_number, second_number, third_number)
### Result ###

print(resultat)
