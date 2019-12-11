x = int(input("Enter a 1st number of the list"))
y = int(input("Enter a last number of the list"))
list=[]
simple = []
i = 0

for x in range(y+1):
    list.append(x)
for z in list:
    if z < 2:
        continue

    while i < (len(list)-1):
        i += 1
        if i == 1:
            continue
        if i == 2 or i == 3 or i == 5 or i == 7:
            simple.append(i)
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            continue
        if i % z != 0:
            simple.append(i)

print(list)
print(simple)
