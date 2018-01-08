import math

def finddigits(numberin):

    if numberin > 0:
        digits = int(math.log10(numberin))+1
    elif numberin == 0:
        digits = 0
    else:
        digits = int(math.log10(-numberin))+1

    return digits

def get_digit(numberin, digit):

    return numberin // 10**digit % 10

def is_armstrong(numberin):
    total = 0
    powerto = finddigits(numberin)

    for digit in range(powerto):

        total += get_digit(numberin, digit)**powerto

    if (total == numberin):
        return True
    else:
        return False