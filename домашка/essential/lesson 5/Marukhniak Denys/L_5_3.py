# Задание 3
# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова
# данного текста.


text = input('Enter a text: ')

tmp_str = ['']
tmp = []
i = 0
still_is_space = False
new_str = ''

for char in text:
    if not char.isspace():
        still_is_space = False
        tmp_str[i] += char
    elif still_is_space is True:
        pass
    else:
        tmp_str.append('')
        i += 1
        still_is_space = True

for x in range(len(tmp_str)):
    tmp.append(sorted(tmp_str[x]))
    for y in tmp[x]:
        new_str += y
    new_str += ' '

print(f'Sorted text: {new_str}')
