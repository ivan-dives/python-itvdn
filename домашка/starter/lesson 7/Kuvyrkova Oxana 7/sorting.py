
import random
new_list = [random.randint(0, 500) for i in range(10)]
#print(new_list)
for a in range(len(new_list) - 1):
    for b in range(len(new_list) - a - 1):
        if new_list[b] > new_list[b+1]:
            new_list[b], new_list[b + 1] = new_list[b + 1], new_list[b]
print(new_list)