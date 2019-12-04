#створити ієрархію класів з множинним наслідуванням
#вивести на екран порядок вирішення методів для кожного з класів

class Father:
    def __init__(self):
        self.can_earn = True
        self.can_cook = False
        self.can_dance = False
        self.can_draw = False
        self.can_sing = True

    def show_abilities(self):
        print(type(self).__name__, ':')
        print('Can earn', self.can_earn)
        print('Can cook', self.can_cook)
        print('Can dance', self.can_dance)
        print('Can sing', self.can_sing)
        print('Can draw', self.can_draw)

class Mother:
    def __init__(self):
        self.can_earn = False
        self.can_cook = True
        self.can_dance = True
        self.can_draw = True
        self.can_sing = False

    def show_abilities(self):
        print(type(self).__name__, ':')
        print('Can earn', self.can_earn)
        print('Can cook', self.can_cook)
        print('Can dance', self.can_dance)
        print('Can sing', self.can_sing)
        print('Can draw', self.can_draw)

class Child_1(Father):
    def __init__(self):
        super().__init__()
        self.can_draw = True
        

class Child_2(Mother, Father):
    def __init__(self):
        super().__init__()
        self.can_earn = False
        self.can_sing = True
    

class Child_3(Mother, Father):
    def __init__(self):
        super().__init__()
        self.can_earn = False
        self.can_dance = True
        self.can_cook = False
    


if __name__ == '__main__':
    father = Father()
    father.show_abilities()

    mother = Mother()
    mother.show_abilities()

    child1 = Child_1()
    child1.show_abilities()

    child2 = Child_2()
    child2.show_abilities()

    child3 = Child_3()
    child3.show_abilities()
