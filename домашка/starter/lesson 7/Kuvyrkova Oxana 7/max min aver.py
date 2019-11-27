my_list = list(range(50))

max = 0
min = len(my_list) - 1
aver = 0

for i in range(1, len(my_list)):
    if my_list[i] > my_list[max]:
        max = i

    if my_list[i] < my_list[min]:
        min = i
    else:
        aver += my_list[i]

print(max)
print(min)
print(aver/len(my_list))



