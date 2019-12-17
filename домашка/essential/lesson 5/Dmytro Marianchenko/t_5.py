numbers = input()
x = len(numbers)
tmp = []
for i in numbers:
    tmp.append(i)
    x -= 1
    if x == 0:
        break
    else:
        pass
    numbers = sorted(tmp, key=str)
print(numbers)


