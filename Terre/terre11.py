############### Terre : ok ###############

import sys

### Function ###


def time_conversion_split(hour_time):

    hour_time = "".join(hour_time).split(":")
    return hour_time


def time_conversion(hour_time, am, pm):

    hour_and_minute = time_conversion_split(hour_time)

    hour, minute = int("".join(hour_and_minute[0])), int(
        "".join(hour_and_minute[1]))

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

    hour_and_minute = time_conversion_split(sys.argv[1:])

    if not hour_and_minute[0].isdigit() or not hour_and_minute[1].isdigit():
        print("Heure et minute doivent correspondre à des nombre")
        exit()
    elif len(hour_and_minute) != 2 or len(hour_and_minute[0]) > 2 or len(hour_and_minute[1]) > 2:
        print("Veuillez à entrer le bon modèle d'heure et de minutes")
        exit()
    elif int(hour_and_minute[0]) > 23 or int(hour_and_minute[1]) > 59:
        print("Les heures ne peuvent dépasser 23 et les minutes 59.")
        exit()


### Error ###

error()

### Parsing ###

hour_complet = sys.argv[1]
morning = "AM"
evening = "PM"

### Problem solving ###

resultat = time_conversion(hour_complet, morning, evening)

### Result ###

print(resultat)
