a = 3
b = int(input('Enter second side of rectangle'))

for i in range(5):
    if i > 0:
        break
    for j in range(b+1):
        if j == 0:
            continue
        print('*'*j)
    else:
        print()
