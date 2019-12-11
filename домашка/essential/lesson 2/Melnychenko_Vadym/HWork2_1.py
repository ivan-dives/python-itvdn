class Editor():
    def view_document(self):
        print('Просмотр документа')

    def edit_document(self):
        print('редактирование документов недоступно')


class ProEditor(Editor):
    def edit_document(self):
        print('редактирование документов доступно')


k = input('Введите ключ активации: ')
if k == '111':
    print('Продукт активирован')
    editor = ProEditor()

else:
    print('Введен неверный ключ, повторите попытку')
    editor = Editor()


editor.edit_document()
editor.view_document()