# Задание 1
# Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка, а
# также сумму и среднее арифметическое его значений.


def try_cast_to_foat(s):
    """Функция проверки вохможности преобразования переданного аргумента в число типа float"""
    try:
        return float(s)
    except:
        return None


def lst_min(lst):
    """Функцитя вычисления минимального значения среди элементов списка, переданного в аргументе"""
    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        min_x = lst[0]
        for x in lst[1:]:
            if x < min_x:
                min_x = x
        return min_x


def lst_max(lst):
    """Функцитя вычисления минимального значения среди элементов списка, переданного в аргументе"""
    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        max_x = lst[0]
        for x in lst[1:]:
            if x > max_x:
                max_x = x
        return max_x

def lst_sum(lst):
    """Функцитя вычисления суммы значений элементов списка, переданного в аргументе"""
    if not lst:
        return None
    else:
        sum_x = 0
        for x in lst:
            sum_x += x
        return sum_x


def lst_avg(lst):
    """Функцитя вычисления среднего арифметического значений элементов списка, переданного в аргументе"""
    if not lst:
        return None
    else:
        return lst_sum(lst)/len(lst)

def main():
    # Введём список натуральных чисел разделённых пробелами и отфильтруем его от "мусора"
    lst_nums = input("Введите список натуральных чисел, разделённых пробелами: ").split()
    print("Введён список:", lst_nums)
    lst_nums = [float(x) for x in lst_nums if try_cast_to_foat(x)]
    print("Отфильтрованный список:", lst_nums)

    # Проверим отфильтрованный список на пустоту
    if not lst_nums:
        print("отфильтрованный список пуст!")
        return

    # Вычисляем и выводим результаты
    print("Элемент списка с наибольшим значением:", lst_max(lst_nums))
    print("Элемент списка с наименьшим значением:", lst_min(lst_nums))
    print("Сумма значений элементов списка:", lst_sum(lst_nums))
    print("Среднее арифметическое значений элементов списка:", lst_avg(lst_nums))


if __name__ == '__main__':
    main()