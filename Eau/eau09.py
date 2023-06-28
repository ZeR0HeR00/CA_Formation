############### Eau : ok ###############

import sys

### Function ###
def display_between_min_and_max(first_digit, second_digit):

    mini, maxi = first_digit, second_digit
    if first_digit < second_digit:
        mini, maxi = first_digit, second_digit
    else:
        mini, maxi = second_digit, first_digit
    
    while mini < maxi:
        mini += 1
        print(mini - 1)


def handle_error():

    if len(sys.argv) != 3:
        print("Error")
        exit()

    if not sys.argv[1].lstrip("-+").isdigit() or not sys.argv[2].lstrip("-+").isdigit():
        print("Error")
        exit()
### Error ###

handle_error()

### Parsing ###

first_digit = int(sys.argv[1])
second_digit = int(sys.argv[2])

### Problem solving and resutat ###

display_between_min_and_max(first_digit, second_digit)

