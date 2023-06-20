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
    
    if hour >= 12 and am_or_pm == "AM":
        hour -= 12
        return f"{hour}:{minute}"
    elif hour >= 1 or hour <= 12 and am_or_pm == "AM" or "PM":
        return f"{hour}:{minute}"
    elif hour >= 0 or hour <= 12 and am_or_pm == "PM":
        hour += 12
        return f"{hour}:{minute}"
    
### Error ###



### Parsing ###

hour_complet = sys.argv[1]
am_pm = sys.argv[2]
### Problem solving ###

resultat = time_conversion(hour_complet,am_pm)

### Result ###

print(resultat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             