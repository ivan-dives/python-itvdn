class Mouse:
    def button(self, sq, x, y):
        sq.coordinates(x, y)

x = int(input('Enter x-axis value '))
y = int(input('Enter y-axis value '))

class Sqear:
    def __init__(self, top, bottom, right, left):
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left

    def coordinates(self, x, y):
        if self.top <= x <= self.bottom or self.right <= y <= self.left:
            print('You hit the target')
        else:
            print('You missed')

s = Sqear(100, 200, 300, 400)
m = Mouse()

m.button(s, x, y)