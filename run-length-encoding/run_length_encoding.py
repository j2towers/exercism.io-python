
def decode(text):
    mult = 1
    textout = ""
    for index, char in enumerate(text):
        if char.isdigit():
            if text[index - 1].isdigit():
                mult = int(str(text[index - 1] + char))
            else:
                mult = char
        elif char.isalpha() or char.isspace():
            if text[index - 1].isalpha() or text[index - 1].isspace():
                textout += char
            else:
                for run in range(int(mult)):
                    textout += char
    return textout



def encode(text):
    textout = ""
    count = 1
    maxidx = len(text)
    for index, char in enumerate(text):
        if index < maxidx - 1:
            if char == text[index + 1]:
                count += 1
            else:
                if count > 1:
                    textout += str(count) + char
                    count = 1
                else:
                    textout += char
        else:
            if count > 1:
                textout += str(count) + char
            else:
                textout += char
    return textout

