lst = [x for x in range(10)]
print(lst)
new_lst = list(filter(lambda x: x % 2 != 0, lst))  # отбираем нечетные
print(list(map(lambda x: x**2, new_lst)))  # возводим в степень
