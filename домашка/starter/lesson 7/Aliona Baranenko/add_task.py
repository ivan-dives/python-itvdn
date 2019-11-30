import random

my_list = []

for i in range(10):
    my_list.append(random.randint(0, 10))

print(my_list)
print(my_list[::-1])