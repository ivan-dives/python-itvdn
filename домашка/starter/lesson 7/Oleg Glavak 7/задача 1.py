list = [7, 12, 24, 2, 14, 54, 36, 8, 51, 10, 3, 18]

def Sumlist(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + Sumlist(l[1:])

print(Sumlist(list))
#######################################

def minmaxlist(l):
    return min(l), max(l)

def minmaxlist2(l):
    l.sort()
    return l[0], l[-1]

print(minmaxlist(list))
print(minmaxlist2(list))
########################################

def mid(l):
    if len(l) == 1:
        return l[0]
    else:
        return (l[0] + Sumlist(l[1:])) / len(l)

print(mid(list))