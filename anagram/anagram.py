def detect_anagrams(stringin, listin):
    listout = list()

    for a in listin:
        astring = str(a).lower()
        instring = str(stringin).lower()
        if instring != astring:
            if sorted(instring) == sorted(astring):
                listout.append(a)

    return listout
