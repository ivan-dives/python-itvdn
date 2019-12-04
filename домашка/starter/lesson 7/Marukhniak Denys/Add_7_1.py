# 1) мемоизация под факториал (или фибоначчи или любой другой алгоритм рекурсивный)


def factorial(f):
    if len(memoize) > f:
        return memoize[f]
    else:
        memoize.append(memoize[len(memoize)-1]*len(memoize))
        return factorial(f)


memoize = [1, 1]
num = int(input('Enter a number for n!: '))
result = factorial(num)
print(f'{num}! = {result}')
