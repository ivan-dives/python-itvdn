# Задание 1
# Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка, а
# также сумму и среднее арифметическое его значений.

list = []

while True:
    '''
    ввод значиний в список до 5
    '''
    list.append(input('number: '))
    x = len(list)
    sum = list[0]
    if x == 5:
        min = min(list)
        max = max(list)
        break

print()
print(f'минимальное значение {min}')
print(f'максимальное значение {max}')
print(list)
print()

def sumlist(none):
    sum = 0
    for x in none:
        sum = sum + int(x)
    return sum

def average(none):
    average = sumlist(none) / len(none)
    return average

# sum = 0
# for x in list:
#     sum = sum + int(x)
#
# print(sum)

print(f'Сумма элементов списка {list}:  {sumlist(list)}')
print(f'Среднее арифметическое значение списка {list}:  {average(list)}')
