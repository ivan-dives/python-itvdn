lst = []
str = input("Enter some text: ")

for x in str.split(" "):
    if x == "":
        continue
    else:
        lst.append(x)

lst.sort()

print(f"Sorted: {lst = }")