while True:
    print('Enter two numbers, a and b with condition (a<b): ')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    if a < b:
        break
    else:
        print('a >= b, so try again . . .', end='\n\n')
res = 0
for cur_num in range(a, b+1):
    res += cur_num
    print(f'{cur_num}', end=' + ')
print(f'= {res}')
