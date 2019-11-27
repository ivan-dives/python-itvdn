# Создайте список, введите количество его элементов и сами значения, выведите эти значения на
# экран в обратном порядке.

cloud = []
element = 0
length = int(input('Enter length of list: '))
for i in range(length):
    element = input(f'Enter {i+1} element of list: ')
    cloud.append(element)

print('Your list with reversed elements:')
for i in cloud[::-1]:
    print(i, end=' ')
