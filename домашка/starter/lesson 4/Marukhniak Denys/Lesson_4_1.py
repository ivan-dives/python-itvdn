width = int(input('Enter a width of rectangle: '))
height = int(input('Enter a height of rectangle: '))

for x in range(height):
    for y in range(width):
        print("*", sep='', end='')
    print()