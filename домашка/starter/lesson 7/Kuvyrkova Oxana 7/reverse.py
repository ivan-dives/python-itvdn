

x = int(input("enter 1st element of the list"))
y = int(input("enter last element of the list"))
list=[]
for x in range(y+1):
    list.append(x*2)
new_list = list[::-1]
print (list)
print (new_list)
