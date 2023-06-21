############### Eau : ok ###############

### Function ###
def combinaison_tree_number():

    for tree_number in range(0, 1000):
        tree_number = str(tree_number).zfill(3)

        if tree_number[0] < tree_number[1] and tree_number[1] < tree_number[2]:
            print(f"{tree_number[0]}{tree_number[1]}{tree_number[2]}")
    exit()


### Error ###


### Parsing ###

### Problem solving ###

resultat = combinaison_tree_number()

### Result ###

print(resultat)


"""

Autre manière de réssoudre l'exercice 

 def combinaison():

    for first_number in range(0, 10):

        for second_number in range(0, 10):

            for third_number in range(0, 10):

                if first_number < second_number and second_number < third_number:
                    print(f"{first_number}{second_number}{third_number}")
"""
