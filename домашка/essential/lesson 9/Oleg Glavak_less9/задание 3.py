from functools import lru_cache

@lru_cache(maxsize = None)
def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

a = int(input("введите число - "))
print()

Z = list(filter(lambda x: not int (x) % 2, fibonacci(a)))

for x in Z:
    print(x)