def to_rna(string):
    rnadict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ""
    for letteritem in string:
        if letteritem in rnadict.keys():
            rna += rnadict[letteritem[0]]
        else:
            return ""
    return rna
