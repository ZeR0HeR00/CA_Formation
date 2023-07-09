############### Eau : ok ###############

import sys

### Function ###

def my_select_sort(number_array):
    
    new_array = [int(element) for element in number_array]
    
    for i in range(len(new_array)):
        min_index = i
        
        for j in range(i + 1, len(new_array)):
            if new_array[j] < new_array[min_index]:
                min_index = j
        
        new_array[i], new_array[min_index] = new_array[min_index], new_array[i]
    
    return new_array

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

result = my_select_sort(number_array)


### Result ###

print(" ".join([str(element) for element in result]))