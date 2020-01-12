x = input('Введите последовательность целых чисел через пробел: ').split()

l = [int(i) for i in x]
print(sorted(l))

