def sum(a,b):
    print(a+b)

def subtraction(a,b):
    print(a-b)

def multiplication(a,b):
    print(a*b)

def division(a,b):
    if a!= 0 and b!= 0:
        print(a/b)
    else:
        print('sorry but don\'t use 0')


while True:
    z = input('|+|-|/|*|exit|')
    if z == 'exit':
        break
    a = int(input('first number'))
    b = int(input('second number'))
    if z == '+':
        sum(a,b)
    elif z == '-':
        subtraction(a,b)
    elif z == '*':
        multiplication(a,b)
    elif z == '/':
        division(a,b)
    else:
        print('choose one of these characters |+|-|/|*|exit|')