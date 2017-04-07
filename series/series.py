def slices(stringin, slength):

    listout = list()

    if slength > len(stringin) or slength == 0:
        raise ValueError
    else:
        for index, num in enumerate(stringin):
            liststring = list()
            if index + slength <= len(stringin):
                for a in range(slength):
                    liststring.append(int(stringin[index + a]))
                listout.append(liststring)
        return listout


