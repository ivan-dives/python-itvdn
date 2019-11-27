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
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    sum += m1[i][k] * m2[k][j]
                tmp.append(sum)
                sum = 0
            res.append(tmp)
            t= []
        return res


print(mul_matrix(m1, m2))