# Задание 2
# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
# умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
# продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
# отрицательную степень.


class Calc:
    def __init__(self):  # конструктор
        self.__oper_name = None
        self.__f_arg = None
        self.__s_arg = None
        self.__operation_list = ["+","-","*","/","^", "exit"]

    def operation_input(self):  # ввод операции
        self.__oper_name = input("Введите операцию (+, -, *, /, ^) либо команду 'exit' для выхода: ").strip().lower()
        if not (self.__oper_name in self.__operation_list):
            raise NotImplementedError('введена неподдерживаемая операция')

    def arguments_input(self): # ввод операндов
        self.__f_arg = float(input("Введите первое число: "))
        self.__s_arg = float(input("Введите второе число: "))

    def need_exit(self):  # необходимость завершения работы
        return self.__oper_name == "exit"

    def op_add(self):  # операция сложения
        return self.__f_arg + self.__s_arg

    def op_del(self):  # операция вычитания
        return self.__f_arg - self.__s_arg

    def op_mult(self):  # операция умножения
        return self.__f_arg * self.__s_arg

    def op_div(self):  # операция деления
        return self.__f_arg / self.__s_arg

    def op_pow(self):  # операция возведения в степень
        return self.__f_arg ** self.__s_arg

    def run_operation(self):
        if self.__oper_name == "+":
            return self.op_add
        elif self.__oper_name == "-":
            return self.op_del
        elif self.__oper_name == "*":
            return self.op_mult
        elif self.__oper_name == "/":
            return self.op_div
        elif self.__oper_name == "^":
            return self.op_pow
        else:
            raise NotImplementedError('введена неподдерживаемая операция')

    def __str__(self):
        return f"{self.__f_arg} {self.__oper_name} {self.__s_arg}"


def main():
    calc = Calc()  # Создаём экземпляр калькулятора

    # Цикл работы калькулятора
    while True:
        try:
            calc.operation_input()
        except NotImplementedError:
            print("Введён некорректный аргумент операции!")
            continue
        finally:
            print()
        if calc.need_exit():
            return
        try:
            calc.arguments_input()
        except ValueError:
            print("Введён некорректный аргумент операции!")
        else:
            try:
                res = calc.run_operation()()
            except (ArithmeticError, NotImplementedError) as error:
                print(f'При вычислении ({calc}) произошла ошибка: {error}')
            else:
                print(f'{calc} = {res}')
        finally:
            print()


if __name__ == '__main__':
    main()