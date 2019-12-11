# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
# edit_document выводит на экран информацию о том, что редактирование документов недоступно для
# бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
# иначе Editor. Вызовите методы просмотра и редактирования документов.


class Editor:
    document = "Текущий текст"

    def view_document(self):
        print(f'Текущий текст:\n'
              f'{self.document}')

    def edit_document(self):
        print('Редактирование документов недоступно для бесплатной версии')


class ProEditor(Editor):

    def edit_document(self):
        print('Редактирование документов разрешено')
        do = input('Хотите ввести другой текст (Yes/No)?')
        if do.lower() == 'yes':
            new_doc = input('Введите новый текст:')
            self.document = new_doc
        else:
            do = input('Хотите дописать текст (Yes/No)?')
            if do.lower() == 'yes':
                new_doc = input('Введите текст:')
                self.document += new_doc
        print(f'Новый текст:\n'
              f'{self.document}')


license_pass = input('Введите лицензионный ключ: ')

doc = ProEditor() if license_pass == 'password' else Editor()
doc.view_document()
doc.edit_document()

