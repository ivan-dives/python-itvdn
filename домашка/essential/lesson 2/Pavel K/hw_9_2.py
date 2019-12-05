class Target:
    w = [200, 1600]
    h = [200, 800]


class Shot(Target):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def decision(self):
        if self.w[0] <= x <= self.w[1] and self.h[0] <= y <= self.h[1]:
            print('It’s a masterpiece!')
        else:
            print("I'm sorry but you lose!")


x, y =  map(int, input('screen resolution(1920х1080)').split())
s = Shot(x, y)
s.decision()