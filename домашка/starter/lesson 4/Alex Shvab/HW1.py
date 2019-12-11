print("Enter a and b. a < b")
a = int(input("a: "))
b = int(input("b: "))
x = 0

while a <= b:
    x = x + a
    a += 1
print(f"sum = {x}")