from math import sin, cos, tan

print('What do you want to calculate?')
operation = input('Choose one operation between: -, +, *, /, ^, sin, cos, tan: ')
#temp_operation = str.lower(operation)

if operation == '^' or 'sin' or 'cos' or 'tan':
    number = int(input('Enter a number: '))
    if operation == '^':
        print('Result of {}^2 = {}'.format(number, number**2))
    elif operation == 'sin':
        print('Result of sin({}) = {:5.2f}'.format(number, sin(number)))
    elif operation == 'cos':
        print('Result of cos({}) = {:5.2f}'.format(number, cos(number)))
    elif operation == 'tan':
        print('Result of tan ({}) = {:5.2f}'.format(number, tan(number)))
elif operation == '-' or '+' or '*' or '/':
    number1 = int(input('Enter a first number: '))
    number2 = int(input('Enter a second number: '))
    if operation == '-':
        print('Result of {} - {} = {}'.format(number1, number2, number1-number2))
    elif operation == '+':
        print('Result of {} + {} = {}'.format(number1, number2, number1+number2))
    elif operation == '*':
        print('Result of {} * {} = {}'.format(number1, number2, number1*number2))
    elif operation == '/':
        print('Result of {} / {} = {:5.2f}'.format(number1, number2, number1/number2))
else:
    print("You have entered wrong operation, try again")
