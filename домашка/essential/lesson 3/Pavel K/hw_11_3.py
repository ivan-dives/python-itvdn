# Задание 3
# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу. Конструктор должен генерировать исключение,
# если заданы неправильные данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты после заданного года.

class Person:
    instanses = []
    def __init__(self, name, surname, office, when_got_to_work):
        self.name = name
        self.surname = surname
        self.office = office
        Person.instanses.append(self)
        try:
            self.when_got_to_work = when_got_to_work
            if when_got_to_work < 2009:
                raise Exception (f'Наша компания основана в 2009 году. Вы ввели некоректную дату приема на работу {when_got_to_work}.')
        except Exception as exp:
            print(exp)

    @classmethod
    def print2(cls, year):
        for i in Person.instanses:
            if i.when_got_to_work > year:
                print(i)

    def __str__(self):
        return (f'Имя - {self.name}, Фамилия - {self.surname}, Отдел №{self.office}, работает с {self.when_got_to_work}')



tk1 = Person('Pasha', 'Korotkov', 6, 2010)
tk2 = Person('Andrey', 'Izmailov', 6, 2016)
tk3 = Person('Sasha', 'Tokar\'', 6, 2017)
tk4 = Person('Elena', 'Antonov', 6, 2011)
tk5 = Person('Irina', 'Slantov', 6, 2008)



tk2.print2(2009)

# Аналог через for ... in
# for person in [tk1,tk2, tk3, tk4, tk5]:
#     person.print2()
#     if person.when_got_to_work > 2011:
#         print(person)