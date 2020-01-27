import time
import random
import copy
from numpy import unique

black_square_symbol = chr(int('25A0', 16))


def get_cell_state(table, row, col):
    if row in range(len(table)) and col in range(len(table[0])):
        return 1 if table[row][col] else 0
    return 0


def get_neighboring_cells(table, row, col):
    sum = 0
    for row_shift in (-1, 0, 1):
        for col_shift in (-1, 0, 1):
            if row_shift or col_shift:
                sum += get_cell_state(table, row + row_shift, col + col_shift)
    return sum


def generate_table(height, width, rand_seed=time.time()):
    random.seed(rand_seed)
    table = [[None] * width for _ in range(height)]
    for row in range(height):
        for col in range(width):
            table[row][col] = random.choice([True, False])
    return table


def update_table(table, height, width):
    new_table = copy.deepcopy(table)
    for row in range(height):
        for col in range(width):
            neighboring_cells = get_neighboring_cells(table, row, col)
            if neighboring_cells < 2 and table[row][col]:

                new_table[row][col] = False
            elif neighboring_cells > 3 and table[row][col]:

                new_table[row][col] = False
            elif neighboring_cells == 3 and not table[row][col]:

                new_table[row][col] = True
    return new_table


def print_table(table):
    for row in table:
        for elem in row:
            print(black_square_symbol if elem else '*', end='_')
        print()
    t2 = []
    t2 = unique(table)
    if True not in t2:
        exit()


def main():
    height = int(input('Enter table height: '))
    width = int(input('Enter table width: '))

    table = generate_table(width, height)
    year = 1
    while True:
        print_table(table)
        print('year:', year)
        year += 1
        table = update_table(table, height, width)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
