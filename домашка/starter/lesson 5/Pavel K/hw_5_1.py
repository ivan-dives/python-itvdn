def username(x = 'Pasha'):
    print(f'Hello, {x}!')

z = input('Write your name__')
if z == '':
    username()
else:
    username(z)

