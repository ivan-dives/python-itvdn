import pprint
world = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]


def next_gen(world_current):
    new_w = []
    for i in range(len(world_current[0])):
        new_w.append([0] * len(world_current))
        for j in range(len(world_current)):
            if world_current[i][j] == 0:
                count = count_neighbor(i, j)
                if count == 3:
                    new_w[i][j] = 1
                else:
                    new_w[i][j] = 0

            if world_current[i][j] == 1:
                count = count_neighbor(i, j)
                if count < 2 or count > 3:
                    new_w[i][j] = 0
                else:
                    new_w[i][j] = 1

    if new_w == world_current:
        return 1

    if not any_survivors(new_w):
        return 2

    pprint.pprint(new_w)
    global world
    world = new_w


def any_survivors(w):
    for i in range(len(w[0])):
        for j in range(len(w)):
            if w[i][j] == 1:
                return True
    return False


def count_neighbor(x, y):
    n = 0
    for a in [x-1, x, x+1]:
        for b in [y-1, y, y+1]:
            if a == x and b == y:
                continue
            try:
                n += world[a][b]
            except IndexError:
                pass
    return n


def main():
    pprint.pprint(world)
    life = int(input("Enter number of life: "))
    for x in range(life):
        print(f"Generation {x}")
        res = next_gen(world)
        if res == 1:
            print("End")
            break
        elif res == 2:
            print("All dead")
            break
        print()


if __name__ == "__main__":
    main()
