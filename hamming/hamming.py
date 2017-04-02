def distance(stringa, stringb):
    if len(stringa) == len(stringb):
        hamcount = 0
        for letteritem in range(len(stringa)):
            if stringa[letteritem] != stringb[letteritem]:
                hamcount += 1
        return hamcount
    else:
        raise ValueError