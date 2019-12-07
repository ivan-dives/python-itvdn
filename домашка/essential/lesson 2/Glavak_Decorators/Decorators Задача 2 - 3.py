import time

def val(f):
    def qwe(s, x, y):
        result = f(s, x, y)
        print(f'входные значения {x} и {y}')
        print('результат: ' + result)
    return qwe

def testtime(f):
    def dec(*a, **k):
        start_time = time.time()
        result = f(*a, **k)
        end_time = time.time()
        print("- Finished '{}', time = {:0.5f}s ".format(f.__name__,end_time - start_time))
        return result
    dec.__name__ = f.__name__
    return dec

class Mouse:
    @testtime
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

    @val
    @testtime
    def coordinates(self, x, y):
        if self.top <= x <= self.bottom or self.right <= y <= self.left:
            return ('You hit the target')
        else:
            return ('You missed')

s = Sqear(100, 200, 300, 400)
m = Mouse()

m.button(s, x, y)