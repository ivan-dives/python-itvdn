a = 1
b = int(input("Enter number: "))
sum = 1

while a <= b:
    sum = sum * a
    a = a + 1
print(f"Factorial {b} = {sum}")