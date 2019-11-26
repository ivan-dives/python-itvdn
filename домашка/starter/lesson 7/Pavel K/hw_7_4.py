from random import randint

num = [] # create list
for i in range(20):
    num.append(randint(-10,40))

print(len(num))
print(num)
print(num[::-1])