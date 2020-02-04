# Створіть функцію num_split яка на вхід отримує один аргумент, що є цілим невід'ємним числом та розбиває його
# на цифри. Повертає список цифр з яких складається число.


def num_split(n):
    sn = str(n)
    res = []
    for i in sn:
        res.append(int(i))
    return res


print(num_split(24))