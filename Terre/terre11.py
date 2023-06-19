############### Terre : ok ###############

import sys

### Function ###

def time_conversion_split(heure):

    heure = "".join(heure).split(":")
    return heure

def time_conversion(heure, am, pm):

    liste = time_conversion_split(heure)

    hour, minute = int("".join(liste[0])), int("".join(liste[1]))
    
    if hour == 00:
        hour = 12
        return f"{hour}:{minute} {am}"

    if hour == 13 or hour <= 23:
        hour = hour - 12
        return f"{hour}:{minute} {pm}"

    if hour > 00 and hour < 12:
        return f"{hour}:{minute} {am}"
    else:
        return f"{hour}:{minute} {pm}"

def error():

    liste = time_conversion_split(sys.argv[1:])

    if not liste[0].isdigit() or not liste[1].isdigit():
        print("heure et minute doivent correspandre à des nombre")
        exit()
    elif len(liste) != 2 or len(liste[0]) > 2 or len(liste[1]) > 2:
        print("erreur")
        exit()


### Error ###

error()

### Parsing ###

heures_complet = sys.argv[1]
morning = "AM"
evening = "PM"

### Problem solving ###

resultat = time_conversion(heures_complet, morning, evening)

### Result ###

print(resultat)