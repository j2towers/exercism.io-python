import re

def word_count(string):
    string = re.sub(r'[^a-zA-Z0-9]', ' ', string)
    stringdict = {}
    for stringkey in re.split("[^a-zA-Z1-9]", string.lower()):
        if stringkey.isalnum():
            stringdict[stringkey] = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(stringkey), string.lower()))
    return stringdict