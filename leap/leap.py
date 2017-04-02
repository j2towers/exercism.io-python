def is_leap_year(inputyear):
    leaptrue = False
    if inputyear % 4 == 0 and inputyear % 100 != 0:
        leaptrue = True
    elif inputyear % 400 == 0:
        leaptrue = True
    return(leaptrue)
    pass
