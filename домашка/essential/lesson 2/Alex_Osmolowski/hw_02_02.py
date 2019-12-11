# Задание 2
# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать
# нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите
# метод нажатия на кнопку.


class GraphicalObject:
    """ Класс графического объекта """

    def click(self):
        try:
            self.on_click()
        except AttributeError:
            print(self.__class__.__name__, 'Сюда нажимать не стоит!')


class Rectangle(GraphicalObject):
    """ Класс прямоугольника с опциональным текстом """

    def __init__(self, width, height, text=''):
        super().__init__()

        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        # Проверяем задан ли текст
        if self.text:
            padded_text = ' ' + self.text + ' '  # если задан - добавляем поля
        else:
            padded_text = self.text
        padded_text_len = len(padded_text)  # считаем длину получившегося текста

        # Центрируем строку с текстом по горизонтали
        left_padding = round((self.width - padded_text_len) / 2)  # количество звёздочек слева от текста
        left = '*' * left_padding  # звёздочки слева от текста
        right = '*' * (self.width - left_padding - padded_text_len) # звёздочки справа от текста

        # Цмкл вывода прямоугольника из звёздочек с возможным текстом
        for i in range(self.height):
            # Центрируем тестк по вертикали
            if i == round(self.height / 2):
                print(left, padded_text, right, sep='')  # вывод строки звёздочек с возможным текстом
            else:
                print('*' * self.width)  # вывод строки звёздочек без текста


class Clickable:
    """ Класс объекта - обработчика нажатия мыши """

    def on_click(self):
        print(self.__class__.__name__, 'clicked')


class Button(Rectangle, Clickable):
    """ Класс кнопки """
    def __init__(self, width=25, height=5, text=None):
        if text is None:
            text = self.__class__.__name__
        super().__init__(width, height, text)


def main():
    rect = Rectangle(20, 5)
    rect.draw()
    rect.click()

    print()

    button = Button()
    button.draw()
    button.click()

    print()

    button = Button(text="Княпочка")
    button.draw()
    button.click()


if __name__ == '__main__':
    main()