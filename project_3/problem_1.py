
PRECEISE = 0.000001
import math
class InputError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise InputError('number must be positive')
    elif number == 0:
        return 0
    
    guess = 1.0
    while math.fabs(guess * guess - number) /  number >= PRECEISE: 
        guess = (number / guess + guess) / 2  
        #print(f'guess: {guess}')
    return round(guess, 0)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print ("Pass" if  (2 == sqrt(5)) else "Fail")
print ("Pass" if  (1000 == sqrt(1_000_000)) else "Fail")
print ("Pass" if  (31623 == sqrt(1_000_000_000)) else "Fail")