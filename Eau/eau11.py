############### Eau : ok ###############

import sys

### Function ###
    
def absolut_min_difference(number_array):
    try:

        for i in range(len(number_array)):
            number_array[i] = int(number_array[i])

    
    except ValueError:
        print("Enter numbers only")
        exit()

    number_array = sorted(number_array)
   
    minimum = abs(number_array[0] - number_array[1])

    for i in range(1, len(number_array) - 1):
        result_substraction = abs(number_array[i] - number_array[i + 1])
            
        if minimum > result_substraction:
            minimum = result_substraction
    
    return minimum
    
def handle_error():

    if len(sys.argv) == 2:
        print("Error")
        exit()

### Error ###

handle_error()


### Parsing ###

number_array = sys.argv[1:]

### Problem solving & result###

print(absolut_min_difference(number_array))