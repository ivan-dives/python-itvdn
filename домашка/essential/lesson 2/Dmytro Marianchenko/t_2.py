class Screen:
    def __init__(self, pix_h, pix_w, mp1, mp2):
        self.pix_h = pix_h
        self.pix_w = pix_w
        self.mp1 = mp1
        self.mp2 = mp2


class Button(Screen):
    def paint(self):
        for i in range(self.pix_h):
            print('0' * self.pix_w)


class Mouse(Button):
    def mouse_point(self):
        if self.mp1 < 0 or self.mp1 > self.pix_h:
            print()
            print("Курсор вышел за граници объекта")
        elif self.mp2 < 0 or self.mp2 > self.pix_w:
            print()
            print("Курсор вышел за граници объекта")
        else:
            print()
            print("Курсор в рамках объекта!!!")


def main():
    pix_h = int(input("Введите высоту объекта:  "))
    pix_w = int(input("Введите ширину объекта:  "))
    btn = Button(pix_h, pix_w, "", "")
    btn.paint()
    mp1 = int(input("Введите координаты мыши по вертикали:  "))
    mp2 = int(input("Введите координаты миши по горизонтали:  "))
    btn1 = Mouse(pix_h, pix_w, mp1, mp2)
    btn1.mouse_point()
    print()
    ext = input("Для выхода введите 'exit', для продолжения нажмите 'Enter':  ")
    if ext == "exit":
        exit()
    else:
        main()


if __name__ == '__main__':
    main()
