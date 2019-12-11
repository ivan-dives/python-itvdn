m1 = [[1, 4],
     [2, 5],
     [3, 6]]

m2 = [[1, 3, 5],
      [2, 4, 6]]


def trans_matrix(m):
    res = []
    for i in range(len(m[0])):
        temp = []
        for j in range(len(m)):
                temp.append(m[j][i])
        res.append(temp)
    print(res)

trans_matrix(m1)
trans_matrix(m2)



