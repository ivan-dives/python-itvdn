a = int(input('Enter the number "A"'))
b = int(input('Enter the number "B"'))
z = a
while True:
    a += 1
    z += a
    if a >= b:
        break
print(z)