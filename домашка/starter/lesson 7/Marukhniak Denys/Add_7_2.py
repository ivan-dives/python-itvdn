# 3 сортировки

# сортировка 1
cloud = [-1, 5, 0, 3, -4, 7, 11, 8, 3]
print(cloud)
for i in range(len(cloud)):
    for j in range(len(cloud)):
        if cloud[j] < cloud[i]:
            cloud[i], cloud[j] = cloud[j], cloud[i]
print(cloud)

# сортировка 2






