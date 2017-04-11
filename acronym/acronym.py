

def abbreviate(stringin):
    stringout = ""
    listin = list()

    if ":" in stringin:
        listin = stringin.split(":")
        return listin[0].strip()
    else:
        for index, testitem in enumerate(stringin):
            if testitem.isupper() or stringin[index - 1].isspace() or not stringin[index - 1].isalnum():
                print(testitem)
                if stringin[index - 1].isspace() or stringin[index - 1].islower() or not stringin[index - 1].isalnum():
                    stringout += testitem.strip()
        return stringout.upper()

