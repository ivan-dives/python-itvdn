class Editor:
    def edit_document(self):
        print('редактирование документов недоступно для бесплатной версии')
    def view_document(self):
        pass

class ProEditor(Editor):
    def edit_document(self):
        print('редактирование документов доступно')
        pass

def main():
    c = input('')
    password = '1523wW'
    if c == password:
        k = ProEditor()
        k.edit_document()
        k.view_document()
    else:
        z = Editor()
        z.edit_document()
        z.view_document()

if __name__ == '__main__':
    main()