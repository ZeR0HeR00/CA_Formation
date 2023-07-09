############### Eau : ok ###############

import sys

### Function ###

def sort_by_ascii_order(arguments):
    
    for i in range(len(arguments)):
        for j in range(i + 1, len(arguments)):
            if compare_ascii(arguments[i], arguments[j]) > 0:

                arguments[i], arguments[j] = arguments[j], arguments[i]
    return " ".join(arguments)

def compare_ascii(first_word, second_word):
    min_length = min(len(first_word), len(second_word))
    
    for i in range(min_length):
        if ord(first_word[i]) < ord(second_word[i]):
            return -1
        elif ord(first_word[i]) > ord(second_word[i]):
            return 1
    if len(first_word) < len(second_word):
        return -1
    elif len(first_word) > len(second_word):
        return 1
    else:
        return 0

def handle_error():

    if len(sys.argv[1:]) < 2:
        print("Please enter several arguments")
        exit()

### Error ###

handle_error()

### Parsing ###

arguments = sys.argv[1:]

### Problem solving ###

result = sort_by_ascii_order(arguments)

### Result ###

print(result)