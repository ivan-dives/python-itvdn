"""
Модуль реализации клоасса таблицы вселенной
"""


class SpaceTable:

    def __init__(self, n):
        self.__space = []
        for i in range(n):
            ln = []
            for j in range(n):
                ln.insert(j, False)
            self.__space.insert(i, ln)

    def get_elem(self, i, j):
        return self.__space[i][j]

    def set_elem(self, i, j, b):
        self.__space[i][j] = b

    def set_points(self, lst_pnts):
        for i in range(len(lst_pnts)):
            self.set_elem(lst_pnts[i][0], lst_pnts[i][1], True)

    def prn_st(self):
        for i in range(len(self.__space)):
            for j in range(len(self.__space[i])):
                if self.get_elem(i, j):
                    smb = "* "
                else:
                    smb = "X "
                print(smb, end="")
            print()

    def neib_count(self, pnt):
        sum = 0
        for i in range(pnt[0]-1, pnt[0]+2):
            for j in range(pnt[1]-1, pnt[1]+2):
                if not (i == pnt[0] and j ==pnt[1]):
                    try:
                        b = self.get_elem(i, j)
                    except IndexError:
                        pass
                    else:
                        if b:
                            sum += 1
        return sum


def main():
    st = SpaceTable(10)
    st.set_points([(0, 1), (1, 2), (2, 3)])
    st.prn_st()
    print(st.neib_count((0, 1)))
    print(st.neib_count((1, 2)))
    print(st.neib_count((2, 3)))


if __name__ == '__main__':
    main()

