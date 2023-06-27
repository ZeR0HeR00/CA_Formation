############### Eau : ok ###############
import sys
### Function ###

def comparaison(chaine_one, chaine_two):
    
    for debut in range(0, len(chaine_one) - len(chaine_two) + 1):
        
        if chaine_two == chaine_one[debut : debut + len(chaine_two)]:
            return True

    return False

def handle_error():

    if len(sys.argv) != 3:
        print("Error")
        exit()
    if sys.argv[1].strip("-").isdigit() or sys.argv[2].strip("-").isdigit():
        print("Please enter a string")
        exit()
    

### Error ###

handle_error()


### Parsing ###

first_word = sys.argv[1]
second_word = sys.argv[2]

### Problem solving ###

resultat = comparaison(first_word, second_word)

### Result ###

print(resultat)