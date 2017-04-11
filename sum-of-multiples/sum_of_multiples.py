def sum_of_multiples(cap, multilist):
    sumlist = list()
    for number in range(cap):
        for divisor in multilist:
            if not number % divisor:
                if number not in sumlist:
                    sumlist.append(number)
    return sum(sumlist)

