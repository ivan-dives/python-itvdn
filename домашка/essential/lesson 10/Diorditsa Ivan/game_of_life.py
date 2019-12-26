MAP = [
    [0, 1, 1],
    [0, 1, 0],
    [0, 0, 0],
]

WIDTH = 3
HEIGHT = 3

class World:
    grid = []

    def __init__(self):
        

def count_neighbors(world, x, y):
    neighbors = 0

    for a in [x-1,x,x+1]:
        for b in [y-1,y,y+1]:
            if a == x and b == y:
                continue
            try:
                neighbors += world[a][b]
            except IndexError:
                pass

    return neighbors


def next_gen(world):
    next_world = []
    for x in range(0, HEIGHT):
        next_world.append([0] * WIDTH)
        for y in range(0, WIDTH):
            neighbors = count_neighbors(world, x, y)
            if world[x][y] == 0:
                if neighbors == 3:
                    next_world[x][y] = 1
                else:
                    next_world[x][y] = 0
            else: # MAP[x][y] == 1
                if neighbors in [2,3]:
                    next_world[x][y] = 1
                else:
                    next_world[x][y] = 0
    return next_world


world = MAP
print(world)
world = next_gen(world)
print(world)
