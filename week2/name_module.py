def reverse(strg):
    lis = " "
    for i in range(len(strg)-1, -1, -1):
        lis += strg[i]
    return lis.lstrip()