# Задание
# Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её
# отсортированной в порядке возрастания.


numbers = input('Enter numbers separated by one space: ')

tmp_str = ['']
i = 0
still_is_space = False

for char in numbers:
    if not char.isspace() and char.isdigit():
        still_is_space = False
        tmp_str[i] += char
    elif still_is_space is True:
        pass
    else:
        tmp_str.append('')
        i += 1
        still_is_space = True

tmp_str.sort()
new_str = [int(n) for n in tmp_str]
print(f'Sorted numbers: {new_str}')

