
def sieve(capnum):
    outlist = []

    for num in range(2, capnum + 1):
        for checknum in range(2, num):
            if not num % checknum:
                break
        else:
            outlist.append(num)
    return outlist






