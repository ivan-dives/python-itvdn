def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):

    if b != 0:
        return a / b
    else:
        return ('mistake \n')

while True:

        print(" for summation enter 1 \n for subtraction enter 2 \n for multiplication enter 3 \n for division enter 4 \n for exit enter 5")
        n = int(input())
        if n == 1:
            a = float(input('please enter 1st number'))
            b = float(input('please enter 2nd number'))
            print ('Your result = ', sum(a,b), '\n')

        if n == 2:
            a = float(input('please enter 1st number'))
            b = float(input('please enter 2nd number'))
            print ('Your result = ', sub(a,b), '\n')

        if n == 3:
            a = float(input('please enter 1st number'))
            b = float(input('please enter 2nd number'))
            print ('Your result = ', mult(a,b), '\n')

        if n == 4:
            a = float(input('please enter 1st number'))
            b = float(input('please enter 2nd number'))
            print ('Your result = ', div(a,b), '\n')
        if n == 5:
            break






