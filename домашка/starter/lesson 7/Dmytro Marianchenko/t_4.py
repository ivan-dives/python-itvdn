n = int(input("Введите цифру соответствующую длинне списка:  "))
lst = [i for i in range(1,n+1)]
print(lst)


while True:
    add = input("Хотите добавить значение в список? (y/n):  ")
    if add == "y":
        el = input("Введите значение, которое хотите добавить:  ")
        pos = int(input("Введите позицию в списке"))
        lst.insert(pos - 1, el)
        lst.pop(pos + 1)
        print()
        print(lst)
        print()
    elif add == "n":
        break

print(lst)

add = input("Хотите перевернуть список? (y/n):  ")
    if add == "y":
        lst.reverse()
        print(lst)
        lst.reverse() # разворот в исходную позицию
    elif add == "n":
        pass