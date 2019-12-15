lst = []
str = input("Enter some  numbers separated by space: ")

for x in str.split(" "):
    if x == "":
        continue
    else:
        try:
            x = int(x)
        except ValueError:
            continue
        else:
            lst.append(int(x))

lst.sort()

print(f"Sort: {lst = }")