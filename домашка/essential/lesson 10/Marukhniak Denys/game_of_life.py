from time import sleep

life = []
n = int(input('Задайте размер квадрата для точек (+): '))
print(f'Вводите по {n} символов в каждой строке: точка(+), а пустота(-).')
for _ in range(n):
    tmp = input()
    life.append(list(tmp))

life = [[1 if life[a][b] == '+' else 0 for b in range(n)] for a in range(n)]

for x in range(len(life[0])):
    for y in range(len(life)):
        if life[x][y] == 1:
            print('+', end='  ')
        else:
            print('-', end='  ')
    print()

generation = int(input('Сколько поколений показать? \n'))
for i in range(generation):
    next_life = [[0 for _ in range(len(life))] for _ in range(len(life))]
    for x in range(len(life[0])):
        for y in range(len(life)):
            die_or_life = 0
            try:
                for j in [x-1, x, x+1]:
                    for l in [y-1, y, y+1]:
                        if x == j and y == l:
                            continue
                        die_or_life += life[j][l]
            except IndexError:
                continue
            if die_or_life == 3 and life[x][y] == 0:         # Появление точки при 3 соседках.
                next_life[x][y] = 1
            elif 3 < die_or_life < 2 and life[x][y] == 1:    # Смерть точки от перенаселения или скуки.
                next_life[x][y] = 0
            elif die_or_life in [2, 3] and life[x][y] == 1:  # Точка остается жива.
                next_life[x][y] = 1

    result = next_life
    if result == [[0 for _ in range(len(result))] for _ in range(len(result))]:
        print(f'Все точки (+) погибли на {i+1} поколении.')
        break
    elif result == [[1 for _ in range(len(result))] for _ in range(len(result))]:
        print(f'Точки (+) все заполонили на {i+1} поколении.')
        break
    elif life == next_life:
        print(f'Точки (+) нашли идиллию на {i + 1} поколении.')
        break
    else:
        print(f'{i+1} поколение:')
        for x in range(len(result[0])):
            for y in range(len(result)):
                if result[x][y] == 1:
                    print('+', end='  ')
                else:
                    print('-', end='  ')
            print()
        sleep(0.5)
    life = result
