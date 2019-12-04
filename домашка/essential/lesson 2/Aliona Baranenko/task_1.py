#створити клас едітор, котрий має методи едіт і вью
#метод едіт повинен виводити на екран інформацію, що редагування не доступно
#створити підклас проедітор, змінивши метод едіт в підклассі
#ключ ліцензії повинен вводитись з клавіатури
#і якщо він правильний, повинен створюватись екземпляр класу проедітор, а якщо ні - едітор
#викликати методи едіт і вью

class Editor:
    def view_document(self):
        print("you have access to viewing the current document")

    def edit_document(self):
        print("you have no access to editorial revision")

class ProEditor(Editor):
    def edit_document(self):
        key = input("enter the access key - ")
        if key == "qwerty1234":
            print("access granted")
            editor = ProEditor()
        else:
            print("password is incorrect, you have no access to editorial revision")
            editor = Editor()

def main():
    editor.edit_document()
    editor.view_document()

if __name__ == '__main__':
    main()