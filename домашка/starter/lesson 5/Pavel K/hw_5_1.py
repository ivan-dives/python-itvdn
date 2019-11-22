def username(x = 'Pasha'):
    print(f'Hello, {x}!')

z = input('Write your name__')
if z.replace(' ','') == '':
    username()
else:
    username(z)

