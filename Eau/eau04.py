############### Eau : ok ###############

import sys
### Function ###

def next_prime_number(number):
    
    i = 2
    while i < number and number % i != 0:
        i += 1
    
    if i == number:
        return f"The next prime number is : {number}"
    else:
        return f"{next_prime_number(number + 1)}"

def handle_error():

    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Please enter a number")
        exit()
    
    if  int(sys.argv[1]) < 0:
        print("-1")
        exit()

### Error ###

handle_error()

### Parsing ###

prime_number = int(sys.argv[1])

### Problem solving ###

resultat = next_prime_number(prime_number)

### Result ###

print(resultat)