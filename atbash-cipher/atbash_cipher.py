import string

revalpha = string.ascii_lowercase[::-1]

def encode(stringin):
    stringin = stringin.lower().strip().translate(None, string.punctuation)
    stringout = ""

    for letter in stringin:
        for index, match in enumerate(string.ascii_lowercase):
            if letter == match:
                stringout += revalpha[index]
    for space in range(0, len(stringout) + 1, 5):
        stringout = stringout[:space] + " " + stringout[space:]
    return stringout


def decode(stringin):
    stringin = stringin.lower().strip()
    stringout = ""

    for letter in stringin:
        for index, match in enumerate(revalpha):
            if letter == match:
                stringout += alpha[index]
    return stringout
