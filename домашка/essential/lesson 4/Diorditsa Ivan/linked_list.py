class Slots:
    __slots__ = ('prev', 'next')

s = Slots()
print(s.prev)

exit()


val = [10, 20, 30]

class Head:
    def __init__(self, value):
        self.prev = self
        self.next = self
        self.value = value

h1 = Head(val[0])

h2 = Head(val[1])
h1.next = h2
h1.prev = h2
h2.next = h1
h2.prev = h1

h3 = Head(val[2])
h3.next = h1
h3.prev = h2
h2.next = h3
h1.prev = h3

start = h1
while True:
    print(start.value)
    start = start.next
    if start == h1:
        break
