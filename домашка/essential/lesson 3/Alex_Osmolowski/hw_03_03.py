# Задание 3
# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год
# поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные
# данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты
# после заданного года.


import datetime

# Минимально допустимый год
MINIMAL_YEAR = 1991


def read_int(message, check_function=None):
    """Функция безопасного чтения числа с клавиатуры
    :param message:        поясняющее сообщение
    :param check_function: функция-предикат проверки корректности либо None
    :return:               введённое значение
    """

    while True:
        try:
            value = int(input(message).strip())
            if check_function and not check_function(value):
                raise ValueError('введено некорректное значение')
        except ValueError as error:
            print('Произошла ошибка:', error)
        else:
            return value


def is_year_correct(year):
    """Функция проверки корректности года.
    Возвращает True, если заданный год входит в диапазон от года основания
    компании до текущего года.
    """
    return MINIMAL_YEAR <= year <= datetime.date.today().year


def read_year(message):
    """Функция безопасного чтения года"""
    return read_int(message, is_year_correct)


class Worker:
    """Класс сотрудника"""

    def __init__(self, first_name, last_name, job_title, initial_year):
        if not first_name:
            raise ValueError('имя сотрудника не может быть пустым')
        if not last_name:
            raise ValueError('фамилия сотрудника не может быть пустой')
        if not job_title:
            raise ValueError('должность сотрудника не может быть пустой')
        if not is_year_correct(initial_year):
            raise ValueError('некорректный год приёма: {}'.format(initial_year))

        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.initial_year = initial_year

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.job_title}, {self.initial_year}'

    @staticmethod
    def read_worker():
        """Статический метод чтения нового сотрудника с клавиатуры"""
        first_name = input('Введите имя: ').strip()
        last_name = input('Введите фамилию: ').strip()
        job_title = input('Введите должность: ').strip()
        year = read_year('Введите год приёма на работу: ')
        return Worker(first_name, last_name, job_title, year)


def main():
    workers_count = read_int('Количество сотрудников: ')
    workers = []

    while len(workers) < workers_count:
        try:
            worker = Worker.read_worker()
        except ValueError as error:
            print('Ошибка:', error)
        else:
            workers.append(worker)
        finally:
            print()

    year = read_year('Введите год: ')

    for worker in workers:
        if worker.initial_year >= year:
            print(worker)


if __name__ == '__main__':
    main()