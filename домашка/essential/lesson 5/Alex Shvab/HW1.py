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


def avg(*args):
    return sum(args) / len(args)


print(f"{avg(*lst) = }")
print(f"{avg(*lst[0:2]) = }")
