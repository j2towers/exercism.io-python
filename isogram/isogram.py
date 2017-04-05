def is_isogram(testword):
    for letteritem in testword.lower():
        if testword.lower().count(letteritem) > 1 and letteritem.isalpha():
            return False
    return True