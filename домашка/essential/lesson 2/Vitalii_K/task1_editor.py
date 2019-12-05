class Editor:
    def __str__(self):
        return 'Editor (Freeware)'
    def view_doc(self):
        print('Viewing document...')
    def edit_doc(self):
        print('Editing mode is unavailable in free version...')

class ProEditor(Editor):
    keylist = ['12345', '67890', '54321', '09876']
    key = ''
    def __str__(self):
        return f'ProEditor (Key: {self.key})'
    def view_doc(self):
        super().view_doc()
    def edit_doc(self):
        if self.key in self.keylist:
            print('Editing document...')
        else:
            super().edit_doc()

k = input('Enter product key: ')
if k in ProEditor().keylist:
    p = ProEditor()
    p.key = k
else:
    p = Editor()

print(p)
p.view_doc()
p.edit_doc()
