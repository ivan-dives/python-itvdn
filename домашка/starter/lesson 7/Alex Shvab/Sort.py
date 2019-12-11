import random
list = []
m = int(input("Enter number of elements in list: "))
for y in range(m):
    list.append(random.randint(-100000, 100000))
print(list)


# 1 Method
def bubble(list):
    for j in range(len(list), 0, -1):
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
    return list

print(bubble(list))


#2 Method
def quick(list):
    if len(list) <= 1:
        return list
    else:
        q = random.choice(list)
        s_num = []
        m_num = []
        e_num = []
        for n in list:
            if n < q:
                s_num.append(n)
            elif n > q:
                m_num.append(n)
            else:
                e_num.append(n)
        return  quick(s_num) + e_num + quick(m_num)

print(quick(list))