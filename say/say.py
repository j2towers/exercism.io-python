onedict = {0: "zero",
           1: "one",
           2: "two",
           3: "three",
           4: "four",
           5: "five",
           6: "six",
           7: "seven",
           8: "eight",
           9: "nine"}
tendict = {0: "",
           2: "twenty",
           3: "thirty",
           4: "forty",
           5: "fifty",
           6: "sixty",
           7: "seventy",
           8: "eighty",
           9: "ninety"}
teendict = {0: "ten",
           1: "eleven",
           2: "twelve",
           3: "thirteen",
           4: "fourteen",
           5: "fifteen",
           6: "sixteen",
           7: "seventeen",
           8: "eighteen",
           9: "nineteen"}
lendict = {0: "hundred",
           1: "thousand",
           3: "million",
           4: "billion",
           5: "trillion"}


def say(numin):
    numlist = format(numin, ",").split(",")
    stringout = ""

    x = 0
    for i in range(len(numlist)):
        j = str(i)
        if len(j) > 2:
            stringout += onedict[int(j[0])] + " hundred and"
            if j[1] == "1":
                stringout += teendict[int(j[2])] + " "
                break
            else:
                stringout += tendict[int(j[1])] + " " + onedict[int(j[2])] + " "
        elif len(j) > 1:
            if j[0] == "1":
                stringout += teendict[int(j[1])] + " "
                break
            else:
                stringout += tendict[int(j[0])] + " " + onedict[int(j[1])] + " "
        else:
            stringout += onedict[int(j[0])] + " "
        #stringout += lendict[int(len(numlist) - x)] + " "
        x += 1

    print(int(len(numlist) - x))
    print(stringout)
    return stringout


