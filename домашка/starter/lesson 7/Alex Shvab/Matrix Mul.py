import random
m2 = [[1, 4],
     [2, 5],
     [3, 6]]

m1 = [[1, 3, 5],
      [2, 4, 6]]

def mul_matrix(m1 , m2):
    sum = 0
    tmp = []
    res = []
    if len(m2) != len(m1[0]):
        print("Sorry")
    else:
        r1 = len(m1)
        c1 = len(m1[0])
        r2 = c1
        c2 = len(m2[0])
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    sum += m1[z][i] * m2[i][j]
                tmp.append(sum)
                sum = 0
            res.append(tmp)
            t= []
        return res


print(mul_matrix(m2, m1))