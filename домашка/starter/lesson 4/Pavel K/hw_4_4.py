a = int(input('Enter first side of rectangle'))
b = int(input('Enter second side of rectangle'))

for i in range(a):
    print()
    for j in range(b):
        print('*', end="")

# other way ithout nested function
for i in range(a):
    print('*'*b)