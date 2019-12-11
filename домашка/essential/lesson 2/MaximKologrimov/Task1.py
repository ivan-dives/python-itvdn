# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
# edit_document выводит на экран информацию о том, что редактирование документов недоступно для
# бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
# иначе Editor. Вызовите методы просмотра и редактирования документов.

class Editor:

    def view_document(self):
        print('Документ №1')

    def edit_document(self):
        print('Редактирование документов недоступно для бесплатной версии')

free = Editor()

class ProEditor(Editor):

    def proedit_document(self):
        print('Документ доступен для редактирования')

license = ProEditor()

print('''File:
    1. View
    2. Edit
''')

choice = input('')

if choice == '1':
    free.view_document()
elif choice == '2':
    key = input('Введите лицензионный ключ: ')
    if key == 'Xc34VC1aS':
        license.proedit_document()
    else:
        license.edit_document()
