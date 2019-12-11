# Задание 1
# Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка, а
# также сумму и среднее арифметическое его значений.

cloud = [10, 12, 32, 12, 32, -23, 23, 0, 1]
minimum = cloud[0]
maximum = cloud[0]
result_of_sum = 0

for i in cloud[1:]:
    if minimum > i:
        minimum = i
    elif maximum < i:
        maximum = i
else:
    print(f'Minimum = {minimum}')
    print(f'Maximum = {maximum}')

for i in cloud:
    result_of_sum += i
print(f'Sum = {result_of_sum}')
print(f'Average = {result_of_sum/len(cloud)}')
