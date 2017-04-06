from string import digits as numbers

def square_of_sum(numberin):
    outsum = 0
    numberitem = 1
    while numberitem <= numberin:
        outsum += numberitem
        numberitem += 1
    return outsum ** 2


def sum_of_squares(numberin):
    outsum = 0
    numberitem = 1
    while numberitem <= numberin:
        outsum += numberitem ** 2
        numberitem += 1
    return outsum


def difference(numberin):
    return square_of_sum(numberin) - sum_of_squares(numberin)


