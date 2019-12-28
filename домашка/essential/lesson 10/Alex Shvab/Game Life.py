import pprint
world = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]


def next_gen():
    new_w = []
    for i in range(len(world[0])):
        new_w.append([0] * len(world))
        for j in range(len(world)):
            if world[i][j] == 0:
                count = count_neighbor(i,j)
                if count > 2:
                    new_w[i][j] = 1
                else:
                    new_w[i][j] = 0

            if world[i][j] == 1:
                count = count_neighbor(i,j)
                if count < 2 or count > 3:
                    new_w[i][j] = 0
                else:
                    new_w[i][j] = 1
    pprint.pprint(new_w)


def neighbor(x, y):
    for i in range(x, x+1):
        for j in range(y, y+1):
            if world[i][j] == 1:
                return 1
            else:
                return 0


def count_neighbor(x, y):
    n = 0
    for a in [x-1, x, x+1]:
        for b in [y-1, y, y+1]:
            if a==x and b==y:
                continue
            try:
                n += world[a][b]
            except IndexError:
                pass
    return n

def main():
    life = int(input("Enter number of life: "))
    for x in range(life):
        next_gen()
        print()

if __name__ == "__main__":
    main()