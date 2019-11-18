x = input('Как Вас зовут? ')
x = x.lower()

if x == 'max' or x == 'maxim' or x == 'максим' or x == 'макс':
    print(f'Очень приятно {x}!')
else:
    print('Это же неправда!')
