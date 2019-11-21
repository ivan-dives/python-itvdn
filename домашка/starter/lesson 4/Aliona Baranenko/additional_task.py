a = int(input("Base - "))
b = int(input("Height - "))

for i in range(a):
    for j in range(b):
        print('*', end='')
    print()

sys.exit()

n = int(input("Enter the base value - "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

sys.exit()

n = int(input("Enter the base value - "))

for i in range(n):
    print("*"*n)