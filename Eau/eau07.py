############### Eau : ok ###############
import sys
### Function ###

def is_delimiteur(char):
    return char == " " or char == "\n" or char == "\t"

def uppercase(text):
    text = text.lower()
    chaine_uppercase = ""
    previous_char = ""

    for i in range(len(text)):
        if previous_char == "" or is_delimiteur(previous_char):
            chaine_uppercase += text[i].upper()
        else:
            chaine_uppercase += text[i]
        previous_char = text[i]

    return chaine_uppercase

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

text = sys.argv[1]

### Problem solving ###

resultat = uppercase(text)

### Result ###

print(resultat)