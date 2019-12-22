def any_dict(d1, a, b):
    for qnt in range (int(input('How many elements you would like to add?\n'))):
        a = str(input("your key\n"))
        b = int(input("your number\n"))
        d1[a] = b
    return d1

lim = {'ft': 1, 'in': 2, 'mm': 6, 'cm': 3, 'yd': 5, 'mi': 8}
print(any_dict(lim, 'lb', 4))
