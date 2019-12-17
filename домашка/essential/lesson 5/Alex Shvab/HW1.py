lst = []
str = input("Enter some  numbers separated by space: ")

lst.extend([int(x) for x in str.split(" ") if x != ""])


def avg(*args):
    return sum(args) / len(args)


print(f"{avg(*lst) = }")
print(f"{avg(*lst[0:2]) = }")
