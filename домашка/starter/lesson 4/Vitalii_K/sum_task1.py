a = int(input('Enter first number: '))
b = int(input('Enter last number: '))
x = a
y = 0
for n in range(a, b+1):
    y += x
    x += 1
print(f'The sum of all natural numbers from {a} to {b} is: {y}')
input("Press 'Enter' to exit")