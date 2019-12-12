#
list = [5, 12, "june"]


iterator = iter(list[::-1])
for i in range(len(list)):
    print(next(iterator))


