def steps(x):
    for i in range (x - 2):
        list.append(list[i] + list[i+1])

list = [1, 2]
n = int(input("Enter number of stair steps: "))
steps(n)
print(list)