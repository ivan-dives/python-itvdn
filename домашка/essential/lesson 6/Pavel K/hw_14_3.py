# Ознакомьтесь при помощи документации с классами OrderedDict, defaultdict и ChainMap модуля collections.
from collections import OrderedDict, defaultdict, ChainMap
# ChainMap – это класс, который дает возможность объединить несколько сопоставлений вместе таким образом, чтобы они стали единым целым.

car_parts = {
    'hood' : 500,
    'engine' : 5000,
    'front_door': 7500
}

car_optins = {
    'A/C':1000,
    'Turbo': 2500,
    'rollbar': 300
}

car_accessories = {
    'cover' : 100,
    'hood_ornament' : 150,
    'seat_cover':99
}

car_pricing = ChainMap(car_accessories,car_optins,car_parts)
print(car_pricing['A/C'])
print(car_pricing)


# defaultdict  defaultdict автоматически назначает ноль как значение любому ключу, который еще не имеет значения


from collections import defaultdict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)


# OrderedDict - словарь отслеживает порядок ключей после их добавления. Обычный dict содержит неупорядоченные данные.
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))

print(new_d)
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
