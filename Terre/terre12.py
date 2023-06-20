############### Terre : ok ###############

import sys

### Function ###

def time_conversion_split(hour_time):

    hour_time = "".join(hour_time).split(":")
    return hour_time

def time_conversion(hour_time,am_or_pm):

    hour_and_minute = time_conversion_split(hour_time)
    
    hour, minute = int("".join(hour_and_minute[0])), int(
        "".join(hour_and_minute[1]))
    
    if am_or_pm == "AM":

        if hour >= 12:
            return f"{hour - 12}:{minute}"
        
        if hour >= 1 or hour <= 12:
            return f"{hour}:{minute}"
        
    if am_or_pm == "PM":

        if hour >= 1 or hour <= 11:
            return f"{hour + 12}:{minute}"

def handle_error():

    if sys.argv != 2:
        print("erreur")
        exit()
    
    hour_and_minute = time_conversion_split(sys.argv[1])

    if not hour_and_minute[0].isdigit() or not hour_and_minute[1].isdigit():
        print("Heure et minute doivent correspondre à des nombre")
        exit()
    elif len(hour_and_minute) != 2 or len(hour_and_minute[0]) > 2 or len(hour_and_minute[1]) > 2 or len(sys.arg[2]) != 1:
        print("Veuillez à entrer le bon modèle d'heure et de minutes")
        exit()
    elif int(hour_and_minute[0]) > 12 or int(hour_and_minute[1]) > 59:
        print("Les heures ne peuvent dépasser 12 et les minutes 59.")
        exit()

### Error ###

handle_error()

### Parsing ###

hour_complet = sys.argv[1]
am_pm = sys.argv[2].upper
### Problem solving ###

resultat = time_conversion(hour_complet,am_pm)

### Result ###

print(resultat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             