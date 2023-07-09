############### Eau : ok ###############
import sys

### Function ###

def index_wanted(argument_array,last_argument):
    
    for i in range(len(argument_array)):
        if last_argument[0] == argument_array[i]:
            return i
    return "-1"


def handle_error():

    if len(sys.argv) == 1:
        print("error")
        exit()

### Error ###

handle_error()

### Parsing ###

argument_array = sys.argv[1:-1]
last_argument = sys.argv[-1:]
### Problem solving ###

resultat = index_wanted(argument_array, last_argument)

### Result ###

print(resultat)