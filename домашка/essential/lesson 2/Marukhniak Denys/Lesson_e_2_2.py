# Задание 2
# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать
# нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите
# метод нажатия на кнопку.


class Rectangle:
    left_down = [100, 50]
    right_up = [250, 175]


class Click(Rectangle):

    def __init__(self, x_new, y_new):
        self.x = x_new
        self.y = y_new

    def do_click(self):
        if self.left_down[0] < self.x < self.right_up[0] and \
                self.left_down[1] < self.y < self.right_up[1]:
            print('You hit the rectangle with click')
        else:
            print('You missed the target with a click')


while True:
    print('Where do you want to click?')
    x = int(input('Enter coordinate x: '))
    y = int(input('Enter coordinate y: '))
    click = Click(x, y)
    click.do_click()
    again = input('Do you want to try again (Yes/No)?')
    if not again.lower() in ['yes', 'y']:
        break
