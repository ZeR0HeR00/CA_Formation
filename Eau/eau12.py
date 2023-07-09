############### Eau : ok ###############

import sys

### Function ###

def my_bubble_sort(number_array):

    permuted = True

    while permuted:

        permuted = False
        
        for i in range(len(number_array) - 1):
        
            if number_array[i] > number_array[i + 1]:
                number_array[i], number_array[i + 1] = number_array[i + 1], number_array[i]
                permuted = True
    
    return " ".join(number_array)
               
def handle_error():

    if len(sys.argv[1:]) < 2:
        print("Enter at least 2 numbers")
        exit()
        
    if not "".join(sys.argv[1:]).isdigit(): 
        print("Enter numbers only")
        exit()

### Error ###

handle_error()

### Parsing ###

number_array = sys.argv[1:]

### Problem solving ###

result = my_bubble_sort(number_array)

### Result ###

print(result)