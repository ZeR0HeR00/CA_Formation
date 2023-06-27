############### Eau : ok ###############
import sys
### Function ###

def uppercase_over_two(text):
    
    text = text.lower()
    result = ""
    index_letter = 0

    for i in range(len(text)):
        
        if index_letter % 2 == 0:
            result += text[i].upper()
        else:
            result += text[i]

        if text[i] != " ":
            index_letter += 1
    
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