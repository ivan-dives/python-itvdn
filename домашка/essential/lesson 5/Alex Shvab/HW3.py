lst = []
str = input("Enter some text: ")

lst.extend([x for x in str.split(" ") if x != ""])

lst.sort()

print(f"Sorted: {lst = }")