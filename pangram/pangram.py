import string

def is_pangram(test):
    for letteritem in string.ascii_lowercase:
        if letteritem not in test.lower():
            return False
    return True
