import string

def rotate(stringin, rotation):
    outstring = ""

    for charitem in stringin:
        if charitem.isalpha():
            if charitem.isupper():
                for index, letter in enumerate(string.ascii_uppercase):
                    if charitem is letter:
                        if index + rotation < len(string.ascii_uppercase) - 1:
                            outstring += string.ascii_uppercase[index + rotation]
                        else:
                            newdex = (index + rotation) - 26
                            outstring += string.ascii_uppercase[newdex]
            elif charitem.islower():
                for index, letter in enumerate(string.ascii_lowercase):
                    if charitem is letter:
                        if index + rotation < len(string.ascii_lowercase) - 1:
                            outstring += string.ascii_lowercase[index + rotation]
                        else:
                            newdex = (index + rotation) - 26
                            outstring += string.ascii_lowercase[newdex]
        else:
            outstring += charitem
    return outstring
