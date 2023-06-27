############### Eau : ok ###############
import sys
### Function ###

def is_delimiter_digit(char):
    return char in ["0", "1", "2",
             "3","4", "5", "6", 
             "7", "8", "9"]

def digit_only(text):

    for i in range(len(text)):

        if not is_delimiter_digit(text[i]):
            return False
        
    return True

def handle_error():

    if len(sys.argv) != 2:
        print("Error")
        exit()


### Error ###

handle_error()

### Parsing ###

text = sys.argv[1]

### Problem solving ###

resultat = digit_only(text)

### Result ###

print(resultat)