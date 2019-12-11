# Задание 3
# Простым называется число, которое делится нацело только на единицу и само себя. Число 1 не
# считается простым. Напишите программу, которая находит все простые числа в заданном
# промежутке, выводит их на экран, а затем по требованию пользователя выводит их сумму либо
# произведение


def is_simple_num(n):
    """Функция проверяющая, является ли число простым"""
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True

def main():
    lst_str = input("Задайте через запятую границы промежутка целых положительных чисел: ").split(",")
    # print(lst_str)
    lst_str = [x.strip() for x in lst_str]
    # print(lst_str)
    lst_num = [int(x) for x in lst_str if x.isdigit()]
    if len(lst_num) != 2:
        print("Некорректно заданы границы промежутка!")
        return
    beg = min(lst_num)
    end = max(lst_num)
    simple_lst = [x for x in range(beg, end+1) if is_simple_num(x)]
    print("Список простых чисел  заданном промежутке [{}, {}]:".format(beg, end))
    print(simple_lst)

    while True:
        op = input("Введите операцию над этими числами (+ - сумма, * - произведение): ")
        if op in ["+", "*"]:
            break

    if op == "+":
        res = 0
        for x in simple_lst:
            res += x
        print("Сумма простых чисел  заданном промежутке [{}, {}] = {} ".format(beg, end, res))
    else:
        res = 1
        for x in simple_lst:
            res *= x
        print("Произведение простых чисел  заданном промежутке [{}, {}] = {} ".format(beg, end, res))

if __name__ == '__main__':
    main()