class Editor():
    pass

    def view_document(self):
        with open('D:\\1.txt', 'r', encoding='utf-8') as k2:
            for i in k2:
                print(i)

    def edit_document(self):
        print(f'Редактирование документов недоступно для бесплатной версии.')

class ProEdit(Editor):
    def edit_document(self):
        with open('D:\\1.txt', 'w', encoding='utf-8') as k2:
            k = input("Напишите желаемый текст")
            k2.write(k)


print("Добро пожаловать в программу по чтению и созданию txt файлов.\n"
      "Если хотите ознакомится с пробной версией нажмите любое сочитание клавиш,\n"
      "если вы приобрели пароль от Pro версии введите его.\n"
      "Хотите выйти введите exit")
password = input('_')

if password == 'ur67':
    d = ProEdit()
    while True:
        print('Хотите прочитать файл нажмите любую кнопку, '
              'Написать текст нажмите "w".'
              'Выйти "exit". ')
        t1 = input('_')
        if t1 == 'exit':
           exit(0)
        elif t1 == 'w':
            d.edit_document() # Файл перезаписывается
        else:
            d.view_document() # Привет, как дела?
elif password == 'exit':
    exit(0)
else:
    c = Editor()
    c.view_document() # Привет, как дела?
    c.edit_document() # Редактирование документов недоступно для бесплатной версии.

