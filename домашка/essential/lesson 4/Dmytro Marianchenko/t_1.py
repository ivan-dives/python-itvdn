def sort(some_list):
    next_list = []
    for i in some_list:
        next_list.insert(0, i)
    some_list = next_list
    return some_list


my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list = sort(my_list)
print(my_list)
