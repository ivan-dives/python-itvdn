def gen_revers(n):
    i = len(n) - 1

    if i <= 0:
        return print(None)
    else:
        while i >= 0:
            yield n[i]
            i -= 1


def relise():
    reli = list(input('Введите список: '))
    for i in gen_revers(reli):
        print(i)


relise()
