# Задание 3
# Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну.
# Определите, сколькими способами можно подняться на заданную ступеньку.


def stair(stair_n):
    if stair_n in range(-1, 2):
        return stair_n + 1
    else:
        return stair(stair_n-1) + stair(stair_n-2)


n = int(input('Enter the number of stair you want to climb: '))
print('Result: ', stair(n-1))
