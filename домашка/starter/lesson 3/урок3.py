

name = input('Enter your name, please _ ')

if name == 'Oxana':
    print('That is great, me too!!!''\n\n')
else:
    print('What a surprise...''\n\n')

import math

x = float(input('What is the x value?''\n\n'))

if -math.pi <= x <= math.pi:
    print(math.cos(x*3))
if x < -math.pi or x > math.pi:
    print(x)
    print('\n\n')




while True:
    print('Choose operation, by number:')
    print('1. +')
    print('2. -')
    print('3. *')
    print('4. /')
    print('5. x^n')
    print('6. sin x')
    print('7. cos x')
    print('8. tg x')
    print('9. to exit')

    choice = int(input('\n\n'"_"))

    if choice == 9:
        break
    elif choice == 1:
        a = float(input('Please, eneter a first number_'))
        b = float(input('Please, eneter a second number_'))
        print(f"Result: {a+b}"'\n\n')
    elif choice == 2:
        a = float(input('Please, eneter a first number_'))
        b = float(input('Please, eneter a second number_'))
        print(f"Result: {a - b}"'\n\n')
    elif choice == 3:
        a = float(input('Please, eneter a first number_'))
        b = float(input('Please, eneter a second number_'))
        print(f"Result: {a * b}"'\n\n')
    elif choice == 4:
        a = float(input('Please, eneter a first number_'))
        b = float(input('Please, eneter a second number_'))
        print(f"Result: {a / b}"'\n\n')
    elif choice == 5:
        a = float(input('Please, eneter a number_'))
        b = float(input('Please, eneter an exponenta_'))
        print(f"Result: {a**b}"'\n\n')
    elif choice == 6:
        a = float(input('Please, eneter a number, whose sine need to be found_'))
        print(f"Result: {math.sin(a)}"'\n\n')
    elif choice == 7:
        a = float(input('Please, eneter a number, whose cosine need to be found_'))
        print(f"Result: {math.cos(a)}"'\n\n')
    elif choice == 8:
        a = float(input('Please, eneter a number, whose tangent need to be found_'))
        print(f"Result: {math.tan(a)}"'\n\n')

    else:
        print('Incorrect input, try again')