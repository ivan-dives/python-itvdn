# 1 Method
list = [5, 7, 2, 3, 8, 1, 4]

for j in range(len(list), 0, -1):
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp

print(list)
