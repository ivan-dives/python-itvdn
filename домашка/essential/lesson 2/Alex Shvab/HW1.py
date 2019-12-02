class Editor:
    document = "Этот документ создан Александром"

    def view_document(self):
        print(self.document)

    def edit_document(self):
        print("Вы не можете редактировать документ в бесплатном редакторе")


class ProEditor(Editor):
    def edit_document(self):
        while True:
            print("""Что вы хотите сделать с документом:
            1. Дописать
            2. Переписать
            3. Удалить часть
            4. Выход""")

            ch = int(input("> "))
            if ch == 1:
                print("Введите строку которую хотите дописать.")
                str = input("> ")
                self.document = self.document + str
                print(self.document)
            elif ch == 1:
                print("Введите свой вариант документа")
                str = input("> ")
                self.document = str
                print(self.document)
            elif ch == 3:
                print("С какого по какой символ вы хотите получить")
                s = int(input("> "))
                e = int(input("> "))
                str = self.document[s:e:1]
                print(str)
            elif ch == 4:
                print("Пока")
                break


password = "password"
print("Скажи друг пароль и используй Pro версию")
pas = input("> ")
if pas != password:
    print("Вы испльзуете обычную версию редактора")
    edit = Editor()
    print("""Что вы хотите сделать:
    1. Посмотреть документ
    2. Редактировать документ
    3. Выход""")

    while True:
        ch = int(input(">"))
        if ch == 1:
            edit.view_document()
        elif ch == 2:
            edit.edit_document()
        elif ch == 3:
            print("Пока")
            break
else:
    print("Вы испльзуете Pro версию редактора")
    edit = ProEditor()
    print("""Что вы хотите сделать:
        1. Посмотреть документ
        2. Редактировать документ
        3. Выход""")

    while True:
        ch = int(input(">"))
        if ch == 1:
            edit.view_document()
        elif ch == 2:
            edit.edit_document()
        elif ch == 3:
            print("Пока")
            break

