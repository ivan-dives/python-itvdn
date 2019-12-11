#!/usr/bin/python3
# -*- coding: utf-8 -*_


class MyList(object):

    class _ListNode(object):

        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        self._length = 0
        self._head = None
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def append_by_index(self, element, index=0):
        node = MyList._ListNode(element)

        if not 0 <= index < len(self):
            raise IndexError('list index out of range')
        elif index == self._length - 1 or self._length == 0:
            self.append(element)
        else:
            tmp = self._head
            if index == 0:
                self._head.prev = node
                node.next = self._head
                self._head = node
            else:
                for _ in range(index):
                    tmp = tmp.next
                prev_node = tmp.prev
                prev_node.next = node
                node.next = tmp
                node.prev = tmp.prev

        self._length += 1

    def clear(self):
        self._head.next = None
        self._head = None
        self._tail = None
        self._length = 0

    def delete(self):
        if self._length == 0:
            raise IndexError('list index out of range')
        elif self._length == 1:
            self.clear()
        else:
            tmp = self._tail.prev
            tmp.next = None
            self._tail = tmp

        self._length -= 1

    def delete_by_index(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')
        elif index == self._length - 1 or self._length == 0:
            self.delete()
        else:
            tmp = self._head
            if index == 0:
                self._head.prev = self._head.next
                self._head = self._head.next
            else:
                for _ in range(index):
                    tmp = tmp.next
                tmp.prev.next = tmp.next
            self._length -= 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам
        # последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([5,1, 8])
    my_list.append(10)
    print(my_list)
    my_list.delete()
    print(my_list)
    print(len(my_list))
    my_list.append(40)
    my_list.append_by_index(40)
    my_list.append_by_index(80, 3)
    print(my_list)
    print(len(my_list))
    my_list.delete_by_index(0)
    print(my_list)
    print(len(my_list))



if __name__ == '__main__':
    main()