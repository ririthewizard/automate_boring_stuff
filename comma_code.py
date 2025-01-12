def commaCode(l):
    if len(l) == 0:
        return "That's an empty list!"
    commaString = ""
    for i in l[:-1]:
        commaString = commaString + i +", "
    commaString = commaString + "and " + l[-1]
    return commaString


