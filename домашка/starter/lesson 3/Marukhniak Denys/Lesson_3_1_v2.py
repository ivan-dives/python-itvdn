from math import sin, cos, tan

print('What do you want to calculate?')

while True:
    op = input('Choose one operation between: -, +, *, /, ^, sin, cos, tan: ')
    op = str.lower(op)
    if op == '^' or op == 'sin' or op == 'cos' or op == 'tan':
        number = int(input('Enter a number: '))
        if op == '^':
            print('Result of {}^2 = {}'.format(number, number**2))
        elif op == 'sin':
            print('Result of sin({}) = {:5.2f}'.format(number, sin(number)))
        elif op == 'cos':
            print('Result of cos({}) = {:5.2f}'.format(number, cos(number)))
        elif op == 'tan':
            print('Result of tan ({}) = {:5.2f}'.format(number, tan(number)))
        break
    elif op == '-' or op == '+' or op == '*' or op == '/':
        number1 = int(input('Enter a first number: '))
        number2 = int(input('Enter a second number: '))
        if op == '-':
            print('Result of {} - {} = {}'.format(number1, number2, number1-number2))
        elif op == '+':
            print('Result of {} + {} = {}'.format(number1, number2, number1+number2))
        elif op == '*':
            print('Result of {} * {} = {}'.format(number1, number2, number1*number2))
        elif op == '/':
            print('Result of {} / {} = {:5.2f}'.format(number1, number2, number1/number2))
        break
    else:
        print("\nYou have entered wrong operation, try again...")
