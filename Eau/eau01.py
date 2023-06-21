############### Eau : ok ###############

### Function ###
def combinaison():

    for first_number in range(0, 99):
        first_number = str(first_number).zfill(2)
        
        for second_number in range(0, 99):
            second_number = str(second_number).zfill(2)

            if first_number < second_number:
                print(f"{first_number} {second_number}")
    exit()


### Error ###




### Parsing ###




### Problem solving ###

resultat = combinaison()

### Result ###

print(resultat)