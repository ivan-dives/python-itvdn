# first way
a = int(input('Enter your number'))
z=1
for i in range(1,a+1):
    z *= i
else:
    print(z)

# second way
a = int(input('Enter your number'))
n = 1
while a > 1:
    n *= a
    a -= 1
else:
    print(n)