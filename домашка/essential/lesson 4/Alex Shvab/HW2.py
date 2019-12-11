def revers(str):
    i = len(str) - 1

    while True:
        l = str[i]
        if i < 0:
            break

        i -= 1
        yield l


str = input("Enter some string: ")
res = ""
#for x in revers(str):
#    res += x

s = revers(str)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
