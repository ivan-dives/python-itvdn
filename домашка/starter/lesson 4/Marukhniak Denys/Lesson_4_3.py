n = int(input('Enter number (n) of n!: '))
n_res = 1
print(f'{n}! = ', end='')
while n > 0:
    print(f'{n}', end=' * ')
    n_res *= n
    n -= 1
print(f'= {n_res}')