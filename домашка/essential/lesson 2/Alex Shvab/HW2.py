class Rectungle:
    start = [200, 100]
    end = [800, 700]

class Button(Rectungle):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def press(self):
        if (x > self.start[0] and x < self.end[0]) \
            and (y > self.start[1] and x < self.end[1]):
            print("Вы нажали на кнопку")


while True:
    print("Введите кординаты точки на которую хотите нажать")
    x = int(input("Введите цифру от 0 до 1920: "))
    y = int(input("Введите цифру от 0 до 1080: "))
    mouse = Button(x, y)
    mouse.press()
    print("Если хотите закончить нажмите e")
    exit = input("> ")
    if exit == "e":
        print("Выход")
        break
