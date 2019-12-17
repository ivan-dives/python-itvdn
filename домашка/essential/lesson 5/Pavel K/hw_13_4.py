# Ознакомьтесь при помощи документации с классами namedtuple и deque модуля collections.
from collections import *
a = [2,3,4,5,6,7]
q=deque(a) # deque - двухстороняя очередь. Вторым элементом можно задать [maxlen] и тогда у нас будет ограниченое количество элементов если добавляем лишний в начало он вытолкнет в конце, если добавим в конец вытолкнет в начале.

print(a)#[2, 3, 4, 5, 6, 7]
q.appendleft(4) # удаляем элемент сначала
print(q) # deque([4, 2, 3, 4, 5, 6, 7])
# Делает такие класы которые себя ведут как tuple  с именноваными полями (она апгрейдит tuple).
Person = namedtuple(
    'Person', ['first_name', 'last_name', 'age'],
)
p = Person('Terrence', 'Gilliam',77)
print(p) # Person(first_name='Terrence', last_name='Gilliam', age=77)