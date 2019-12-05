class Editor ():
    def __init__(self):
        self.name = "Document"
    def view_document(self):
        print(self.name)
    def edit_document(self):
        print("редактирование документов недоступно для бесплатной версии")

class ProEditor(Editor):
    def edit_document(self):
        request = input("Для редактирования введите лицензионный ключ\n")
        if request == "pass12345":
           print ("You can edit document")
        else:
            Editor ()
            print("The key is wrong")



new_Editor = Editor()
new_Editor.view_document()
new_Editor.edit_document()
new_Editor2 = ProEditor()
new_Editor2.edit_document()
