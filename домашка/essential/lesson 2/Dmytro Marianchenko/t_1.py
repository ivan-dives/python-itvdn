class Editor:

    def __init__(self, name_pers):
        self.name_pers = name_pers

    def __str__(self):
        return f"\nПривет, {self.name_pers}! Ты запустил TRIAL версию продукта\nты можешь просматривать файлы, " \
               f"но не можешь их редактировать\n"


class ProEditor:

    def __init__(self, paswd):
        self.paswd = paswd

    def validation(self):
        __paced = "123456"
        __vars_pro = "Поздравляю, вы успешно активировали PRO версию"
        __vars_trial = "К сожалению код более не действителен или не существует"
        if self.paswd == __paced:
            print(f"{__vars_pro}")
        else:
            print(f"{__vars_trial}")


name_pers = input("Пожалуйста, введи имя:  ")
hello = Editor(name_pers)
print(hello)
print("Хочешь получить полный доступ к программе, введи пожалуйста пароль: ")
paswd = input("")
vers = ProEditor(paswd)
vers.validation()
