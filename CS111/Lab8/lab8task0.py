#
# lab8task0.py (Lab 8, Task 0)
#
# Simplifying code that uses conditional execution
#
# Computer Science 111
#

def process_grades(grades, poss_pts, threshold):
    """ converts each grade in the list grades to a percentage 
        (based on the specified number of possible points, poss_pts),
        and prints the converted grades. In addition, it counts and 
        returns the number of raw grades that are below the specified 
        threshold
    """
    num_below = 0

    for g in grades:
        if g < threshold:
            num_below += 1
        pct = round(g/poss_pts * 100, 1)
        print(g, '/', poss_pts, '=', pct, 'percent')
    return num_below    

def process_temp(celcius):
    """ converts the specified celcius temperature to fahrenheit, 
        and prints and returns the fahrenheit temperature. In addition, 
        it prints a message if the temperature is below or above 
        the range of typical room temperatures (20-25 C). 
    """
    if celcius < 20 or celcius > 25:
        print(celcius, 'C is below room temperature')
    fahrenheit = 9/5*celcius + 32
    print(celcius, 'C =', fahrenheit, 'F')
