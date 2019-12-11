import functools
@functools.lru_cache(maxsize=None)
def step(x):
    if x == 1 or x == 2:
        return 1
    else:
        return step(x-1) + step(x-2)

n = int(input("Enter number of stair steps: "))

print(f"You can walk {n} stair steps in {step(n+1)} ways")