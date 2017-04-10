
def sieve(capnum):
    outlist = []

    for num in range(2, capnum + 1):
        for checknum in range(2, num):
            if num % checknum == 0:
                break
        else:
            outlist.append(num)
    return outlist






