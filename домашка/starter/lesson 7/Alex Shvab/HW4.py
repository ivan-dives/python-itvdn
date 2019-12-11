list = []

str = input("Enter some  numbers separated by space: ")

list = [int(x) for x in str.split(" ")]

print(f"You enter {list}")
print(f"Revers {list[::-1]}")