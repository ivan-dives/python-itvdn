import random
list = []
m = int(input("Enter number of elements in list: "))
for y in range(m):
    list.append(random.randint(-100000, 100000))
print(list)
# 1 Method


for j in range(len(list), 0, -1):
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp

print(list)
