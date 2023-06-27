############### Eau : ok ###############
import sys
### Function ###

def uppercase_over_two(text):
    
    text = text.lower()

    result = ""

    for i, char in enumerate(text):
        
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char

    return result
    


def handle_error():

    if len(sys.argv) != 2:
        print("Error")
        exit()
        
    if sys.argv[1].isdigit():
        print("Please enter a string")
        exit()

### Error ###

handle_error()

### Parsing ###

text = str(sys.argv[1])

### Problem solving ###

resultat = uppercase_over_two(text)

### Result ###

print(resultat)