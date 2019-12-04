# Задание 2
# Перепишите решение последней задачи из шестого урока так, чтобы она не использовала
# рекурсию и не вычисляла все промежуточные количества вариантов путей множество раз (что
# крайне неэффективно), а сохраняла их в списке.


def stairs(s):
    if len(memoize) > s:
        return memoize[s]
    else:
        memoize.append(memoize[len(memoize)-1]+memoize[len(memoize)-2])
        return stairs(s)


memoize = [0, 1, 2, 3]
stair = int(input('Enter the number of stair you want to climb: '))
result = stairs(stair)
print(f'You can climb {stair} stair(s) in {result} ways')
