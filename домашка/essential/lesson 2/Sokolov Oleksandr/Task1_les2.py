class Editor
    def view_document(self)
        print(You can read document for free!)
    def edit_document(self)
        print(Editing is not allowed in the free version!)
output=Editor()
Editor.view_document(output)
Editor.edit_document(output)
print()

class ProEditor(Editor)
    def edit_document(self)
        print(You have posibility to edit document!)

key = input(Enter a key for editing this document)
if key == q1w2e3
    login = ProEditor()
    ProEditor.edit_document(login)
else
    login_incorrect = Editor()
    Editor.edit_document(login_incorrect)