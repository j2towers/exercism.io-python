def largest_product(series, size):

    total = 0

    if (not str.isalpha(series) and len(series) > 0):

        if (size >= 0 and size <= len(series)):

            for digit in range(len(series)):

                addarray = []
                subtotal = 1

                for arraybuild in range(size):

                    if (digit + arraybuild < len(series)):
                        addarray.append(int(series[digit + arraybuild]))

                if (len(addarray) == size):
                    for addnum in addarray:

                        subtotal *= addnum

                    if (subtotal > total):

                        total = subtotal

        else:

            raise ValueError("Size error.")

    elif (size == 0):

        return 1

    else:

        raise ValueError("Series is not a number.")

    return total







