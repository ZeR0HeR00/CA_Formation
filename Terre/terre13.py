############### Eau : ok ###############

import sys

### Function ###

def find_middle_number(a, b, c, d):

    try:
        if a > b and a < c or a < b and a > c:
            return a
        elif b > a and b < c or b < a and b > c:
            return b
        else:
            c
    except ValueError:
        return d

### Error ###

error = "erreur."

### Parsing ###

first_number = sys.argv[1:2]
second_number = sys.argv[2:3]
third_number = sys.argv[3:4]

### Problem solving ###

resultat = find_middle_number(first_number, second_number, third_number, error)
### Result ###

print(resultat, first_number)