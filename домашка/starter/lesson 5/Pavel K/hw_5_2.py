def algebra1(a, b=2):
    print(f'if a = {a} and b = {b}. Sum = {a + b}')


def algebra2(a, b=2):
    print(f'if a = {a} and b = {b}. Product of numbers = {a * b}')


a = -5
while True:
    algebra1(a)
    algebra2(a)
    a += 0.5
    if a > 5:
        break
