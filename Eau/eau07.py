############### Eau : ok ###############
import sys
### Function ###

def uppercase_over_two(text):
    chaine_uppercase = ""
    word_split = True

    for character in text:
        if character.isalpha():
            if word_split:
                chaine_uppercase += character.upper()
                word_split = False
            else:
                chaine_uppercase += character.lower()
        else:
            chaine_uppercase += character
            word_split = True
    print(chaine_uppercase)
    exit()


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

resultat = uppercase_over_two(text)

### Result ###

print(resultat)