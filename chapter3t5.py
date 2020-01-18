def twoStrings(s1, s2):
    for el in range(len(s1)):
        if s1[el] in s2:
            return 'YES'
            break
    return 'NO'