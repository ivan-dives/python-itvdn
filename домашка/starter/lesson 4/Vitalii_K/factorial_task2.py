a = int(input('Enter the number: '))
x = 1
y = 1
while True:
    if a > 0:
        for n in range(a):
            y *= x
            x += 1
        print(f'The factorial of {a} is: {y}')
        break
    else:
        print('The number should be greater than 0')
        a = int(input('Enter the number: '))
input("Press 'Enter' to exit")